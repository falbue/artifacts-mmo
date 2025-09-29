from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.character_rest_data_schema import CharacterRestDataSchema





T = TypeVar("T", bound="CharacterRestResponseSchema")



@_attrs_define
class CharacterRestResponseSchema:
    """ 
        Attributes:
            data (CharacterRestDataSchema):
     """

    data: 'CharacterRestDataSchema'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.character_rest_data_schema import CharacterRestDataSchema
        data = self.data.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "data": data,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.character_rest_data_schema import CharacterRestDataSchema
        d = dict(src_dict)
        data = CharacterRestDataSchema.from_dict(d.pop("data"))




        character_rest_response_schema = cls(
            data=data,
        )


        character_rest_response_schema.additional_properties = d
        return character_rest_response_schema

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
