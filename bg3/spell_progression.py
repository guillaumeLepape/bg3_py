from typing import Callable, Dict, List, Tuple, Union

from pydantic import BaseModel, ConfigDict

from .classes import Class, SubClass
from .spell_new import SchoolOfMagic, Spell


class CantripToChoose(BaseModel):
    amount: int

    model_config = ConfigDict(extra="forbid")


class SpellToChoose(BaseModel):
    criteria: Callable[[Spell], bool]
    amount: int

    model_config = ConfigDict(extra="forbid")


class AllSpell(BaseModel):
    criteria: Callable[[Spell], bool]

    model_config = ConfigDict(extra="forbid")


def max_level_criteria(max_level: int) -> Callable[[Spell], bool]:
    def func(spell: Spell) -> bool:
        return spell.level <= max_level

    return func


def school_of_magic_criteria(school: SchoolOfMagic) -> Callable[["Spell"], bool]:
    def func(spell: Spell) -> bool:
        return spell.school == school

    return func


def or_(
    criteria1: Callable[[Spell], bool], criteria2: Callable[[Spell], bool]
) -> Callable[[Spell], bool]:
    def func(spell: Spell) -> bool:
        return criteria1(spell) or criteria2(spell)

    return func


def and_(
    criteria1: Callable[[Spell], bool], criteria2: Callable[[Spell], bool]
) -> Callable[[Spell], bool]:
    def func(spell: Spell) -> bool:
        return criteria1(spell) and criteria2(spell)

    return func


def enchantment_or_illusion_criteria(level: int) -> Callable[[Spell], bool]:
    return and_(
        max_level_criteria(level),
        or_(
            school_of_magic_criteria(SchoolOfMagic.ENCHANTMENT),
            school_of_magic_criteria(SchoolOfMagic.ILLUSION),
        ),
    )


LevellingSpell = Tuple[
    List[Union[CantripToChoose, SpellToChoose, AllSpell]],
    List[Union[CantripToChoose, SpellToChoose, AllSpell]],
    List[Union[CantripToChoose, SpellToChoose, AllSpell]],
    List[Union[CantripToChoose, SpellToChoose, AllSpell]],
    List[Union[CantripToChoose, SpellToChoose, AllSpell]],
    List[Union[CantripToChoose, SpellToChoose, AllSpell]],
    List[Union[CantripToChoose, SpellToChoose, AllSpell]],
    List[Union[CantripToChoose, SpellToChoose, AllSpell]],
    List[Union[CantripToChoose, SpellToChoose, AllSpell]],
    List[Union[CantripToChoose, SpellToChoose, AllSpell]],
    List[Union[CantripToChoose, SpellToChoose, AllSpell]],
    List[Union[CantripToChoose, SpellToChoose, AllSpell]],
]


SPELLS_KNOWN_AT_LEVELS: Dict[Union[Class, SubClass], LevellingSpell] = {
    Class.BARD: (
        [SpellToChoose(criteria=max_level_criteria(1), amount=4), CantripToChoose(amount=2)],
        [SpellToChoose(criteria=max_level_criteria(1), amount=1)],
        [SpellToChoose(criteria=max_level_criteria(2), amount=1)],
        [SpellToChoose(criteria=max_level_criteria(2), amount=1), CantripToChoose(amount=1)],
        [SpellToChoose(criteria=max_level_criteria(3), amount=1)],
        [SpellToChoose(criteria=max_level_criteria(3), amount=1)],
        [SpellToChoose(criteria=max_level_criteria(4), amount=1)],
        [SpellToChoose(criteria=max_level_criteria(4), amount=1)],
        [SpellToChoose(criteria=max_level_criteria(5), amount=1)],
        [SpellToChoose(criteria=max_level_criteria(5), amount=1), CantripToChoose(amount=1)],
        [SpellToChoose(criteria=max_level_criteria(6), amount=1)],
        [SpellToChoose(criteria=max_level_criteria(6), amount=1)],
    ),
    Class.CLERIC: (
        [AllSpell(criteria=max_level_criteria(1)), CantripToChoose(amount=3)],
        [],
        [AllSpell(criteria=max_level_criteria(2))],
        [CantripToChoose(amount=1)],
        [AllSpell(criteria=max_level_criteria(3))],
        [],
        [AllSpell(criteria=max_level_criteria(4))],
        [],
        [AllSpell(criteria=max_level_criteria(5))],
        [CantripToChoose(amount=1)],
        [AllSpell(criteria=max_level_criteria(6))],
        [],
    ),
    Class.DRUID: (
        [AllSpell(criteria=max_level_criteria(1)), CantripToChoose(amount=2)],
        [],
        [AllSpell(criteria=max_level_criteria(2))],
        [CantripToChoose(amount=1)],
        [AllSpell(criteria=max_level_criteria(3))],
        [],
        [AllSpell(criteria=max_level_criteria(4))],
        [],
        [AllSpell(criteria=max_level_criteria(5))],
        [CantripToChoose(amount=1)],
        [AllSpell(criteria=max_level_criteria(6))],
        [],
    ),
    SubClass.ELDRITCH_KNIGHT: (
        [],
        [],
        [
            SpellToChoose(criteria=enchantment_or_illusion_criteria(1), amount=2),
            SpellToChoose(criteria=max_level_criteria(1), amount=1),
            CantripToChoose(amount=2),
        ],
        [SpellToChoose(criteria=enchantment_or_illusion_criteria(1), amount=1)],
        [],
        [],
        [SpellToChoose(criteria=enchantment_or_illusion_criteria(2), amount=1)],
        [SpellToChoose(criteria=max_level_criteria(2), amount=1)],
        [],
        [
            SpellToChoose(criteria=enchantment_or_illusion_criteria(2), amount=1),
            CantripToChoose(amount=1),
        ],
        [SpellToChoose(criteria=enchantment_or_illusion_criteria(2), amount=1)],
        [],
    ),
    Class.PALADIN: (
        [AllSpell(criteria=max_level_criteria(1))],
        [],
        [],
        [],
        [AllSpell(criteria=max_level_criteria(2))],
        [],
        [],
        [],
        [AllSpell(criteria=max_level_criteria(3))],
        [],
        [],
        [],
    ),
    Class.RANGER: (
        [],
        [SpellToChoose(criteria=max_level_criteria(1), amount=2)],
        [SpellToChoose(criteria=max_level_criteria(1), amount=1)],
        [],
        [SpellToChoose(criteria=max_level_criteria(2), amount=1)],
        [],
        [SpellToChoose(criteria=max_level_criteria(2), amount=1)],
        [],
        [SpellToChoose(criteria=max_level_criteria(3), amount=1)],
        [],
        [SpellToChoose(criteria=max_level_criteria(3), amount=1)],
        [],
    ),
    SubClass.ARCANE_TRICKSTER: (
        [],
        [],
        [
            SpellToChoose(criteria=enchantment_or_illusion_criteria(1), amount=2),
            SpellToChoose(criteria=max_level_criteria(1), amount=1),
            CantripToChoose(amount=2),
        ],
        [SpellToChoose(criteria=enchantment_or_illusion_criteria(1), amount=1)],
        [],
        [],
        [SpellToChoose(criteria=enchantment_or_illusion_criteria(2), amount=1)],
        [SpellToChoose(criteria=enchantment_or_illusion_criteria(2), amount=1)],
        [],
        [
            SpellToChoose(criteria=enchantment_or_illusion_criteria(2), amount=1),
            CantripToChoose(amount=1),
        ],
        [SpellToChoose(criteria=enchantment_or_illusion_criteria(2), amount=1)],
        [],
    ),
    Class.SORCERER: (
        [SpellToChoose(criteria=max_level_criteria(1), amount=2), CantripToChoose(amount=4)],
        [SpellToChoose(criteria=max_level_criteria(1), amount=1)],
        [SpellToChoose(criteria=max_level_criteria(2), amount=1)],
        [SpellToChoose(criteria=max_level_criteria(2), amount=1), CantripToChoose(amount=1)],
        [SpellToChoose(criteria=max_level_criteria(3), amount=1)],
        [SpellToChoose(criteria=max_level_criteria(3), amount=1)],
        [SpellToChoose(criteria=max_level_criteria(4), amount=1)],
        [SpellToChoose(criteria=max_level_criteria(4), amount=1)],
        [SpellToChoose(criteria=max_level_criteria(5), amount=1)],
        [SpellToChoose(criteria=max_level_criteria(5), amount=1), CantripToChoose(amount=1)],
        [SpellToChoose(criteria=max_level_criteria(6), amount=1)],
        [SpellToChoose(criteria=max_level_criteria(6), amount=1)],
    ),
    Class.WARLOCK: (
        [SpellToChoose(criteria=max_level_criteria(1), amount=2), CantripToChoose(amount=2)],
        [SpellToChoose(criteria=max_level_criteria(1), amount=1)],
        [SpellToChoose(criteria=max_level_criteria(2), amount=1)],
        [SpellToChoose(criteria=max_level_criteria(2), amount=1), CantripToChoose(amount=1)],
        [SpellToChoose(criteria=max_level_criteria(3), amount=1)],
        [SpellToChoose(criteria=max_level_criteria(3), amount=1)],
        [SpellToChoose(criteria=max_level_criteria(4), amount=1)],
        [SpellToChoose(criteria=max_level_criteria(4), amount=1)],
        [SpellToChoose(criteria=max_level_criteria(5), amount=1)],
        [SpellToChoose(criteria=max_level_criteria(5), amount=1), CantripToChoose(amount=1)],
        [SpellToChoose(criteria=max_level_criteria(6), amount=1)],
        [SpellToChoose(criteria=max_level_criteria(6), amount=1)],
    ),
    Class.WIZARD: (
        [SpellToChoose(criteria=max_level_criteria(1), amount=6), CantripToChoose(amount=3)],
        [SpellToChoose(criteria=max_level_criteria(1), amount=2)],
        [SpellToChoose(criteria=max_level_criteria(2), amount=2)],
        [SpellToChoose(criteria=max_level_criteria(2), amount=2), CantripToChoose(amount=1)],
        [SpellToChoose(criteria=max_level_criteria(3), amount=2)],
        [SpellToChoose(criteria=max_level_criteria(3), amount=2)],
        [SpellToChoose(criteria=max_level_criteria(4), amount=2)],
        [SpellToChoose(criteria=max_level_criteria(4), amount=2)],
        [SpellToChoose(criteria=max_level_criteria(5), amount=2)],
        [SpellToChoose(criteria=max_level_criteria(5), amount=2), CantripToChoose(amount=1)],
        [SpellToChoose(criteria=max_level_criteria(6), amount=2)],
        [SpellToChoose(criteria=max_level_criteria(6), amount=2)],
    ),
}
