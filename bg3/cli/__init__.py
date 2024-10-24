import asyncio

import typer

from .build_spell_list import main as build_spells_list_main

app = typer.Typer()


@app.command()
def test() -> None:
    typer.echo("Test command")


@app.command()
def build_spells_list() -> None:
    asyncio.run(build_spells_list_main())


if __name__ == "__main__":
    app()
