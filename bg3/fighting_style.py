from pathlib import Path
from typing import List
from uuid import UUID, uuid5

from pydantic import (
    BaseModel,
    ConfigDict,
    RootModel,
    SerializerFunctionWrapHandler,
    computed_field,
    model_serializer,
)

from .classes import Class, SubClass
from .spell_new import ClassLevel, HowToLearn, SubclassLevel

FIGHTING_STYLE_UUID_NAMESPACE = UUID("0becb2f3-a09d-42ac-9508-1f7331c7bad2")


class FightingStyle(BaseModel):
    name: str
    description: str

    how_to_learn: HowToLearn

    model_config = ConfigDict(extra="forbid")

    @computed_field  # type: ignore[prop-decorator]
    @property
    def id(self) -> UUID:
        return uuid5(FIGHTING_STYLE_UUID_NAMESPACE, self.name)

    # Custom serializer to ensure 'id' comes first
    @model_serializer(mode="wrap")
    def custom_serialize(self, nxt: SerializerFunctionWrapHandler) -> dict:
        return {"id": self.id, **nxt(self)}


ARCHERY = FightingStyle(
    name="Archery",
    description="You gain a +2 bonus to Ranged Weapon attack rolls.",
    how_to_learn=HowToLearn(
        classes=[ClassLevel(name=Class.FIGHTER, level=1), ClassLevel(name=Class.RANGER, level=2)],
        subclasses=[SubclassLevel(name=SubClass.CHAMPION, level=10)],
        races=[],
        subraces=[],
    ),
)

DEFENCE = FightingStyle(
    name="Defence",
    description="You gain a +1 bonus to armour Class while wearing Armour.",
    how_to_learn=HowToLearn(
        classes=[
            ClassLevel(name=Class.FIGHTER, level=1),
            ClassLevel(name=Class.PALADIN, level=2),
            ClassLevel(name=Class.RANGER, level=2),
        ],
        subclasses=[SubclassLevel(name=SubClass.CHAMPION, level=10)],
        races=[],
        subraces=[],
    ),
)

DUELLING = FightingStyle(
    name="Duelling",
    description=(
        "When you are wielding a melee weapon that is not Two-Handed or Versatile in one hand and "
        "no weapon in the other hand, you gain a +2 bonus to damage rolls with that weapon, "
        "increasing your chance to do heavy damage."
    ),
    how_to_learn=HowToLearn(
        classes=[
            ClassLevel(name=Class.FIGHTER, level=1),
            ClassLevel(name=Class.PALADIN, level=2),
            ClassLevel(name=Class.RANGER, level=2),
        ],
        subclasses=[
            SubclassLevel(name=SubClass.COLLEGE_OF_SWORDS, level=3),
            SubclassLevel(name=SubClass.CHAMPION, level=10),
        ],
        races=[],
        subraces=[],
    ),
)

GREAT_WEAPON_FIGHTING = FightingStyle(
    name="Great Weapon Fighting",
    description=(
        "When you roll a 1 or 2 on a damage die for an attack with a Two-Handed melee weapon, that "
        "die is rerolled once."
    ),
    how_to_learn=HowToLearn(
        classes=[
            ClassLevel(name=Class.FIGHTER, level=1),
            ClassLevel(name=Class.PALADIN, level=2),
        ],
        subclasses=[
            SubclassLevel(name=SubClass.CHAMPION, level=10),
        ],
        races=[],
        subraces=[],
    ),
)

PROTECTION = FightingStyle(
    name="Protection",
    description=(
        "When you have a Shield, impose Disadvantage on an enemy who attacks one of your allies "
        "when you are within  1.5 m / 5 ft. You must be able to see the enemy."
    ),
    how_to_learn=HowToLearn(
        classes=[
            ClassLevel(name=Class.FIGHTER, level=1),
            ClassLevel(name=Class.PALADIN, level=2),
        ],
        subclasses=[
            SubclassLevel(name=SubClass.CHAMPION, level=10),
        ],
        races=[],
        subraces=[],
    ),
)

TWO_WEAPON_FIGHTING = FightingStyle(
    name="Two-Weapon Fighting",
    description=(
        "When you make an offhand attack, you can add your Ability Modifier to the damage of the at"
        "tack."
    ),
    how_to_learn=HowToLearn(
        classes=[
            ClassLevel(name=Class.FIGHTER, level=1),
            ClassLevel(name=Class.RANGER, level=2),
        ],
        subclasses=[
            SubclassLevel(name=SubClass.COLLEGE_OF_SWORDS, level=3),
            SubclassLevel(name=SubClass.CHAMPION, level=10),
        ],
        races=[],
        subraces=[],
    ),
)


class FightingStyles(RootModel):
    root: List[FightingStyle]


fighting_styles = FightingStyles(
    root=[ARCHERY, DEFENCE, DUELLING, GREAT_WEAPON_FIGHTING, PROTECTION, TWO_WEAPON_FIGHTING]
)

if __name__ == "__main__":
    (Path(__file__).parent / "cli" / "fighting_styles.json").write_text(
        fighting_styles.model_dump_json(indent=4, exclude_none=True) + "\n"
    )
