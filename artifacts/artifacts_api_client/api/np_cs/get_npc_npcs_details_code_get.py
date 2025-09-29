from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.npc_response_schema import NPCResponseSchema
from typing import cast



def _get_kwargs(
    code: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/npcs/details/{code}".format(code=code,),
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, NPCResponseSchema]]:
    if response.status_code == 200:
        response_200 = NPCResponseSchema.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, NPCResponseSchema]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    code: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Union[Any, NPCResponseSchema]]:
    """ Get Npc

     Retrieve the details of a NPC.

    Args:
        code (str): The code of the NPC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NPCResponseSchema]]
     """


    kwargs = _get_kwargs(
        code=code,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    code: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Optional[Union[Any, NPCResponseSchema]]:
    """ Get Npc

     Retrieve the details of a NPC.

    Args:
        code (str): The code of the NPC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, NPCResponseSchema]
     """


    return sync_detailed(
        code=code,
client=client,

    ).parsed

async def asyncio_detailed(
    code: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Union[Any, NPCResponseSchema]]:
    """ Get Npc

     Retrieve the details of a NPC.

    Args:
        code (str): The code of the NPC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NPCResponseSchema]]
     """


    kwargs = _get_kwargs(
        code=code,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    code: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Optional[Union[Any, NPCResponseSchema]]:
    """ Get Npc

     Retrieve the details of a NPC.

    Args:
        code (str): The code of the NPC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, NPCResponseSchema]
     """


    return (await asyncio_detailed(
        code=code,
client=client,

    )).parsed
