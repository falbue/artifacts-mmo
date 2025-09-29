from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="DropRateSchema")



@_attrs_define
class DropRateSchema:
    """ 
        Attributes:
            code (str): Item code.
            rate (int): Chance rate. (1/rate)
            min_quantity (int): Minimum quantity.
            max_quantity (int): Maximum quantity.
     """

    code: str
    rate: int
    min_quantity: int
    max_quantity: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        code = self.code

        rate = self.rate

        min_quantity = self.min_quantity

        max_quantity = self.max_quantity


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "code": code,
            "rate": rate,
            "min_quantity": min_quantity,
            "max_quantity": max_quantity,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        rate = d.pop("rate")

        min_quantity = d.pop("min_quantity")

        max_quantity = d.pop("max_quantity")

        drop_rate_schema = cls(
            code=code,
            rate=rate,
            min_quantity=min_quantity,
            max_quantity=max_quantity,
        )


        drop_rate_schema.additional_properties = d
        return drop_rate_schema

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
