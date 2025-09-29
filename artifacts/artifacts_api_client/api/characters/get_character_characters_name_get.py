from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.character_response_schema import CharacterResponseSchema
from typing import cast



def _get_kwargs(
    name: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/characters/{name}".format(name=name,),
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, CharacterResponseSchema]]:
    if response.status_code == 200:
        response_200 = CharacterResponseSchema.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, CharacterResponseSchema]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Union[Any, CharacterResponseSchema]]:
    """ Get Character

     Retrieve the details of a character.

    Args:
        name (str): The character name.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CharacterResponseSchema]]
     """


    kwargs = _get_kwargs(
        name=name,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    name: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Optional[Union[Any, CharacterResponseSchema]]:
    """ Get Character

     Retrieve the details of a character.

    Args:
        name (str): The character name.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CharacterResponseSchema]
     """


    return sync_detailed(
        name=name,
client=client,

    ).parsed

async def asyncio_detailed(
    name: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Union[Any, CharacterResponseSchema]]:
    """ Get Character

     Retrieve the details of a character.

    Args:
        name (str): The character name.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CharacterResponseSchema]]
     """


    kwargs = _get_kwargs(
        name=name,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    name: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Optional[Union[Any, CharacterResponseSchema]]:
    """ Get Character

     Retrieve the details of a character.

    Args:
        name (str): The character name.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CharacterResponseSchema]
     """


    return (await asyncio_detailed(
        name=name,
client=client,

    )).parsed
