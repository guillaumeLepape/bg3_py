import logging
from pathlib import Path
from uuid import UUID

from pydantic import BaseModel, computed_field

logger = logging.getLogger(__file__)


class Cantrip(BaseModel):
    id: UUID
    name: str

    @computed_field
    def icon(self) -> str:
        return f"/static/cantrips/{self.name.replace(' ', '_')}.jpg"

    def check_icon(self) -> bool:
        path = self.icon().removeprefix("/")

        return (Path(__file__).parents[1] / path).is_file()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Cantrip):
            raise NotImplementedError

        return self.id == other.id


acid_splash = Cantrip(id="58d8d229-a98a-43b9-aab6-39116849465c", name="Acid Splash")
blade_ward = Cantrip(id="067f812b-102f-4c69-8083-281c435dee78", name="Blade Ward")
bone_chill = Cantrip(id="1142f378-a3f5-4bef-96e5-1455efbd684f", name="Bone Chill")
dancing_lights = Cantrip(id="1f5c5d38-b177-4242-b849-e0c55e66be0c", name="Dancing Lights")
eldritch_blast = Cantrip(id="363a039f-4a7b-4574-bb2f-6151253fadb1", name="Eldritch Blast")
fire_bolt = Cantrip(id="4b3c2e3d-7835-4ba3-a515-66b120c84466", name="Fire Bolt")
friends = Cantrip(id="b1ffe177-ec53-4eb6-82fc-09fe9d93cc41", name="Friends")
guidance = Cantrip(id="b87e3e20-03f7-425e-8616-21f8f54280d7", name="Guidance")
light = Cantrip(id="076905b5-d261-4d0b-a783-e28534e76516", name="Light")
mage_hand = Cantrip(id="cb494eac-b2b2-4c6b-b6ad-cb3ac7fb21e9", name="Mage Hand")
minor_illusion = Cantrip(id="68c5bc19-cec5-48e0-8889-9506746b663d", name="Minor Illusion")
poison_spray = Cantrip(id="b6970f6e-acd0-4d08-b623-85e76e0ac5f3", name="Poison Spray")
produce_flame = Cantrip(id="d0c07345-5789-4485-becc-1b358dfcd614", name="Produce Flame")
ray_of_frost = Cantrip(id="1a6c6ea5-1069-411d-b541-aace66c395e9", name="Ray of Frost")
resistance = Cantrip(id="2fc41a09-6669-4fca-99f8-f7feedd7533c", name="Resistance")
sacred_flame = Cantrip(id="189aa4e7-f8b3-4540-88c7-951a6d3d23f5", name="Sacred Flame")
shillelagh = Cantrip(id="d6b8d9e0-9468-4e72-b6d4-fe54361ad63b", name="Shillelagh")
shocking_grasp = Cantrip(id="a9b58e38-3375-407e-bbec-253eed369fb4", name="Shocking Grasp")
thaumaturgy = Cantrip(id="94183b11-9dff-4c35-8dfd-5397eb642b74", name="Thaumaturgy")
thorn_whip = Cantrip(id="32571be8-3cf1-4eb9-ac6c-cde6728e52ee", name="Thorn Whip")
true_strike = Cantrip(id="be30dd9c-ab58-4842-8880-c618a3cae38f", name="True Strike")
vicious_mockery = Cantrip(id="6f35735d-9e2f-4c78-b9d4-944de96dd56b", name="Vicious Mockery")

wizard_cantrips = [
    acid_splash,
    blade_ward,
    bone_chill,
    dancing_lights,
    fire_bolt,
    friends,
    light,
    mage_hand,
    minor_illusion,
    poison_spray,
    ray_of_frost,
    shocking_grasp,
    true_strike,
]

bard_cantrips = [
    blade_ward,
    mage_hand,
    true_strike,
    friends,
    dancing_lights,
    light,
    minor_illusion,
    vicious_mockery,
]

warlock_cantrips = [
    blade_ward,
    bone_chill,
    eldritch_blast,
    friends,
    mage_hand,
    minor_illusion,
    poison_spray,
    true_strike,
]

cleric_cantrips = [
    blade_ward,
    guidance,
    light,
    produce_flame,
    resistance,
    sacred_flame,
    thaumaturgy,
]

for var in dict(locals()).values():
    if isinstance(var, Cantrip) and var.check_icon() is False:
        logger.warning(f"Icon not found for cantrip: {var.name}")
