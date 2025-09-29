from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.simple_item_schema import SimpleItemSchema





T = TypeVar("T", bound="RewardsSchema")



@_attrs_define
class RewardsSchema:
    """ 
        Attributes:
            items (list['SimpleItemSchema']): Items rewards.
            gold (int): Gold rewards.
     """

    items: list['SimpleItemSchema']
    gold: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.simple_item_schema import SimpleItemSchema
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)



        gold = self.gold


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "items": items,
            "gold": gold,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.simple_item_schema import SimpleItemSchema
        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in (_items):
            items_item = SimpleItemSchema.from_dict(items_item_data)



            items.append(items_item)


        gold = d.pop("gold")

        rewards_schema = cls(
            items=items,
            gold=gold,
        )


        rewards_schema.additional_properties = d
        return rewards_schema

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
