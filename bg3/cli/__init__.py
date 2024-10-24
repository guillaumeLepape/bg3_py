import asyncio

import typer

from bg3.classes import Class

from .build_spell_list import main as build_spells_list_main
from .overlapping_spells import main as overlapping_spells_main

app = typer.Typer()


@app.command()
def build_spells_list() -> None:
    asyncio.run(build_spells_list_main())


@app.command()
def overlapping_spells(class1: Class, class2: Class) -> None:
    overlapping_spells_main(class1, class2)


if __name__ == "__main__":
    app()
