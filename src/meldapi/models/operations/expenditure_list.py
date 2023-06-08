"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import paginatedmeldexpenditureslistviewserializerlistlist as shared_paginatedmeldexpenditureslistviewserializerlistlist
from datetime import datetime
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class ExpenditureListSecurity:
    
    pmo_auth2_authentication: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    
class ExpenditureListStatus(str, Enum):
    APPROVED = 'APPROVED'
    BILLED = 'BILLED'
    DRAFT = 'DRAFT'
    HOLD = 'HOLD'
    IN_REVIEW = 'IN_REVIEW'


@dataclasses.dataclass
class ExpenditureListRequest:
    
    x_pm_org: int = dataclasses.field(metadata={'header': { 'field_name': 'X-Pm-Org', 'style': 'simple', 'explode': False }})
    r"""The management ID (MID), found in the first number of your URL when logged in:  https://app.propertymeld.com/{MID}/m/123"""
    created_gte: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'created__gte', 'style': 'form', 'explode': True }})
    created_interval: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'created__interval', 'style': 'form', 'explode': True }})
    created_lte: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'created__lte', 'style': 'form', 'explode': True }})
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    r"""Number of results to return per page."""
    offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    r"""The initial index from which to return the results."""
    ordering: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'ordering', 'style': 'form', 'explode': True }})
    r"""Which field to use when ordering the results."""
    status: Optional[list[ExpenditureListStatus]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'status', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class ExpenditureListResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    paginated_meld_expenditures_list_view_serializer_list_list: Optional[shared_paginatedmeldexpenditureslistviewserializerlistlist.PaginatedMeldExpendituresListViewSerializerListList] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    