from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.craft_skill import CraftSkill
from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.simple_item_schema import SimpleItemSchema





T = TypeVar("T", bound="CraftSchema")



@_attrs_define
class CraftSchema:
    """ 
        Attributes:
            skill (Union[Unset, CraftSkill]):
            level (Union[Unset, int]): The skill level required to craft the item.
            items (Union[Unset, list['SimpleItemSchema']]): List of items required to craft the item.
            quantity (Union[Unset, int]): Quantity of items crafted.
     """

    skill: Union[Unset, CraftSkill] = UNSET
    level: Union[Unset, int] = UNSET
    items: Union[Unset, list['SimpleItemSchema']] = UNSET
    quantity: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.simple_item_schema import SimpleItemSchema
        skill: Union[Unset, str] = UNSET
        if not isinstance(self.skill, Unset):
            skill = self.skill.value


        level = self.level

        items: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)



        quantity = self.quantity


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if skill is not UNSET:
            field_dict["skill"] = skill
        if level is not UNSET:
            field_dict["level"] = level
        if items is not UNSET:
            field_dict["items"] = items
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.simple_item_schema import SimpleItemSchema
        d = dict(src_dict)
        _skill = d.pop("skill", UNSET)
        skill: Union[Unset, CraftSkill]
        if isinstance(_skill,  Unset):
            skill = UNSET
        else:
            skill = CraftSkill(_skill)




        level = d.pop("level", UNSET)

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in (_items or []):
            items_item = SimpleItemSchema.from_dict(items_item_data)



            items.append(items_item)


        quantity = d.pop("quantity", UNSET)

        craft_schema = cls(
            skill=skill,
            level=level,
            items=items,
            quantity=quantity,
        )


        craft_schema.additional_properties = d
        return craft_schema

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
