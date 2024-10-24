import logging
from pathlib import Path
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, computed_field

from .cost import Cost, action, bonus_action, channel_divinity_charge

logger = logging.getLogger(__file__)


class ClassAction(BaseModel):
    id: UUID
    name: str

    cost: Optional[List[Cost]] = None

    @computed_field
    def icon(self) -> str:
        return f"/static/class_actions/{self.name.replace(' ', '_')}.webp"

    def check_icon(self) -> bool:
        path = self.icon.removeprefix("/")

        return (Path(__file__).parents[1] / path).is_file()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ClassAction):
            raise NotImplementedError

        return self.id == other.id


second_wind = ClassAction(
    id="98c415e1-71d1-47a8-9c54-62681d826b28", name="Second Wind", cost=[bonus_action]
)
action_surge = ClassAction(id="7d5ecad2-3987-4f6f-b6f0-fd5cec6f9b52", name="Action Surge")

# cleric subclasses actions
preserve_life = ClassAction(
    id="dde9e86f-2368-4ab7-814c-1ab08defe7e6",
    name="Preserve Life",
    cost=[action, channel_divinity_charge],
)

radiance_of_dawn = ClassAction(
    id="589a5492-1f5b-4c5c-95ef-7d11b10e2a9c",
    name="Radiance of Dawn",
    cost=[action, channel_divinity_charge],
)

invoke_duplicity = ClassAction(
    id="74f816ac-9c1f-42cf-93f0-7e5032a6d89d",
    name="Invoke Duplicity",
    cost=[action, channel_divinity_charge],
)

knowledge_of_the_ages = ClassAction(
    id="f7a6380e-c789-4e30-a029-18109811ddd7",
    name="Knowledge of the Ages",
    cost=[action, channel_divinity_charge],
)

charm_animals_and_plants = ClassAction(
    id="7f649b70-7a32-4536-bf9f-1cfcb747a4fe",
    name="Charm Animal and Plants",
    cost=[action, channel_divinity_charge],
)

destructive_wrath = ClassAction(
    id="272c7624-287f-45de-8284-170f6c479565",
    name="Destructive Wrath",
    cost=[action, channel_divinity_charge],
)

guided_strike = ClassAction(
    id="0d9635f7-8b76-47e3-855a-58c613283c17",
    name="Guided Strike",
    cost=[action, channel_divinity_charge],
)


for var in dict(locals()).values():
    if isinstance(var, ClassAction) and var.check_icon() is False:
        logger.warning(f"Icon not found for class action: {var.name}")
