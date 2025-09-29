from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.item_slot import ItemSlot
from typing import cast

if TYPE_CHECKING:
  from ..models.character_schema import CharacterSchema
  from ..models.cooldown_schema import CooldownSchema
  from ..models.item_schema import ItemSchema





T = TypeVar("T", bound="EquipRequestSchema")



@_attrs_define
class EquipRequestSchema:
    """ 
        Attributes:
            cooldown (CooldownSchema):
            slot (ItemSlot):
            item (ItemSchema):
            character (CharacterSchema):
     """

    cooldown: 'CooldownSchema'
    slot: ItemSlot
    item: 'ItemSchema'
    character: 'CharacterSchema'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.character_schema import CharacterSchema
        from ..models.cooldown_schema import CooldownSchema
        from ..models.item_schema import ItemSchema
        cooldown = self.cooldown.to_dict()

        slot = self.slot.value

        item = self.item.to_dict()

        character = self.character.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "cooldown": cooldown,
            "slot": slot,
            "item": item,
            "character": character,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.character_schema import CharacterSchema
        from ..models.cooldown_schema import CooldownSchema
        from ..models.item_schema import ItemSchema
        d = dict(src_dict)
        cooldown = CooldownSchema.from_dict(d.pop("cooldown"))




        slot = ItemSlot(d.pop("slot"))




        item = ItemSchema.from_dict(d.pop("item"))




        character = CharacterSchema.from_dict(d.pop("character"))




        equip_request_schema = cls(
            cooldown=cooldown,
            slot=slot,
            item=item,
            character=character,
        )


        equip_request_schema.additional_properties = d
        return equip_request_schema

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
