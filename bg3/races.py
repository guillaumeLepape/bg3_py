from enum import Enum


class Race(str, Enum):
    DRAGONBORN = "Dragonborn"
    DROW = "Drow"
    DWARF = "Dwarf"
    ELF = "Elf"
    GITHYANKI = "Githyanki"
    GNOME = "Gnome"
    HALF_ELF = "Half-Elf"
    HALF_ORC = "Half-Orc"
    HALFLING = "Halfling"
    HUMAN = "Human"
    TIEFLING = "Tiefling"


class SubRace(str, Enum):
    # Dragonborn
    BLACK_DRAGONBORN = "Black Dragonborn"
    BLUE_DRAGONBORN = "Blue Dragonborn"
    BRASS_DRAGONBORN = "Brass Dragonborn"
    BRONZE_DRAGONBORN = "Bronze Dragonborn"
    COPPER_DRAGONBORN = "Copper Dragonborn"
    GOLD_DRAGONBORN = "Gold Dragonborn"
    GREEN_DRAGONBORN = "Green Dragonborn"
    RED_DRAGONBORN = "Red Dragonborn"
    SILVER_DRAGONBORN = "Silver Dragonborn"
    WHITE_DRAGONBORN = "White Dragonborn"

    # Drow
    LOLTH_SWORN_DROW = "Lolth-sworn"
    SELDRARINE_DROW = "Seldarine"

    # Dwarf
    GOLD_DWARF = "Gold Dwarf"
    SHIELD_DWARF = "Shield Dwarf"
    DUERGAR = "Duergar"

    # Elf
    HIGH_ELF = "High Elf"
    WOOD_ELF = "Wood Elf"

    # Githyanki

    # Gnome
    ROCK_GNOME = "Rock Gnome"
    FOREST_GNOME = "Forest Gnome"
    DEEP_GNOME = "Deep Gnome"

    # Half-Elf
    HIGH_HALF_ELF = "High Half-Elf"
    WOOD_HALF_ELF = "Wood Half-Elf"
    DROW_HALF_ELF = "Drow Half-Elf"

    # Half-Orc

    # Halfling
    LIGHTFOOT_HALFLING = "Lightfoot Halfling"
    STRONGHEART_HALFLING = "Strongheart Halfling"

    # Human

    # Tiefling
    ASMODEUS_TIEFLING = "Asmodeus Tiefling"
    MEPHISTOPHELES_TIEFLING = "Mephistopheles Tiefling"
    ZARIEL_TIEFLING = "Zariel Tiefling"


RACE_TO_SUBRACES = {
    Race.DRAGONBORN: {
        SubRace.BLACK_DRAGONBORN,
        SubRace.BLUE_DRAGONBORN,
        SubRace.BRASS_DRAGONBORN,
        SubRace.BRONZE_DRAGONBORN,
        SubRace.COPPER_DRAGONBORN,
        SubRace.GOLD_DRAGONBORN,
        SubRace.GREEN_DRAGONBORN,
        SubRace.RED_DRAGONBORN,
        SubRace.SILVER_DRAGONBORN,
        SubRace.WHITE_DRAGONBORN,
    },
    Race.DROW: {SubRace.LOLTH_SWORN_DROW, SubRace.SELDRARINE_DROW},
    Race.DWARF: {SubRace.GOLD_DWARF, SubRace.SHIELD_DWARF, SubRace.DUERGAR},
    Race.ELF: {SubRace.HIGH_ELF, SubRace.WOOD_ELF},
    Race.GITHYANKI: set(),
    Race.GNOME: {SubRace.ROCK_GNOME, SubRace.FOREST_GNOME, SubRace.DEEP_GNOME},
    Race.HALF_ELF: {SubRace.HIGH_HALF_ELF, SubRace.WOOD_HALF_ELF, SubRace.DROW_HALF_ELF},
    Race.HALF_ORC: set(),
    Race.HALFLING: {SubRace.LIGHTFOOT_HALFLING, SubRace.STRONGHEART_HALFLING},
    Race.HUMAN: set(),
    Race.TIEFLING: {
        SubRace.ASMODEUS_TIEFLING,
        SubRace.MEPHISTOPHELES_TIEFLING,
        SubRace.ZARIEL_TIEFLING,
    },
}
