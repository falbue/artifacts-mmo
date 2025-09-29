from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.effect_subtype import EffectSubtype
from ..models.effect_type import EffectType






T = TypeVar("T", bound="EffectSchema")



@_attrs_define
class EffectSchema:
    """ 
        Attributes:
            name (str): Name of the effect.
            code (str): The code of the effect. This is the effect's unique identifier (ID).
            description (str): Description of the effect. This is a brief description of the effect.
            type_ (EffectType):
            subtype (EffectSubtype):
     """

    name: str
    code: str
    description: str
    type_: EffectType
    subtype: EffectSubtype
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        code = self.code

        description = self.description

        type_ = self.type_.value

        subtype = self.subtype.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "code": code,
            "description": description,
            "type": type_,
            "subtype": subtype,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        code = d.pop("code")

        description = d.pop("description")

        type_ = EffectType(d.pop("type"))




        subtype = EffectSubtype(d.pop("subtype"))




        effect_schema = cls(
            name=name,
            code=code,
            description=description,
            type_=type_,
            subtype=subtype,
        )


        effect_schema.additional_properties = d
        return effect_schema

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
