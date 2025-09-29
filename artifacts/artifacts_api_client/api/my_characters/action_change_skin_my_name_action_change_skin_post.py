from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.change_skin_character_schema import ChangeSkinCharacterSchema
from ...models.change_skin_response_schema import ChangeSkinResponseSchema
from typing import cast



def _get_kwargs(
    name: str,
    *,
    body: ChangeSkinCharacterSchema,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/my/{name}/action/change_skin".format(name=name,),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, ChangeSkinResponseSchema]]:
    if response.status_code == 200:
        response_200 = ChangeSkinResponseSchema.from_dict(response.json())



        return response_200

    if response.status_code == 486:
        response_486 = cast(Any, None)
        return response_486

    if response.status_code == 499:
        response_499 = cast(Any, None)
        return response_499

    if response.status_code == 550:
        response_550 = cast(Any, None)
        return response_550

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, ChangeSkinResponseSchema]]:
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
    body: ChangeSkinCharacterSchema,

) -> Response[Union[Any, ChangeSkinResponseSchema]]:
    """ Action Change Skin

     Change the skin of your character.

    Args:
        name (str): Name of your character.
        body (ChangeSkinCharacterSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ChangeSkinResponseSchema]]
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
    body: ChangeSkinCharacterSchema,

) -> Optional[Union[Any, ChangeSkinResponseSchema]]:
    """ Action Change Skin

     Change the skin of your character.

    Args:
        name (str): Name of your character.
        body (ChangeSkinCharacterSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ChangeSkinResponseSchema]
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
    body: ChangeSkinCharacterSchema,

) -> Response[Union[Any, ChangeSkinResponseSchema]]:
    """ Action Change Skin

     Change the skin of your character.

    Args:
        name (str): Name of your character.
        body (ChangeSkinCharacterSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ChangeSkinResponseSchema]]
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
    body: ChangeSkinCharacterSchema,

) -> Optional[Union[Any, ChangeSkinResponseSchema]]:
    """ Action Change Skin

     Change the skin of your character.

    Args:
        name (str): Name of your character.
        body (ChangeSkinCharacterSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ChangeSkinResponseSchema]
     """


    return (await asyncio_detailed(
        name=name,
client=client,
body=body,

    )).parsed
