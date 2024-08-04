from uuid import UUID

from pydantic import BaseModel


class ArmourProficiency(BaseModel):
    id: UUID
    name: str

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ArmourProficiency):
            raise NotImplementedError

        return self.id == other.id


light_armour_proficiency = ArmourProficiency(
    id="58d8d229-a98a-43b9-aab6-39116849465c", name="Light Armour Proficiency"
)
medium_armour_proficiency = ArmourProficiency(
    id="067f812b-102f-4c69-8083-281c435dee78", name="Medium Armour Proficiency"
)
heavy_armour_proficiency = ArmourProficiency(
    id="b1ffe177-ec53-4eb6-82fc-09fe9d93cc41", name="Heavy Armour Proficiency"
)
shield_proficiency = ArmourProficiency(
    id="ef889bfd-18db-443b-8dd8-34ebc46875d3", name="Shield Proficiency"
)
