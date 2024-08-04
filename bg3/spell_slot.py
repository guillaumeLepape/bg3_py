from enum import Enum
from math import floor
from typing import Dict, List, Tuple

from .classes import Class
from .subclass import Subclass, arcane_trickster, eldricht_knight


class SpellCasting(Enum):
    NONE = 0
    FULL_CASTER = 1
    HALF_CASTER = 2
    SEMI_CASTER = 3
    WARLOCK_CASTER = 4


def get_spell_casting_ability(class_name: Class, subclasses: Dict[Class, Subclass]) -> SpellCasting:
    if (
        class_name == Class.BARD
        or class_name == Class.CLERIC
        or class_name == Class.DRUID
        or class_name == Class.SORCERER
        or class_name == Class.WIZARD
    ):
        return SpellCasting.FULL_CASTER

    if class_name == Class.PALADIN or class_name == Class.RANGER:
        return SpellCasting.HALF_CASTER

    if class_name == Class.WARLOCK:
        return SpellCasting.WARLOCK_CASTER

    if (
        class_name == Class.FIGHTER
        and Class.FIGHTER in subclasses
        and subclasses[Class.FIGHTER] == eldricht_knight
    ) or (
        class_name == Class.ROGUE
        and Class.ROGUE in subclasses
        and subclasses[Class.ROGUE] == arcane_trickster
    ):
        return SpellCasting.SEMI_CASTER

    return SpellCasting.NONE


def totale_classes_without_warlock(classes: List[Class]) -> int:
    return len(set(classes) - {Class.WARLOCK})


def compute_spell_slots(effective_level: int) -> Tuple[int, int, int, int, int, int]:
    if effective_level == 0:
        return (0, 0, 0, 0, 0, 0)
    elif effective_level == 1:
        return (2, 0, 0, 0, 0, 0)
    elif effective_level == 2:
        return (3, 0, 0, 0, 0, 0)
    elif effective_level == 3:
        return (4, 2, 0, 0, 0, 0)
    elif effective_level == 4:
        return (4, 3, 0, 0, 0, 0)
    elif effective_level == 5:
        return (4, 3, 2, 0, 0, 0)
    elif effective_level == 6:
        return (4, 3, 3, 0, 0, 0)
    elif effective_level == 7:
        return (4, 3, 3, 1, 0, 0)
    elif effective_level == 8:
        return (4, 3, 3, 2, 0, 0)
    elif effective_level == 9:
        return (4, 3, 3, 3, 1, 0)
    elif effective_level == 10:
        return (4, 3, 3, 3, 2, 0)
    elif effective_level == 11:
        return (4, 3, 3, 3, 2, 1)
    else:
        return (4, 3, 3, 3, 2, 1)


def compute_warlock_spell_slots(warlock_level: int) -> Tuple[int, int, int, int, int, int]:
    if warlock_level == 0:
        return (0, 0, 0, 0, 0, 0)
    elif warlock_level == 1:
        return (1, 0, 0, 0, 0, 0)
    elif warlock_level == 2:
        return (2, 0, 0, 0, 0, 0)
    elif warlock_level == 3:
        return (0, 2, 0, 0, 0, 0)
    elif warlock_level == 4:
        return (0, 2, 0, 0, 0, 0)
    elif warlock_level == 5:
        return (0, 0, 2, 0, 0, 0)
    elif warlock_level == 6:
        return (0, 0, 2, 0, 0, 0)
    elif warlock_level == 7:
        return (0, 0, 0, 2, 0, 0)
    elif warlock_level == 8:
        return (0, 0, 0, 2, 0, 0)
    elif warlock_level == 9:
        return (0, 0, 0, 0, 2, 0)
    elif warlock_level == 10:
        return (0, 0, 0, 0, 2, 0)
    elif warlock_level == 11:
        return (0, 0, 0, 0, 3, 0)
    else:
        return (0, 0, 0, 0, 3, 0)


def compute_spell_slot_from_classes(
    classes: List[Class], subclasses: Dict[Class, Subclass]
) -> Tuple[Tuple[int, int, int, int, int, int], Tuple[int, int, int, int, int, int]]:
    effective_level = 0
    half_levels = 0.0
    semi_levels = 0.0
    total_classes = totale_classes_without_warlock(classes)

    for class_name in classes:
        spell_casting_ability = get_spell_casting_ability(class_name, subclasses)

        if spell_casting_ability == SpellCasting.FULL_CASTER:
            effective_level += 1

        if spell_casting_ability == SpellCasting.HALF_CASTER:
            half_levels += 0.5

        if spell_casting_ability == SpellCasting.SEMI_CASTER:
            semi_levels += 0.33334

    if total_classes == 1 and half_levels > 0.5:
        half_levels += 0.5

    if total_classes == 1 and semi_levels > 0.7:
        semi_levels += 0.66666667

    effective_level += floor(half_levels) + floor(semi_levels)

    spells = compute_spell_slots(effective_level)

    warlock_spells = compute_warlock_spell_slots(classes.count(Class.WARLOCK))

    return spells, warlock_spells
