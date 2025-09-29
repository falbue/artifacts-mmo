from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="GeOrderHistorySchema")



@_attrs_define
class GeOrderHistorySchema:
    """ 
        Attributes:
            order_id (str): Order id.
            seller (str): Seller account name.
            buyer (str): Buyer account name.
            code (str): Item code.
            quantity (int): Item quantity.
            price (int): Item price per unit.
            sold_at (datetime.datetime): Sale datetime.
     """

    order_id: str
    seller: str
    buyer: str
    code: str
    quantity: int
    price: int
    sold_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        order_id = self.order_id

        seller = self.seller

        buyer = self.buyer

        code = self.code

        quantity = self.quantity

        price = self.price

        sold_at = self.sold_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "order_id": order_id,
            "seller": seller,
            "buyer": buyer,
            "code": code,
            "quantity": quantity,
            "price": price,
            "sold_at": sold_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        order_id = d.pop("order_id")

        seller = d.pop("seller")

        buyer = d.pop("buyer")

        code = d.pop("code")

        quantity = d.pop("quantity")

        price = d.pop("price")

        sold_at = isoparse(d.pop("sold_at"))




        ge_order_history_schema = cls(
            order_id=order_id,
            seller=seller,
            buyer=buyer,
            code=code,
            quantity=quantity,
            price=price,
            sold_at=sold_at,
        )


        ge_order_history_schema.additional_properties = d
        return ge_order_history_schema

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
