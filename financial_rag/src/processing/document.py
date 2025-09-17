"""Document processing utilities (stub)."""

from pathlib import Path
from typing import List, Dict

class DocumentProcessor:
    def process_file(self, path: str, language: str = "en") -> List[Dict]:
        """Extract text/chunks from a file path (PDF/HTML/txt) - placeholder."""
        p = Path(path)
        return [{"content": f"Stub content for {p.name}", "metadata": {"source": str(p), "language": language}}]