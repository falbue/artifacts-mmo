from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.map_response_schema import MapResponseSchema
from typing import cast



def _get_kwargs(
    x: int,
    y: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/maps/{x}/{y}".format(x=x,y=y,),
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, MapResponseSchema]]:
    if response.status_code == 200:
        response_200 = MapResponseSchema.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, MapResponseSchema]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    x: int,
    y: int,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Union[Any, MapResponseSchema]]:
    """ Get Map

     Retrieve the details of a map.

    Args:
        x (int): The position x of the map.
        y (int): The position X of the map.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, MapResponseSchema]]
     """


    kwargs = _get_kwargs(
        x=x,
y=y,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    x: int,
    y: int,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Optional[Union[Any, MapResponseSchema]]:
    """ Get Map

     Retrieve the details of a map.

    Args:
        x (int): The position x of the map.
        y (int): The position X of the map.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, MapResponseSchema]
     """


    return sync_detailed(
        x=x,
y=y,
client=client,

    ).parsed

async def asyncio_detailed(
    x: int,
    y: int,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Union[Any, MapResponseSchema]]:
    """ Get Map

     Retrieve the details of a map.

    Args:
        x (int): The position x of the map.
        y (int): The position X of the map.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, MapResponseSchema]]
     """


    kwargs = _get_kwargs(
        x=x,
y=y,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    x: int,
    y: int,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Optional[Union[Any, MapResponseSchema]]:
    """ Get Map

     Retrieve the details of a map.

    Args:
        x (int): The position x of the map.
        y (int): The position X of the map.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, MapResponseSchema]
     """


    return (await asyncio_detailed(
        x=x,
y=y,
client=client,

    )).parsed
