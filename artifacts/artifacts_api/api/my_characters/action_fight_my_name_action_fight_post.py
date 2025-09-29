from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.character_fight_response_schema import CharacterFightResponseSchema
from typing import cast



def _get_kwargs(
    name: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/my/{name}/action/fight".format(name=name,),
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, CharacterFightResponseSchema]]:
    if response.status_code == 200:
        response_200 = CharacterFightResponseSchema.from_dict(response.json())



        return response_200

    if response.status_code == 486:
        response_486 = cast(Any, None)
        return response_486

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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, CharacterFightResponseSchema]]:
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

) -> Response[Union[Any, CharacterFightResponseSchema]]:
    """ Action Fight

     Start a fight against a monster on the character's map.

    Args:
        name (str): Name of your character.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CharacterFightResponseSchema]]
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
    client: AuthenticatedClient,

) -> Optional[Union[Any, CharacterFightResponseSchema]]:
    """ Action Fight

     Start a fight against a monster on the character's map.

    Args:
        name (str): Name of your character.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CharacterFightResponseSchema]
     """


    return sync_detailed(
        name=name,
client=client,

    ).parsed

async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient,

) -> Response[Union[Any, CharacterFightResponseSchema]]:
    """ Action Fight

     Start a fight against a monster on the character's map.

    Args:
        name (str): Name of your character.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CharacterFightResponseSchema]]
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
    client: AuthenticatedClient,

) -> Optional[Union[Any, CharacterFightResponseSchema]]:
    """ Action Fight

     Start a fight against a monster on the character's map.

    Args:
        name (str): Name of your character.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CharacterFightResponseSchema]
     """


    return (await asyncio_detailed(
        name=name,
client=client,

    )).parsed
