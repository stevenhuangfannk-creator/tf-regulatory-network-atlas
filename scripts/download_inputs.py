"""Download immutable public inputs with streaming SHA256 verification."""
from pathlib import Path
import hashlib
import json
import requests

ROOT = Path(__file__).resolve().parents[1]
SOURCES = {
    "periodontal_atlas": ("https://datasets.cellxgene.cziscience.com/171607d7-dcc2-4993-9deb-bbc62cf13273.h5ad", "data/raw/periodontal_atlas.h5ad"),
    "collectri": ("https://zenodo.org/records/8192729/files/CollecTRI_regulons.csv?download=1", "data/cache/collectri.csv"),
}

def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def download(url, path, expected_size):
    partial = path.with_suffix(path.suffix + ".part")
    for attempt in range(3):
        offset = partial.stat().st_size if partial.exists() else 0
        if expected_size and offset == expected_size:
            partial.replace(path)
            return
        headers = {"Range": f"bytes={offset}-"} if offset else {}
        try:
            with requests.get(url, headers=headers, stream=True, timeout=(30, 120)) as response:
                response.raise_for_status()
                append = offset > 0 and response.status_code == 206
                if append and not response.headers.get("Content-Range", "").startswith(f"bytes {offset}-"):
                    raise ValueError("Unexpected byte range; do not concatenate unrelated data")
                total = expected_size or (offset if append else 0) + int(response.headers.get("Content-Length", 0))
                with partial.open("ab" if append else "wb") as target:
                    for chunk in response.iter_content(1024 * 1024):
                        target.write(chunk)
            if not total or partial.stat().st_size == total:
                partial.replace(path)
                return
            print(f"Incomplete input, resuming attempt {attempt + 2}: {partial.name}", flush=True)
        except requests.RequestException:
            if attempt == 2:
                raise
    raise RuntimeError(f"Incomplete download retained at {partial}; retry to resume")

def main():
    manifest_path = ROOT / "data/input_manifest.json"
    expected = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {}
    output = {}
    for key, (url, relative) in SOURCES.items():
        path = ROOT / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists():
            download(url, path, expected.get(key, {}).get("bytes"))
        digest = sha256(path)
        if key in expected and digest != expected[key]["sha256"]:
            raise ValueError(f"Checksum mismatch: {key}; immutable version changed or file incomplete")
        output[key] = {"url": url, "path": relative, "bytes": path.stat().st_size, "sha256": digest}
        print(key, path.stat().st_size, digest, flush=True)
    manifest_path.write_text(json.dumps(output, indent=2), encoding="utf-8")

if __name__ == "__main__":
    main()
