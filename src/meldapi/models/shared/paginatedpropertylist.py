"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import property as shared_property
from dataclasses_json import Undefined, dataclass_json
from meldapi import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PaginatedPropertyList:
    count: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('count'), 'exclude': lambda f: f is None }})
    next: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('next'), 'exclude': lambda f: f is None }})
    previous: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('previous'), 'exclude': lambda f: f is None }})
    results: Optional[list[shared_property.Property]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('results'), 'exclude': lambda f: f is None }})
    

