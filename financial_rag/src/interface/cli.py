"""CLI entrypoint using click (stub)."""

import click
from ..rag.core import FinancialRAG

@click.group()
@click.option("--config", default="config/config.yaml", help="Path to config")
@click.pass_context
def main(ctx, config):
    ctx.obj = {"config": config, "rag": FinancialRAG()}

@main.command()
@click.argument("query")
@click.option("--language", default="en")
@click.pass_context
def query(ctx, query, language):
    rag: FinancialRAG = ctx.obj["rag"]
    res = rag.process_query(query, language)
    click.echo(res.answer)

if __name__ == "__main__":
    main()