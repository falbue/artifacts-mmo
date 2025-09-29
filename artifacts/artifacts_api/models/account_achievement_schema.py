from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.achievement_type import AchievementType
from dateutil.parser import isoparse
from typing import cast
from typing import cast, Union
import datetime

if TYPE_CHECKING:
  from ..models.achievement_rewards_schema import AchievementRewardsSchema





T = TypeVar("T", bound="AccountAchievementSchema")



@_attrs_define
class AccountAchievementSchema:
    """ 
        Attributes:
            name (str): Name of the achievement.
            code (str): Code of the achievement.
            description (str): Description of the achievement.
            points (int): Points of the achievement. Used for the leaderboard.
            type_ (AchievementType):
            target (Union[None, str]): Target of the achievement.
            total (int): Total to do.
            rewards (AchievementRewardsSchema):
            current (int): Current progress.
            completed_at (Union[None, datetime.datetime]): Completed at.
     """

    name: str
    code: str
    description: str
    points: int
    type_: AchievementType
    target: Union[None, str]
    total: int
    rewards: 'AchievementRewardsSchema'
    current: int
    completed_at: Union[None, datetime.datetime]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.achievement_rewards_schema import AchievementRewardsSchema
        name = self.name

        code = self.code

        description = self.description

        points = self.points

        type_ = self.type_.value

        target: Union[None, str]
        target = self.target

        total = self.total

        rewards = self.rewards.to_dict()

        current = self.current

        completed_at: Union[None, str]
        if isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "code": code,
            "description": description,
            "points": points,
            "type": type_,
            "target": target,
            "total": total,
            "rewards": rewards,
            "current": current,
            "completed_at": completed_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.achievement_rewards_schema import AchievementRewardsSchema
        d = dict(src_dict)
        name = d.pop("name")

        code = d.pop("code")

        description = d.pop("description")

        points = d.pop("points")

        type_ = AchievementType(d.pop("type"))




        def _parse_target(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        target = _parse_target(d.pop("target"))


        total = d.pop("total")

        rewards = AchievementRewardsSchema.from_dict(d.pop("rewards"))




        current = d.pop("current")

        def _parse_completed_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = isoparse(data)



                return completed_at_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        completed_at = _parse_completed_at(d.pop("completed_at"))


        account_achievement_schema = cls(
            name=name,
            code=code,
            description=description,
            points=points,
            type_=type_,
            target=target,
            total=total,
            rewards=rewards,
            current=current,
            completed_at=completed_at,
        )


        account_achievement_schema.additional_properties = d
        return account_achievement_schema

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
