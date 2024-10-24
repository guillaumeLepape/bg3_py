from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class Cost(BaseModel):
    id: UUID
    name: str
    level: Optional[int] = None


ACTION = Cost(id="bcf456ed-0788-4e9c-9b70-29b7214cde0e", name="Action")
BONUS_ACTION = Cost(id="e4e85d3a-f253-4c72-8b92-61a351033cc3", name="Bonus Action")
REACTION = Cost(id="20407051-3230-4a26-80ed-934ef57cf7a2", name="Reaction")


def spell_slot(level: int) -> Cost:
    return Cost(id="c7e1c0e6-4b2a-4f7f-9f6f-4f0c1d3f8e8b", name="Spell Slot", level=level)


channel_divinity_charge = Cost(
    id="c728c238-7371-4f8a-a798-1420a15a6618", name="Channel Divinity Charge"
)
