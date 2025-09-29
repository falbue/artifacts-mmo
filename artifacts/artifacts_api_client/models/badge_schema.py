from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.badge_condition_schema import BadgeConditionSchema





T = TypeVar("T", bound="BadgeSchema")



@_attrs_define
class BadgeSchema:
    """ 
        Attributes:
            code (str): Code of the badge. This is the badge's unique identifier (ID).
            description (str): Description of the badge.
            conditions (list['BadgeConditionSchema']): Conditions to get the badge.
            season (Union[None, Unset, int]): Season of the badge.
     """

    code: str
    description: str
    conditions: list['BadgeConditionSchema']
    season: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.badge_condition_schema import BadgeConditionSchema
        code = self.code

        description = self.description

        conditions = []
        for conditions_item_data in self.conditions:
            conditions_item = conditions_item_data.to_dict()
            conditions.append(conditions_item)



        season: Union[None, Unset, int]
        if isinstance(self.season, Unset):
            season = UNSET
        else:
            season = self.season


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "code": code,
            "description": description,
            "conditions": conditions,
        })
        if season is not UNSET:
            field_dict["season"] = season

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.badge_condition_schema import BadgeConditionSchema
        d = dict(src_dict)
        code = d.pop("code")

        description = d.pop("description")

        conditions = []
        _conditions = d.pop("conditions")
        for conditions_item_data in (_conditions):
            conditions_item = BadgeConditionSchema.from_dict(conditions_item_data)



            conditions.append(conditions_item)


        def _parse_season(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        season = _parse_season(d.pop("season", UNSET))


        badge_schema = cls(
            code=code,
            description=description,
            conditions=conditions,
            season=season,
        )


        badge_schema.additional_properties = d
        return badge_schema

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
