from typing import Optional

from pydantic import BaseModel


class ClassResources(BaseModel):
    rage_points: Optional[int] = None
    bardic_inspirations: Optional[int] = None
    channel_divinity_charges: Optional[int] = None
    superiority_dices: Optional[int] = None

    def __add__(self, other: object) -> "ClassResources":
        if not isinstance(other, ClassResources):
            raise NotImplementedError

        return ClassResources(
            rage_points=(
                (self.rage_points or 0) + (other.rage_points or 0)
                if self.rage_points is not None or other.rage_points is not None
                else None
            ),
            bardic_inspirations=(
                (self.channel_divinity_charges or 0) + (other.channel_divinity_charges or 0)
                if self.bardic_inspirations is not None or other.bardic_inspirations is not None
                else None
            ),
            channel_divinity_charges=(
                (self.channel_divinity_charges or 0) + (other.channel_divinity_charges or 0)
                if (
                    self.channel_divinity_charges is not None
                    or other.channel_divinity_charges is not None
                )
                else None
            ),
            superiority_dices=(
                (self.superiority_dices or 0) + (other.superiority_dices or 0)
                if self.superiority_dices is not None or other.superiority_dices is not None
                else None
            ),
        )
