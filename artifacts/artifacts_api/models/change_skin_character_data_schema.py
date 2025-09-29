from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.character_schema import CharacterSchema
  from ..models.cooldown_schema import CooldownSchema





T = TypeVar("T", bound="ChangeSkinCharacterDataSchema")



@_attrs_define
class ChangeSkinCharacterDataSchema:
    """ 
        Attributes:
            cooldown (CooldownSchema):
            skin (str): Craft details.
            character (CharacterSchema):
     """

    cooldown: 'CooldownSchema'
    skin: str
    character: 'CharacterSchema'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.character_schema import CharacterSchema
        from ..models.cooldown_schema import CooldownSchema
        cooldown = self.cooldown.to_dict()

        skin = self.skin

        character = self.character.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "cooldown": cooldown,
            "skin": skin,
            "character": character,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.character_schema import CharacterSchema
        from ..models.cooldown_schema import CooldownSchema
        d = dict(src_dict)
        cooldown = CooldownSchema.from_dict(d.pop("cooldown"))




        skin = d.pop("skin")

        character = CharacterSchema.from_dict(d.pop("character"))




        change_skin_character_data_schema = cls(
            cooldown=cooldown,
            skin=skin,
            character=character,
        )


        change_skin_character_data_schema.additional_properties = d
        return change_skin_character_data_schema

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
