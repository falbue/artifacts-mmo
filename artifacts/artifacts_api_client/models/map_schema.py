from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import cast, Union

if TYPE_CHECKING:
  from ..models.map_content_schema import MapContentSchema





T = TypeVar("T", bound="MapSchema")



@_attrs_define
class MapSchema:
    """ 
        Attributes:
            name (str): Name of the map.
            skin (str): Skin of the map.
            x (int): Position X of the map.
            y (int): Position Y of the map.
            content (Union['MapContentSchema', None]): Content of the map.
     """

    name: str
    skin: str
    x: int
    y: int
    content: Union['MapContentSchema', None]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.map_content_schema import MapContentSchema
        name = self.name

        skin = self.skin

        x = self.x

        y = self.y

        content: Union[None, dict[str, Any]]
        if isinstance(self.content, MapContentSchema):
            content = self.content.to_dict()
        else:
            content = self.content


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "skin": skin,
            "x": x,
            "y": y,
            "content": content,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.map_content_schema import MapContentSchema
        d = dict(src_dict)
        name = d.pop("name")

        skin = d.pop("skin")

        x = d.pop("x")

        y = d.pop("y")

        def _parse_content(data: object) -> Union['MapContentSchema', None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                content_type_0 = MapContentSchema.from_dict(data)



                return content_type_0
            except: # noqa: E722
                pass
            return cast(Union['MapContentSchema', None], data)

        content = _parse_content(d.pop("content"))


        map_schema = cls(
            name=name,
            skin=skin,
            x=x,
            y=y,
            content=content,
        )


        map_schema.additional_properties = d
        return map_schema

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
