from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GiveGoldSchema")



@_attrs_define
class GiveGoldSchema:
    """ 
        Attributes:
            quantity (int): Gold quantity.
            character (str): Character name. The name of the character who will receive the gold.
     """

    quantity: int
    character: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        quantity = self.quantity

        character = self.character


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "quantity": quantity,
            "character": character,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        quantity = d.pop("quantity")

        character = d.pop("character")

        give_gold_schema = cls(
            quantity=quantity,
            character=character,
        )


        give_gold_schema.additional_properties = d
        return give_gold_schema

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
