"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import paginatedfloorserializerlistlist as shared_paginatedfloorserializerlistlist
from typing import Optional


@dataclasses.dataclass
class FloorListSecurity:
    
    pmo_auth2_authentication: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class FloorListRequest:
    
    x_pm_org: int = dataclasses.field(metadata={'header': { 'field_name': 'X-Pm-Org', 'style': 'simple', 'explode': False }})
    r"""The management ID (MID), found in the first number of your URL when logged in:  https://app.propertymeld.com/{MID}/m/123"""
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    r"""Number of results to return per page."""
    offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    r"""The initial index from which to return the results."""
    ordering: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'ordering', 'style': 'form', 'explode': True }})
    r"""Which field to use when ordering the results."""
    

@dataclasses.dataclass
class FloorListResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    paginated_floor_serializer_list_list: Optional[shared_paginatedfloorserializerlistlist.PaginatedFloorSerializerListList] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    