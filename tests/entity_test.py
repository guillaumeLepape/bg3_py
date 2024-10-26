from bg3.entity import (
    Character,
    EntityCharacteristic,
    Foe,
    Proficiencies,
    Weapon,
    attack,
    compute_probably_to_hit,
)
from bg3.weapon import FLAIL, MARTIAL_WEAPONS, SCIMITAR, SIMPLE_WEAPONS


def test_compute_probably_to_hit():
    character = Character(
        level=3,
        health_points=100,
        armour_class=18,
        name="Me",
        characteristics=EntityCharacteristic(
            strength=16, dexterity=16, constitution=16, intelligence=8, wisdom=12, charisma=10
        ),
        weapon=Weapon(roll=(1, 8), enchantment=1, finesse=False, type=SCIMITAR),
        proficiencies=Proficiencies(weapons=MARTIAL_WEAPONS + SIMPLE_WEAPONS),
    )

    foe = Foe(
        level=3,
        health_points=50,
        armour_class=14,
        name="Gobelin",
        characteristics=EntityCharacteristic(
            strength=16, dexterity=14, constitution=16, intelligence=8, wisdom=12, charisma=10
        ),
        weapon=Weapon(roll=(1, 8), enchantment=1, finesse=False, type=FLAIL),
        proficiencies=Proficiencies(weapons=MARTIAL_WEAPONS + SIMPLE_WEAPONS),
    )

    assert compute_probably_to_hit(character, foe) == 65

    for _ in range(10):
        attack(character, foe)
