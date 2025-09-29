from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.character_skin import CharacterSkin






T = TypeVar("T", bound="AddCharacterSchema")



@_attrs_define
class AddCharacterSchema:
    """ 
        Attributes:
            name (str): Your desired character name. It's unique and all players can see it.
            skin (CharacterSkin):
     """

    name: str
    skin: CharacterSkin
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        skin = self.skin.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "skin": skin,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        skin = CharacterSkin(d.pop("skin"))




        add_character_schema = cls(
            name=name,
            skin=skin,
        )


        add_character_schema.additional_properties = d
        return add_character_schema

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
