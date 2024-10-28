from uuid import UUID, uuid5

from pydantic import (
    BaseModel,
    ConfigDict,
    SerializerFunctionWrapHandler,
    computed_field,
    model_serializer,
)

from .classes import Class, SubClass
from .favoured_enemy import RANGER_KNIGHT
from .levelling import ClassLevel, HowToLearn, RaceLevel, SubclassLevel, SubRaceLevel, Via
from .races import Race, SubRace

ARMOUR_TYPE_UUID_NAMESPACE = UUID("79f6ff8f-b514-4d41-af4c-60a788077ab0")


class ArmourType(BaseModel):
    name: str

    how_to_learn: HowToLearn

    model_config = ConfigDict(extra="forbid")

    @computed_field  # type: ignore[prop-decorator]
    @property
    def id(self) -> UUID:
        return uuid5(ARMOUR_TYPE_UUID_NAMESPACE, self.name)

    # Custom serializer to ensure 'id' comes first
    @model_serializer(mode="wrap")
    def custom_serialize(self, nxt: SerializerFunctionWrapHandler) -> dict:
        return {"id": self.id, **nxt(self)}


LIGHT_ARMOUR = ArmourType(
    name="Light Armour",
    how_to_learn=HowToLearn(
        classes=[
            ClassLevel(name=Class.BARBARIAN, level=1),
            ClassLevel(name=Class.BARD, level=1),
            ClassLevel(name=Class.CLERIC, level=1),
            ClassLevel(name=Class.DRUID, level=1),
            ClassLevel(name=Class.FIGHTER, level=1),
            ClassLevel(name=Class.PALADIN, level=1),
            ClassLevel(name=Class.RANGER, level=1),
            ClassLevel(name=Class.ROGUE, level=1),
            ClassLevel(name=Class.WARLOCK, level=1),
        ],
        subclasses=[],
        races=[RaceLevel(name=Race.HALF_ELF, level=1), RaceLevel(name=Race.HUMAN, level=1)],
        subraces=[],
    ),
)
MEDIUM_ARMOUR = ArmourType(
    name="Medium Armour",
    how_to_learn=HowToLearn(
        classes=[
            ClassLevel(name=Class.BARBARIAN, level=1),
            ClassLevel(name=Class.CLERIC, level=1),
            ClassLevel(name=Class.DRUID, level=1),
            ClassLevel(name=Class.FIGHTER, level=1),
            ClassLevel(name=Class.PALADIN, level=1),
            ClassLevel(name=Class.RANGER, level=1),
        ],
        subclasses=[
            SubclassLevel(name=SubClass.COLLEGE_OF_SWORDS, level=3),
            SubclassLevel(name=SubClass.COLLEGE_OF_VALOR, level=3),
        ],
        races=[RaceLevel(name=Race.GITHYANKI, level=1)],
        subraces=[SubRaceLevel(name=SubRace.SHIELD_DWARF, level=1)],
    ),
)
HEAVY_ARMOUR = ArmourType(
    name="Heavy Armour",
    how_to_learn=HowToLearn(
        classes=[
            ClassLevel(name=Class.FIGHTER, level=1),
            ClassLevel(name=Class.PALADIN, level=1),
            ClassLevel(name=Class.RANGER, level=1, via=Via(favoured_enemy=RANGER_KNIGHT)),
        ],
        subclasses=[
            SubclassLevel(name=SubClass.LIFE_DOMAIN, level=1),
            SubclassLevel(name=SubClass.NATURE_DOMAIN, level=1),
            SubclassLevel(name=SubClass.TEMPEST_DOMAIN, level=1),
            SubclassLevel(name=SubClass.WAR_DOMAIN, level=1),
        ],
        races=[],
        subraces=[],
    ),
)
SHIELD = ArmourType(
    name="Shield",
    how_to_learn=HowToLearn(
        classes=[
            ClassLevel(name=Class.BARBARIAN, level=1),
            ClassLevel(name=Class.CLERIC, level=1),
            ClassLevel(name=Class.DRUID, level=1),
            ClassLevel(name=Class.FIGHTER, level=1),
            ClassLevel(name=Class.PALADIN, level=1),
            ClassLevel(name=Class.RANGER, level=1),
        ],
        subclasses=[SubclassLevel(name=SubClass.COLLEGE_OF_VALOR, level=3)],
        races=[RaceLevel(name=Race.HALF_ELF, level=1), RaceLevel(name=Race.HUMAN, level=1)],
        subraces=[],
    ),
)
