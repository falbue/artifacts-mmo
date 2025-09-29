from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.event_map_schema import EventMapSchema
  from ..models.event_content_schema import EventContentSchema





T = TypeVar("T", bound="EventSchema")



@_attrs_define
class EventSchema:
    """ 
        Attributes:
            name (str): Name of the event.
            code (str): Code of the event.
            content (EventContentSchema):
            maps (list['EventMapSchema']): Map list of the event.
            duration (int): Duration in minutes.
            rate (int): Rate spawn of the event. (1/rate every minute)
     """

    name: str
    code: str
    content: 'EventContentSchema'
    maps: list['EventMapSchema']
    duration: int
    rate: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.event_map_schema import EventMapSchema
        from ..models.event_content_schema import EventContentSchema
        name = self.name

        code = self.code

        content = self.content.to_dict()

        maps = []
        for maps_item_data in self.maps:
            maps_item = maps_item_data.to_dict()
            maps.append(maps_item)



        duration = self.duration

        rate = self.rate


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "code": code,
            "content": content,
            "maps": maps,
            "duration": duration,
            "rate": rate,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_map_schema import EventMapSchema
        from ..models.event_content_schema import EventContentSchema
        d = dict(src_dict)
        name = d.pop("name")

        code = d.pop("code")

        content = EventContentSchema.from_dict(d.pop("content"))




        maps = []
        _maps = d.pop("maps")
        for maps_item_data in (_maps):
            maps_item = EventMapSchema.from_dict(maps_item_data)



            maps.append(maps_item)


        duration = d.pop("duration")

        rate = d.pop("rate")

        event_schema = cls(
            name=name,
            code=code,
            content=content,
            maps=maps,
            duration=duration,
            rate=rate,
        )


        event_schema.additional_properties = d
        return event_schema

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
