from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.achievement_type import AchievementType
from ...models.data_page_account_achievement_schema import DataPageAccountAchievementSchema
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    account: str,
    *,
    type_: Union[Unset, AchievementType] = UNSET,
    completed: Union[Unset, bool] = UNSET,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_type_: Union[Unset, str] = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params["completed"] = completed

    params["page"] = page

    params["size"] = size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/accounts/{account}/achievements".format(account=account,),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, DataPageAccountAchievementSchema]]:
    if response.status_code == 200:
        response_200 = DataPageAccountAchievementSchema.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, DataPageAccountAchievementSchema]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account: str,
    *,
    client: Union[AuthenticatedClient, Client],
    type_: Union[Unset, AchievementType] = UNSET,
    completed: Union[Unset, bool] = UNSET,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> Response[Union[Any, DataPageAccountAchievementSchema]]:
    """ Get Account Achievements

     Retrieve the achievements of a account.

    Args:
        account (str): The character name.
        type_ (Union[Unset, AchievementType]):
        completed (Union[Unset, bool]): Filter by completed achievements.
        page (Union[Unset, int]): Page number Default: 1.
        size (Union[Unset, int]): Page size Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DataPageAccountAchievementSchema]]
     """


    kwargs = _get_kwargs(
        account=account,
type_=type_,
completed=completed,
page=page,
size=size,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    account: str,
    *,
    client: Union[AuthenticatedClient, Client],
    type_: Union[Unset, AchievementType] = UNSET,
    completed: Union[Unset, bool] = UNSET,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> Optional[Union[Any, DataPageAccountAchievementSchema]]:
    """ Get Account Achievements

     Retrieve the achievements of a account.

    Args:
        account (str): The character name.
        type_ (Union[Unset, AchievementType]):
        completed (Union[Unset, bool]): Filter by completed achievements.
        page (Union[Unset, int]): Page number Default: 1.
        size (Union[Unset, int]): Page size Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DataPageAccountAchievementSchema]
     """


    return sync_detailed(
        account=account,
client=client,
type_=type_,
completed=completed,
page=page,
size=size,

    ).parsed

async def asyncio_detailed(
    account: str,
    *,
    client: Union[AuthenticatedClient, Client],
    type_: Union[Unset, AchievementType] = UNSET,
    completed: Union[Unset, bool] = UNSET,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> Response[Union[Any, DataPageAccountAchievementSchema]]:
    """ Get Account Achievements

     Retrieve the achievements of a account.

    Args:
        account (str): The character name.
        type_ (Union[Unset, AchievementType]):
        completed (Union[Unset, bool]): Filter by completed achievements.
        page (Union[Unset, int]): Page number Default: 1.
        size (Union[Unset, int]): Page size Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DataPageAccountAchievementSchema]]
     """


    kwargs = _get_kwargs(
        account=account,
type_=type_,
completed=completed,
page=page,
size=size,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    account: str,
    *,
    client: Union[AuthenticatedClient, Client],
    type_: Union[Unset, AchievementType] = UNSET,
    completed: Union[Unset, bool] = UNSET,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> Optional[Union[Any, DataPageAccountAchievementSchema]]:
    """ Get Account Achievements

     Retrieve the achievements of a account.

    Args:
        account (str): The character name.
        type_ (Union[Unset, AchievementType]):
        completed (Union[Unset, bool]): Filter by completed achievements.
        page (Union[Unset, int]): Page number Default: 1.
        size (Union[Unset, int]): Page size Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DataPageAccountAchievementSchema]
     """


    return (await asyncio_detailed(
        account=account,
client=client,
type_=type_,
completed=completed,
page=page,
size=size,

    )).parsed
