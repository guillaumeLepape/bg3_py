from enum import Enum

from .characteristic import Characteristic


class Skill(str, Enum):
    ATHLETICS = "Athletics"

    ACROBATICS = "Acrobatics"
    SLEIGHT_OF_HAND = "Sleight of Hand"
    STEALTH = "Stealth"

    ARCANA = "Arcana"
    HISTORY = "History"
    INVESTIGATION = "Investigation"
    NATURE = "Nature"
    RELIGION = "Religion"

    ANIMAL_HANDLING = "Animal Handling"
    INSIGHT = "Insight"
    MEDICINE = "Medicine"
    PERCEPTION = "Perception"
    SURVIVAL = "Survival"

    DECEPTION = "Deception"
    INTIMIDATION = "Intimidation"
    PERFORMANCE = "Performance"
    PERSUASION = "Persuasion"


CHARACTERISTIC_TO_SKILLS = {
    Characteristic.STRENGTH: {Skill.ATHLETICS},
    Characteristic.DEXTERITY: {Skill.ACROBATICS, Skill.SLEIGHT_OF_HAND, Skill.STEALTH},
    Characteristic.INTELLIGENCE: {
        Skill.ARCANA,
        Skill.HISTORY,
        Skill.INVESTIGATION,
        Skill.NATURE,
        Skill.RELIGION,
    },
    Characteristic.WISDOM: {
        Skill.ANIMAL_HANDLING,
        Skill.INSIGHT,
        Skill.MEDICINE,
        Skill.PERCEPTION,
        Skill.SURVIVAL,
    },
    Characteristic.CHARISMA: {
        Skill.DECEPTION,
        Skill.INTIMIDATION,
        Skill.PERFORMANCE,
        Skill.PERSUASION,
    },
}
