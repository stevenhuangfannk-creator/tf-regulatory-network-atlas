"""Run the real case in order; fail immediately on any unsuccessful stage."""
import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rscript", default=shutil.which("Rscript"), help="Rscript executable; R_LIBS selects isolated libraries")
    parser.add_argument("--figures-only", action="store_true", help="Regenerate real figures from existing result tables")
    args = parser.parse_args()
    if not args.rscript:
        parser.error("Rscript is required; provide --rscript or put it on PATH")
    for name in ["OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMBA_NUM_THREADS"]:
        os.environ.setdefault(name, "2")
    commands = []
    if not args.figures_only:
        commands = [
            [sys.executable, "scripts/download_inputs.py"],
            [sys.executable, "workflows/periodontal_tf.py"],
            [args.rscript, "methods/viper/run_viper.R"],
            [sys.executable, "workflows/validate_viper.py"],
            [sys.executable, "workflows/pathway_context.py"],
            [sys.executable, "workflows/expression_activity.py"],
            [sys.executable, "workflows/regulon_sensitivity.py"],
            [sys.executable, "scripts/build_report.py"],
        ]
    commands += [[args.rscript, "scripts/plot_atlas.R"], [sys.executable, "scripts/run_tests.py"]]
    for command in commands:
        print("Running", " ".join(command[1:]), flush=True)
        subprocess.run(command, cwd=ROOT, check=True)

if __name__ == "__main__":
    main()
