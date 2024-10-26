from pathlib import Path
from typing import List
from uuid import UUID, uuid5

from pydantic import (
    BaseModel,
    RootModel,
    SerializerFunctionWrapHandler,
    computed_field,
    model_serializer,
)

from .classes import Class
from .spell_new import ClassLevel, HowToLearn

FAVOURED_ENEMY_UUID_NAMESPACE = UUID("d05f8f8e-ecf9-45f3-94f6-0b2e44152e3e")


class FavouredEnemy(BaseModel):
    name: str
    description: str
    grants: List[str]

    how_to_learn: HowToLearn

    @computed_field  # type: ignore[prop-decorator]
    @property
    def id(self) -> UUID:
        return uuid5(FAVOURED_ENEMY_UUID_NAMESPACE, self.name)

    # Custom serializer to ensure 'id' comes first
    @model_serializer(mode="wrap")
    def custom_serialize(self, nxt: SerializerFunctionWrapHandler) -> dict:
        return {"id": self.id, **nxt(self)}


HOW_TO_LEARN_FAVOURED_ENEMY = HowToLearn(
    classes=[
        ClassLevel(name=Class.RANGER, level=1),
        ClassLevel(name=Class.RANGER, level=6),
        ClassLevel(name=Class.RANGER, level=10),
    ],
    subclasses=[],
    races=[],
    subraces=[],
)


BOUNTY_HUNTER = FavouredEnemy(
    name="Bounty Hunter",
    description=(
        "Gain Proficiency in Investigation. Creatures you hit with Ensnaring Strike (either ranged "
        "or melee) have Disadvantage on their Saving Throw."
    ),
    grants=["Investigation Proficiency"],
    how_to_learn=HOW_TO_LEARN_FAVOURED_ENEMY,
)


KEEPER_OF_THE_VEIL = FavouredEnemy(
    name="Keeper of the Veil",
    description=(
        "You specialise in hunting creatures from other planes of existence. You gain Proficiency "
        "in Arcana and can grant protection against aberrations, celestials, elementals, fey, "
        "fiends, and undead."
    ),
    grants=["Arcana Proficiency", "Protection from Evil and Good, Recharge on long rest."],
    how_to_learn=HOW_TO_LEARN_FAVOURED_ENEMY,
)

MAGE_BREAKER = FavouredEnemy(
    name="Mage Breaker",
    description=(
        "You have a history of battling spellcasters. Gain Proficiency with Arcana and True "
        "Strike, which gives you Advantage Icon.png Advantage on Attack Rolls against a creature. "
        "Wisdom is your Spellcasting Ability for this spell."
    ),
    grants=["Arcana Proficiency", "Cantrip: True Strike"],
    how_to_learn=HOW_TO_LEARN_FAVOURED_ENEMY,
)

RANGER_KNIGHT = FavouredEnemy(
    name="Ranger Knight",
    description=(
        "You have sworn to serve a crown or nation and seek to bring its foes to ruin. Gain "
        "Proficiency with History and Proficiency with Heavy Armour."
    ),
    grants=["Heavy armour Proficiency", "History Proficiency"],
    how_to_learn=HOW_TO_LEARN_FAVOURED_ENEMY,
)

SANCTIFIED_STALKER = FavouredEnemy(
    name="Sanctified Stalker",
    description=(
        "You swore to hunt the enemies of a holy or druidic order. Gain Proficiency with Religion "
        "and the Sacred Flame Cantrip, which deals 1d8 Radiant damage. Wisdom is your Spellcasting "
        "Ability for the Cantrip."
    ),
    grants=["Religion Proficiency", "Cantrip: Sacred Flame"],
    how_to_learn=HOW_TO_LEARN_FAVOURED_ENEMY,
)


class FavouredEnemies(RootModel):
    root: List[FavouredEnemy]


favoured_enemies = FavouredEnemies(
    root=[
        BOUNTY_HUNTER,
        KEEPER_OF_THE_VEIL,
        MAGE_BREAKER,
        RANGER_KNIGHT,
        SANCTIFIED_STALKER,
    ]
)

if __name__ == "__main__":
    (Path(__file__).parent / "cli" / "favoured_enemies.json").write_text(
        favoured_enemies.model_dump_json(indent=4, exclude_none=True) + "\n"
    )
