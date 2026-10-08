"""Contracts for the actual source files, donor replication and derived tables."""
import hashlib
import json
import unittest
from pathlib import Path

import h5py
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]


class DataContracts(unittest.TestCase):
    @unittest.skipUnless((ROOT / "data/raw/periodontal_atlas.h5ad").exists() and (ROOT / "data/cache/collectri.csv").exists(), "Large local source inputs are not included in Git")
    def test_input_hashes_match_actual_files(self):
        for name, record in json.loads((ROOT / "data/input_manifest.json").read_text()).items():
            with self.subTest(input=name):
                path = ROOT / record["path"]
                self.assertEqual(path.stat().st_size, record["bytes"])
                digest = hashlib.sha256()
                with path.open("rb") as stream:
                    for block in iter(lambda: stream.read(8 * 1024 * 1024), b""):
                        digest.update(block)
                self.assertEqual(digest.hexdigest(), record["sha256"])

    def test_donor_mapping_preserves_condition_and_repeated_biopsies(self):
        mapping = pd.read_csv(ROOT / "data/donor_map.csv")
        self.assertTrue(mapping.sample_id.is_unique)
        self.assertEqual(mapping.groupby("biological_donor").condition.nunique().max(), 1)
        self.assertEqual(mapping.groupby("biological_donor").assay.nunique().max(), 1)
        self.assertEqual(mapping.groupby("condition").biological_donor.nunique().to_dict(), {"normal": 13, "periodontitis": 5})
        for prefix, number in [("PD161", 2), ("PD164", 3)]:
            rows = mapping[mapping.sample_title.str.startswith(prefix)]
            self.assertEqual(len(rows), number)
            self.assertEqual(set(rows.biological_donor), {prefix})
            self.assertFalse(rows.verified.any())

    def test_cell_counts_match_donor_pseudobulk_without_pseudoreplication(self):
        samples = pd.read_csv(ROOT / "results/tables/pseudobulk_metadata.csv").set_index("sample")
        cells = pd.read_csv(ROOT / "results/tables/cells.csv.gz", usecols=["cell_id", "sample_id", "donor", "condition", "cell_type"])
        mapping = pd.read_csv(ROOT / "data/donor_map.csv").set_index("sample_id")
        cfg = json.loads((ROOT / "config/analysis.json").read_text())
        self.assertTrue(cells.cell_id.is_unique)
        self.assertTrue((cells.donor == cells.sample_id.map(mapping.biological_donor)).all())
        self.assertTrue((cells.condition == cells.sample_id.map(mapping.condition).map({"normal": "Healthy", "periodontitis": "Periodontitis"})).all())
        counts = cells.groupby(cells.donor + "|" + cells.cell_type).size().sort_index()
        pd.testing.assert_series_equal(counts, samples.n_cells.sort_index(), check_names=False)
        self.assertTrue((samples.n_cells >= cfg["min_cells_per_donor_celltype"]).all())
        self.assertEqual(len(samples), 46)
        self.assertEqual(int(samples.n_cells.sum()), len(cells))
        for cell_type, group in samples.groupby("cell_type"):
            self.assertGreaterEqual(group.groupby("condition").donor.nunique().min(), cfg["min_donors_per_condition"], cell_type)

    @unittest.skipUnless((ROOT / "data/local/pseudobulk_counts.npz").exists() and (ROOT / "data/raw/periodontal_atlas.h5ad").exists() and (ROOT / "data/cache/collectri.csv").exists(), "Raw-input integration contracts require local data")
    def test_regulon_coverage_and_finite_activity(self):
        coverage = pd.read_csv(ROOT / "results/tables/regulon_coverage.csv").set_index("tf")
        with np.load(ROOT / "data/local/pseudobulk_counts.npz") as archive:
            genes, counts = archive["genes"], archive["counts"]
        net = pd.read_csv(ROOT / "data/cache/collectri.csv").drop_duplicates(["source", "target"]).dropna(subset=["source", "target", "weight"])
        present = net[net.target.isin(genes)].groupby("source").target.nunique()
        expected = present.reindex(coverage.index, fill_value=0)
        np.testing.assert_array_equal(coverage.n_targets_present, expected)
        np.testing.assert_allclose(coverage.coverage, coverage.n_targets_present / coverage.n_targets_total)
        threshold = json.loads((ROOT / "config/analysis.json").read_text())["min_targets"]
        for method in ["ulm", "viper"]:
            activity = pd.read_csv(ROOT / f"results/tables/{method}_activity_matrix.csv", index_col=0)
            self.assertTrue(np.isfinite(activity.to_numpy()).all())
            self.assertTrue((coverage.loc[activity.columns, "n_targets_present"] >= threshold).all())
        self.assertEqual(len(genes), len(np.unique(genes)))
        self.assertTrue((counts >= 0).all())
        np.testing.assert_array_equal(counts, np.rint(counts))
        with h5py.File(ROOT / "data/raw/periodontal_atlas.h5ad", "r") as handle:
            names = handle["raw/var/feature_name"]
            original = names["categories"].asstr()[:][names["codes"][:]] if isinstance(names, h5py.Group) else names.asstr()[:]
        run = json.loads((ROOT / "reports/run_manifest.json").read_text())
        self.assertEqual(run["genes_original"], len(original))
        self.assertEqual(run["genes_unique"], len(np.unique(original)))
        self.assertEqual(run["genes_original"] - run["genes_unique"], 9)


if __name__ == "__main__":
    unittest.main()
