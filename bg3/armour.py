from uuid import UUID, uuid5

from pydantic import BaseModel, SerializerFunctionWrapHandler, computed_field, model_serializer

ARMOUR_TYPE_UUID_NAMESPACE = UUID("79f6ff8f-b514-4d41-af4c-60a788077ab0")


class ArmourType(BaseModel):
    name: str

    @computed_field  # type: ignore[prop-decorator]
    @property
    def id(self) -> UUID:
        return uuid5(ARMOUR_TYPE_UUID_NAMESPACE, self.name)

    # Custom serializer to ensure 'id' comes first
    @model_serializer(mode="wrap")
    def custom_serialize(self, nxt: SerializerFunctionWrapHandler) -> dict:
        return {"id": self.id, **nxt(self)}


LIGHT_ARMOUR = ArmourType(name="Light Armour")
MEDIUM_ARMOUR = ArmourType(name="Medium Armour")
HEAVY_ARMOUR = ArmourType(name="Heavy Armour")
SHIELD = ArmourType(name="Shield")
