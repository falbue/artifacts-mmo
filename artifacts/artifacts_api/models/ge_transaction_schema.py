from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GETransactionSchema")



@_attrs_define
class GETransactionSchema:
    """ 
        Attributes:
            id (str): Order id.
            code (str): Item code.
            quantity (int): Item quantity.
            price (int): Item price.
            total_price (int): Total price of the transaction.
     """

    id: str
    code: str
    quantity: int
    price: int
    total_price: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        code = self.code

        quantity = self.quantity

        price = self.price

        total_price = self.total_price


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "code": code,
            "quantity": quantity,
            "price": price,
            "total_price": total_price,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        code = d.pop("code")

        quantity = d.pop("quantity")

        price = d.pop("price")

        total_price = d.pop("total_price")

        ge_transaction_schema = cls(
            id=id,
            code=code,
            quantity=quantity,
            price=price,
            total_price=total_price,
        )


        ge_transaction_schema.additional_properties = d
        return ge_transaction_schema

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
