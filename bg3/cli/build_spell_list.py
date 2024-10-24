import asyncio
import re
import warnings
from itertools import chain
from pathlib import Path
from typing import Any, Iterable, List, Optional, Tuple, Union

import httpx
from bs4 import BeautifulSoup

from bg3.characteristic import TRIGRAM_TO_CHARACTERISTIC, Characteristic, trigram_to_characteristic
from bg3.classes import CLASS_TO_SUBCLASSES, Class, SubClass
from bg3.cost import ACTION, BONUS_ACTION, REACTION, Cost, spell_slot
from bg3.races import Race, SubRace

from .common import (
    DRACONIC_ANCESTRY_TO_DAMAGE_TYPE,
    ClassLevel,
    FavouredEnemy,
    HowToLearn,
    LandCircle,
    NaturalExplorer,
    PactBoon,
    RaceLevel,
    SchoolOfMagic,
    Spell,
    SpellProperties,
    Spells,
    SubclassLevel,
    SubRaceLevel,
    Via,
    WildShape,
)

BASE_URL = "https://bg3.wiki"


def parse_cost(raw_cost: str) -> Cost:
    if raw_cost.lower() == "action":
        return ACTION

    if raw_cost.lower() == "bonus action":
        return BONUS_ACTION

    if raw_cost.lower() == "reaction":
        return REACTION

    match_regex = re.match(r"Level ([1-6]) Spell Slot", raw_cost)

    if match_regex:
        try:
            return spell_slot(int(match_regex.group(1)))
        except ValueError:
            pass

    exception_description = f"Invalid action: {raw_cost}"
    raise ValueError(exception_description)


def find_level_spells_header(soup: BeautifulSoup, level: int) -> Any:
    if level == 0:
        search_id = "Cantrips"
    else:
        search_id = f"Level_{level}_spells"

    for h4 in soup.find_all("h4"):
        if h4.find("span", id=search_id):
            return h4

    raise ValueError(f"Header not found for spells level {level}")


def prepare_spell_requests(
    spell_headers: Iterable[Tuple[int, Any]],
) -> List[Tuple[str, int, str]]:
    requests: List[Tuple[str, int, str]] = []

    for level, header in spell_headers:
        next_div = header.find_next("div")
        if next_div:
            for li in next_div.find_all("li"):
                span = li.find("span", class_="bg3wiki-icontext-text")

                name = span.a.text
                page_uri = span.a.get("href")

                requests.append((name, level, BASE_URL + page_uri))
        else:
            print(f"No div found following the spells level {level}.")

    return requests


def find_cost(properties: Any) -> List[str]:
    for dt in properties.find_all("dt"):
        if dt.text == "Cost":
            return dt.find_next("dd").text.split(" + ")

    raise ValueError(f"Cannot find cost in properties: {properties}")


def find_cost_on_hit(properties: Any) -> Optional[List[str]]:
    for dt in properties.find_all("dt"):
        if dt.text == "Cost on hit":
            return dt.find_next("dd").text.split(" + ")

    return None


def find_details(properties: Any) -> List[str]:
    for dt in properties.find_all("dt"):
        if dt.text == "Details":
            return [dd.text.rstrip().lstrip() for dd in dt.find_next_siblings("dd")]

    raise ValueError(f"Not details found: {properties}")


def find_upcast(soup: BeautifulSoup) -> bool:
    return (
        "Casting this spell at a higher level grants no additional benefit."
        not in soup.find("span", id="At_higher_levels").find_next("p").text
    )


def extract_additional_information(raw_name: str) -> Tuple[str, Optional[str]]:
    match_regex = re.match(r"^(.*?) \((.*?)\)$", raw_name)

    if match_regex is None:
        return raw_name, None

    raw_name, raw_via = match_regex.groups()

    return raw_name, raw_via


def parse_via(
    class_or_subclass: Union[Class, SubClass], raw_via: Optional[str]
) -> Union[Via, str, None]:
    if raw_via is None:
        return None

    # Sorcerer : Draconic Bloodline
    if class_or_subclass == SubClass.DRACONIC_BLOODLINE:
        for draconic_ancestry, damage_type in DRACONIC_ANCESTRY_TO_DAMAGE_TYPE.items():
            if f"{draconic_ancestry}/{damage_type}".lower() in raw_via.lower():
                return Via(draconic_ancestry=draconic_ancestry)

    # Sorcerer : Storm Sorcery
    if class_or_subclass == SubClass.STORM_SORCERY:
        if "Storm Spell".lower() in raw_via.lower():
            # skipping via, redundant with the subclass
            return None

    # Bard and Bard : College of Lore
    if (
        class_or_subclass == Class.BARD or class_or_subclass == SubClass.COLLEGE_OF_LORE
    ) and "Magical Secrets".lower() in raw_via.lower():
        return "magical_secrets"

    # Warlock
    if class_or_subclass == Class.WARLOCK:
        for pact_boon in PactBoon:
            if pact_boon.value.lower() in raw_via.lower():
                return Via(pact_boon=pact_boon)

    # Paladin subclasses
    if class_or_subclass in CLASS_TO_SUBCLASSES[Class.PALADIN]:
        if "Oath Spell".lower() in raw_via.lower():
            # skipping via, redundant with the subclass
            return None

    # Cleric subclasses
    if class_or_subclass in CLASS_TO_SUBCLASSES[Class.CLERIC]:
        if "Domain Spell".lower() in raw_via.lower() or "Domain".lower() in raw_via.lower():
            # skipping via, redundant with the subclass
            return None

    # Druid : Circle of the Land
    if class_or_subclass == SubClass.CIRCLE_OF_THE_LAND:
        land_circles: List[LandCircle] = []
        for land_circle in LandCircle:
            if land_circle.value.lower() in raw_via.lower():
                land_circles.append(land_circle)

        return Via(land_circles=land_circles)

    # Druid : Circle of the Spores
    if class_or_subclass == SubClass.CIRCLE_OF_THE_SPORES:
        if "Circle Spell".lower() in raw_via.lower():
            # skipping via, redundant with the subclass
            return None

    # Ranger : Natural Explorer
    if class_or_subclass == Class.RANGER:
        for natural_explorer in NaturalExplorer:
            if natural_explorer.value.lower() in raw_via.lower():
                return Via(natural_explorer=natural_explorer)

    # Ranger : Favoured Enemy
    if class_or_subclass == Class.RANGER:
        for favoured_enemy in FavouredEnemy:
            if favoured_enemy.value.lower() in raw_via.lower():
                return Via(favoured_enemy=favoured_enemy)

    # Wizard : School of Conjuration
    if class_or_subclass == SubClass.CONJURATION:
        if "Conjuration".lower() in raw_via.lower():
            # skipping via, redundant with the subclass
            return None

    # Druid
    if class_or_subclass == Class.DRUID:
        if "Wild Shape: Deep Rothé".lower() in raw_via.lower():
            return Via(wild_shape=WildShape.DEEP_ROTHE)

    raise ValueError(f'couldn\'t parse via: "{raw_via}"')


def parse_class_level(raw_class_level: str) -> Tuple[List[ClassLevel], List[SubclassLevel]]:
    match_regex = re.match(r"^Class Level (1[0-2]|[1-9]): (.*?), and (.*?)$", raw_class_level)

    if match_regex is not None:
        level = int(match_regex.group(1))

        names = [
            extract_additional_information(raw_name)
            for raw_name in match_regex.group(2).split(", ")
        ] + [extract_additional_information(match_regex.group(3))]

        classes: List[ClassLevel] = []
        subclasses: List[SubclassLevel] = []

        for name, raw_via in names:
            try:
                class_name = Class(name)
            except ValueError:
                try:
                    subclass_name = SubClass(name)
                except ValueError:
                    pass
                else:
                    via = parse_via(subclass_name, raw_via)

                    subclasses.append(
                        SubclassLevel(
                            name=subclass_name,
                            level=level,
                            via=via,
                        )
                    )
            else:
                via = parse_via(class_name, raw_via)

                classes.append(ClassLevel(name=class_name, level=level, via=via))

        return classes, subclasses

    match_regex = re.match(r"^Class Level (1[0-2]|[1-9]): (.*?)$", raw_class_level)

    if match_regex is not None:
        level = int(match_regex.group(1))

        name, raw_via = extract_additional_information(match_regex.group(2))

        try:
            class_name = Class(name)
        except ValueError:
            try:
                subclass_name = SubClass(name)
            except ValueError:
                pass
            else:
                via = parse_via(subclass_name, raw_via)

                return [], [SubclassLevel(name=subclass_name, level=level, via=via)]
        else:
            via = parse_via(class_name, raw_via)

            return [ClassLevel(name=class_name, level=level, via=via)], []

    raise ValueError(f"Couldn't parse: {raw_class_level}")


def parse_race_level(raw_race_level: str) -> Tuple[List[RaceLevel], List[SubRaceLevel]]:
    match_regex = re.match(r"^Character level (1[0-2]|[1-9]): (.*?), and (.*?)$", raw_race_level)

    if match_regex is not None:
        level = int(match_regex.group(1))

        names = [raw_name for raw_name in match_regex.group(2).split(", ")] + [match_regex.group(3)]

        races: List[RaceLevel] = []
        subraces: List[SubRaceLevel] = []

        for name in names:
            try:
                race_name = Race(name)
            except ValueError:
                try:
                    subrace_name = SubRace(name)
                except ValueError:
                    pass
                else:
                    subraces.append(SubRaceLevel(name=subrace_name, level=level))
            else:
                races.append(RaceLevel(name=race_name, level=level))

        return races, subraces

    match_regex = re.match(r"^Character level (1[0-2]|[1-9]): (.*?)$", raw_race_level)

    if match_regex is not None:
        level = int(match_regex.group(1))

        name = match_regex.group(2)

        try:
            race_name = Race(name)
        except ValueError:
            try:
                subrace_name = SubRace(name)
            except ValueError:
                pass
            else:
                return [], [SubRaceLevel(name=subrace_name, level=level)]
        else:
            return [RaceLevel(name=race_name, level=level)], []

    raise ValueError(f"Couldn't parse: {raw_race_level}")


def match_class_level(content: str) -> bool:
    match_regex = re.match(r"^Class Level (1[0-2]|[1-9]):", str(content))

    return match_regex is not None


def match_race_level(content: str) -> bool:
    match_regex = re.match(r"^Character level (1[0-2]|[1-9]):", str(content))

    return match_regex is not None


def extract_class_requirements(soup: BeautifulSoup) -> Tuple[List[ClassLevel], List[SubclassLevel]]:
    classes: List[ClassLevel] = []
    subclasses: List[SubclassLevel] = []

    for p in soup.find("span", id="How_to_learn").find_next("div").find_all("p"):
        if p.text.startswith("Classes"):
            for sibling in p.find_next_siblings():
                if sibling.name == "ul" and match_class_level(sibling.li.contents[0]):
                    new_classes, new_subclasses = parse_class_level(sibling.li.text)

                    classes.extend(new_classes)
                    subclasses.extend(new_subclasses)

    return classes, subclasses


def extract_races_requirements(soup: BeautifulSoup) -> Tuple[List[RaceLevel], List[SubRaceLevel]]:
    races: List[RaceLevel] = []
    subraces: List[SubRaceLevel] = []

    for p in soup.find("span", id="How_to_learn").find_next("div").find_all("p"):
        if p.text.startswith("Races"):
            for sibling in p.find_next_siblings():
                if sibling.name == "ul" and match_race_level(sibling.li.contents[0]):
                    new_classes, new_subclasses = parse_race_level(sibling.li.text)

                    races.extend(new_classes)
                    subraces.extend(new_subclasses)

    return races, subraces


def determine_magic_school(description: str) -> SchoolOfMagic:
    for school in SchoolOfMagic:
        if school.value.lower() in description.lower():
            return school

    raise ValueError(f"Couldn't determine magic school: {description}")


def determine_saving_throw(details: List[str]) -> Optional[Characteristic]:
    for detail in details:
        match_regex = re.match(f"({'|'.join(TRIGRAM_TO_CHARACTERISTIC)}) Save", detail)

        if match_regex:
            return trigram_to_characteristic(match_regex.group(1))

    return None


async def add_spell_details_from_page(
    client: httpx.AsyncClient, url: str, name: str, level: int
) -> Spell:
    url = url.removesuffix("_(Melee)")
    url = url.removesuffix("_(Ranged)")

    response = await client.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    properties = soup.find("div", class_="bg3wiki-property-list")

    costs = [parse_cost(raw_cost) for raw_cost in find_cost(properties)]

    cost_on_hit_property = find_cost_on_hit(properties)

    if cost_on_hit_property is not None:
        cost_on_hit = [parse_cost(raw_cost) for raw_cost in cost_on_hit_property]
    else:
        cost_on_hit = None

    classes, subclasses = extract_class_requirements(soup)

    if (
        not classes
        and not subclasses
        and name not in ("Curriculum of Strategy: Artistry of War", "Dethrone")
    ):
        warnings.warn(f"Missing classes or subclasses: {name}")

    races, subraces = extract_races_requirements(soup)

    if name == "Hellish Rebuke":
        details = []
    else:
        details = find_details(soup)

    saving_throw = determine_saving_throw(details)

    ritual = "Ritual" in details
    concentration = "Concentration" in details

    short_description = (
        soup.find("div", class_="bg3wiki-tooltip-box bg3wiki-tooltip-gradient-common")
        .find_next("p")
        .text.rstrip("\n")
        .rstrip()
    )

    school = determine_magic_school(short_description)

    return Spell(
        name=name,
        short_description=short_description,
        long_description="",
        school=school,
        level=level,
        properties=SpellProperties(
            cost=costs,
            cost_on_hit=cost_on_hit,
            concentration=concentration,
            ritual=ritual,
            saving_throw=saving_throw,
        ),
        can_upcast=find_upcast(soup),
        how_to_learn=HowToLearn(
            classes=classes, subclasses=subclasses, races=races, subraces=subraces
        ),
    )


async def main() -> int:
    # Step 1: Fetch the webpage content
    list_of_spells_uri = "/wiki/List_of_all_spells"

    with httpx.Client() as client:
        response = client.get(BASE_URL + list_of_spells_uri)

    # Step 2: Parse the content with BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Step 3: Concatenate all spells header from cantrip to level 6 slot
    spell_headers = chain((level, find_level_spells_header(soup, level)) for level in range(7))

    # Step 4: Get the next div following the target h4
    requests: List[Tuple[str, int, str]] = prepare_spell_requests(spell_headers)

    async with httpx.AsyncClient() as client:  # use httpx
        spells = Spells(
            await asyncio.gather(
                *[
                    add_spell_details_from_page(client, url, name, level)
                    for name, level, url in requests
                ]
            )
        )

    # Step 5: Write the spells to a file
    print(f"Number of spells found: {len(spells)}")

    (Path(__file__).parent / "spells.json").write_text(
        spells.model_dump_json(indent=4, exclude_none=True) + "\n",
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
