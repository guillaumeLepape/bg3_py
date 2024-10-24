from pathlib import Path
from typing import List

from bg3.classes import Class
from bg3.spell_new import Spell, Spells


def is_spell_from_class(spell: Spell, class_: Class) -> bool:
    for spell_class in spell.how_to_learn.classes:
        if spell_class.name == class_:
            return True

    return False


def is_spell_from_class_or_subclass(spell: Spell, class_: Class) -> bool:
    return is_spell_from_class(spell, class_)


def overlapping_spells(spells: List[Spell], class1: Class, class2: Class) -> None:
    class1_spells = [spell for spell in spells if is_spell_from_class_or_subclass(spell, class1)]

    header = f"-------------------- {class1.value} / {class2.value} -----------------------"

    print(header)

    print(f"Number of {class1.value} spells: {len(class1_spells)}")

    class2_spells = [spell for spell in spells if is_spell_from_class_or_subclass(spell, class2)]

    print(f"Number of {class2.value} spells: {len(class2_spells)}")
    print()

    class1_spells_set = set(spell.name for spell in class1_spells)
    class2_spells_set = set(spell.name for spell in class2_spells)

    common_spells = class1_spells_set & class2_spells_set

    print(f"Number of spells in common: {len(common_spells)}")
    print(f"Spells in common: {', '.join(common_spells)}")
    print()

    print(
        f"{class1.value} spells not {class2.value} "
        f"spells: {', '.join(class1_spells_set - class2_spells_set)}"
    )
    print()

    print(
        f"{class2.value} spells not {class1.value} "
        f"spells: {', '.join(class2_spells_set - class1_spells_set)}"
    )
    print(len(header) * "-")
    print()


def class_most_spells(spells: List[Spell]) -> None:
    print("---------------------- Classes with most spells ---------------------------")

    class_to_number_of_spells = {}

    for class_ in Class:
        class_to_number_of_spells[class_] = sum(
            1 for spell in spells if is_spell_from_class(spell, class_)
        )

    for class_, number_of_spells in sorted(
        class_to_number_of_spells.items(), key=lambda key_value: key_value[1], reverse=True
    ):
        print(f"{class_.value}: {number_of_spells}")

    print("---------------------------------------------------------------------------")


def main(class1: Class, class2: Class) -> int:
    spells = Spells.model_validate_json((Path(__file__).parent / "spells.json").read_text())

    overlapping_spells(spells.spells, class1, class2)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
