"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import projectlistviewserializerproperty as shared_projectlistviewserializerproperty
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from marshmallow import fields
from meldapi import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ProjectListViewSerializerUnit:
    
    created: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    prop: shared_projectlistviewserializerproperty.ProjectListViewSerializerProperty = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('prop') }})
    updated: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    apartment: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('apartment'), 'exclude': lambda f: f is None }})
    department: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('department'), 'exclude': lambda f: f is None }})
    is_active: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_active'), 'exclude': lambda f: f is None }})
    maintenance_notes: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maintenance_notes'), 'exclude': lambda f: f is None }})
    room: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('room'), 'exclude': lambda f: f is None }})
    suite: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('suite'), 'exclude': lambda f: f is None }})
    unit: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unit'), 'exclude': lambda f: f is None }})
    