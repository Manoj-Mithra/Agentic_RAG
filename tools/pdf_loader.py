from __future__ import annotations

from pathlib import Path

import fitz

from core.schemas import DocumentChunk, SourceType
from tools.text_splitter import split_pages


def load_pdf(path: str | Path) -> list[DocumentChunk]:
    pdf_path = Path(path)
    pages: list[tuple[int, str]] = []
    try:
        with fitz.open(pdf_path) as doc:
            for page_index, page in enumerate(doc, start=1):
                text = page.get_text("text")
                if text.strip():
                    pages.append((page_index, text))
    except Exception as exc:
        raise RuntimeError(f"Could not parse PDF '{pdf_path.name}': {exc}") from exc

    return split_pages(
        pages,
        source=pdf_path.name,
        source_type=SourceType.UPLOAD,
        metadata={"path": str(pdf_path), "document_name": pdf_path.name},
    )
