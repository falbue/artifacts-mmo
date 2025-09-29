from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="InventorySlot")



@_attrs_define
class InventorySlot:
    """ 
        Attributes:
            slot (int): Inventory slot identifier.
            code (str): Item code.
            quantity (int): Quantity in the slot.
     """

    slot: int
    code: str
    quantity: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        slot = self.slot

        code = self.code

        quantity = self.quantity


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "slot": slot,
            "code": code,
            "quantity": quantity,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        slot = d.pop("slot")

        code = d.pop("code")

        quantity = d.pop("quantity")

        inventory_slot = cls(
            slot=slot,
            code=code,
            quantity=quantity,
        )


        inventory_slot.additional_properties = d
        return inventory_slot

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
