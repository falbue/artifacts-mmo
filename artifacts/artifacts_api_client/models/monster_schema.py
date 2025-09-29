from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.simple_effect_schema import SimpleEffectSchema
  from ..models.drop_rate_schema import DropRateSchema





T = TypeVar("T", bound="MonsterSchema")



@_attrs_define
class MonsterSchema:
    """ 
        Attributes:
            name (str): Name of the monster.
            code (str): The code of the monster. This is the monster's unique identifier (ID).
            level (int): Monster level.
            hp (int): Monster hit points.
            attack_fire (int): Monster fire attack.
            attack_earth (int): Monster earth attack.
            attack_water (int): Monster water attack.
            attack_air (int): Monster air attack.
            res_fire (int): Monster % fire resistance.
            res_earth (int): Monster % earth resistance.
            res_water (int): Monster % water resistance.
            res_air (int): Monster % air resistance.
            critical_strike (int): Monster % critical strike.
            min_gold (int): Monster minimum gold drop.
            max_gold (int): Monster maximum gold drop.
            drops (list['DropRateSchema']): Monster drops. This is a list of items that the monster drops after killing the
                monster.
            effects (Union[Unset, list['SimpleEffectSchema']]): List of effects.
     """

    name: str
    code: str
    level: int
    hp: int
    attack_fire: int
    attack_earth: int
    attack_water: int
    attack_air: int
    res_fire: int
    res_earth: int
    res_water: int
    res_air: int
    critical_strike: int
    min_gold: int
    max_gold: int
    drops: list['DropRateSchema']
    effects: Union[Unset, list['SimpleEffectSchema']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.simple_effect_schema import SimpleEffectSchema
        from ..models.drop_rate_schema import DropRateSchema
        name = self.name

        code = self.code

        level = self.level

        hp = self.hp

        attack_fire = self.attack_fire

        attack_earth = self.attack_earth

        attack_water = self.attack_water

        attack_air = self.attack_air

        res_fire = self.res_fire

        res_earth = self.res_earth

        res_water = self.res_water

        res_air = self.res_air

        critical_strike = self.critical_strike

        min_gold = self.min_gold

        max_gold = self.max_gold

        drops = []
        for drops_item_data in self.drops:
            drops_item = drops_item_data.to_dict()
            drops.append(drops_item)



        effects: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.effects, Unset):
            effects = []
            for effects_item_data in self.effects:
                effects_item = effects_item_data.to_dict()
                effects.append(effects_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "code": code,
            "level": level,
            "hp": hp,
            "attack_fire": attack_fire,
            "attack_earth": attack_earth,
            "attack_water": attack_water,
            "attack_air": attack_air,
            "res_fire": res_fire,
            "res_earth": res_earth,
            "res_water": res_water,
            "res_air": res_air,
            "critical_strike": critical_strike,
            "min_gold": min_gold,
            "max_gold": max_gold,
            "drops": drops,
        })
        if effects is not UNSET:
            field_dict["effects"] = effects

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.simple_effect_schema import SimpleEffectSchema
        from ..models.drop_rate_schema import DropRateSchema
        d = dict(src_dict)
        name = d.pop("name")

        code = d.pop("code")

        level = d.pop("level")

        hp = d.pop("hp")

        attack_fire = d.pop("attack_fire")

        attack_earth = d.pop("attack_earth")

        attack_water = d.pop("attack_water")

        attack_air = d.pop("attack_air")

        res_fire = d.pop("res_fire")

        res_earth = d.pop("res_earth")

        res_water = d.pop("res_water")

        res_air = d.pop("res_air")

        critical_strike = d.pop("critical_strike")

        min_gold = d.pop("min_gold")

        max_gold = d.pop("max_gold")

        drops = []
        _drops = d.pop("drops")
        for drops_item_data in (_drops):
            drops_item = DropRateSchema.from_dict(drops_item_data)



            drops.append(drops_item)


        effects = []
        _effects = d.pop("effects", UNSET)
        for effects_item_data in (_effects or []):
            effects_item = SimpleEffectSchema.from_dict(effects_item_data)



            effects.append(effects_item)


        monster_schema = cls(
            name=name,
            code=code,
            level=level,
            hp=hp,
            attack_fire=attack_fire,
            attack_earth=attack_earth,
            attack_water=attack_water,
            attack_air=attack_air,
            res_fire=res_fire,
            res_earth=res_earth,
            res_water=res_water,
            res_air=res_air,
            critical_strike=critical_strike,
            min_gold=min_gold,
            max_gold=max_gold,
            drops=drops,
            effects=effects,
        )


        monster_schema.additional_properties = d
        return monster_schema

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
