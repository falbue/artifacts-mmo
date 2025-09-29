from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.character_schema import CharacterSchema
  from ..models.cooldown_schema import CooldownSchema
  from ..models.fight_schema import FightSchema





T = TypeVar("T", bound="CharacterFightDataSchema")



@_attrs_define
class CharacterFightDataSchema:
    """ 
        Attributes:
            cooldown (CooldownSchema):
            fight (FightSchema):
            character (CharacterSchema):
     """

    cooldown: 'CooldownSchema'
    fight: 'FightSchema'
    character: 'CharacterSchema'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.character_schema import CharacterSchema
        from ..models.cooldown_schema import CooldownSchema
        from ..models.fight_schema import FightSchema
        cooldown = self.cooldown.to_dict()

        fight = self.fight.to_dict()

        character = self.character.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "cooldown": cooldown,
            "fight": fight,
            "character": character,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.character_schema import CharacterSchema
        from ..models.cooldown_schema import CooldownSchema
        from ..models.fight_schema import FightSchema
        d = dict(src_dict)
        cooldown = CooldownSchema.from_dict(d.pop("cooldown"))




        fight = FightSchema.from_dict(d.pop("fight"))




        character = CharacterSchema.from_dict(d.pop("character"))




        character_fight_data_schema = cls(
            cooldown=cooldown,
            fight=fight,
            character=character,
        )


        character_fight_data_schema.additional_properties = d
        return character_fight_data_schema

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
