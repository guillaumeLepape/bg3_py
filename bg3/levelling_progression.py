from typing import Callable, Dict, List, Tuple, Union

from pydantic import BaseModel, ConfigDict

from .background import Background
from .classes import Class, SubClass
from .favoured_enemy import (
    BOUNTY_HUNTER,
    FAVOURED_ENEMIES,
    KEEPER_OF_THE_VEIL,
    MAGE_BREAKER,
    RANGER_KNIGHT,
    SANCTIFIED_STALKER,
    FavouredEnemy,
)
from .fighting_style import (
    ARCHERY,
    DEFENCE,
    DUELLING,
    GREAT_WEAPON_FIGHTING,
    PROTECTION,
    TWO_WEAPON_FIGHTING,
    FightingStyle,
)
from .levelling import (
    BackgroundLevel,
    ClassLevel,
    HowToLearn,
    Race,
    RaceLevel,
    SubclassLevel,
    SubRaceLevel,
    Via,
)
from .natural_explorer import URBAN_TRACKER
from .races import SubRace
from .skill import Skill
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


def is_magical_secret(spell: Spell) -> bool:
    for class_level in spell.how_to_learn.classes:
        if class_level.name == Class.BARD and class_level.via == "magical_secrets":
            return True

    for subclass_level in spell.how_to_learn.subclasses:
        if (
            subclass_level.name == SubClass.COLLEGE_OF_LORE
            and subclass_level.via == "magical_secrets"
        ):
            return True

    return False


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

MAGICAL_SECRETS_KNOWN_AT_LEVELS: Dict[Union[Class, SubClass], LevellingSpell] = {
    Class.BARD: (
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [SpellToChoose(criteria=and_(max_level_criteria(5), is_magical_secret), amount=2)],
        [],
        [],
    ),
    SubClass.COLLEGE_OF_LORE: (
        [],
        [],
        [],
        [],
        [],
        [SpellToChoose(criteria=and_(max_level_criteria(3), is_magical_secret), amount=2)],
        [],
        [],
        [],
        [],
        [],
        [],
    ),
}


class FightingStyleToChoose(BaseModel):
    level: int
    choices: List[FightingStyle]


FIGHTING_STYLE_KNOWN_AT_LEVELS: Dict[Union[Class, SubClass], FightingStyleToChoose] = {
    SubClass.COLLEGE_OF_SWORDS: FightingStyleToChoose(
        level=3, choices=[DUELLING, TWO_WEAPON_FIGHTING]
    ),
    Class.FIGHTER: FightingStyleToChoose(
        level=1,
        choices=[
            ARCHERY,
            DEFENCE,
            DUELLING,
            GREAT_WEAPON_FIGHTING,
            PROTECTION,
            TWO_WEAPON_FIGHTING,
        ],
    ),
    SubClass.CHAMPION: FightingStyleToChoose(
        level=10,
        choices=[
            ARCHERY,
            DEFENCE,
            DUELLING,
            GREAT_WEAPON_FIGHTING,
            PROTECTION,
            TWO_WEAPON_FIGHTING,
        ],
    ),
    Class.PALADIN: FightingStyleToChoose(
        level=2, choices=[DEFENCE, DUELLING, GREAT_WEAPON_FIGHTING, PROTECTION]
    ),
    Class.RANGER: FightingStyleToChoose(
        level=2, choices=[ARCHERY, DEFENCE, DUELLING, TWO_WEAPON_FIGHTING]
    ),
}


class FavouredEnemyToChoose(BaseModel):
    level: List[int]
    choices: List[FavouredEnemy]


FAVOURED_ENEMY_KNOWN_AT_LEVELS: Dict[Union[Class], FavouredEnemyToChoose] = {
    Class.RANGER: FavouredEnemyToChoose(level=[1, 6, 10], choices=FAVOURED_ENEMIES),
}


SKILL_PROFICIENCY: Dict[Skill, HowToLearn] = {
    Skill.ATHLETICS: HowToLearn(
        classes=[
            ClassLevel(name=Class.BARBARIAN, level=1),
            ClassLevel(name=Class.BARD, level=1),
            ClassLevel(name=Class.FIGHTER, level=1),
            ClassLevel(name=Class.MONK, level=1),
            ClassLevel(name=Class.PALADIN, level=1),
            ClassLevel(name=Class.RANGER, level=1),
            ClassLevel(name=Class.ROGUE, level=1),
        ],
        subclasses=[],
        races=[],
        subraces=[],
        backgrounds=[
            BackgroundLevel(name=Background.OUTLANDER, level=1),
            BackgroundLevel(name=Background.SOLDIER, level=1),
        ],
    ),
    Skill.ACROBATICS: HowToLearn(
        classes=[
            ClassLevel(name=Class.BARD, level=1),
            ClassLevel(name=Class.FIGHTER, level=1),
            ClassLevel(name=Class.MONK, level=1),
            ClassLevel(name=Class.ROGUE, level=1),
        ],
        subclasses=[],
        races=[],
        subraces=[],
        backgrounds=[BackgroundLevel(name=Background.ENTERTAINER, level=1)],
    ),
    Skill.SLEIGHT_OF_HAND: HowToLearn(
        classes=[
            ClassLevel(name=Class.BARD, level=1),
            ClassLevel(name=Class.RANGER, level=1, via=Via(natural_explorer=URBAN_TRACKER)),
            ClassLevel(name=Class.ROGUE, level=1),
        ],
        subclasses=[],
        races=[],
        subraces=[],
        backgrounds=[
            BackgroundLevel(name=Background.CHARLATAN, level=1),
            BackgroundLevel(name=Background.URCHIN, level=1),
        ],
    ),
    Skill.STEALTH: HowToLearn(
        classes=[
            ClassLevel(name=Class.BARD, level=1),
            ClassLevel(name=Class.MONK, level=1),
            ClassLevel(name=Class.RANGER, level=1),
            ClassLevel(name=Class.ROGUE, level=1),
        ],
        subclasses=[],
        races=[],
        subraces=[
            SubRaceLevel(name=SubRace.WOOD_ELF, level=1),
            SubRaceLevel(name=SubRace.WOOD_HALF_ELF, level=1),
        ],
        backgrounds=[
            BackgroundLevel(name=Background.CRIMINAL, level=1),
            BackgroundLevel(name=Background.URCHIN, level=1),
        ],
    ),
    Skill.ARCANA: HowToLearn(
        classes=[
            ClassLevel(name=Class.BARD, level=1),
            ClassLevel(name=Class.DRUID, level=1),
            ClassLevel(name=Class.RANGER, level=1, via=Via(favoured_enemy=KEEPER_OF_THE_VEIL)),
            ClassLevel(name=Class.RANGER, level=1, via=Via(favoured_enemy=MAGE_BREAKER)),
            ClassLevel(name=Class.SORCERER, level=1),
            ClassLevel(name=Class.WARLOCK, level=1),
            ClassLevel(name=Class.WIZARD, level=1),
        ],
        subclasses=[SubclassLevel(name=SubClass.KNOWLEDGE_DOMAIN, level=1)],
        races=[],
        subraces=[],
        backgrounds=[BackgroundLevel(name=Background.SAGE, level=1)],
    ),
    Skill.HISTORY: HowToLearn(
        classes=[
            ClassLevel(name=Class.BARD, level=1),
            ClassLevel(name=Class.CLERIC, level=1),
            ClassLevel(name=Class.FIGHTER, level=1),
            ClassLevel(name=Class.RANGER, level=1, via=Via(favoured_enemy=RANGER_KNIGHT)),
            ClassLevel(name=Class.MONK, level=1),
            ClassLevel(name=Class.WARLOCK, level=1),
            ClassLevel(name=Class.WIZARD, level=1),
        ],
        subclasses=[SubclassLevel(name=SubClass.KNOWLEDGE_DOMAIN, level=1)],
        races=[],
        subraces=[SubRaceLevel(name=SubRace.ROCK_GNOME, level=1)],
        backgrounds=[
            BackgroundLevel(name=Background.NOBLE, level=1),
            BackgroundLevel(name=Background.SAGE, level=1),
        ],
    ),
    Skill.INVESTIGATION: HowToLearn(
        classes=[
            ClassLevel(name=Class.BARD, level=1),
            ClassLevel(name=Class.RANGER, level=1),
            ClassLevel(name=Class.RANGER, level=1, via=Via(favoured_enemy=BOUNTY_HUNTER)),
            ClassLevel(name=Class.ROGUE, level=1),
            ClassLevel(name=Class.WARLOCK, level=1),
            ClassLevel(name=Class.WIZARD, level=1),
        ],
        subclasses=[],
        races=[],
        subraces=[],
        backgrounds=[],
    ),
    Skill.NATURE: HowToLearn(
        classes=[
            ClassLevel(name=Class.BARBARIAN, level=1),
            ClassLevel(name=Class.BARD, level=1),
            ClassLevel(name=Class.DRUID, level=1),
            ClassLevel(name=Class.RANGER, level=1),
            ClassLevel(name=Class.WARLOCK, level=1),
        ],
        subclasses=[SubclassLevel(name=SubClass.KNOWLEDGE_DOMAIN, level=1)],
        races=[],
        subraces=[],
        backgrounds=[],
    ),
    Skill.RELIGION: HowToLearn(
        classes=[
            ClassLevel(name=Class.BARD, level=1),
            ClassLevel(name=Class.CLERIC, level=1),
            ClassLevel(name=Class.DRUID, level=1),
            ClassLevel(name=Class.MONK, level=1),
            ClassLevel(name=Class.PALADIN, level=1),
            ClassLevel(name=Class.RANGER, level=1, via=Via(favoured_enemy=SANCTIFIED_STALKER)),
            ClassLevel(name=Class.SORCERER, level=1),
            ClassLevel(name=Class.WARLOCK, level=1),
            ClassLevel(name=Class.WIZARD, level=1),
        ],
        subclasses=[SubclassLevel(name=SubClass.KNOWLEDGE_DOMAIN, level=1)],
        races=[],
        subraces=[],
        backgrounds=[BackgroundLevel(name=Background.ACOLYTE, level=1)],
    ),
    Skill.ANIMAL_HANDLING: HowToLearn(
        classes=[
            ClassLevel(name=Class.BARBARIAN, level=1),
            ClassLevel(name=Class.BARD, level=1),
            ClassLevel(name=Class.DRUID, level=1),
            ClassLevel(name=Class.FIGHTER, level=1),
            ClassLevel(name=Class.RANGER, level=1),
        ],
        subclasses=[],
        races=[],
        subraces=[],
        backgrounds=[BackgroundLevel(name=Background.FOLK_HERO, level=1)],
    ),
    Skill.INSIGHT: HowToLearn(
        classes=[
            ClassLevel(name=Class.BARD, level=1),
            ClassLevel(name=Class.CLERIC, level=1),
            ClassLevel(name=Class.DRUID, level=1),
            ClassLevel(name=Class.FIGHTER, level=1),
            ClassLevel(name=Class.MONK, level=1),
            ClassLevel(name=Class.PALADIN, level=1),
            ClassLevel(name=Class.ROGUE, level=1),
            ClassLevel(name=Class.SORCERER, level=1),
            ClassLevel(name=Class.WIZARD, level=1),
        ],
        subclasses=[],
        races=[],
        subraces=[],
        backgrounds=[
            BackgroundLevel(name=Background.ACOLYTE, level=1),
            BackgroundLevel(name=Background.GUILD_ARTISAN, level=1),
        ],
    ),
    Skill.MEDICINE: HowToLearn(
        classes=[
            ClassLevel(name=Class.BARD, level=1),
            ClassLevel(name=Class.CLERIC, level=1),
            ClassLevel(name=Class.DRUID, level=1),
            ClassLevel(name=Class.PALADIN, level=1),
            ClassLevel(name=Class.WIZARD, level=1),
        ],
        subclasses=[],
        races=[],
        subraces=[],
        backgrounds=[BackgroundLevel(name=Background.HAUNTED_ONE, level=1)],
    ),
    Skill.PERCEPTION: HowToLearn(
        classes=[
            ClassLevel(name=Class.BARBARIAN, level=1),
            ClassLevel(name=Class.BARD, level=1),
            ClassLevel(name=Class.DRUID, level=1),
            ClassLevel(name=Class.FIGHTER, level=1),
            ClassLevel(name=Class.RANGER, level=1),
            ClassLevel(name=Class.ROGUE, level=1),
        ],
        subclasses=[],
        races=[RaceLevel(name=Race.ELF, level=1), RaceLevel(name=Race.DROW, level=1)],
        subraces=[],
        backgrounds=[],
    ),
    Skill.SURVIVAL: HowToLearn(
        classes=[
            ClassLevel(name=Class.BARBARIAN, level=1),
            ClassLevel(name=Class.BARD, level=1),
            ClassLevel(name=Class.DRUID, level=1),
            ClassLevel(name=Class.FIGHTER, level=1),
            ClassLevel(name=Class.RANGER, level=1),
        ],
        subclasses=[],
        races=[],
        subraces=[],
        backgrounds=[
            BackgroundLevel(name=Background.FOLK_HERO, level=1),
            BackgroundLevel(name=Background.OUTLANDER, level=1),
        ],
    ),
    Skill.DECEPTION: HowToLearn(
        classes=[
            ClassLevel(name=Class.BARD, level=1),
            ClassLevel(name=Class.ROGUE, level=1),
            ClassLevel(name=Class.SORCERER, level=1),
            ClassLevel(name=Class.WARLOCK, level=1),
        ],
        subclasses=[],
        races=[],
        subraces=[],
        backgrounds=[
            BackgroundLevel(name=Background.CHARLATAN, level=1),
            BackgroundLevel(name=Background.CRIMINAL, level=1),
        ],
    ),
    Skill.INTIMIDATION: HowToLearn(
        classes=[
            ClassLevel(name=Class.BARBARIAN, level=1),
            ClassLevel(name=Class.BARD, level=1),
            ClassLevel(name=Class.FIGHTER, level=1),
            ClassLevel(name=Class.PALADIN, level=1),
            ClassLevel(name=Class.ROGUE, level=1),
            ClassLevel(name=Class.SORCERER, level=1),
            ClassLevel(name=Class.WARLOCK, level=1),
        ],
        subclasses=[],
        races=[RaceLevel(name=Race.HALF_ORC, level=1)],
        subraces=[],
        backgrounds=[
            BackgroundLevel(name=Background.HAUNTED_ONE, level=1),
            BackgroundLevel(name=Background.SOLDIER, level=1),
        ],
    ),
    Skill.PERFORMANCE: HowToLearn(
        classes=[ClassLevel(name=Class.BARD, level=1), ClassLevel(name=Class.ROGUE, level=1)],
        subclasses=[],
        races=[],
        subraces=[],
        backgrounds=[BackgroundLevel(name=Background.ENTERTAINER, level=1)],
    ),
    Skill.PERSUASION: HowToLearn(
        classes=[
            ClassLevel(name=Class.BARD, level=1),
            ClassLevel(name=Class.CLERIC, level=1),
            ClassLevel(name=Class.PALADIN, level=1),
            ClassLevel(name=Class.ROGUE, level=1),
            ClassLevel(name=Class.SORCERER, level=1),
        ],
        subclasses=[],
        races=[],
        subraces=[],
        backgrounds=[
            BackgroundLevel(name=Background.GUILD_ARTISAN, level=1),
            BackgroundLevel(name=Background.NOBLE, level=1),
        ],
    ),
}


SKILL_EXPERTISE = {
    Skill.ARCANA: HowToLearn(
        classes=[],
        subclasses=[SubclassLevel(name=SubClass.KNOWLEDGE_DOMAIN, level=1)],
        races=[],
        subraces=[],
        backgrounds=[],
    ),
    Skill.HISTORY: HowToLearn(
        classes=[],
        subclasses=[SubclassLevel(name=SubClass.KNOWLEDGE_DOMAIN, level=1)],
        races=[],
        subraces=[SubRaceLevel(name=SubRace.ROCK_GNOME, level=1)],
        backgrounds=[],
    ),
    Skill.NATURE: HowToLearn(
        classes=[],
        subclasses=[SubclassLevel(name=SubClass.KNOWLEDGE_DOMAIN, level=1)],
        races=[],
        subraces=[],
        backgrounds=[],
    ),
    Skill.RELIGION: HowToLearn(
        classes=[],
        subclasses=[SubclassLevel(name=SubClass.KNOWLEDGE_DOMAIN, level=1)],
        races=[],
        subraces=[],
        backgrounds=[],
    ),
    None: HowToLearn(
        classes=[
            ClassLevel(name=Class.ROGUE, level=1),
            ClassLevel(name=Class.BARD, level=3),
            ClassLevel(name=Class.ROGUE, level=6),
            ClassLevel(name=Class.BARD, level=10),
        ],
        subclasses=[],
        races=[],
        subraces=[],
        backgrounds=[],
    ),
}
