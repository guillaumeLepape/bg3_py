from enum import Enum
from uuid import UUID, uuid5


class Background(str, Enum):
    ACOLYTE = "ACOLYTE"
    CHARLATAN = "CHARLATAN"
    CRIMINAL = "CRIMINAL"
    ENTERTAINER = "ENTERTAINER"
    FOLK_HERO = "FOLK_HERO"
    GUILD_ARTISAN = "GUILD_ARTISAN"
    HAUNTED_ONE = "HAUNTED_ONE"
    NOBLE = "NOBLE"
    OUTLANDER = "OUTLANDER"
    SAGE = "SAGE"
    SOLDIER = "SOLDIER"
    URCHIN = "URCHIN"


BACKGROUND_UUID_NAMESPACE = UUID("5460987c-945d-413f-bf20-0656d049279d")


def background_uuid(background: Background) -> UUID:
    return uuid5(BACKGROUND_UUID_NAMESPACE, background)
