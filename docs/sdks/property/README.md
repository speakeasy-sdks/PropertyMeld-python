# property

### Available Operations

* [property_create](#property_create)
* [property_destroy](#property_destroy)
* [property_list](#property_list)
* [property_partial_update](#property_partial_update)
* [property_retrieve](#property_retrieve)
* [property_update](#property_update)

## property_create

### Example Usage

```python
import meldapi
from meldapi.models import operations, shared

s = meldapi.MeldAPI()

req = shared.PropertyInput(
    city='Destineecester',
    country='Svalbard & Jan Mayen Islands',
    county_province='soluta',
    line_1='accusantium',
    line_2='aliquam',
    line_3='sapiente',
    maintenance_notes='dicta',
    other_address_details='ullam',
    owners=[
        356707,
        391774,
    ],
    postcode='51845',
    property_groups=[
        680270,
        99615,
        609178,
        945302,
    ],
    property_name='quasi',
    units=[
        92027,
        454162,
        55965,
        326701,
    ],
)

res = s.property.property_create(req, operations.PropertyCreateSecurity(
    pmo_auth2_authentication="",
))

if res.property is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [shared.PropertyInput](../../models/shared/propertyinput.md)                           | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.PropertyCreateSecurity](../../models/operations/propertycreatesecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.PropertyCreateResponse](../../models/operations/propertycreateresponse.md)**


## property_destroy

### Example Usage

```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.PropertyDestroyRequest(
    id='1339d080-86a1-4840-b94c-26071f93f5f0',
)

res = s.property.property_destroy(req, operations.PropertyDestroySecurity(
    pmo_auth2_authentication="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PropertyDestroyRequest](../../models/operations/propertydestroyrequest.md)   | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.PropertyDestroySecurity](../../models/operations/propertydestroysecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |


### Response

**[operations.PropertyDestroyResponse](../../models/operations/propertydestroyresponse.md)**


## property_list

### Example Usage

```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.PropertyListRequest(
    limit=409054,
    offset=310067,
    ordering='consequuntur',
)

res = s.property.property_list(req, operations.PropertyListSecurity(
    pmo_auth2_authentication="",
))

if res.paginated_property_list is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.PropertyListRequest](../../models/operations/propertylistrequest.md)   | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `security`                                                                         | [operations.PropertyListSecurity](../../models/operations/propertylistsecurity.md) | :heavy_check_mark:                                                                 | The security requirements to use for the request.                                  |


### Response

**[operations.PropertyListResponse](../../models/operations/propertylistresponse.md)**


## property_partial_update

### Example Usage

```python
import meldapi
from meldapi.models import operations, shared

s = meldapi.MeldAPI()

req = operations.PropertyPartialUpdateRequest(
    patched_property_input=shared.PatchedPropertyInput(
        city='Oklahoma City',
        country='Singapore',
        county_province='dignissimos',
        line_1='officia',
        line_2='asperiores',
        line_3='nemo',
        maintenance_notes='quae',
        other_address_details='quaerat',
        owners=[
            801836,
            288398,
            70447,
            241418,
        ],
        postcode='63266-9584',
        property_groups=[
            554688,
            427834,
        ],
        property_name='labore',
        units=[
            706575,
            738227,
            414857,
            447144,
        ],
    ),
    id='5fd5e60b-375e-4d4f-afbe-e41f33317fe3',
)

res = s.property.property_partial_update(req, operations.PropertyPartialUpdateSecurity(
    pmo_auth2_authentication="",
))

if res.property is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PropertyPartialUpdateRequest](../../models/operations/propertypartialupdaterequest.md)   | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.PropertyPartialUpdateSecurity](../../models/operations/propertypartialupdatesecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |


### Response

**[operations.PropertyPartialUpdateResponse](../../models/operations/propertypartialupdateresponse.md)**


## property_retrieve

### Example Usage

```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.PropertyRetrieveRequest(
    id='5b60eb1e-a426-4555-ba3c-28744ed53b88',
)

res = s.property.property_retrieve(req, operations.PropertyRetrieveSecurity(
    pmo_auth2_authentication="",
))

if res.property is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PropertyRetrieveRequest](../../models/operations/propertyretrieverequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.PropertyRetrieveSecurity](../../models/operations/propertyretrievesecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.PropertyRetrieveResponse](../../models/operations/propertyretrieveresponse.md)**


## property_update

### Example Usage

```python
import meldapi
from meldapi.models import operations, shared

s = meldapi.MeldAPI()

req = operations.PropertyUpdateRequest(
    property_input=shared.PropertyInput(
        city='Compton',
        country='New Caledonia',
        county_province='corrupti',
        line_1='pariatur',
        line_2='totam',
        line_3='hic',
        maintenance_notes='exercitationem',
        other_address_details='nobis',
        owners=[
            699575,
        ],
        postcode='91974',
        property_groups=[
            70869,
            611749,
            292794,
        ],
        property_name='laborum',
        units=[
            447516,
        ],
    ),
    id='6b26916f-e1f0-48f4-a94e-3698f447f603',
)

res = s.property.property_update(req, operations.PropertyUpdateSecurity(
    pmo_auth2_authentication="",
))

if res.property is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.PropertyUpdateRequest](../../models/operations/propertyupdaterequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.PropertyUpdateSecurity](../../models/operations/propertyupdatesecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.PropertyUpdateResponse](../../models/operations/propertyupdateresponse.md)**

