import sys

if sys.version_info >= (3, 9):
    from typing import Annotated
else:
    from typing_extensions import Annotated

import json
import logging
from typing import Any, Awaitable, Callable, Dict, List, Optional
from uuid import UUID

from fastapi import FastAPI, Path, Request, Response
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, computed_field

from .armour import HEAVY_ARMOUR, LIGHT_ARMOUR, MEDIUM_ARMOUR, SHIELD
from .cantrip import bard_cantrips, cleric_cantrips
from .characteristic import Characteristic
from .class_action import (
    ClassAction,
    action_surge,
    charm_animals_and_plants,
    destructive_wrath,
    guided_strike,
    invoke_duplicity,
    knowledge_of_the_ages,
    preserve_life,
    radiance_of_dawn,
    second_wind,
)
from .class_resources import ClassResources
from .classes import Class
from .feat import new_feat
from .feature import Feature
from .fighting_style import (
    ARCHERY,
    DEFENCE,
    DUELLING,
    GREAT_WEAPON_FIGHTING,
    PROTECTION,
    TWO_WEAPON_FIGHTING,
    FightingStyle,
)
from .proficiency import Proficiencies
from .spell import bard_level_1_spells
from .subclass import (
    CantripChoice,
    Choices,
    SpellChoice,
    Subclass,
    battle_master,
    berserker,
    champion,
    college_of_lore,
    college_of_swords,
    college_of_valour,
    eldricht_knight,
    knowledge_domain,
    life_domain,
    light_domain,
    nature_domain,
    tempest_domain,
    trickery_domain,
    war_domain,
    wild_magic,
    wildheart,
)
from .weapon import (
    CLUB,
    DAGGER,
    FLAIL,
    HAND_CROSSBOW,
    JAVELIN,
    LIGHT_CROSSBOW,
    LONGSWORD,
    MACE,
    MARTIAL_WEAPONS,
    MORNINGSTAR,
    QUARTERSTAFF,
    RAPIER,
    SCIMITAR,
    SHORTSWORD,
    SICKLE,
    SIMPLE_WEAPONS,
    SPEAR,
)

logging.basicConfig(
    filename="bg3_py.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


__version__ = "0.1.0"


class PrettyJSONResponse(Response):
    media_type = "application/json"

    def render(self, content: Any) -> bytes:
        return json.dumps(
            content,
            ensure_ascii=False,
            allow_nan=False,
            indent=4,
            separators=(", ", ": "),
        ).encode("utf-8")


app = FastAPI()


class ClassLevellingResult(BaseModel):
    class_name: Class
    level: int
    feat: Optional[bool] = None
    class_actions: Optional[List[ClassAction]] = None
    features: Optional[List[Feature]] = None
    fighting_style: Optional[List[FightingStyle]] = None
    class_resources: Optional[ClassResources] = None
    proficiencies: Optional[Proficiencies] = None
    choices: Optional[Choices] = None


class Character(BaseModel):
    classes: List[Class]

    subclasses: Dict[Class, Subclass]

    @computed_field  # type: ignore[prop-decorator]
    @property
    def level(self) -> int:
        return len(self.classes)


db: Dict[UUID, Character] = {
    UUID("3a732dff-8ed6-4cbd-a39b-897a17f04888"): Character(
        classes=[Class.CLERIC, Class.CLERIC, Class.CLERIC],
        subclasses={Class.CLERIC: tempest_domain},
    ),
    UUID("22f7ecfa-9059-41c8-bd92-870e86499b4f"): Character(
        classes=[
            Class.FIGHTER,
            Class.FIGHTER,
            Class.FIGHTER,
            Class.FIGHTER,
            Class.FIGHTER,
            Class.FIGHTER,
            Class.FIGHTER,
        ],
        subclasses={Class.FIGHTER: battle_master},
    ),
    UUID("df4c67ae-e992-4fde-bc95-4118709ee1e9"): Character(
        classes=[
            Class.FIGHTER,
            Class.FIGHTER,
            Class.FIGHTER,
            Class.FIGHTER,
            Class.FIGHTER,
            Class.FIGHTER,
            Class.FIGHTER,
            Class.FIGHTER,
        ],
        subclasses={Class.FIGHTER: eldricht_knight},
    ),
}


app.mount("/static", StaticFiles(directory="static"), name="static")


@app.middleware("http")
async def add_content_type_static_files(
    request: Request, call_next: Callable[[Request], Awaitable[Response]]
) -> Response:
    response = await call_next(request)

    if request.url.path.startswith("/static/") and request.url.path.endswith(".webp"):
        response.headers["content-type"] = "image/webp"

    return response


@app.get("/characters/{character_id}", response_class=PrettyJSONResponse)
def get_character(character_id: UUID) -> Character:
    return db[character_id]


@app.get(
    "/users/{user_id}/classes/{class_name}",
    response_class=PrettyJSONResponse,
    response_model_exclude_unset=True,
)
def classes(
    user_id: Annotated[UUID, Path()], class_name: Annotated[Class, Path()]
) -> ClassLevellingResult:
    character = db[user_id]

    level = character.classes.count(class_name) + 1

    result = ClassLevellingResult(class_name=class_name, level=level)

    feat = new_feat(class_name, level)

    if feat is True:
        result.feat = True

    print(level)

    if class_name == Class.BARBARIAN:
        if level == 0:
            result.proficiencies = Proficiencies(
                armours=[LIGHT_ARMOUR, MEDIUM_ARMOUR, SHIELD],
                weapons=SIMPLE_WEAPONS + MARTIAL_WEAPONS,
                saving_throws=[Characteristic.STRENGTH, Characteristic.CONSTITUTION],
            )
        elif level == 1:
            result.features = [Feature(name="Rage"), Feature(name="Unarmored defense")]
            result.class_resources = ClassResources(rage_points=2)
        elif level == 2:
            result.features = [Feature(name="Reckless attack"), Feature(name="Danger sense")]
        elif level == 3:
            result.features = [Feature(name="Primal path")]
            result.class_resources = ClassResources(rage_points=3)
            result.choices = Choices(subclass=[wildheart, berserker, wild_magic])
        elif level == 4:
            pass
        elif level == 5:
            result.features = [Feature(name="Extra attack"), Feature(name="Fast movement")]
        elif level == 6:
            result.class_resources = ClassResources(rage_points=4)
        elif level == 7:
            result.features = [Feature(name="Feral instinct")]
        elif level == 8:
            pass
        elif level == 9:
            result.features = [Feature(name="Brutal Critical")]
        elif level == 10:
            pass
        elif level == 11:
            result.features = [Feature(name="Relentless rage")]
        elif level == 12:
            result.class_resources = ClassResources(rage_points=5)

    if class_name == Class.BARD:
        if level == 0:
            result.proficiencies = Proficiencies(
                armours=[LIGHT_ARMOUR],
                weapons=SIMPLE_WEAPONS + [HAND_CROSSBOW, RAPIER, LONGSWORD, SHORTSWORD],
                saving_throws=[Characteristic.DEXTERITY, Characteristic.CHARISMA],
            )
        elif level == 1:
            result.class_resources = ClassResources(bardic_inspirations=3)
            result.choices = Choices(
                cantrips=CantripChoice(number=2, cantrips=bard_cantrips),
                spells=SpellChoice(number=4, spells=bard_level_1_spells),
            )
        elif level == 2:
            result.features = [Feature(name="Song of the Rest"), Feature(name="Jack of All Trades")]
        elif level == 3:
            result.choices = Choices(
                subclass=[college_of_lore, college_of_valour, college_of_swords]
            )

    if class_name == Class.CLERIC:
        if level == 0:
            result.proficiencies = Proficiencies(
                armours=[LIGHT_ARMOUR, MEDIUM_ARMOUR, SHIELD],
                weapons=SIMPLE_WEAPONS + [FLAIL, MORNINGSTAR],
                saving_throws=[Characteristic.WISDOM, Characteristic.CHARISMA],
            )
        elif level == 1:
            result.choices = Choices(
                cantrips=CantripChoice(number=3, cantrips=cleric_cantrips),
                subclass=[
                    life_domain,
                    light_domain,
                    trickery_domain,
                    knowledge_domain,
                    nature_domain,
                    tempest_domain,
                    war_domain,
                ],
            )
        elif level == 2:
            result.class_resources = ClassResources(channel_divinity_charges=1)

            if Class.CLERIC not in character.subclasses:
                raise ValueError("No subclass chosen")

            if character.subclasses[class_name] == life_domain:
                result.class_actions = [preserve_life]
            elif character.subclasses[class_name] == light_domain:
                result.class_actions = [radiance_of_dawn]
            elif character.subclasses[class_name] == trickery_domain:
                result.class_actions = [invoke_duplicity]
            elif character.subclasses[class_name] == knowledge_domain:
                result.class_actions = [knowledge_of_the_ages]
            elif character.subclasses[class_name] == nature_domain:
                result.class_actions = [charm_animals_and_plants]
            elif character.subclasses[class_name] == tempest_domain:
                result.class_actions = [destructive_wrath]
            else:
                result.class_actions = [guided_strike]

    if class_name == Class.DRUID:
        if level == 0:
            result.proficiencies = Proficiencies(
                armours=[LIGHT_ARMOUR, MEDIUM_ARMOUR, SHIELD],
                weapons=[CLUB, DAGGER, JAVELIN, MACE, QUARTERSTAFF, SCIMITAR, SICKLE, SPEAR],
                saving_throws=[Characteristic.WISDOM, Characteristic.INTELLIGENCE],
            )

    if class_name == Class.FIGHTER:
        if level == 0:
            result.proficiencies = Proficiencies(
                armours=[
                    LIGHT_ARMOUR,
                    MEDIUM_ARMOUR,
                    HEAVY_ARMOUR,
                    SHIELD,
                ],
                weapons=SIMPLE_WEAPONS + MARTIAL_WEAPONS,
                saving_throws=[Characteristic.STRENGTH, Characteristic.CONSTITUTION],
            )
        elif level == 1:
            result.fighting_style = [
                ARCHERY,
                DEFENCE,
                DUELLING,
                GREAT_WEAPON_FIGHTING,
                PROTECTION,
                TWO_WEAPON_FIGHTING,
            ]
            result.class_actions = [second_wind]
        elif level == 2:
            result.class_actions = [action_surge]
        elif level == 3:
            result.choices = Choices(subclass=[battle_master, eldricht_knight, champion])
        elif level == 4:
            pass
        elif level == 5:
            result.features = [Feature(name="Extra attack")]
        elif level == 6:
            pass
        elif level == 7:
            if class_name not in character.subclasses:
                raise ValueError("No subclass chosen")

            if character.subclasses[class_name] == battle_master:
                # 2 additional manoeuvres
                result.class_resources = ClassResources(superiority_dices=5)
            elif character.subclasses[class_name] == eldricht_knight:
                result.features = [Feature(name="War Magic")]
            else:
                result.features = [
                    Feature(name="Remarkable Athlete: Jump"),
                    Feature(name="Remarkable Athlete: Proficiency"),
                ]
        elif level == 8:
            pass
        elif level == 9:
            result.features = [Feature(name="Indomitable")]
        elif level == 10:
            pass
        elif level == 11:
            result.features = [Feature(name="Improved Extra Attack")]
        elif level == 12:
            pass

    if class_name == Class.MONK:
        if level == 0:
            result.proficiencies = Proficiencies(
                armours=[],
                weapons=SIMPLE_WEAPONS + [SHORTSWORD],
                saving_throws=[Characteristic.STRENGTH, Characteristic.DEXTERITY],
            )

    if class_name == Class.PALADIN:
        if level == 0:
            result.proficiencies = Proficiencies(
                armours=[
                    LIGHT_ARMOUR,
                    MEDIUM_ARMOUR,
                    HEAVY_ARMOUR,
                    SHIELD,
                ],
                weapons=SIMPLE_WEAPONS + MARTIAL_WEAPONS,
                saving_throws=[Characteristic.WISDOM, Characteristic.CHARISMA],
            )

    if class_name == Class.RANGER:
        if level == 0:
            result.proficiencies = Proficiencies(
                armours=[LIGHT_ARMOUR, MEDIUM_ARMOUR],
                weapons=SIMPLE_WEAPONS + MARTIAL_WEAPONS,
                saving_throws=[Characteristic.STRENGTH, Characteristic.DEXTERITY],
            )

    if class_name == Class.ROGUE:
        if level == 0:
            result.proficiencies = Proficiencies(
                armours=[LIGHT_ARMOUR],
                weapons=SIMPLE_WEAPONS + [HAND_CROSSBOW, LONGSWORD, RAPIER, SHORTSWORD],
                saving_throws=[Characteristic.DEXTERITY, Characteristic.INTELLIGENCE],
            )

    if class_name == Class.SORCERER:
        if level == 0:
            result.proficiencies = Proficiencies(
                armours=[],
                weapons=[DAGGER, QUARTERSTAFF, LIGHT_CROSSBOW],
                saving_throws=[Characteristic.CHARISMA, Characteristic.CONSTITUTION],
            )

    if class_name == Class.WARLOCK:
        if level == 0:
            result.proficiencies = Proficiencies(
                armours=[LIGHT_ARMOUR],
                weapons=SIMPLE_WEAPONS,
                saving_throws=[Characteristic.WISDOM, Characteristic.CHARISMA],
            )

    if class_name == Class.WIZARD:
        if level == 0:
            result.proficiencies = Proficiencies(
                armours=[],
                weapons=[DAGGER, QUARTERSTAFF, LIGHT_CROSSBOW],
                saving_throws=[Characteristic.INTELLIGENCE, Characteristic.WISDOM],
            )

    return result
