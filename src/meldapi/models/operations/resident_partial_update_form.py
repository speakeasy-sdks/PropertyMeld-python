"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import patchedresident as shared_patchedresident
from ..shared import resident as shared_resident
from typing import Optional


@dataclasses.dataclass
class ResidentPartialUpdateFormSecurity:
    
    pmo_auth2_authentication: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class ResidentPartialUpdateFormRequest:
    
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    patched_resident_input1: Optional[shared_patchedresident.PatchedResidentInput1] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    

@dataclasses.dataclass
class ResidentPartialUpdateFormResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    resident: Optional[shared_resident.Resident] = dataclasses.field(default=None)
    