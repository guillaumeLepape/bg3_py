from enum import Enum
from uuid import UUID


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


RACES_UUID = {
    Race.DRAGONBORN: UUID("b5c46ed0-1f59-425c-bb7c-83476d189c69"),
    Race.DROW: UUID("70ec2cd4-508e-4db7-8f83-8e2043ab1af3"),
    Race.DWARF: UUID("f0ca65d7-6337-42b3-9b62-990c3f6ca6cc"),
    Race.ELF: UUID("e13a8502-9bcb-484a-8a20-a25f5ef7d4cd"),
    Race.GITHYANKI: UUID("851dd22e-a1bc-46b5-9890-72402d10cf1c"),
    Race.GNOME: UUID("aa6f6712-2102-4492-a491-d31b29980f25"),
    Race.HALF_ELF: UUID("d605ece4-1ff3-4697-aafd-1a5918ca66b8"),
    Race.HALF_ORC: UUID("45bb20cb-f0c4-4cc9-9187-9f35cf76d026"),
    Race.HALFLING: UUID("d0553e4b-5d0e-45fa-a6b4-6afbb68c661e"),
    Race.HUMAN: UUID("acba17c9-ff2f-4d34-bd80-28ed4b2efa04"),
    Race.TIEFLING: UUID("6cc80e4a-06eb-4f95-8798-31468762244e"),
}


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


SUBRACES_UUID = {
    SubRace.BLACK_DRAGONBORN: UUID("0b04c247-0c20-417e-b525-e9146602bb81"),
    SubRace.BLUE_DRAGONBORN: UUID("e6fdb964-6239-4809-8a1b-2e5004d5e45c"),
    SubRace.BRASS_DRAGONBORN: UUID("a78c6dbf-7482-4522-8175-7a6616e1ea99"),
    SubRace.BRONZE_DRAGONBORN: UUID("0f283fb3-efe6-4f78-aab7-b4e4dfd393c7"),
    SubRace.COPPER_DRAGONBORN: UUID("69d79c24-f207-41cd-87f9-53f2413c3ddd"),
    SubRace.GOLD_DRAGONBORN: UUID("4fd58c4f-c0c7-49b1-8756-05d32b165e63"),
    SubRace.GREEN_DRAGONBORN: UUID("1a701d21-207f-4066-b978-1e1b1964ce0a"),
    SubRace.RED_DRAGONBORN: UUID("cbbf2607-b1ae-43ff-b19d-371ef7c80b7c"),
    SubRace.SILVER_DRAGONBORN: UUID("6417af3f-bca9-42a9-b5d0-6dc0fb8455fb"),
    SubRace.WHITE_DRAGONBORN: UUID("83e16d07-7c2b-42e2-9c9b-709b59e6edfc"),
    SubRace.LOLTH_SWORN_DROW: UUID("88f80dcb-1d26-472a-9fb6-008113326078"),
    SubRace.SELDRARINE_DROW: UUID("4f6609e2-8243-481d-815f-ea1a96ce09f0"),
    SubRace.GOLD_DWARF: UUID("24c53e60-5f71-453c-acc8-b43a664a579c"),
    SubRace.SHIELD_DWARF: UUID("1efd19da-8907-4fce-8fa5-d906845070ba"),
    SubRace.DUERGAR: UUID("ef3a0707-a319-471c-aed4-a98ec69f5ff8"),
    SubRace.HIGH_ELF: UUID("ce963b4a-2855-45bd-8ec2-9b74cb30983d"),
    SubRace.WOOD_ELF: UUID("62bcdb2d-8503-4c70-8a86-119e3bdc9884"),
    SubRace.ROCK_GNOME: UUID("c89a1d35-e5dd-43dd-bb99-4a9ada9e53f3"),
    SubRace.FOREST_GNOME: UUID("c5cd8a5b-6c19-4e74-8d33-50f8a8d18994"),
    SubRace.DEEP_GNOME: UUID("d7fa1db0-73cd-4a1f-b627-06441a5063bc"),
    SubRace.HIGH_HALF_ELF: UUID("034abf20-3295-4e6e-ab03-de196e96a36a"),
    SubRace.WOOD_HALF_ELF: UUID("d27bc071-4032-4098-8d12-7ca11ae0dff4"),
    SubRace.DROW_HALF_ELF: UUID("05a2d091-4f8e-4af2-a21a-29be841473cd"),
    SubRace.LIGHTFOOT_HALFLING: UUID("87281eea-4cf1-4043-86f3-fe0d53e1cc86"),
    SubRace.STRONGHEART_HALFLING: UUID("e58f22df-c941-4a5c-adf4-b486b0967b7b"),
    SubRace.ASMODEUS_TIEFLING: UUID("2b37ebaf-9a16-477f-934c-798ec8fc02d8"),
    SubRace.MEPHISTOPHELES_TIEFLING: UUID("f52a31a1-36bc-4197-8aac-683cd5f4fcc0"),
    SubRace.ZARIEL_TIEFLING: UUID("984ef62d-1035-473b-acd3-516ad63db530"),
}

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
