from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.character_leaderboard_type import CharacterLeaderboardType
from ...models.data_page_character_leaderboard_schema import DataPageCharacterLeaderboardSchema
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    sort: Union[Unset, CharacterLeaderboardType] = UNSET,
    name: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_sort: Union[Unset, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    params["name"] = name

    params["page"] = page

    params["size"] = size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/leaderboard/characters",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[DataPageCharacterLeaderboardSchema]:
    if response.status_code == 200:
        response_200 = DataPageCharacterLeaderboardSchema.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[DataPageCharacterLeaderboardSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    sort: Union[Unset, CharacterLeaderboardType] = UNSET,
    name: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> Response[DataPageCharacterLeaderboardSchema]:
    """ Get Characters Leaderboard

     Fetch leaderboard details.

    Args:
        sort (Union[Unset, CharacterLeaderboardType]):
        name (Union[Unset, str]): Find a character by name.
        page (Union[Unset, int]): Page number Default: 1.
        size (Union[Unset, int]): Page size Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataPageCharacterLeaderboardSchema]
     """


    kwargs = _get_kwargs(
        sort=sort,
name=name,
page=page,
size=size,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    sort: Union[Unset, CharacterLeaderboardType] = UNSET,
    name: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> Optional[DataPageCharacterLeaderboardSchema]:
    """ Get Characters Leaderboard

     Fetch leaderboard details.

    Args:
        sort (Union[Unset, CharacterLeaderboardType]):
        name (Union[Unset, str]): Find a character by name.
        page (Union[Unset, int]): Page number Default: 1.
        size (Union[Unset, int]): Page size Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataPageCharacterLeaderboardSchema
     """


    return sync_detailed(
        client=client,
sort=sort,
name=name,
page=page,
size=size,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    sort: Union[Unset, CharacterLeaderboardType] = UNSET,
    name: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> Response[DataPageCharacterLeaderboardSchema]:
    """ Get Characters Leaderboard

     Fetch leaderboard details.

    Args:
        sort (Union[Unset, CharacterLeaderboardType]):
        name (Union[Unset, str]): Find a character by name.
        page (Union[Unset, int]): Page number Default: 1.
        size (Union[Unset, int]): Page size Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataPageCharacterLeaderboardSchema]
     """


    kwargs = _get_kwargs(
        sort=sort,
name=name,
page=page,
size=size,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    sort: Union[Unset, CharacterLeaderboardType] = UNSET,
    name: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> Optional[DataPageCharacterLeaderboardSchema]:
    """ Get Characters Leaderboard

     Fetch leaderboard details.

    Args:
        sort (Union[Unset, CharacterLeaderboardType]):
        name (Union[Unset, str]): Find a character by name.
        page (Union[Unset, int]): Page number Default: 1.
        size (Union[Unset, int]): Page size Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataPageCharacterLeaderboardSchema
     """


    return (await asyncio_detailed(
        client=client,
sort=sort,
name=name,
page=page,
size=size,

    )).parsed
