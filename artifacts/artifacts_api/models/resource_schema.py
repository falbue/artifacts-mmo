from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.gathering_skill import GatheringSkill
from typing import cast

if TYPE_CHECKING:
  from ..models.drop_rate_schema import DropRateSchema





T = TypeVar("T", bound="ResourceSchema")



@_attrs_define
class ResourceSchema:
    """ 
        Attributes:
            name (str): The name of the resource
            code (str): The code of the resource. This is the resource's unique identifier (ID).
            skill (GatheringSkill):
            level (int): The skill level required to gather this resource.
            drops (list['DropRateSchema']): The drops of this resource.
     """

    name: str
    code: str
    skill: GatheringSkill
    level: int
    drops: list['DropRateSchema']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.drop_rate_schema import DropRateSchema
        name = self.name

        code = self.code

        skill = self.skill.value

        level = self.level

        drops = []
        for drops_item_data in self.drops:
            drops_item = drops_item_data.to_dict()
            drops.append(drops_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "code": code,
            "skill": skill,
            "level": level,
            "drops": drops,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.drop_rate_schema import DropRateSchema
        d = dict(src_dict)
        name = d.pop("name")

        code = d.pop("code")

        skill = GatheringSkill(d.pop("skill"))




        level = d.pop("level")

        drops = []
        _drops = d.pop("drops")
        for drops_item_data in (_drops):
            drops_item = DropRateSchema.from_dict(drops_item_data)



            drops.append(drops_item)


        resource_schema = cls(
            name=name,
            code=code,
            skill=skill,
            level=level,
            drops=drops,
        )


        resource_schema.additional_properties = d
        return resource_schema

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
