"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import resident as shared_resident
from typing import Optional



@dataclasses.dataclass
class ResidentCreateJSONSecurity:
    pmo_auth2_authentication: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    




@dataclasses.dataclass
class ResidentCreateJSONResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    resident: Optional[shared_resident.Resident] = dataclasses.field(default=None)
    

