from enum import Enum


class Characteristic(str, Enum):
    STRENGTH = "Strength"
    DEXTERITY = "Dexterity"
    CONSTITUTION = "Constitution"
    INTELLIGENCE = "Intelligence"
    WISDOM = "Wisdom"
    CHARISMA = "Charisma"


TRIGRAM_TO_CHARACTERISTIC = {
    "STR": Characteristic.STRENGTH,
    "DEX": Characteristic.DEXTERITY,
    "CON": Characteristic.CONSTITUTION,
    "INT": Characteristic.INTELLIGENCE,
    "WIS": Characteristic.WISDOM,
    "CHA": Characteristic.CHARISMA,
}


def trigram_to_characteristic(trigram: str) -> Characteristic:
    if trigram not in TRIGRAM_TO_CHARACTERISTIC:
        raise ValueError(f"Invalid characteristic trigram: {trigram}")

    return TRIGRAM_TO_CHARACTERISTIC[trigram]
