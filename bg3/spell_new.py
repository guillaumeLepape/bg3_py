from enum import Enum
from typing import List, Optional
from uuid import UUID, uuid5

from pydantic import (
    BaseModel,
    ConfigDict,
    SerializerFunctionWrapHandler,
    computed_field,
    model_serializer,
)

from .characteristic import Characteristic
from .cost import Cost
from .levelling import HowToLearn


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


class CantripProperties(BaseModel):
    cost: List[Cost]
    # cost_on_hit: Optional[List[Cost]] = None
    concentration: bool
    # ritual: bool
    saving_throw: Optional[Characteristic] = None

    model_config = ConfigDict(extra="forbid")


class Cantrip(BaseModel):
    name: str
    short_description: str
    long_description: str
    school: SchoolOfMagic
    properties: CantripProperties
    how_to_learn: HowToLearn

    model_config = ConfigDict(extra="forbid")

    @computed_field  # type: ignore[prop-decorator]
    @property
    def id(self) -> UUID:
        return uuid5(SPELL_UUID_NAMESPACE, self.name)

    # Custom serializer to ensure 'id' comes first
    @model_serializer(mode="wrap")
    def custom_serialize(self, nxt: SerializerFunctionWrapHandler) -> dict:
        return {"id": self.id, **nxt(self)}


class SpellProperties(BaseModel):
    cost: List[Cost]
    cost_on_hit: Optional[List[Cost]] = None
    concentration: bool
    ritual: bool
    saving_throw: Optional[Characteristic] = None

    model_config = ConfigDict(extra="forbid")


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
        return {"id": self.id, **nxt(self)}


class Spells(BaseModel):
    cantrips: List[Cantrip]
    spells: List[Spell]
