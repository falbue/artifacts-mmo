from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.data_page_monster_schema import DataPageMonsterSchema
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    name: Union[Unset, str] = UNSET,
    min_level: Union[Unset, int] = UNSET,
    max_level: Union[Unset, int] = UNSET,
    drop: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["name"] = name

    params["min_level"] = min_level

    params["max_level"] = max_level

    params["drop"] = drop

    params["page"] = page

    params["size"] = size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/monsters",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[DataPageMonsterSchema]:
    if response.status_code == 200:
        response_200 = DataPageMonsterSchema.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[DataPageMonsterSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    name: Union[Unset, str] = UNSET,
    min_level: Union[Unset, int] = UNSET,
    max_level: Union[Unset, int] = UNSET,
    drop: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> Response[DataPageMonsterSchema]:
    """ Get All Monsters

     Fetch monsters details.

    Args:
        name (Union[Unset, str]): Name of the monster.
        min_level (Union[Unset, int]): Monster minimum level.
        max_level (Union[Unset, int]): Monster maximum level.
        drop (Union[Unset, str]): Item code of the drop.
        page (Union[Unset, int]): Page number Default: 1.
        size (Union[Unset, int]): Page size Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataPageMonsterSchema]
     """


    kwargs = _get_kwargs(
        name=name,
min_level=min_level,
max_level=max_level,
drop=drop,
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
    name: Union[Unset, str] = UNSET,
    min_level: Union[Unset, int] = UNSET,
    max_level: Union[Unset, int] = UNSET,
    drop: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> Optional[DataPageMonsterSchema]:
    """ Get All Monsters

     Fetch monsters details.

    Args:
        name (Union[Unset, str]): Name of the monster.
        min_level (Union[Unset, int]): Monster minimum level.
        max_level (Union[Unset, int]): Monster maximum level.
        drop (Union[Unset, str]): Item code of the drop.
        page (Union[Unset, int]): Page number Default: 1.
        size (Union[Unset, int]): Page size Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataPageMonsterSchema
     """


    return sync_detailed(
        client=client,
name=name,
min_level=min_level,
max_level=max_level,
drop=drop,
page=page,
size=size,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    name: Union[Unset, str] = UNSET,
    min_level: Union[Unset, int] = UNSET,
    max_level: Union[Unset, int] = UNSET,
    drop: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> Response[DataPageMonsterSchema]:
    """ Get All Monsters

     Fetch monsters details.

    Args:
        name (Union[Unset, str]): Name of the monster.
        min_level (Union[Unset, int]): Monster minimum level.
        max_level (Union[Unset, int]): Monster maximum level.
        drop (Union[Unset, str]): Item code of the drop.
        page (Union[Unset, int]): Page number Default: 1.
        size (Union[Unset, int]): Page size Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataPageMonsterSchema]
     """


    kwargs = _get_kwargs(
        name=name,
min_level=min_level,
max_level=max_level,
drop=drop,
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
    name: Union[Unset, str] = UNSET,
    min_level: Union[Unset, int] = UNSET,
    max_level: Union[Unset, int] = UNSET,
    drop: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> Optional[DataPageMonsterSchema]:
    """ Get All Monsters

     Fetch monsters details.

    Args:
        name (Union[Unset, str]): Name of the monster.
        min_level (Union[Unset, int]): Monster minimum level.
        max_level (Union[Unset, int]): Monster maximum level.
        drop (Union[Unset, str]): Item code of the drop.
        page (Union[Unset, int]): Page number Default: 1.
        size (Union[Unset, int]): Page size Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataPageMonsterSchema
     """


    return (await asyncio_detailed(
        client=client,
name=name,
min_level=min_level,
max_level=max_level,
drop=drop,
page=page,
size=size,

    )).parsed
