"""Record the actual test runner outcome, including raw-input skips in CI."""
import json
import time
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
started = time.monotonic()
suite = unittest.defaultTestLoader.discover(str(ROOT / "tests"))
result = unittest.TextTestRunner(verbosity=2).run(suite)
report = {"command": "python scripts/run_tests.py", "status": "PASS" if result.wasSuccessful() else "FAIL", "tests_run": result.testsRun, "failures": len(result.failures), "errors": len(result.errors), "skipped": len(result.skipped), "skip_reasons": [reason for _, reason in result.skipped], "seconds": time.monotonic() - started, "unit_fixture_policy": "Synthetic bytes/arrays are used only in numerical/download regression unit tests, never for scientific figures", "limit": "Tests check data/numeric contracts; large ignored inputs are skipped when missing, not silently declared validated"}
(ROOT / "reports/test_status.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
raise SystemExit(0 if result.wasSuccessful() else 1)
