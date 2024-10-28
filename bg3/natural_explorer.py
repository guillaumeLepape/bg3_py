from pathlib import Path
from typing import Iterator, List
from uuid import UUID, uuid5

from pydantic import (
    BaseModel,
    RootModel,
    SerializerFunctionWrapHandler,
    computed_field,
    model_serializer,
)

NATURAL_EXPLORER_UUID_NAMESPACE = UUID("d05f8f8e-ecf9-45f3-94f6-0b2e44152e3e")


class NaturalExplorer(BaseModel):
    name: str
    description: str
    grants: str

    @computed_field  # type: ignore[prop-decorator]
    @property
    def id(self) -> UUID:
        return uuid5(NATURAL_EXPLORER_UUID_NAMESPACE, self.name)

    # Custom serializer to ensure 'id' comes first
    @model_serializer(mode="wrap")
    def custom_serialize(self, nxt: SerializerFunctionWrapHandler) -> dict:
        return {"id": self.id, **nxt(self)}


BEAST_TAMER = NaturalExplorer(
    name="Beast Tamer",
    description="Find Familiar as a ritual.",
    grants="Cast Find Familiar once per short rest",
)


URBAN_TRACKER = NaturalExplorer(
    name="Urban Tracker",
    description=(
        "An expert at navigating the wild within the city, you gain Sleight of Hand Proficiency."
    ),
    grants="Sleight of Hand Proficiency",
)

WASTELAND_WANDERER_COLD = NaturalExplorer(
    name="Wasteland Wanderer: Cold",
    description=(
        "You have spent endless days surviving desolate tundras. Gain resistance to Cold damage, "
        "taking only half damage from it."
    ),
    grants="Cold Resistance",
)

WASTELAND_WANDERER_FIRE = NaturalExplorer(
    name="Wasteland Wanderer: Fire",
    description=(
        "You have spent endless days surviving forbidding deserts. Gain resistance to Fire damage, "
        "taking only half damage from it."
    ),
    grants="Fire Resistance",
)

WASTELAND_WANDERER_POISON = NaturalExplorer(
    name="Wasteland Wanderer: Poison",
    description=(
        "You have spent endless days surviving fetid swamps. Gain resistance to Poison damage, "
        "taking only half damage from it."
    ),
    grants="Poison Resistance",
)


class NaturalExplorers(RootModel):
    root: List[NaturalExplorer]

    def __getitem__(self, index: int) -> NaturalExplorer:
        return self.root[index]

    def __iter__(self) -> Iterator[NaturalExplorer]:  # type: ignore[override]
        return iter(self.root)


NATURAL_EXPLORERS = NaturalExplorers(
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
        NATURAL_EXPLORERS.model_dump_json(indent=4, exclude_none=True) + "\n"
    )
