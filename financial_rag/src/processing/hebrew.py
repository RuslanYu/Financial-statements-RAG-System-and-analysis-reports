"""Hebrew text helpers (stub)."""

import re

class HebrewUtils:
    @staticmethod
    def is_hebrew(text: str) -> bool:
        return any("\u0590" <= c <= "\u05FF" for c in text)

    @staticmethod
    def normalize(text: str) -> str:
        # Basic normalization: trim and collapse whitespace
        return re.sub(r"\s+", " ", text).strip()