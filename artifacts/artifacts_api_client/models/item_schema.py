from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.condition_schema import ConditionSchema
  from ..models.simple_effect_schema import SimpleEffectSchema
  from ..models.craft_schema import CraftSchema





T = TypeVar("T", bound="ItemSchema")



@_attrs_define
class ItemSchema:
    """ 
        Attributes:
            name (str): Item name.
            code (str): Item code. This is the item's unique identifier (ID).
            level (int): Item level.
            type_ (str): Item type.
            subtype (str): Item subtype.
            description (str): Item description.
            tradeable (bool): Item tradeable status. A non-tradeable item cannot be exchanged or sold.
            conditions (Union[Unset, list['ConditionSchema']]): Item conditions. If applicable. Conditions for using or
                equipping the item.
            effects (Union[Unset, list['SimpleEffectSchema']]): List of object effects. For equipment, it will include item
                stats.
            craft (Union['CraftSchema', None, Unset]): Craft information. If applicable.
     """

    name: str
    code: str
    level: int
    type_: str
    subtype: str
    description: str
    tradeable: bool
    conditions: Union[Unset, list['ConditionSchema']] = UNSET
    effects: Union[Unset, list['SimpleEffectSchema']] = UNSET
    craft: Union['CraftSchema', None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.condition_schema import ConditionSchema
        from ..models.simple_effect_schema import SimpleEffectSchema
        from ..models.craft_schema import CraftSchema
        name = self.name

        code = self.code

        level = self.level

        type_ = self.type_

        subtype = self.subtype

        description = self.description

        tradeable = self.tradeable

        conditions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()
                conditions.append(conditions_item)



        effects: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.effects, Unset):
            effects = []
            for effects_item_data in self.effects:
                effects_item = effects_item_data.to_dict()
                effects.append(effects_item)



        craft: Union[None, Unset, dict[str, Any]]
        if isinstance(self.craft, Unset):
            craft = UNSET
        elif isinstance(self.craft, CraftSchema):
            craft = self.craft.to_dict()
        else:
            craft = self.craft


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "code": code,
            "level": level,
            "type": type_,
            "subtype": subtype,
            "description": description,
            "tradeable": tradeable,
        })
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if effects is not UNSET:
            field_dict["effects"] = effects
        if craft is not UNSET:
            field_dict["craft"] = craft

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.condition_schema import ConditionSchema
        from ..models.simple_effect_schema import SimpleEffectSchema
        from ..models.craft_schema import CraftSchema
        d = dict(src_dict)
        name = d.pop("name")

        code = d.pop("code")

        level = d.pop("level")

        type_ = d.pop("type")

        subtype = d.pop("subtype")

        description = d.pop("description")

        tradeable = d.pop("tradeable")

        conditions = []
        _conditions = d.pop("conditions", UNSET)
        for conditions_item_data in (_conditions or []):
            conditions_item = ConditionSchema.from_dict(conditions_item_data)



            conditions.append(conditions_item)


        effects = []
        _effects = d.pop("effects", UNSET)
        for effects_item_data in (_effects or []):
            effects_item = SimpleEffectSchema.from_dict(effects_item_data)



            effects.append(effects_item)


        def _parse_craft(data: object) -> Union['CraftSchema', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                craft_type_0 = CraftSchema.from_dict(data)



                return craft_type_0
            except: # noqa: E722
                pass
            return cast(Union['CraftSchema', None, Unset], data)

        craft = _parse_craft(d.pop("craft", UNSET))


        item_schema = cls(
            name=name,
            code=code,
            level=level,
            type_=type_,
            subtype=subtype,
            description=description,
            tradeable=tradeable,
            conditions=conditions,
            effects=effects,
            craft=craft,
        )


        item_schema.additional_properties = d
        return item_schema

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
