from enum import Enum
from typing import List, Optional, Union
from uuid import UUID

from pydantic import (
    BaseModel,
    ConfigDict,
    SerializerFunctionWrapHandler,
    computed_field,
    model_serializer,
)

from .classes import Class, SubClass, class_uuid, subclass_uuid
from .favoured_enemy import FavouredEnemy
from .natural_explorer import NaturalExplorer
from .races import RACES_UUID, SUBRACES_UUID, Race, SubRace


class DraconicAncestry(str, Enum):
    BLACK = "Black"
    BLUE = "Blue"
    BRASS = "Brass"
    BRONZE = "Bronze"
    COPPER = "Copper"
    GOLD = "Gold"
    GREEN = "Green"
    RED = "Red"
    SILVER = "Silver"
    WHITE = "White"


class DamageType(str, Enum):
    ACID = "Acid"
    BLUDGEONING = "Bludgeoning"
    COLD = "Cold"
    FIRE = "Fire"
    FORCE = "Force"
    LIGHTNING = "Lightning"
    NECROTIC = "Necrotic"
    PIERCING = "Piercing"
    POISON = "Poison"
    PSYCHIC = "Psychic"
    RADIANT = "Radiant"
    SLASHING = "Slashing"
    THUNDER = "Thunder"


DRACONIC_ANCESTRY_TO_DAMAGE_TYPE = {
    DraconicAncestry.BLACK: DamageType.ACID,
    DraconicAncestry.BLUE: DamageType.LIGHTNING,
    DraconicAncestry.BRASS: DamageType.FIRE,
    DraconicAncestry.BRONZE: DamageType.LIGHTNING,
    DraconicAncestry.COPPER: DamageType.ACID,
    DraconicAncestry.GOLD: DamageType.FIRE,
    DraconicAncestry.GREEN: DamageType.POISON,
    DraconicAncestry.RED: DamageType.FIRE,
    DraconicAncestry.SILVER: DamageType.COLD,
    DraconicAncestry.WHITE: DamageType.COLD,
}


class PactBoon(str, Enum):
    PACT_OF_THE_BLADE = "Pact of the Blade"
    PACT_OF_THE_CHAIN = "Pact of the Chain"
    PACT_OF_THE_TOME = "Pact of the Tome"


class LandCircle(str, Enum):
    ARCTIC = "Arctic"
    COAST = "Coast"
    DESERT = "Desert"
    FOREST = "Forest"
    GRASSLAND = "Grassland"
    MOUNTAIN = "Mountain"
    SWAMP = "Swamp"
    UNDERDARK = "Underdark"


class WildShape(str, Enum):
    DEEP_ROTHE = "Deep Rothé"


class Via(BaseModel):
    draconic_ancestry: Optional[DraconicAncestry] = None
    pact_boon: Optional[PactBoon] = None
    land_circles: Optional[List[LandCircle]] = None
    natural_explorer: Optional[NaturalExplorer] = None
    favoured_enemy: Optional[FavouredEnemy] = None
    wild_shape: Optional[WildShape] = None

    model_config = ConfigDict(extra="forbid")


class ClassLevel(BaseModel):
    name: Class
    level: int
    via: Union[str, Via, None] = None

    model_config = ConfigDict(extra="forbid")

    @computed_field  # type: ignore[prop-decorator]
    @property
    def id(self) -> UUID:
        return class_uuid(self.name)

    # Custom serializer to ensure 'id' comes first
    @model_serializer(mode="wrap")
    def custom_serialize(self, nxt: SerializerFunctionWrapHandler) -> dict:
        return {"id": self.id, **nxt(self)}


class SubclassLevel(BaseModel):
    name: SubClass
    level: int
    via: Union[str, Via, None] = None

    model_config = ConfigDict(extra="forbid")

    @computed_field  # type: ignore[prop-decorator]
    @property
    def id(self) -> UUID:
        return subclass_uuid(self.name)

    # Custom serializer to ensure 'id' comes first
    @model_serializer(mode="wrap")
    def custom_serialize(self, nxt: SerializerFunctionWrapHandler) -> dict:
        return {"id": self.id, **nxt(self)}


class RaceLevel(BaseModel):
    name: Race
    level: int

    model_config = ConfigDict(extra="forbid")

    @computed_field  # type: ignore[prop-decorator]
    @property
    def id(self) -> UUID:
        return RACES_UUID[self.name]

    # Custom serializer to ensure 'id' comes first
    @model_serializer(mode="wrap")
    def custom_serialize(self, nxt: SerializerFunctionWrapHandler) -> dict:
        return {"id": self.id, **nxt(self)}


class SubRaceLevel(BaseModel):
    name: SubRace
    level: int

    model_config = ConfigDict(extra="forbid")

    @computed_field  # type: ignore[prop-decorator]
    @property
    def id(self) -> UUID:
        return SUBRACES_UUID[self.name]

    # Custom serializer to ensure 'id' comes first
    @model_serializer(mode="wrap")
    def custom_serialize(self, nxt: SerializerFunctionWrapHandler) -> dict:
        return {"id": self.id, **nxt(self)}


class HowToLearn(BaseModel):
    classes: List[ClassLevel]
    subclasses: List[SubclassLevel]
    races: List[RaceLevel]
    subraces: List[SubRaceLevel]

    model_config = ConfigDict(extra="forbid")
