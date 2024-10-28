from bg3.characteristic import Characteristic
from bg3.skill import CHARACTERISTIC_TO_SKILLS, Skill


def test_skill() -> None:
    assert len(Skill) == 18
    assert len(CHARACTERISTIC_TO_SKILLS) == 5
    assert {skill for skills in CHARACTERISTIC_TO_SKILLS.values() for skill in skills} == set(Skill)

    assert len(CHARACTERISTIC_TO_SKILLS[Characteristic.STRENGTH]) == 1
    assert len(CHARACTERISTIC_TO_SKILLS[Characteristic.DEXTERITY]) == 3
    assert len(CHARACTERISTIC_TO_SKILLS[Characteristic.INTELLIGENCE]) == 5
    assert len(CHARACTERISTIC_TO_SKILLS[Characteristic.WISDOM]) == 5
    assert len(CHARACTERISTIC_TO_SKILLS[Characteristic.CHARISMA]) == 4
