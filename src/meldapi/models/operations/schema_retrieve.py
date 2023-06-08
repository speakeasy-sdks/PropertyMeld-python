"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from enum import Enum
from typing import Any, Optional


@dataclasses.dataclass
class SchemaRetrieveSecurity:
    
    pmo_auth2_authentication: Optional[str] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    
class SchemaRetrieveFormat(str, Enum):
    JSON = 'json'
    YAML = 'yaml'


@dataclasses.dataclass
class SchemaRetrieveRequest:
    
    x_pm_org: int = dataclasses.field(metadata={'header': { 'field_name': 'X-Pm-Org', 'style': 'simple', 'explode': False }})
    r"""The management ID (MID), found in the first number of your URL when logged in:  https://app.propertymeld.com/{MID}/m/123"""
    format: Optional[SchemaRetrieveFormat] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'format', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class SchemaRetrieveResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    body: Optional[bytes] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    schema_retrieve_200_application_json_object: Optional[dict[str, Any]] = dataclasses.field(default=None)
    schema_retrieve_200_application_vnd_oai_openapi_plus_json_object: Optional[dict[str, Any]] = dataclasses.field(default=None)
    