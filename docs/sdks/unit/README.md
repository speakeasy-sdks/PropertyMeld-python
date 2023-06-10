# unit

### Available Operations

* [unit_create](#unit_create)
* [unit_destroy](#unit_destroy)
* [unit_list](#unit_list)
* [unit_partial_update](#unit_partial_update)
* [unit_retrieve](#unit_retrieve)
* [unit_update](#unit_update)

## unit_create

### Example Usage

```python
import meldapi
from meldapi.models import operations, shared

s = meldapi.MeldAPI()

req = shared.UnitInput(
    approval_currency_limit='quae',
    current_residents=[
        208253,
        348357,
    ],
    maintenance_notes='itaque',
    property_id=88248,
    unit='ipsum',
    unit_address=shared.Address(
        city='Stiedemanncester',
        country='Sierra Leone',
        county_province='quia',
        line_1='quia',
        line_2='nostrum',
        line_3='omnis',
        postcode='16786-5804',
    ),
)

res = s.unit.unit_create(req, operations.UnitCreateSecurity(
    pmo_auth2_authentication="",
))

if res.unit is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.UnitInput](../../models/shared/unitinput.md)                           | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `security`                                                                     | [operations.UnitCreateSecurity](../../models/operations/unitcreatesecurity.md) | :heavy_check_mark:                                                             | The security requirements to use for the request.                              |


### Response

**[operations.UnitCreateResponse](../../models/operations/unitcreateresponse.md)**


## unit_destroy

### Example Usage

```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.UnitDestroyRequest(
    id='0e1084cb-0672-4d1a-9879-eeb9665b85ef',
)

res = s.unit.unit_destroy(req, operations.UnitDestroySecurity(
    pmo_auth2_authentication="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.UnitDestroyRequest](../../models/operations/unitdestroyrequest.md)   | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `security`                                                                       | [operations.UnitDestroySecurity](../../models/operations/unitdestroysecurity.md) | :heavy_check_mark:                                                               | The security requirements to use for the request.                                |


### Response

**[operations.UnitDestroyResponse](../../models/operations/unitdestroyresponse.md)**


## unit_list

### Example Usage

```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.UnitListRequest(
    limit=737279,
    offset=872303,
    ordering='alias',
)

res = s.unit.unit_list(req, operations.UnitListSecurity(
    pmo_auth2_authentication="",
))

if res.paginated_unit_list is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.UnitListRequest](../../models/operations/unitlistrequest.md)   | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `security`                                                                 | [operations.UnitListSecurity](../../models/operations/unitlistsecurity.md) | :heavy_check_mark:                                                         | The security requirements to use for the request.                          |


### Response

**[operations.UnitListResponse](../../models/operations/unitlistresponse.md)**


## unit_partial_update

### Example Usage

```python
import meldapi
from meldapi.models import operations, shared

s = meldapi.MeldAPI()

req = operations.UnitPartialUpdateRequest(
    patched_unit_input=shared.PatchedUnitInput(
        approval_currency_limit='quia',
        current_residents=[
            684126,
            919508,
            34070,
        ],
        maintenance_notes='expedita',
        property_id=885208,
        unit='eos',
        unit_address=shared.Address(
            city='Lawton',
            country='Lithuania',
            county_province='odit',
            line_1='explicabo',
            line_2='corporis',
            line_3='error',
            postcode='29626-3164',
        ),
    ),
    id='f92443da-7ce5-42b8-95c5-37c6454efb0b',
)

res = s.unit.unit_partial_update(req, operations.UnitPartialUpdateSecurity(
    pmo_auth2_authentication="",
))

if res.unit is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UnitPartialUpdateRequest](../../models/operations/unitpartialupdaterequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.UnitPartialUpdateSecurity](../../models/operations/unitpartialupdatesecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.UnitPartialUpdateResponse](../../models/operations/unitpartialupdateresponse.md)**


## unit_retrieve

### Example Usage

```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.UnitRetrieveRequest(
    id='34896c3c-a5ac-4fbe-afd5-707577929177',
)

res = s.unit.unit_retrieve(req, operations.UnitRetrieveSecurity(
    pmo_auth2_authentication="",
))

if res.unit is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.UnitRetrieveRequest](../../models/operations/unitretrieverequest.md)   | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `security`                                                                         | [operations.UnitRetrieveSecurity](../../models/operations/unitretrievesecurity.md) | :heavy_check_mark:                                                                 | The security requirements to use for the request.                                  |


### Response

**[operations.UnitRetrieveResponse](../../models/operations/unitretrieveresponse.md)**


## unit_update

### Example Usage

```python
import meldapi
from meldapi.models import operations, shared

s = meldapi.MeldAPI()

req = operations.UnitUpdateRequest(
    unit_input=shared.UnitInput(
        approval_currency_limit='pariatur',
        current_residents=[
            627735,
            763165,
            401428,
            311486,
        ],
        maintenance_notes='commodi',
        property_id=888616,
        unit='placeat',
        unit_address=shared.Address(
            city='Heidenreichport',
            country='Cote d'Ivoire',
            county_province='modi',
            line_1='ipsa',
            line_2='sint',
            line_3='vero',
            postcode='97193',
        ),
    ),
    id='a2b12eb0-7f11-46db-9954-5fc95fa88970',
)

res = s.unit.unit_update(req, operations.UnitUpdateSecurity(
    pmo_auth2_authentication="",
))

if res.unit is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.UnitUpdateRequest](../../models/operations/unitupdaterequest.md)   | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `security`                                                                     | [operations.UnitUpdateSecurity](../../models/operations/unitupdatesecurity.md) | :heavy_check_mark:                                                             | The security requirements to use for the request.                              |


### Response

**[operations.UnitUpdateResponse](../../models/operations/unitupdateresponse.md)**

