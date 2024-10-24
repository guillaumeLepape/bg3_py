from uuid import UUID

from pydantic import BaseModel


class FightingStyle(BaseModel):
    id: UUID
    name: str
    description: str


archery = FightingStyle(
    id="f9cf5a8b-e701-48bd-8a3f-ab34356754fc",
    name="Archery",
    description="You gain a +2 bonus to Ranged Weapon attack rolls.",
)

defence = FightingStyle(
    id="e9c499f0-d6ba-4eb8-98d2-2583c35e30c5",
    name="Defence",
    description="You gain a +1 bonus to armour Class while wearing Armour.",
)

duelling = FightingStyle(
    id="d738da35-7546-49b6-9145-a192c9ccde83",
    name="Duelling",
    description=(
        "When you are wielding a melee weapon that is not Two-Handed or Versatile in one hand and "
        "no weapon in the other hand, you gain a +2 bonus to damage rolls with that weapon, "
        "increasing your chance to do heavy damage."
    ),
)

great_weapon_fighting = FightingStyle(
    id="5a3784b7-8792-4d76-90b1-38e9f54a496d",
    name="Great Weapon Fighting",
    description=(
        "When you roll a 1 or 2 on a damage die for an attack with a Two-Handed melee weapon, that "
        "die is rerolled once."
    ),
)

protection = FightingStyle(
    id="1c9f4f1b-e52d-447e-91df-2d5c40e5e049",
    name="Protection",
    description=(
        "When you have a Shield, impose Disadvantage on an enemy who attacks one of your allies "
        "when you are within  1.5 m / 5 ft. You must be able to see the enemy."
    ),
)

two_weapon_fighting = FightingStyle(
    id="065f1944-5357-417d-98dd-a1ba21da6ffb",
    name="Two-Weapon Fighting",
    description=(
        "When you make an offhand attack, you can add your Ability Modifier to the damage of the at"
        "tack."
    ),
)
