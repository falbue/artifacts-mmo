from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.drop_schema import DropSchema





T = TypeVar("T", bound="SkillInfoSchema")



@_attrs_define
class SkillInfoSchema:
    """ 
        Attributes:
            xp (int): The amount of xp gained.
            items (list['DropSchema']): Objects received.
     """

    xp: int
    items: list['DropSchema']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.drop_schema import DropSchema
        xp = self.xp

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "xp": xp,
            "items": items,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.drop_schema import DropSchema
        d = dict(src_dict)
        xp = d.pop("xp")

        items = []
        _items = d.pop("items")
        for items_item_data in (_items):
            items_item = DropSchema.from_dict(items_item_data)



            items.append(items_item)


        skill_info_schema = cls(
            xp=xp,
            items=items,
        )


        skill_info_schema.additional_properties = d
        return skill_info_schema

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
