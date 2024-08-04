from uuid import UUID

from pydantic import BaseModel


class Cost(BaseModel):
    id: UUID
    name: str


action = Cost(id="bcf456ed-0788-4e9c-9b70-29b7214cde0e", name="Action")
bonus_action = Cost(id="e4e85d3a-f253-4c72-8b92-61a351033cc3", name="Bonus Action")
channel_divinity_charge = Cost(
    id="c728c238-7371-4f8a-a798-1420a15a6618", name="Channel Divinity Charge"
)
