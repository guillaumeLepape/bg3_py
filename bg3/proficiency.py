from typing import List, Optional

from pydantic import BaseModel

from .armour import ArmourProficiency
from .characteristic import Characteristic
from .weapon import WeaponProficiency


class Proficiencies(BaseModel):
    armours: Optional[List[ArmourProficiency]] = None
    weapons: Optional[List[WeaponProficiency]] = None
    saving_throws: Optional[List[Characteristic]] = None
