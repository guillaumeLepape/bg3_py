from uuid import UUID, uuid5

from pydantic import BaseModel, computed_field

FIGHTING_STYLE_UUID_NAMESPACE = UUID("0becb2f3-a09d-42ac-9508-1f7331c7bad2")


class FightingStyle(BaseModel):
    name: str
    description: str

    @computed_field  # type: ignore[prop-decorator]
    @property
    def id(self) -> UUID:
        return uuid5(FIGHTING_STYLE_UUID_NAMESPACE, self.name)


ARCHERY = FightingStyle(
    name="Archery", description="You gain a +2 bonus to Ranged Weapon attack rolls."
)

DEFENCE = FightingStyle(
    name="Defence", description="You gain a +1 bonus to armour Class while wearing Armour."
)

DUELLING = FightingStyle(
    name="Duelling",
    description=(
        "When you are wielding a melee weapon that is not Two-Handed or Versatile in one hand and "
        "no weapon in the other hand, you gain a +2 bonus to damage rolls with that weapon, "
        "increasing your chance to do heavy damage."
    ),
)

GREAT_WEAPON_FIGHTING = FightingStyle(
    name="Great Weapon Fighting",
    description=(
        "When you roll a 1 or 2 on a damage die for an attack with a Two-Handed melee weapon, that "
        "die is rerolled once."
    ),
)

PROTECTION = FightingStyle(
    name="Protection",
    description=(
        "When you have a Shield, impose Disadvantage on an enemy who attacks one of your allies "
        "when you are within  1.5 m / 5 ft. You must be able to see the enemy."
    ),
)

TWO_WEAPON_FIGHTING = FightingStyle(
    name="Two-Weapon Fighting",
    description=(
        "When you make an offhand attack, you can add your Ability Modifier to the damage of the at"
        "tack."
    ),
)
