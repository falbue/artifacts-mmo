from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.fight_result import FightResult
from typing import cast

if TYPE_CHECKING:
  from ..models.drop_schema import DropSchema





T = TypeVar("T", bound="FightSchema")



@_attrs_define
class FightSchema:
    """ 
        Attributes:
            xp (int): The amount of xp gained from the fight.
            gold (int): The amount of gold gained from the fight.
            drops (list['DropSchema']): The items dropped from the fight.
            turns (int): Numbers of the turns of the combat.
            logs (list[str]): The fight logs.
            result (FightResult):
     """

    xp: int
    gold: int
    drops: list['DropSchema']
    turns: int
    logs: list[str]
    result: FightResult
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.drop_schema import DropSchema
        xp = self.xp

        gold = self.gold

        drops = []
        for drops_item_data in self.drops:
            drops_item = drops_item_data.to_dict()
            drops.append(drops_item)



        turns = self.turns

        logs = self.logs



        result = self.result.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "xp": xp,
            "gold": gold,
            "drops": drops,
            "turns": turns,
            "logs": logs,
            "result": result,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.drop_schema import DropSchema
        d = dict(src_dict)
        xp = d.pop("xp")

        gold = d.pop("gold")

        drops = []
        _drops = d.pop("drops")
        for drops_item_data in (_drops):
            drops_item = DropSchema.from_dict(drops_item_data)



            drops.append(drops_item)


        turns = d.pop("turns")

        logs = cast(list[str], d.pop("logs"))


        result = FightResult(d.pop("result"))




        fight_schema = cls(
            xp=xp,
            gold=gold,
            drops=drops,
            turns=turns,
            logs=logs,
            result=result,
        )


        fight_schema.additional_properties = d
        return fight_schema

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
