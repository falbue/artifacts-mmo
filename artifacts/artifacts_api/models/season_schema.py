from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import Union
import datetime

if TYPE_CHECKING:
  from ..models.season_skin_schema import SeasonSkinSchema
  from ..models.season_badge_schema import SeasonBadgeSchema





T = TypeVar("T", bound="SeasonSchema")



@_attrs_define
class SeasonSchema:
    """ 
        Attributes:
            badges (list['SeasonBadgeSchema']): Season badges with required achievement points.
            skins (list['SeasonSkinSchema']): Season skins with required achievement points.
            name (Union[Unset, str]): Season name.
            number (Union[Unset, int]): Season number.
            start_date (Union[Unset, datetime.datetime]): Season start date.
     """

    badges: list['SeasonBadgeSchema']
    skins: list['SeasonSkinSchema']
    name: Union[Unset, str] = UNSET
    number: Union[Unset, int] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.season_skin_schema import SeasonSkinSchema
        from ..models.season_badge_schema import SeasonBadgeSchema
        badges = []
        for badges_item_data in self.badges:
            badges_item = badges_item_data.to_dict()
            badges.append(badges_item)



        skins = []
        for skins_item_data in self.skins:
            skins_item = skins_item_data.to_dict()
            skins.append(skins_item)



        name = self.name

        number = self.number

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "badges": badges,
            "skins": skins,
        })
        if name is not UNSET:
            field_dict["name"] = name
        if number is not UNSET:
            field_dict["number"] = number
        if start_date is not UNSET:
            field_dict["start_date"] = start_date

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.season_skin_schema import SeasonSkinSchema
        from ..models.season_badge_schema import SeasonBadgeSchema
        d = dict(src_dict)
        badges = []
        _badges = d.pop("badges")
        for badges_item_data in (_badges):
            badges_item = SeasonBadgeSchema.from_dict(badges_item_data)



            badges.append(badges_item)


        skins = []
        _skins = d.pop("skins")
        for skins_item_data in (_skins):
            skins_item = SeasonSkinSchema.from_dict(skins_item_data)



            skins.append(skins_item)


        name = d.pop("name", UNSET)

        number = d.pop("number", UNSET)

        _start_date = d.pop("start_date", UNSET)
        start_date: Union[Unset, datetime.datetime]
        if isinstance(_start_date,  Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)




        season_schema = cls(
            badges=badges,
            skins=skins,
            name=name,
            number=number,
            start_date=start_date,
        )


        season_schema.additional_properties = d
        return season_schema

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
