from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.characters_list_schema import CharactersListSchema
from typing import cast



def _get_kwargs(
    account: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/accounts/{account}/characters".format(account=account,),
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[CharactersListSchema]:
    if response.status_code == 200:
        response_200 = CharactersListSchema.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[CharactersListSchema]:
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

) -> Response[CharactersListSchema]:
    """ Get Account Characters

     Account character lists.

    Args:
        account (str): The character name.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CharactersListSchema]
     """


    kwargs = _get_kwargs(
        account=account,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    account: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Optional[CharactersListSchema]:
    """ Get Account Characters

     Account character lists.

    Args:
        account (str): The character name.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CharactersListSchema
     """


    return sync_detailed(
        account=account,
client=client,

    ).parsed

async def asyncio_detailed(
    account: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[CharactersListSchema]:
    """ Get Account Characters

     Account character lists.

    Args:
        account (str): The character name.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CharactersListSchema]
     """


    kwargs = _get_kwargs(
        account=account,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    account: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Optional[CharactersListSchema]:
    """ Get Account Characters

     Account character lists.

    Args:
        account (str): The character name.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CharactersListSchema
     """


    return (await asyncio_detailed(
        account=account,
client=client,

    )).parsed
