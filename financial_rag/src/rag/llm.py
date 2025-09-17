"""LLM wrapper scaffold."""

from typing import List

class FinancialLLM:
    def __init__(self, config: dict):
        self.config = config
        # TODO: initialize OpenAI / other LLM clients and prompt templates

    def analyze(self, question: str, context: List[str], language: str = "en") -> str:
        """Return an analysis string synthesizing context (placeholder)."""
        # TODO: call LLM with appropriate prompt templates
        return "LLM analysis stub"