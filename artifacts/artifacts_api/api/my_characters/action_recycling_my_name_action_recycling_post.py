from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.recycling_response_schema import RecyclingResponseSchema
from ...models.recycling_schema import RecyclingSchema
from typing import cast



def _get_kwargs(
    name: str,
    *,
    body: RecyclingSchema,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/my/{name}/action/recycling".format(name=name,),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, RecyclingResponseSchema]]:
    if response.status_code == 200:
        response_200 = RecyclingResponseSchema.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 473:
        response_473 = cast(Any, None)
        return response_473

    if response.status_code == 478:
        response_478 = cast(Any, None)
        return response_478

    if response.status_code == 486:
        response_486 = cast(Any, None)
        return response_486

    if response.status_code == 493:
        response_493 = cast(Any, None)
        return response_493

    if response.status_code == 497:
        response_497 = cast(Any, None)
        return response_497

    if response.status_code == 498:
        response_498 = cast(Any, None)
        return response_498

    if response.status_code == 499:
        response_499 = cast(Any, None)
        return response_499

    if response.status_code == 598:
        response_598 = cast(Any, None)
        return response_598

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, RecyclingResponseSchema]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    *,
    client: AuthenticatedClient,
    body: RecyclingSchema,

) -> Response[Union[Any, RecyclingResponseSchema]]:
    """ Action Recycling

     Recycling an item. The character must be on a map with a workshop (only for equipments and weapons).

    Args:
        name (str): Name of your character.
        body (RecyclingSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, RecyclingResponseSchema]]
     """


    kwargs = _get_kwargs(
        name=name,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    name: str,
    *,
    client: AuthenticatedClient,
    body: RecyclingSchema,

) -> Optional[Union[Any, RecyclingResponseSchema]]:
    """ Action Recycling

     Recycling an item. The character must be on a map with a workshop (only for equipments and weapons).

    Args:
        name (str): Name of your character.
        body (RecyclingSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, RecyclingResponseSchema]
     """


    return sync_detailed(
        name=name,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient,
    body: RecyclingSchema,

) -> Response[Union[Any, RecyclingResponseSchema]]:
    """ Action Recycling

     Recycling an item. The character must be on a map with a workshop (only for equipments and weapons).

    Args:
        name (str): Name of your character.
        body (RecyclingSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, RecyclingResponseSchema]]
     """


    kwargs = _get_kwargs(
        name=name,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient,
    body: RecyclingSchema,

) -> Optional[Union[Any, RecyclingResponseSchema]]:
    """ Action Recycling

     Recycling an item. The character must be on a map with a workshop (only for equipments and weapons).

    Args:
        name (str): Name of your character.
        body (RecyclingSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, RecyclingResponseSchema]
     """


    return (await asyncio_detailed(
        name=name,
client=client,
body=body,

    )).parsed
