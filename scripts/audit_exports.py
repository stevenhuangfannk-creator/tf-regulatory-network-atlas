"""Inspect exported R artifacts without drawing or rerendering any figures."""
import json
import re
import struct
from pathlib import Path
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
figures = ROOT / "results/figures"
rows = []
for pdf in sorted(figures.glob("*.pdf")):
    with pymupdf.open(pdf) as document:
        spans = [s for page in document for b in page.get_text("dict")["blocks"] if b.get("type") == 0 for line in b["lines"] for s in line["spans"] if s["text"].strip()]
        minimum = min(s["size"] for s in spans)
        assert minimum >= 5, f"Effective font below 5pt: {pdf.name}"
        dimensions = [document[0].rect.width / 72 * 25.4, document[0].rect.height / 72 * 25.4]
    png = pdf.with_suffix(".png").read_bytes()
    assert png[:8] == b"\x89PNG\r\n\x1a\n"
    pos, dpi = 8, None
    while pos < len(png):
        length = struct.unpack(">I", png[pos:pos + 4])[0]
        kind, payload = png[pos + 4:pos + 8], png[pos + 8:pos + 8 + length]
        if kind == b"pHYs":
            x, y, unit = struct.unpack(">IIB", payload)
            if unit == 1:
                dpi = [x * .0254, y * .0254]
        pos += length + 12
    assert dpi and min(dpi) >= 599
    svg = pdf.with_suffix(".svg").read_text(encoding="utf-8")
    assert "<text" in svg, f"SVG text missing: {pdf.stem}"
    rows.append({"figure": pdf.stem, "minimum_effective_font_pt": minimum, "dimensions_mm": dimensions, "text_spans": len(spans), "png_dpi": dpi, "svg_editable_text": True})
assert len(rows) == 13, "This case requires thirteen actual figure bundles"
report = {"status": "PASS", "nonvisual_inspection": "Effective text spans account for Cairo normalized Tf=1 and text-matrix scaling; R is the only renderer", "figures": rows}
(ROOT / "reports/export_check.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
print("PASS: 13 R-exported PDF/SVG/600dpi PNG bundles; effective font >=5pt")
