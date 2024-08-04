from typing import List, Optional

from pydantic import BaseModel

from .ability import Ability
from .armour import ArmourProficiency
from .weapon import WeaponProficiency


class Proficiencies(BaseModel):
    armours: Optional[List[ArmourProficiency]] = None
    weapons: Optional[List[WeaponProficiency]] = None
    saving_throws: Optional[List[Ability]] = None
