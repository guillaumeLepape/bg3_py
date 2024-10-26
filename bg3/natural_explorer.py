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

NATURAL_EXPLORER_UUID_NAMESPACE = UUID("d05f8f8e-ecf9-45f3-94f6-0b2e44152e3e")


class NaturalExplorer(BaseModel):
    name: str
    description: str
    grants: str

    how_to_learn: HowToLearn

    @computed_field  # type: ignore[prop-decorator]
    @property
    def id(self) -> UUID:
        return uuid5(NATURAL_EXPLORER_UUID_NAMESPACE, self.name)

    # Custom serializer to ensure 'id' comes first
    @model_serializer(mode="wrap")
    def custom_serialize(self, nxt: SerializerFunctionWrapHandler) -> dict:
        return {"id": self.id, **nxt(self)}


HOW_TO_LEARN_NATURAL_EXPLORER = HowToLearn(
    classes=[
        ClassLevel(name=Class.RANGER, level=1),
        ClassLevel(name=Class.RANGER, level=6),
        ClassLevel(name=Class.RANGER, level=10),
    ],
    subclasses=[],
    races=[],
    subraces=[],
)


BEAST_TAMER = NaturalExplorer(
    name="Beast Tamer",
    description="Find Familiar as a ritual.",
    grants="Cast Find Familiar once per short rest",
    how_to_learn=HOW_TO_LEARN_NATURAL_EXPLORER,
)


URBAN_TRACKER = NaturalExplorer(
    name="Urban Tracker",
    description=(
        "An expert at navigating the wild within the city, you gain Sleight of Hand Proficiency."
    ),
    grants="Sleight of Hand Proficiency",
    how_to_learn=HOW_TO_LEARN_NATURAL_EXPLORER,
)

WASTELAND_WANDERER_COLD = NaturalExplorer(
    name="Wasteland Wanderer: Cold",
    description=(
        "You have spent endless days surviving desolate tundras. Gain resistance to Cold damage, "
        "taking only half damage from it."
    ),
    grants="Cold Resistance",
    how_to_learn=HOW_TO_LEARN_NATURAL_EXPLORER,
)

WASTELAND_WANDERER_FIRE = NaturalExplorer(
    name="Wasteland Wanderer: Fire",
    description=(
        "You have spent endless days surviving forbidding deserts. Gain resistance to Fire damage, "
        "taking only half damage from it."
    ),
    grants="Fire Resistance",
    how_to_learn=HOW_TO_LEARN_NATURAL_EXPLORER,
)

WASTELAND_WANDERER_POISON = NaturalExplorer(
    name="Wasteland Wanderer: Poison",
    description=(
        "You have spent endless days surviving fetid swamps. Gain resistance to Poison damage, "
        "taking only half damage from it."
    ),
    grants="Poison Resistance",
    how_to_learn=HOW_TO_LEARN_NATURAL_EXPLORER,
)


class NaturalExplorers(RootModel):
    root: List[NaturalExplorer]


natural_explorers = NaturalExplorers(
    root=[
        BEAST_TAMER,
        URBAN_TRACKER,
        WASTELAND_WANDERER_COLD,
        WASTELAND_WANDERER_FIRE,
        WASTELAND_WANDERER_POISON,
    ]
)

if __name__ == "__main__":
    (Path(__file__).parent / "cli" / "natural_explorers.json").write_text(
        natural_explorers.model_dump_json(indent=4, exclude_none=True) + "\n"
    )
