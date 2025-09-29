from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="BankSchema")



@_attrs_define
class BankSchema:
    """ 
        Attributes:
            slots (int): Maximum slots in your bank.
            expansions (int): Bank expansions.
            next_expansion_cost (int): Next expansion cost.
            gold (int): Quantity of gold in your bank.
     """

    slots: int
    expansions: int
    next_expansion_cost: int
    gold: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        slots = self.slots

        expansions = self.expansions

        next_expansion_cost = self.next_expansion_cost

        gold = self.gold


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "slots": slots,
            "expansions": expansions,
            "next_expansion_cost": next_expansion_cost,
            "gold": gold,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        slots = d.pop("slots")

        expansions = d.pop("expansions")

        next_expansion_cost = d.pop("next_expansion_cost")

        gold = d.pop("gold")

        bank_schema = cls(
            slots=slots,
            expansions=expansions,
            next_expansion_cost=next_expansion_cost,
            gold=gold,
        )


        bank_schema.additional_properties = d
        return bank_schema

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
