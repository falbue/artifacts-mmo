from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.map_schema import MapSchema





T = TypeVar("T", bound="ActiveEventSchema")



@_attrs_define
class ActiveEventSchema:
    """ 
        Attributes:
            name (str): Name of the event.
            code (str): Code of the event.
            map_ (MapSchema):
            previous_map (MapSchema):
            duration (int): Duration in minutes.
            expiration (datetime.datetime): Expiration datetime.
            created_at (datetime.datetime): Start datetime.
     """

    name: str
    code: str
    map_: 'MapSchema'
    previous_map: 'MapSchema'
    duration: int
    expiration: datetime.datetime
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.map_schema import MapSchema
        name = self.name

        code = self.code

        map_ = self.map_.to_dict()

        previous_map = self.previous_map.to_dict()

        duration = self.duration

        expiration = self.expiration.isoformat()

        created_at = self.created_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "code": code,
            "map": map_,
            "previous_map": previous_map,
            "duration": duration,
            "expiration": expiration,
            "created_at": created_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.map_schema import MapSchema
        d = dict(src_dict)
        name = d.pop("name")

        code = d.pop("code")

        map_ = MapSchema.from_dict(d.pop("map"))




        previous_map = MapSchema.from_dict(d.pop("previous_map"))




        duration = d.pop("duration")

        expiration = isoparse(d.pop("expiration"))




        created_at = isoparse(d.pop("created_at"))




        active_event_schema = cls(
            name=name,
            code=code,
            map_=map_,
            previous_map=previous_map,
            duration=duration,
            expiration=expiration,
            created_at=created_at,
        )


        active_event_schema.additional_properties = d
        return active_event_schema

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
