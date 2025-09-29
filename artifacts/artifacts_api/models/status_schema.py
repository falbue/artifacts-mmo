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
  from ..models.announcement_schema import AnnouncementSchema
  from ..models.rate_limit_schema import RateLimitSchema
  from ..models.season_schema import SeasonSchema





T = TypeVar("T", bound="StatusSchema")



@_attrs_define
class StatusSchema:
    """ 
        Attributes:
            version (str): Game version.
            server_time (datetime.datetime): Server time.
            max_level (int): Maximum level.
            max_skill_level (int): Maximum skill level.
            characters_online (int): Characters online.
            announcements (list['AnnouncementSchema']): Server announcements.
            rate_limits (list['RateLimitSchema']): Rate limits.
            season (Union[Unset, SeasonSchema]):
     """

    version: str
    server_time: datetime.datetime
    max_level: int
    max_skill_level: int
    characters_online: int
    announcements: list['AnnouncementSchema']
    rate_limits: list['RateLimitSchema']
    season: Union[Unset, 'SeasonSchema'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.announcement_schema import AnnouncementSchema
        from ..models.rate_limit_schema import RateLimitSchema
        from ..models.season_schema import SeasonSchema
        version = self.version

        server_time = self.server_time.isoformat()

        max_level = self.max_level

        max_skill_level = self.max_skill_level

        characters_online = self.characters_online

        announcements = []
        for announcements_item_data in self.announcements:
            announcements_item = announcements_item_data.to_dict()
            announcements.append(announcements_item)



        rate_limits = []
        for rate_limits_item_data in self.rate_limits:
            rate_limits_item = rate_limits_item_data.to_dict()
            rate_limits.append(rate_limits_item)



        season: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.season, Unset):
            season = self.season.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "version": version,
            "server_time": server_time,
            "max_level": max_level,
            "max_skill_level": max_skill_level,
            "characters_online": characters_online,
            "announcements": announcements,
            "rate_limits": rate_limits,
        })
        if season is not UNSET:
            field_dict["season"] = season

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.announcement_schema import AnnouncementSchema
        from ..models.rate_limit_schema import RateLimitSchema
        from ..models.season_schema import SeasonSchema
        d = dict(src_dict)
        version = d.pop("version")

        server_time = isoparse(d.pop("server_time"))




        max_level = d.pop("max_level")

        max_skill_level = d.pop("max_skill_level")

        characters_online = d.pop("characters_online")

        announcements = []
        _announcements = d.pop("announcements")
        for announcements_item_data in (_announcements):
            announcements_item = AnnouncementSchema.from_dict(announcements_item_data)



            announcements.append(announcements_item)


        rate_limits = []
        _rate_limits = d.pop("rate_limits")
        for rate_limits_item_data in (_rate_limits):
            rate_limits_item = RateLimitSchema.from_dict(rate_limits_item_data)



            rate_limits.append(rate_limits_item)


        _season = d.pop("season", UNSET)
        season: Union[Unset, SeasonSchema]
        if isinstance(_season,  Unset):
            season = UNSET
        else:
            season = SeasonSchema.from_dict(_season)




        status_schema = cls(
            version=version,
            server_time=server_time,
            max_level=max_level,
            max_skill_level=max_skill_level,
            characters_online=characters_online,
            announcements=announcements,
            rate_limits=rate_limits,
            season=season,
        )


        status_schema.additional_properties = d
        return status_schema

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
