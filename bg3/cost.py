from typing import Optional
from uuid import UUID, uuid5

from pydantic import BaseModel, computed_field

COST_UUID_NAMESPACE = UUID("2c035d10-f9cc-4ac8-af3a-9ad4ac15073a")


class Cost(BaseModel):
    name: str
    level: Optional[int] = None

    @computed_field  # type: ignore[prop-decorator]
    @property
    def id(self) -> UUID:
        if self.level is not None:
            hash = f"{self.name}{self.level}"
        else:
            hash = self.name

        return uuid5(COST_UUID_NAMESPACE, hash)


ACTION = Cost(name="Action")
BONUS_ACTION = Cost(name="Bonus Action")
REACTION = Cost(name="Reaction")


def spell_slot(level: int) -> Cost:
    return Cost(name="Spell Slot", level=level)


channel_divinity_charge = Cost(
    id="c728c238-7371-4f8a-a798-1420a15a6618", name="Channel Divinity Charge"
)
