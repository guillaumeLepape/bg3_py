from typing import Dict, List, Tuple

import pytest

from bg3.classes import Class
from bg3.spell_slot import compute_spell_slot_from_classes
from bg3.subclass import Subclass, eldricht_knight, gloom_stalker, the_fiend


@pytest.mark.parametrize(
    ("classes", "subclasses", "spell_slots"),
    [
        ([Class.RANGER], {}, ((0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0))),
        ([Class.RANGER, Class.RANGER], {}, ((2, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0))),
        (
            [Class.FIGHTER, Class.FIGHTER, Class.FIGHTER],
            {Class.FIGHTER: eldricht_knight},
            ((2, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0)),
        ),
        (
            [
                Class.FIGHTER,
                Class.FIGHTER,
                Class.FIGHTER,
                Class.FIGHTER,
                Class.FIGHTER,
                Class.FIGHTER,
                Class.FIGHTER,
            ],
            {Class.FIGHTER: eldricht_knight},
            ((4, 2, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0)),
        ),
        (
            [
                Class.WARLOCK,
                Class.WARLOCK,
                Class.WARLOCK,
                Class.WARLOCK,
                Class.WARLOCK,
                Class.WARLOCK,
                Class.WARLOCK,
                Class.RANGER,
                Class.RANGER,
                Class.RANGER,
                Class.RANGER,
                Class.RANGER,
            ],
            {Class.WARLOCK: the_fiend, Class.RANGER: gloom_stalker},
            ((4, 2, 0, 0, 0, 0), (0, 0, 0, 2, 0, 0)),
        ),
    ],
)
def test_spell_slots_computation(
    classes: List[Class],
    subclasses: Dict[Class, Subclass],
    spell_slots: Tuple[Tuple[int, int, int, int, int, int], Tuple[int, int, int, int, int, int]],
) -> None:
    assert compute_spell_slot_from_classes(classes, subclasses) == spell_slots
