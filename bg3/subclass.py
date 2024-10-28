from __future__ import annotations

from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from .class_action import ClassAction
from .class_resources import ClassResources
from .feature import Feature
from .spell import Spell
from .spell_new import Cantrip


class CantripChoice(BaseModel):
    number: int
    cantrips: List[Cantrip]


class SpellChoice(BaseModel):
    number: int
    spells: List[Spell]


class Choices(BaseModel):
    cantrips: Optional[CantripChoice] = None
    spells: Optional[SpellChoice] = None
    subclass: Optional[List[Subclass]] = None


class Subclass(BaseModel):
    id: UUID
    name: str
    features: Optional[List[Feature]] = None
    class_actions: Optional[List[ClassAction]] = None
    class_resources: Optional[ClassResources] = None
    choices: Optional[Choices] = None

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Subclass):
            raise NotImplementedError

        return self.id == other.id


# Barbarian subclasses
wildheart = Subclass(id="1c88b2b1-c375-4f73-9bf5-75a6671e790e", name="Wildheart")
berserker = Subclass(id="a3b2b0d5-0a4e-4b3d-8f3b-5c3d9e3e1e6d", name="Berserker")
wild_magic = Subclass(id="e7c4b9e3-4e0a-4c1d-9f8c-3f5f5e7f0b5b", name="Wild Magic")

# Bard subclasses
college_of_lore = Subclass(
    id="2918b21a-dd37-48b7-887c-cd0defa4a6b7",
    name="College of Lore",
    features=[Feature(name="Cutting Words")],
)
college_of_valour = Subclass(
    id="df14418a-a4ef-4e79-80ed-1b932238c9d6",
    name="College of Valour",
)
college_of_swords = Subclass(
    id="ebfbf46b-d0eb-42dc-8328-e6eb9bc4e6f8",
    name="College of Swords",
)

# Cleric subclasses
life_domain = Subclass(
    id="dd0b071b-d34f-4c2a-a6ff-cdb81e7a5c3d",
    name="Life",
    features=[Feature(name="Disciple of Life")],
)
light_domain = Subclass(
    id="5ec6eefa-9ecf-4495-b598-04839e3b7c98",
    name="Light",
    features=[Feature(name="Warding Flare")],
)
trickery_domain = Subclass(
    id="8b2f90db-5825-4559-8a79-106223b6fe66",
    name="Trickery",
    features=[Feature(name="Blessing of the Trickster")],
)
knowledge_domain = Subclass(
    id="503b56f6-3ec1-4954-a5b8-cffdea686afb",
    name="Knowledge",
    features=[Feature(name="Knowledge")],
)
nature_domain = Subclass(
    id="0e17411c-b4b0-4bd3-9cd2-6507a03fda48",
    name="Nature",
    features=[Feature(name="Acolyte of Nature")],
)
tempest_domain = Subclass(
    id="71b5b70c-2b7c-49c4-a778-3f8c240b8365",
    name="Tempest",
    features=[Feature(name="Wrath of the Storm")],
)
war_domain = Subclass(
    id="bd97f295-2ab2-4ac9-a228-b540310e6c0e",
    name="War",
    features=[Feature(name="War Priest")],
)

# Fighter subclasses
battle_master = Subclass(
    id="4863c105-afcf-4043-a180-554c93141506",
    name="Battle Master",
    class_resources=ClassResources(superiority_dices=4),
)
eldricht_knight = Subclass(
    id="f1b5b7d4-4e6e-4c6e-8f6c-1b7e9e4f6b3c",
    name="Eldricht Knight",
    features=[Feature(name="Weapon Bond")],
)
champion = Subclass(
    id="16b2fc47-8b1e-41a1-ad1c-bca3762dca4e",
    name="Champion",
    features=[Feature(name="Improved Critical Hit")],
)

# Ranger subclasses
gloom_stalker = Subclass(id="1cbdf943-0533-4c54-82dd-ebcc5bcace6b", name="Gloom Stalker")

# Rogue subclasses
arcane_trickster = Subclass(id="58ffa98a-9089-4d4b-9af4-47a03e624f80", name="Arcane Trickster")

# Warlock subclasses
the_fiend = Subclass(id="a2b5f9fb-32c9-4898-b252-47b1253a5d17", name="The Fiend")
