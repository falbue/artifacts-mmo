from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.data_page_effect_schema import DataPageEffectSchema
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page"] = page

    params["size"] = size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/effects",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[DataPageEffectSchema]:
    if response.status_code == 200:
        response_200 = DataPageEffectSchema.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[DataPageEffectSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> Response[DataPageEffectSchema]:
    """ Get All Effects

     List of all effects. Effects are used by equipment, tools, runes, consumables and monsters. An
    effect is an action that produces an effect on the game.

    Args:
        page (Union[Unset, int]): Page number Default: 1.
        size (Union[Unset, int]): Page size Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataPageEffectSchema]
     """


    kwargs = _get_kwargs(
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
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> Optional[DataPageEffectSchema]:
    """ Get All Effects

     List of all effects. Effects are used by equipment, tools, runes, consumables and monsters. An
    effect is an action that produces an effect on the game.

    Args:
        page (Union[Unset, int]): Page number Default: 1.
        size (Union[Unset, int]): Page size Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataPageEffectSchema
     """


    return sync_detailed(
        client=client,
page=page,
size=size,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> Response[DataPageEffectSchema]:
    """ Get All Effects

     List of all effects. Effects are used by equipment, tools, runes, consumables and monsters. An
    effect is an action that produces an effect on the game.

    Args:
        page (Union[Unset, int]): Page number Default: 1.
        size (Union[Unset, int]): Page size Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataPageEffectSchema]
     """


    kwargs = _get_kwargs(
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
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> Optional[DataPageEffectSchema]:
    """ Get All Effects

     List of all effects. Effects are used by equipment, tools, runes, consumables and monsters. An
    effect is an action that produces an effect on the game.

    Args:
        page (Union[Unset, int]): Page number Default: 1.
        size (Union[Unset, int]): Page size Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataPageEffectSchema
     """


    return (await asyncio_detailed(
        client=client,
page=page,
size=size,

    )).parsed
