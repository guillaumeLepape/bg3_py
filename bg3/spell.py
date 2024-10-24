import logging
from pathlib import Path
from uuid import UUID

from pydantic import BaseModel, computed_field

logger = logging.getLogger(__file__)


class Spell(BaseModel):
    id: UUID
    name: str
    level: int
    ritual: bool = False

    @computed_field
    def icon(self) -> str:
        return f"/static/cantrips/{self.name.lower().replace(' ', '_')}.jpg"

    def check_icon(self) -> bool:
        path = self.icon.removeprefix("/")

        return (Path(__file__).parents[1] / path).is_file()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Spell):
            raise NotImplementedError

        return self.id == other.id


animal_friendship = Spell(
    id="198bc18f-bac8-4b72-a73f-d20bd94a80af", name="Animal Friendship", level=1
)
bane = Spell(id="384471af-e2f5-481e-80a0-c364151e814e", name="Bane", level=1)
charm_person = Spell(id="c1a4b8c4-0f0a-4f6e-8d6e-2b0b1e6d5c7a", name="Charm Person", level=1)
cure_wounds = Spell(id="6d7b9e4a-9e4e-4e0b-8e2e-7e9e8e1e7e9e", name="Cure Wounds", level=1)
disguise_self = Spell(
    id="4d7b9e4a-9e4e-4e0b-8e2e-7e9e8e1e7e9e", name="Disguise Self", level=1, ritual=True
)
dissonant_whispers = Spell(
    id="8d7b9e4a-9e4e-4e0b-8e2e-7e9e8e1e7e9e", name="Dissonant Whispers", level=1
)
faerie_fire = Spell(id="2d7b9e4a-9e4e-4e0b-8e2e-7e9e8e1e7e9e", name="Faerie Fire", level=1)
feather_fall = Spell(
    id="1d7b9e4a-9e4e-4e0b-8e2e-7e9e8e1e7e9e", name="Feather Fall", level=1, ritual=True
)
healing_word = Spell(id="0d7b9e4a-9e4e-4e0b-8e2e-7e9e8e1e7e9e", name="Healing Word", level=1)
heroism = Spell(id="3d7b9e4a-9e4e-4e0b-8e2e-7e9e8e1e7e9e", name="Heroism", level=1)
longstrider = Spell(
    id="5d7b9e4a-9e4e-4e0b-8e2e-7e9e8e1e7e9e", name="Longstrider", level=1, ritual=True
)
sleep = Spell(id="7d7b9e4a-9e4e-4e0b-8e2e-7e9e8e1e7e9e", name="Sleep", level=1)
speak_with_animals = Spell(
    id="9d7b9e4a-9e4e-4e0b-8e2e-7e9e8e1e7e9e", name="Speak with Animals", level=1, ritual=True
)
tasha_hideous_laughter = Spell(
    id="ad7b9e4a-9e4e-4e0b-8e2e-7e9e8e1e7e9e", name="Tasha's Hideous Laughter", level=1
)
thunderwave = Spell(id="bd7b9e4a-9e4e-4e0b-8e2e-7e9e8e1e7e9e", name="Thunderwave", level=1)

bard_level_1_spells = [
    animal_friendship,
    bane,
    charm_person,
    cure_wounds,
    disguise_self,
    dissonant_whispers,
    faerie_fire,
    feather_fall,
    healing_word,
    heroism,
    longstrider,
    sleep,
    speak_with_animals,
    tasha_hideous_laughter,
    thunderwave,
]


for var in dict(locals()).values():
    if isinstance(var, Spell) and var.check_icon() is False:
        logger.warning(f"Icon not found for spell: {var.name}")
