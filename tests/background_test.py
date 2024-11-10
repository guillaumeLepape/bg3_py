from collections import OrderedDict
from typing import Dict, Set

from bg3.background import Background
from bg3.levelling_progression import SKILL_PROFICIENCY
from bg3.skill import Skill


def test_background_size() -> None:
    assert len(Background) == 12


def test_background_to_skills() -> None:
    background_to_skills: Dict[Background, Set[Skill]] = OrderedDict()

    for skill_proficiency, how_to_learn in SKILL_PROFICIENCY.items():
        for background in (background_level.name for background_level in how_to_learn.backgrounds):
            if background not in background_to_skills:
                background_to_skills[background] = {skill_proficiency}
            else:
                background_to_skills[background].add(skill_proficiency)

    assert background_to_skills == {
        Background.ACOLYTE: {Skill.INSIGHT, Skill.RELIGION},
        Background.CHARLATAN: {Skill.DECEPTION, Skill.SLEIGHT_OF_HAND},
        Background.CRIMINAL: {Skill.DECEPTION, Skill.STEALTH},
        Background.ENTERTAINER: {Skill.ACROBATICS, Skill.PERFORMANCE},
        Background.FOLK_HERO: {Skill.ANIMAL_HANDLING, Skill.SURVIVAL},
        Background.GUILD_ARTISAN: {Skill.INSIGHT, Skill.PERSUASION},
        Background.HAUNTED_ONE: {Skill.MEDICINE, Skill.INTIMIDATION},
        Background.NOBLE: {Skill.HISTORY, Skill.PERSUASION},
        Background.OUTLANDER: {Skill.ATHLETICS, Skill.SURVIVAL},
        Background.SAGE: {Skill.ARCANA, Skill.HISTORY},
        Background.SOLDIER: {Skill.ATHLETICS, Skill.INTIMIDATION},
        Background.URCHIN: {Skill.SLEIGHT_OF_HAND, Skill.STEALTH},
    }
