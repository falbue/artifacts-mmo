from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="GEOrderCreatedSchema")



@_attrs_define
class GEOrderCreatedSchema:
    """ 
        Attributes:
            id (str): Order id.
            created_at (datetime.datetime): Order created at.
            code (str): Item code.
            quantity (int): Item quantity.
            price (int): Item price per unit.
            total_price (int): Total price.
            tax (int): Listing tax (3%, minimum 1)
     """

    id: str
    created_at: datetime.datetime
    code: str
    quantity: int
    price: int
    total_price: int
    tax: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        created_at = self.created_at.isoformat()

        code = self.code

        quantity = self.quantity

        price = self.price

        total_price = self.total_price

        tax = self.tax


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "created_at": created_at,
            "code": code,
            "quantity": quantity,
            "price": price,
            "total_price": total_price,
            "tax": tax,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        created_at = isoparse(d.pop("created_at"))




        code = d.pop("code")

        quantity = d.pop("quantity")

        price = d.pop("price")

        total_price = d.pop("total_price")

        tax = d.pop("tax")

        ge_order_created_schema = cls(
            id=id,
            created_at=created_at,
            code=code,
            quantity=quantity,
            price=price,
            total_price=total_price,
            tax=tax,
        )


        ge_order_created_schema.additional_properties = d
        return ge_order_created_schema

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
