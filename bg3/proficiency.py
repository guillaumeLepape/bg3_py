from typing import List, Optional

from pydantic import BaseModel

from .armour import ArmourType
from .characteristic import Characteristic
from .weapon import WeaponType


class Proficiencies(BaseModel):
    armours: Optional[List[ArmourType]] = None
    weapons: Optional[List[WeaponType]] = None
    saving_throws: Optional[List[Characteristic]] = None
