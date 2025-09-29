from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.account_status import AccountStatus






T = TypeVar("T", bound="CharacterLeaderboardSchema")



@_attrs_define
class CharacterLeaderboardSchema:
    """ 
        Attributes:
            position (int): Position in the leaderboard.
            name (str): Character name.
            account (str): Account name.
            status (AccountStatus):
            skin (str): Character skin code.
            level (int): Combat level.
            total_xp (int): Total XP of your character.
            mining_level (int): Mining level.
            mining_total_xp (int): Mining total xp.
            woodcutting_level (int): Woodcutting level.
            woodcutting_total_xp (int): Woodcutting total xp.
            fishing_level (int): Fishing level.
            fishing_total_xp (int): Fishing total xp.
            weaponcrafting_level (int): Weaponcrafting level.
            weaponcrafting_total_xp (int): Weaponcrafting total xp.
            gearcrafting_level (int): Gearcrafting level.
            gearcrafting_total_xp (int): Gearcrafting total xp.
            jewelrycrafting_level (int): Jewelrycrafting level.
            jewelrycrafting_total_xp (int): Jewelrycrafting total xp.
            cooking_level (int): Cooking level.
            cooking_total_xp (int): Cooking total xp.
            alchemy_level (int): Alchemy level.
            alchemy_total_xp (int): Alchemy total xp.
            gold (int): The numbers of gold on this character.
     """

    position: int
    name: str
    account: str
    status: AccountStatus
    skin: str
    level: int
    total_xp: int
    mining_level: int
    mining_total_xp: int
    woodcutting_level: int
    woodcutting_total_xp: int
    fishing_level: int
    fishing_total_xp: int
    weaponcrafting_level: int
    weaponcrafting_total_xp: int
    gearcrafting_level: int
    gearcrafting_total_xp: int
    jewelrycrafting_level: int
    jewelrycrafting_total_xp: int
    cooking_level: int
    cooking_total_xp: int
    alchemy_level: int
    alchemy_total_xp: int
    gold: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        position = self.position

        name = self.name

        account = self.account

        status = self.status.value

        skin = self.skin

        level = self.level

        total_xp = self.total_xp

        mining_level = self.mining_level

        mining_total_xp = self.mining_total_xp

        woodcutting_level = self.woodcutting_level

        woodcutting_total_xp = self.woodcutting_total_xp

        fishing_level = self.fishing_level

        fishing_total_xp = self.fishing_total_xp

        weaponcrafting_level = self.weaponcrafting_level

        weaponcrafting_total_xp = self.weaponcrafting_total_xp

        gearcrafting_level = self.gearcrafting_level

        gearcrafting_total_xp = self.gearcrafting_total_xp

        jewelrycrafting_level = self.jewelrycrafting_level

        jewelrycrafting_total_xp = self.jewelrycrafting_total_xp

        cooking_level = self.cooking_level

        cooking_total_xp = self.cooking_total_xp

        alchemy_level = self.alchemy_level

        alchemy_total_xp = self.alchemy_total_xp

        gold = self.gold


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "position": position,
            "name": name,
            "account": account,
            "status": status,
            "skin": skin,
            "level": level,
            "total_xp": total_xp,
            "mining_level": mining_level,
            "mining_total_xp": mining_total_xp,
            "woodcutting_level": woodcutting_level,
            "woodcutting_total_xp": woodcutting_total_xp,
            "fishing_level": fishing_level,
            "fishing_total_xp": fishing_total_xp,
            "weaponcrafting_level": weaponcrafting_level,
            "weaponcrafting_total_xp": weaponcrafting_total_xp,
            "gearcrafting_level": gearcrafting_level,
            "gearcrafting_total_xp": gearcrafting_total_xp,
            "jewelrycrafting_level": jewelrycrafting_level,
            "jewelrycrafting_total_xp": jewelrycrafting_total_xp,
            "cooking_level": cooking_level,
            "cooking_total_xp": cooking_total_xp,
            "alchemy_level": alchemy_level,
            "alchemy_total_xp": alchemy_total_xp,
            "gold": gold,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        position = d.pop("position")

        name = d.pop("name")

        account = d.pop("account")

        status = AccountStatus(d.pop("status"))




        skin = d.pop("skin")

        level = d.pop("level")

        total_xp = d.pop("total_xp")

        mining_level = d.pop("mining_level")

        mining_total_xp = d.pop("mining_total_xp")

        woodcutting_level = d.pop("woodcutting_level")

        woodcutting_total_xp = d.pop("woodcutting_total_xp")

        fishing_level = d.pop("fishing_level")

        fishing_total_xp = d.pop("fishing_total_xp")

        weaponcrafting_level = d.pop("weaponcrafting_level")

        weaponcrafting_total_xp = d.pop("weaponcrafting_total_xp")

        gearcrafting_level = d.pop("gearcrafting_level")

        gearcrafting_total_xp = d.pop("gearcrafting_total_xp")

        jewelrycrafting_level = d.pop("jewelrycrafting_level")

        jewelrycrafting_total_xp = d.pop("jewelrycrafting_total_xp")

        cooking_level = d.pop("cooking_level")

        cooking_total_xp = d.pop("cooking_total_xp")

        alchemy_level = d.pop("alchemy_level")

        alchemy_total_xp = d.pop("alchemy_total_xp")

        gold = d.pop("gold")

        character_leaderboard_schema = cls(
            position=position,
            name=name,
            account=account,
            status=status,
            skin=skin,
            level=level,
            total_xp=total_xp,
            mining_level=mining_level,
            mining_total_xp=mining_total_xp,
            woodcutting_level=woodcutting_level,
            woodcutting_total_xp=woodcutting_total_xp,
            fishing_level=fishing_level,
            fishing_total_xp=fishing_total_xp,
            weaponcrafting_level=weaponcrafting_level,
            weaponcrafting_total_xp=weaponcrafting_total_xp,
            gearcrafting_level=gearcrafting_level,
            gearcrafting_total_xp=gearcrafting_total_xp,
            jewelrycrafting_level=jewelrycrafting_level,
            jewelrycrafting_total_xp=jewelrycrafting_total_xp,
            cooking_level=cooking_level,
            cooking_total_xp=cooking_total_xp,
            alchemy_level=alchemy_level,
            alchemy_total_xp=alchemy_total_xp,
            gold=gold,
        )


        character_leaderboard_schema.additional_properties = d
        return character_leaderboard_schema

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
