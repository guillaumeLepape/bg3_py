from enum import Enum
from uuid import UUID, uuid5

from pydantic import BaseModel, SerializerFunctionWrapHandler, computed_field, model_serializer


class Category(Enum):
    SIMPLE = "simple"
    MARTIAL = "martial"


WEAPON_TYPE_UUID_NAMESPACE = UUID("81ac0b4e-bc28-438e-b43b-4759a4f30e33")


class WeaponType(BaseModel):
    name: str
    category: Category

    @computed_field  # type: ignore[prop-decorator]
    @property
    def id(self) -> UUID:
        return uuid5(WEAPON_TYPE_UUID_NAMESPACE, self.name)

    # Custom serializer to ensure 'id' comes first
    @model_serializer(mode="wrap")
    def custom_serialize(self, nxt: SerializerFunctionWrapHandler) -> dict:
        return {"id": self.id, **nxt(self)}


FLAIL = WeaponType(name="Flail", category=Category.MARTIAL)
MORNINGSTAR = WeaponType(name="Morningstar", category=Category.MARTIAL)
RAPIER = WeaponType(name="Rapier", category=Category.MARTIAL)
SCIMITAR = WeaponType(name="Scimitar", category=Category.MARTIAL)
SHORTSWORD = WeaponType(name="Shortsword", category=Category.MARTIAL)
WAR_PICK = WeaponType(name="War Pick", category=Category.MARTIAL)
BATTLEAXE = WeaponType(name="Battleaxe", category=Category.MARTIAL)
LONGSWORD = WeaponType(name="Longsword", category=Category.MARTIAL)
TRIDENT = WeaponType(name="Trident", category=Category.MARTIAL)
WARHAMMER = WeaponType(name="Warhammer", category=Category.MARTIAL)
GLAIVE = WeaponType(name="Glaive", category=Category.MARTIAL)
GREATAXE = WeaponType(name="Greataxe", category=Category.MARTIAL)
GREATSWORD = WeaponType(name="Greatsword", category=Category.MARTIAL)
HALBERD = WeaponType(name="Halberd", category=Category.MARTIAL)
MAUL = WeaponType(name="Maul", category=Category.MARTIAL)
PIKE = WeaponType(name="Pike", category=Category.MARTIAL)
HAND_CROSSBOW = WeaponType(name="Hand Crossbow", category=Category.MARTIAL)
HEAVY_CROSSBOW = WeaponType(name="Heavy Crossbow", category=Category.MARTIAL)
LONGBOW = WeaponType(name="Longbow", category=Category.MARTIAL)

MARTIAL_WEAPONS = [
    FLAIL,
    MORNINGSTAR,
    RAPIER,
    SCIMITAR,
    SHORTSWORD,
    WAR_PICK,
    BATTLEAXE,
    LONGSWORD,
    TRIDENT,
    WARHAMMER,
    GLAIVE,
    GREATAXE,
    GREATSWORD,
    HALBERD,
    MAUL,
    PIKE,
    HAND_CROSSBOW,
    HEAVY_CROSSBOW,
    LONGBOW,
]

CLUB = WeaponType(name="Club", category=Category.SIMPLE)
DAGGER = WeaponType(name="Dagger", category=Category.SIMPLE)
HANDAXE = WeaponType(name="Handaxe", category=Category.SIMPLE)
JAVELIN = WeaponType(name="Javelin", category=Category.SIMPLE)
LIGHT_HAMMER = WeaponType(name="Light Hammer", category=Category.SIMPLE)
MACE = WeaponType(name="Mace", category=Category.SIMPLE)
SICKLE = WeaponType(name="Sickle", category=Category.SIMPLE)
QUARTERSTAFF = WeaponType(name="Quarterstaff", category=Category.SIMPLE)
SPEAR = WeaponType(name="Spear", category=Category.SIMPLE)
GREATCLUB = WeaponType(name="Greatclub", category=Category.SIMPLE)
LIGHT_CROSSBOW = WeaponType(name="Light Crossbow", category=Category.SIMPLE)
SHORTBOW = WeaponType(name="Shortbow", category=Category.SIMPLE)

SIMPLE_WEAPONS = [
    CLUB,
    DAGGER,
    HANDAXE,
    JAVELIN,
    LIGHT_HAMMER,
    MACE,
    SICKLE,
    QUARTERSTAFF,
    SPEAR,
    GREATCLUB,
    LIGHT_CROSSBOW,
    SHORTBOW,
]
