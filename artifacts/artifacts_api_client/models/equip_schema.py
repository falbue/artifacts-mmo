from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.item_slot import ItemSlot
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="EquipSchema")



@_attrs_define
class EquipSchema:
    """ 
        Attributes:
            code (str): Item code.
            slot (ItemSlot):
            quantity (Union[Unset, int]): Item quantity. Applicable to utilities only. Default: 1.
     """

    code: str
    slot: ItemSlot
    quantity: Union[Unset, int] = 1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        code = self.code

        slot = self.slot.value

        quantity = self.quantity


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "code": code,
            "slot": slot,
        })
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        slot = ItemSlot(d.pop("slot"))




        quantity = d.pop("quantity", UNSET)

        equip_schema = cls(
            code=code,
            slot=slot,
            quantity=quantity,
        )


        equip_schema.additional_properties = d
        return equip_schema

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
