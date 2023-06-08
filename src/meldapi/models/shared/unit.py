"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import address as shared_address
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from marshmallow import fields
from meldapi import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UnitInput:
    
    property_id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('property_id') }, 'form': { 'field_name': 'property_id' }, 'multipart_form': { 'field_name': 'property_id' }})
    approval_currency_limit: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('approval_currency_limit'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'approval_currency_limit' }, 'multipart_form': { 'field_name': 'approval_currency_limit' }})
    current_residents: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('current_residents'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'current_residents' }, 'multipart_form': { 'field_name': 'current_residents' }})
    maintenance_notes: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maintenance_notes'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'maintenance_notes' }, 'multipart_form': { 'field_name': 'maintenance_notes' }})
    unit: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unit'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'unit' }, 'multipart_form': { 'field_name': 'unit' }})
    r"""This field indicates the particular dwelling within a larger building or complex. For example, in the address 123 Main St, Unit 302, the unit is 302"""
    unit_address: Optional[shared_address.Address] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unit_address'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'unit_address', 'json': True }, 'multipart_form': { 'field_name': 'unit_address', 'json': True }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Unit:
    
    created: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    is_active: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_active') }})
    property_id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('property_id') }})
    updated: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    approval_currency_limit: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('approval_currency_limit'), 'exclude': lambda f: f is None }})
    current_residents: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('current_residents'), 'exclude': lambda f: f is None }})
    maintenance_notes: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maintenance_notes'), 'exclude': lambda f: f is None }})
    unit: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unit'), 'exclude': lambda f: f is None }})
    r"""This field indicates the particular dwelling within a larger building or complex. For example, in the address 123 Main St, Unit 302, the unit is 302"""
    unit_address: Optional[shared_address.Address] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unit_address'), 'exclude': lambda f: f is None }})
    