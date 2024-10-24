from typing import List, Tuple, Union

import pytest

from bg3.classes import Class, SubClass
from bg3.levelling_progression import (
    FIGHTING_STYLE_KNOWN_AT_LEVELS,
    SPELLS_KNOWN_AT_LEVELS,
    CantripToChoose,
    SpellToChoose,
)


@pytest.mark.parametrize(
    ("class_or_subclass", "expected_spell_progression"),
    [
        (
            Class.BARD,
            [
                (2, 4),
                (2, 5),
                (2, 6),
                (3, 7),
                (3, 8),
                (3, 9),
                (3, 10),
                (3, 11),
                (3, 12),
                (4, 13),
                (4, 14),
                (4, 15),
            ],
        ),
        (
            SubClass.ELDRITCH_KNIGHT,
            [
                (0, 0),
                (0, 0),
                (2, 3),
                (2, 4),
                (2, 4),
                (2, 4),
                (2, 5),
                (2, 6),
                (2, 6),
                (3, 7),
                (3, 8),
                (3, 8),
            ],
        ),
        (
            Class.SORCERER,
            [
                (4, 2),
                (4, 3),
                (4, 4),
                (5, 5),
                (5, 6),
                (5, 7),
                (5, 8),
                (5, 9),
                (5, 10),
                (6, 11),
                (6, 12),
                (6, 13),
            ],
        ),
        (
            Class.RANGER,
            [
                (0, 0),
                (0, 2),
                (0, 3),
                (0, 3),
                (0, 4),
                (0, 4),
                (0, 5),
                (0, 5),
                (0, 6),
                (0, 6),
                (0, 7),
                (0, 7),
            ],
        ),
        (
            SubClass.ARCANE_TRICKSTER,
            [
                (0, 0),
                (0, 0),
                (2, 3),
                (2, 4),
                (2, 4),
                (2, 4),
                (2, 5),
                (2, 6),
                (2, 6),
                (3, 7),
                (3, 8),
                (3, 8),
            ],
        ),
        (
            Class.WARLOCK,
            [
                (2, 2),
                (2, 3),
                (2, 4),
                (3, 5),
                (3, 6),
                (3, 7),
                (3, 8),
                (3, 9),
                (3, 10),
                (4, 11),
                (4, 12),
                (4, 13),
            ],
        ),
        (
            Class.WIZARD,
            [
                (3, 6),
                (3, 8),
                (3, 10),
                (4, 12),
                (4, 14),
                (4, 16),
                (4, 18),
                (4, 20),
                (4, 22),
                (5, 24),
                (5, 26),
                (5, 28),
            ],
        ),
    ],
)
def test_number_of_spells_known_learner(
    class_or_subclass: Union[Class, SubClass], expected_spell_progression: List[Tuple[int, int]]
) -> None:
    number_of_cumulative_spells_known: List[Tuple[int, int]] = []

    number_of_cantrips_known = 0
    number_of_spells_known = 0

    for new_spells in SPELLS_KNOWN_AT_LEVELS[class_or_subclass]:
        for spell in new_spells:
            if isinstance(spell, SpellToChoose):
                number_of_spells_known += spell.amount
            elif isinstance(spell, CantripToChoose):
                number_of_cantrips_known += spell.amount
            else:
                raise ValueError(f"Unknown spell type: {spell}")

        number_of_cumulative_spells_known.append((number_of_cantrips_known, number_of_spells_known))

    assert len(number_of_cumulative_spells_known) == 12
    assert number_of_cumulative_spells_known == expected_spell_progression


def test_fighting_style() -> None:
    assert len(FIGHTING_STYLE_KNOWN_AT_LEVELS) == 5

    assert FIGHTING_STYLE_KNOWN_AT_LEVELS[SubClass.COLLEGE_OF_SWORDS].level == 3
    assert len(FIGHTING_STYLE_KNOWN_AT_LEVELS[SubClass.COLLEGE_OF_SWORDS].choices) == 2

    assert FIGHTING_STYLE_KNOWN_AT_LEVELS[Class.FIGHTER].level == 1
    assert len(FIGHTING_STYLE_KNOWN_AT_LEVELS[Class.FIGHTER].choices) == 6

    assert FIGHTING_STYLE_KNOWN_AT_LEVELS[SubClass.CHAMPION].level == 10
    assert len(FIGHTING_STYLE_KNOWN_AT_LEVELS[SubClass.CHAMPION].choices) == 6

    assert FIGHTING_STYLE_KNOWN_AT_LEVELS[Class.PALADIN].level == 2
    assert len(FIGHTING_STYLE_KNOWN_AT_LEVELS[Class.PALADIN].choices) == 4

    assert FIGHTING_STYLE_KNOWN_AT_LEVELS[Class.RANGER].level == 2
    assert len(FIGHTING_STYLE_KNOWN_AT_LEVELS[Class.RANGER].choices) == 4
