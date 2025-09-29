from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.data_page_event_schema import DataPageEventSchema
from ...models.map_content_type import MapContentType
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    type_: Union[Unset, MapContentType] = UNSET,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_type_: Union[Unset, str] = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params["page"] = page

    params["size"] = size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/events",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[DataPageEventSchema]:
    if response.status_code == 200:
        response_200 = DataPageEventSchema.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[DataPageEventSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    type_: Union[Unset, MapContentType] = UNSET,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> Response[DataPageEventSchema]:
    """ Get All Events

     Fetch events details.

    Args:
        type_ (Union[Unset, MapContentType]):
        page (Union[Unset, int]): Page number Default: 1.
        size (Union[Unset, int]): Page size Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataPageEventSchema]
     """


    kwargs = _get_kwargs(
        type_=type_,
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
    type_: Union[Unset, MapContentType] = UNSET,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> Optional[DataPageEventSchema]:
    """ Get All Events

     Fetch events details.

    Args:
        type_ (Union[Unset, MapContentType]):
        page (Union[Unset, int]): Page number Default: 1.
        size (Union[Unset, int]): Page size Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataPageEventSchema
     """


    return sync_detailed(
        client=client,
type_=type_,
page=page,
size=size,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    type_: Union[Unset, MapContentType] = UNSET,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> Response[DataPageEventSchema]:
    """ Get All Events

     Fetch events details.

    Args:
        type_ (Union[Unset, MapContentType]):
        page (Union[Unset, int]): Page number Default: 1.
        size (Union[Unset, int]): Page size Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataPageEventSchema]
     """


    kwargs = _get_kwargs(
        type_=type_,
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
    type_: Union[Unset, MapContentType] = UNSET,
    page: Union[Unset, int] = 1,
    size: Union[Unset, int] = 50,

) -> Optional[DataPageEventSchema]:
    """ Get All Events

     Fetch events details.

    Args:
        type_ (Union[Unset, MapContentType]):
        page (Union[Unset, int]): Page number Default: 1.
        size (Union[Unset, int]): Page size Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataPageEventSchema
     """


    return (await asyncio_detailed(
        client=client,
type_=type_,
page=page,
size=size,

    )).parsed
