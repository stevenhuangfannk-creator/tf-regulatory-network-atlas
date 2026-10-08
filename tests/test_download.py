"""Regression test for the observed early-EOF download, using test-only bytes."""
import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("download_inputs", ROOT / "scripts/download_inputs.py")
download_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(download_module)

class DownloadRegression(unittest.TestCase):
    def test_truncated_download_resumes_correct_range(self):
        class Response:
            def __init__(self, status, payload, headers):
                self.status_code, self.payload, self.headers = status, payload, headers
            def __enter__(self):
                return self
            def __exit__(self, *args):
                pass
            def raise_for_status(self):
                pass
            def iter_content(self, chunk_size):
                yield self.payload
        responses = [Response(200, b"01234", {"Content-Length": "10"}), Response(206, b"56789", {"Content-Range": "bytes 5-9/10", "Content-Length": "5"})]
        with tempfile.TemporaryDirectory() as temporary, patch.object(download_module.requests, "get", side_effect=responses) as get:
            path = Path(temporary) / "test_input.bin"
            download_module.download("https://test.invalid/fixture", path, 10)
            self.assertEqual(path.read_bytes(), b"0123456789")
            self.assertEqual(get.call_args_list[1].kwargs["headers"], {"Range": "bytes=5-"})
            self.assertFalse(path.with_suffix(".bin.part").exists())

if __name__ == "__main__":
    unittest.main()
