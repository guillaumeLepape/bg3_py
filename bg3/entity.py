import random
from functools import partial
from typing import List, MutableMapping, Tuple, Union

from pydantic import BaseModel

from .characteristic import Characteristic
from .proficiency import Proficiencies
from .weapon import WeaponType


def roll_dice(number_of_faces: int) -> int:
    return random.randint(1, number_of_faces + 1)


roll_d20 = partial(roll_dice, 20)


class Weapon(BaseModel):
    roll: Tuple[int, int]
    finesse: bool = False
    enchantment: int
    type: WeaponType


def proficiency_bonus(level: int) -> int:
    return (level - 1) // 4 + 2


def compute_modifier(characteristic: int) -> int:
    return (characteristic - 10) // 2


class EntityCharacteristic(BaseModel, MutableMapping[Characteristic, int]):
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int

    def __getitem__(self, key: Characteristic) -> int:
        if key == Characteristic.STRENGTH:
            return self.strength
        elif key == Characteristic.DEXTERITY:
            return self.dexterity
        elif key == Characteristic.CONSTITUTION:
            return self.constitution
        elif key == Characteristic.INTELLIGENCE:
            return self.intelligence
        elif key == Characteristic.WISDOM:
            return self.wisdom
        elif key == Characteristic.CHARISMA:
            return self.charisma
        else:
            raise KeyError(key)

    def __setitem__(self, key: Characteristic, value: int):
        if key == Characteristic.STRENGTH:
            self.strength = value
        elif key == Characteristic.DEXTERITY:
            self.dexterity = value
        elif key == Characteristic.CONSTITUTION:
            self.constitution = value
        elif key == Characteristic.INTELLIGENCE:
            self.intelligence = value
        elif key == Characteristic.WISDOM:
            self.wisdom = value
        elif key == Characteristic.CHARISMA:
            self.charisma = value
        else:
            raise KeyError(key)

    def __delitem__(self, key: Characteristic):
        raise ValueError("Cannot delete characteristics")

    def __iter__(self):
        return iter(
            [
                Characteristic.STRENGTH,
                Characteristic.DEXTERITY,
                Characteristic.CONSTITUTION,
                Characteristic.INTELLIGENCE,
                Characteristic.WISDOM,
                Characteristic.CHARISMA,
            ]
        )

    def __len__(self):
        return 6


class Character(BaseModel):
    level: int
    health_points: int
    armour_class: int
    name: str
    characteristics: EntityCharacteristic
    weapon: Weapon
    proficiencies: Proficiencies


class Foe(BaseModel):
    level: int
    health_points: int
    armour_class: int
    name: str
    characteristics: EntityCharacteristic
    weapon: Weapon
    proficiencies: Proficiencies


Entity = Union[Character, Foe]


def is_proficient_with(weapon_proficiencies: List[WeaponType], weapon: Weapon) -> bool:
    return weapon.type in weapon_proficiencies


def compute_attack_modifier(attacker: Entity) -> int:
    if attacker.weapon.finesse:
        return max(
            compute_modifier(attacker.characteristics[Characteristic.STRENGTH]),
            compute_modifier(attacker.characteristics[Characteristic.DEXTERITY]),
        )
    else:
        return compute_modifier(attacker.characteristics[Characteristic.STRENGTH])


def compute_attack_roll_bonus(attacker: Entity) -> int:
    attack_modifier = compute_attack_modifier(attacker)

    return attack_modifier + attacker.weapon.enchantment + proficiency_bonus(attacker.level)


def compute_probably_to_hit(attacker: Entity, target: Entity) -> int:
    return max(21 - (target.armour_class - compute_attack_roll_bonus(attacker)), 1) * 5


def compute_damage(attacker: Entity) -> int:
    damage = 0
    for _ in range(attacker.weapon.roll[0]):
        damage += roll_dice(attacker.weapon.roll[1])
    return damage


def is_hit(attacker: Entity, target: Entity) -> bool:
    roll = roll_d20()

    if roll == 20:
        return True
    elif roll == 1:
        return False
    else:
        return roll + compute_attack_roll_bonus(attacker) >= target.armour_class


def attack(attacker: Entity, target: Entity):
    if is_hit(attacker, target):
        # Compute the damage
        print(f"{attacker.name} hits {target.name}")

        damage = compute_damage(attacker)

        target.health_points -= damage
        print(f"{target.name} takes {damage} damage")
    else:
        print(f"{attacker.name} misses {target.name}")
