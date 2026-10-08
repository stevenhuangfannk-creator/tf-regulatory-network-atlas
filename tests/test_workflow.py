"""Numerical regression fixtures; these tiny arrays are test data, never results."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

import h5py
import numpy as np
import pandas as pd
from scipy import sparse, stats

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("periodontal_tf", ROOT / "workflows/periodontal_tf.py")
workflow = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(workflow)


class WorkflowNumerics(unittest.TestCase):
    def test_csr_rows_preserve_integer_counts_across_chunk_boundaries(self):
        # Explicit synthetic unit fixture with an empty row and duplicate symbols.
        dense = np.array([[1, 0, 4, 2], [0, 0, 0, 0], [3, 9, 0, 5], [0, 2, 7, 0]], dtype=np.int32)
        matrix = sparse.csr_matrix(dense)
        with tempfile.TemporaryDirectory() as temporary:
            with h5py.File(Path(temporary) / "fixture.h5", "w") as handle:
                group = handle.create_group("counts")
                group.attrs["shape"] = matrix.shape
                for name in ["data", "indices", "indptr"]:
                    group.create_dataset(name, data=getattr(matrix, name))
                restored = sparse.vstack([workflow.csr_rows(group, 0, 2), workflow.csr_rows(group, 2, 4)]).toarray()
                np.testing.assert_array_equal(restored, dense)
                np.testing.assert_array_equal(workflow.csr_rows(group, 1, 3).toarray(), dense[1:3])
        # Duplicate A counts must be summed, conserving library totals.
        _, inverse = np.unique(["A", "B", "A", "C"], return_inverse=True)
        collapse = sparse.csr_matrix((np.ones(4), (np.arange(4), inverse)), shape=(4, 3))
        collapsed = (matrix @ collapse).toarray()
        np.testing.assert_array_equal(collapsed, [[5, 0, 2], [0, 0, 0], [3, 9, 5], [7, 2, 0]])
        np.testing.assert_array_equal(collapsed.sum(1), dense.sum(1))

    def test_ulm_fixed_gene_background_is_chunk_invariant_and_matches_t_statistic(self):
        # Gene Z is zero only in the first chunk: dropping empty features would
        # silently change its gene-background universe and its ULM t statistic.
        data = pd.DataFrame([[2, 1, 0, 4, 2, 1, 0], [1, 3, 2, 0, 1, 5, 0], [3, 0, 1, 2, 5, 2, 7]], columns=list("ABCDEFZ"), index=["test_1", "test_2", "test_3"], dtype=float)
        net = pd.DataFrame({"source": ["TEST_TF"] * 3, "target": list("ABC"), "weight": [1.0, -1.0, 1.0]})
        cfg = {"min_targets": 2, "viper_pleiotropy": False}
        whole = workflow.score(data, net, "ulm", cfg)
        chunks = pd.concat([workflow.score(data.iloc[:2], net, "ulm", cfg), workflow.score(data.iloc[2:], net, "ulm", cfg)])
        pd.testing.assert_frame_equal(whole, chunks, atol=1e-6, rtol=1e-6)
        weights = np.array([1, -1, 1, 0, 0, 0, 0], dtype=float)
        expected = []
        for row in data.to_numpy():
            correlation = stats.pearsonr(weights, row).statistic
            expected.append(correlation * np.sqrt((len(row) - 2) / (1 - correlation ** 2)))
        np.testing.assert_allclose(whole["TEST_TF"], expected, atol=1e-6, rtol=1e-6)


if __name__ == "__main__":
    unittest.main()
