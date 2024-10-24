from enum import Enum
from typing import List, Optional, Union
from uuid import UUID, uuid5

from pydantic import (
    BaseModel,
    ConfigDict,
    RootModel,
    SerializerFunctionWrapHandler,
    computed_field,
    model_serializer,
)

from bg3.characteristic import Characteristic
from bg3.classes import CLASSES_UUID, SUBCLASSES_UUID, Class, SubClass
from bg3.cost import Cost
from bg3.races import RACES_UUID, SUBRACES_UUID, Race, SubRace


class SpellProperties(BaseModel):
    cost: List[Cost]
    cost_on_hit: Optional[List[Cost]] = None
    concentration: bool
    ritual: bool
    saving_throw: Optional[Characteristic] = None

    model_config = ConfigDict(extra="forbid")


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


class NaturalExplorer(str, Enum):
    BEAST_TAMER = "Beast Tamer"
    URBAN_TRACKER = "Urban Tracker"
    WASTELAND_WANDERER_COLD = "Wasteland Wanderer: Cold"
    WASTELAND_WANDERER_FIRE = "Wasteland Wanderer: Fire"
    WASTELAND_WANDERER_POISON = "Wasteland Wanderer: Poison"


class FavouredEnemy(str, Enum):
    BOUNTY_HUNTER = "Bounty Hunter"
    KEEPER_OF_THE_VEIL = "Keeper of the Veil"
    MAGE_BREAKER = "Mage Breaker"
    RANGER_KNIGHT = "Ranger Knight"
    SANCTIFIED_STALKER = "Sanctified Stalker"


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
        return CLASSES_UUID[self.name]

    # Custom serializer to ensure 'id' comes first
    @model_serializer(mode="wrap")
    def custom_serialize(self, nxt: SerializerFunctionWrapHandler) -> dict:
        # Ensure 'id' comes first
        return {"id": self.id, **nxt(self)}


class SubclassLevel(BaseModel):
    name: SubClass
    level: int
    via: Union[str, Via, None] = None

    model_config = ConfigDict(extra="forbid")

    @computed_field  # type: ignore[prop-decorator]
    @property
    def id(self) -> UUID:
        return SUBCLASSES_UUID[self.name]

    # Custom serializer to ensure 'id' comes first
    @model_serializer(mode="wrap")
    def custom_serialize(self, nxt: SerializerFunctionWrapHandler) -> dict:
        # Ensure 'id' comes first
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
        # Ensure 'id' comes first
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
        # Ensure 'id' comes first
        return {"id": self.id, **nxt(self)}


class HowToLearn(BaseModel):
    classes: List[ClassLevel]
    subclasses: List[SubclassLevel]
    races: List[RaceLevel]
    subraces: List[SubRaceLevel]

    model_config = ConfigDict(extra="forbid")


class SchoolOfMagic(str, Enum):
    ABJURATION = "Abjuration"
    CONJURATION = "Conjuration"
    DIVINATION = "Divination"
    ENCHANTMENT = "Enchantment"
    EVOCATION = "Evocation"
    ILLUSION = "Illusion"
    NECROMANCY = "Necromancy"
    TRANSMUTATION = "Transmutation"


SPELL_UUID_NAMESPACE = UUID("4d783016-42b9-4a02-9fa2-03b0372081ec")


class Spell(BaseModel):
    name: str
    short_description: str
    long_description: str
    school: SchoolOfMagic
    level: int
    properties: SpellProperties
    can_upcast: bool
    how_to_learn: HowToLearn

    model_config = ConfigDict(extra="forbid")

    @computed_field  # type: ignore[prop-decorator]
    @property
    def id(self) -> UUID:
        return uuid5(SPELL_UUID_NAMESPACE, self.name)

    # Custom serializer to ensure 'id' comes first
    @model_serializer(mode="wrap")
    def custom_serialize(self, nxt: SerializerFunctionWrapHandler) -> dict:
        # Ensure 'id' comes first
        return {"id": self.id, **nxt(self)}


class Spells(RootModel):
    root: List[Spell]

    def append(self, spell: Spell) -> None:
        return self.root.append(spell)

    def __getitem__(self, item):
        return self.root[item]

    def __iter__(self):
        return iter(self.root)

    def __len__(self) -> int:
        return len(self.root)
