from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union






T = TypeVar("T", bound="NPCItem")



@_attrs_define
class NPCItem:
    """ 
        Attributes:
            code (str): The code of the NPC. This is the NPC's unique identifier (ID).
            npc (str): Code of the NPC that sells/buys the item.
            currency (str): Currency used to buy/sell the item. If it's not gold, it's the item code.
            buy_price (Union[None, int]): Price to buy the item.
            sell_price (Union[None, int]): Price to sell the item.
     """

    code: str
    npc: str
    currency: str
    buy_price: Union[None, int]
    sell_price: Union[None, int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        code = self.code

        npc = self.npc

        currency = self.currency

        buy_price: Union[None, int]
        buy_price = self.buy_price

        sell_price: Union[None, int]
        sell_price = self.sell_price


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "code": code,
            "npc": npc,
            "currency": currency,
            "buy_price": buy_price,
            "sell_price": sell_price,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        npc = d.pop("npc")

        currency = d.pop("currency")

        def _parse_buy_price(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        buy_price = _parse_buy_price(d.pop("buy_price"))


        def _parse_sell_price(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        sell_price = _parse_sell_price(d.pop("sell_price"))


        npc_item = cls(
            code=code,
            npc=npc,
            currency=currency,
            buy_price=buy_price,
            sell_price=sell_price,
        )


        npc_item.additional_properties = d
        return npc_item

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
