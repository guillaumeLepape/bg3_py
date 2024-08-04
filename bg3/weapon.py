from enum import Enum
from uuid import UUID

from pydantic import BaseModel


class Category(Enum):
    SIMPLE = "simple"
    MARTIAL = "martial"


class WeaponProficiency(BaseModel):
    id: UUID
    name: str
    category: Category

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, WeaponProficiency):
            raise NotImplementedError

        return self.id == other.id


flail_proficiency = WeaponProficiency(
    id="a35f05f3-4a28-44ea-8454-ad99a58466c4", name="Flail Proficiency", category=Category.MARTIAL
)
morningstar_proficiency = WeaponProficiency(
    id="f3b3b3b3-4a28-44ea-8454-ad99a58466c4",
    name="Morningstar Proficiency",
    category=Category.MARTIAL,
)
rapier_proficiency = WeaponProficiency(
    id="f3b3b3b3-4a28-44ea-8454-ad99a58466c4", name="Rapier Proficiency", category=Category.MARTIAL
)
scimitar_proficiency = WeaponProficiency(
    id="4516569c-a6b4-49e4-b66e-f6203ef2ece0",
    name="Scimitar Proficiency",
    category=Category.MARTIAL,
)
shortsword_proficiency = WeaponProficiency(
    id="2b4d8585-725e-439e-b469-290206c1282f",
    name="Shortsword Proficiency",
    category=Category.MARTIAL,
)
war_pick_proficiency = WeaponProficiency(
    id="05be82e7-5f08-439f-b86b-a59d11d496db",
    name="War Pick Proficiency",
    category=Category.MARTIAL,
)
battleaxe_proficiency = WeaponProficiency(
    id="1c5add85-0e3d-4c2c-964a-ed7650bb338e",
    name="Battleaxe Proficiency",
    category=Category.MARTIAL,
)
longsword_proficiency = WeaponProficiency(
    id="68f52edc-c1f9-43c9-a781-c2b3d0715b21",
    name="Longsword Proficiency",
    category=Category.MARTIAL,
)
trident_proficiency = WeaponProficiency(
    id="45c0b1af-d14a-4f9c-8ac1-b03337babd6c", name="Trident Proficiency", category=Category.MARTIAL
)
warhammer_proficiency = WeaponProficiency(
    id="d8c02b4c-45f0-4cc4-8cd2-77a829017189",
    name="Warhammer Proficiency",
    category=Category.MARTIAL,
)
glaive_proficiency = WeaponProficiency(
    id="f50d4534-0b23-4244-a588-701a931c7448", name="Glaive Proficiency", category=Category.MARTIAL
)
greataxe_proficiency = WeaponProficiency(
    id="712dbcc4-caeb-4386-8b2e-0f95947038e8",
    name="Greataxe Proficiency",
    category=Category.MARTIAL,
)
greatsword_proficiency = WeaponProficiency(
    id="4cd491e1-be66-4965-a905-a1fcd134f006",
    name="Greatsword Proficiency",
    category=Category.MARTIAL,
)
halberd_proficiency = WeaponProficiency(
    id="5c2f585a-f459-4b7d-a92e-ba769ea7ae4d", name="Halberd Proficiency", category=Category.MARTIAL
)
maul_proficiency = WeaponProficiency(
    id="afef9d35-f0e4-4a02-8e02-e8930c223c78", name="Maul Proficiency", category=Category.MARTIAL
)
pike_proficiency = WeaponProficiency(
    id="53053a31-0305-4802-a7f1-ca4b6fd39b1b", name="Pike Proficiency", category=Category.MARTIAL
)
hand_crossbow_proficiency = WeaponProficiency(
    id="7230cac0-a4ad-4910-ac06-4f64ee09f5ff",
    name="Hand Crossbow Proficiency",
    category=Category.MARTIAL,
)
heavy_crossbow_proficiency = WeaponProficiency(
    id="d7417a56-dbd4-4132-9e47-86054a3360e3",
    name="Heavy Crossbow Proficiency",
    category=Category.MARTIAL,
)
longbow_proficiency = WeaponProficiency(
    id="a1eeab82-8ff0-4afa-a14f-925fe9264489", name="Longbow Proficiency", category=Category.MARTIAL
)

martial_weapon_proficiencies = [
    flail_proficiency,
    morningstar_proficiency,
    rapier_proficiency,
    scimitar_proficiency,
    shortsword_proficiency,
    war_pick_proficiency,
    battleaxe_proficiency,
    longsword_proficiency,
    trident_proficiency,
    warhammer_proficiency,
    glaive_proficiency,
    greataxe_proficiency,
    greatsword_proficiency,
    halberd_proficiency,
    maul_proficiency,
    pike_proficiency,
    hand_crossbow_proficiency,
    heavy_crossbow_proficiency,
    longbow_proficiency,
]

club_proficiency = WeaponProficiency(
    id="e4d09736-c398-48ea-87f1-33f8b6ebb5cc", name="Club Proficiency", category=Category.SIMPLE
)
dagger_proficiency = WeaponProficiency(
    id="1d5384ed-3bfe-48e7-8341-57df7fe29f84", name="Dagger Proficiency", category=Category.SIMPLE
)
handaxe_proficiency = WeaponProficiency(
    id="09d00638-6014-4dc5-82e3-116cffbb101a", name="Handaxe Proficiency", category=Category.SIMPLE
)
javelin_proficiency = WeaponProficiency(
    id="9b2b84f3-82b2-4ba4-847a-4b7e36433d11", name="Javelin Proficiency", category=Category.SIMPLE
)
light_hammer_proficiency = WeaponProficiency(
    id="a1f3e0b4-8c4b-4b0e-8c9d-7e1f7b2f3f5b",
    name="Light Hammer Proficiency",
    category=Category.SIMPLE,
)
mace_proficiency = WeaponProficiency(
    id="b6b4c1b6-5e9e-4f8b-8b7d-7f9e0b5e9e4b", name="Mace Proficiency", category=Category.SIMPLE
)
sickle_proficiency = WeaponProficiency(
    id="543cb544-48c5-4a7e-99ba-347fbf1fdcb9", name="Sickle Proficiency", category=Category.SIMPLE
)
quarterstaff_proficiency = WeaponProficiency(
    id="c8d29344-9ffe-486b-ab4a-077b31c47d3b",
    name="Quarterstaff Proficiency",
    category=Category.SIMPLE,
)
spear_proficiency = WeaponProficiency(
    id="3c1d46ae-b148-45e6-829e-0f3072ce2f02", name="Spear Proficiency", category=Category.SIMPLE
)
greatclub_proficiency = WeaponProficiency(
    id="6bf5a338-5716-4dc9-b7a5-5efe5d59dea4",
    name="Greatclub Proficiency",
    category=Category.SIMPLE,
)
light_crossbow_proficiency = WeaponProficiency(
    id="909c3cea-48d2-4788-b726-22fe00d504b5",
    name="Light Crossbow Proficiency",
    category=Category.SIMPLE,
)
shortbow_proficiency = WeaponProficiency(
    id="42719a6e-99ef-44ea-93d0-13eab5d0dc11", name="Shortbow Proficiency", category=Category.SIMPLE
)

simple_weapon_proficiencies = [
    club_proficiency,
    dagger_proficiency,
    handaxe_proficiency,
    javelin_proficiency,
    light_hammer_proficiency,
    mace_proficiency,
    sickle_proficiency,
    quarterstaff_proficiency,
    spear_proficiency,
    greatclub_proficiency,
    light_crossbow_proficiency,
    shortbow_proficiency,
]
