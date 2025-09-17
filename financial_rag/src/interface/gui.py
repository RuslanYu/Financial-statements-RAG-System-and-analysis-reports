"""Simple GUI entrypoint (stub)."""

import tkinter as tk

class FinancialRAGGUI:
    def __init__(self, config: dict):
        self.config = config

    def run(self):
        root = tk.Tk()
        root.title("Financial RAG — GUI stub")
        label = tk.Label(root, text="Financial Statements RAG System — GUI stub")
        label.pack(padx=20, pady=20)
        root.mainloop()

if __name__ == "__main__":
    FinancialRAGGUI({}).run()