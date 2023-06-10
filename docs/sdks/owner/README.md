# owner

### Available Operations

* [owner_create](#owner_create)
* [owner_destroy](#owner_destroy)
* [owner_list](#owner_list)
* [owner_partial_update](#owner_partial_update)
* [owner_retrieve](#owner_retrieve)
* [owner_update](#owner_update)

## owner_create

### Example Usage

```python
import meldapi
from meldapi.models import operations, shared

s = meldapi.MeldAPI()

req = shared.OwnerInput(
    address=shared.Address(
        city='State College',
        country='Saint Helena',
        county_province='dicta',
        line_1='laborum',
        line_2='totam',
        line_3='incidunt',
        postcode='17734',
    ),
    contact=shared.Contact(
        business_phone='molestias',
        business_phone_ext='temporibus',
        cell_phone='qui',
        cell_phone_ext='neque',
        fax='fugit',
        home_phone='magni',
        home_phone_ext='odio',
        primary_email='Fiona.Reichert76@gmail.com',
        secondary_email='Nella.Bosco8@hotmail.com',
        tertiary_email='Katrine.Reynolds@hotmail.com',
    ),
    email='Corene24@hotmail.com',
    first_name='Marianne',
    hub_access_level=shared.HubAccessLevelEnum.DIRECT_ONLY,
    invited_to_hub=False,
    last_name='Berge',
    properties=[
        555649,
    ],
)

res = s.owner.owner_create(req, operations.OwnerCreateSecurity(
    pmo_auth2_authentication="",
))

if res.owner is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [shared.OwnerInput](../../models/shared/ownerinput.md)                           | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `security`                                                                       | [operations.OwnerCreateSecurity](../../models/operations/ownercreatesecurity.md) | :heavy_check_mark:                                                               | The security requirements to use for the request.                                |


### Response

**[operations.OwnerCreateResponse](../../models/operations/ownercreateresponse.md)**


## owner_destroy

### Example Usage

```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.OwnerDestroyRequest(
    id='e0adcf4b-9218-479f-8e95-3f73ef7fbc7a',
)

res = s.owner.owner_destroy(req, operations.OwnerDestroySecurity(
    pmo_auth2_authentication="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.OwnerDestroyRequest](../../models/operations/ownerdestroyrequest.md)   | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `security`                                                                         | [operations.OwnerDestroySecurity](../../models/operations/ownerdestroysecurity.md) | :heavy_check_mark:                                                                 | The security requirements to use for the request.                                  |


### Response

**[operations.OwnerDestroyResponse](../../models/operations/ownerdestroyresponse.md)**


## owner_list

### Example Usage

```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.OwnerListRequest(
    limit=708548,
    offset=874288,
    ordering='ducimus',
)

res = s.owner.owner_list(req, operations.OwnerListSecurity(
    pmo_auth2_authentication="",
))

if res.paginated_owner_list is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.OwnerListRequest](../../models/operations/ownerlistrequest.md)   | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `security`                                                                   | [operations.OwnerListSecurity](../../models/operations/ownerlistsecurity.md) | :heavy_check_mark:                                                           | The security requirements to use for the request.                            |


### Response

**[operations.OwnerListResponse](../../models/operations/ownerlistresponse.md)**


## owner_partial_update

### Example Usage

```python
import meldapi
from meldapi.models import operations, shared

s = meldapi.MeldAPI()

req = operations.OwnerPartialUpdateRequest(
    patched_owner_input=shared.PatchedOwnerInput(
        address=shared.Address(
            city='Port Rosina',
            country='Comoros',
            county_province='natus',
            line_1='impedit',
            line_2='aut',
            line_3='voluptatibus',
            postcode='81799',
        ),
        contact=shared.Contact(
            business_phone='iusto',
            business_phone_ext='eligendi',
            cell_phone='ducimus',
            cell_phone_ext='alias',
            fax='officia',
            home_phone='tempora',
            home_phone_ext='ipsam',
            primary_email='Brielle.Keebler18@yahoo.com',
            secondary_email='Johnpaul98@yahoo.com',
            tertiary_email='Gustave_Stoltenberg@gmail.com',
        ),
        email='Victor.Schamberger77@yahoo.com',
        first_name='Flossie',
        hub_access_level=shared.HubAccessLevelEnum.ALL_NOTIFICATIONS,
        invited_to_hub=False,
        last_name='Jacobi',
        properties=[
            301831,
        ],
    ),
    id='6c3e250f-b008-4c42-a141-aac366c8dd6b',
)

res = s.owner.owner_partial_update(req, operations.OwnerPartialUpdateSecurity(
    pmo_auth2_authentication="",
))

if res.owner is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.OwnerPartialUpdateRequest](../../models/operations/ownerpartialupdaterequest.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.OwnerPartialUpdateSecurity](../../models/operations/ownerpartialupdatesecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |


### Response

**[operations.OwnerPartialUpdateResponse](../../models/operations/ownerpartialupdateresponse.md)**


## owner_retrieve

### Example Usage

```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.OwnerRetrieveRequest(
    id='14429074-7477-48a7-bd46-6d28c10ab3cd',
)

res = s.owner.owner_retrieve(req, operations.OwnerRetrieveSecurity(
    pmo_auth2_authentication="",
))

if res.owner is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.OwnerRetrieveRequest](../../models/operations/ownerretrieverequest.md)   | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [operations.OwnerRetrieveSecurity](../../models/operations/ownerretrievesecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |


### Response

**[operations.OwnerRetrieveResponse](../../models/operations/ownerretrieveresponse.md)**


## owner_update

### Example Usage

```python
import meldapi
from meldapi.models import operations, shared

s = meldapi.MeldAPI()

req = operations.OwnerUpdateRequest(
    owner_input=shared.OwnerInput(
        address=shared.Address(
            city='Parkerburgh',
            country='China',
            county_province='voluptas',
            line_1='ab',
            line_2='cupiditate',
            line_3='consequatur',
            postcode='83117',
        ),
        contact=shared.Contact(
            business_phone='esse',
            business_phone_ext='recusandae',
            cell_phone='aperiam',
            cell_phone_ext='distinctio',
            fax='quod',
            home_phone='dignissimos',
            home_phone_ext='inventore',
            primary_email='Josiah48@yahoo.com',
            secondary_email='Harvey64@yahoo.com',
            tertiary_email='Alfonzo_Sawayn@yahoo.com',
        ),
        email='Carol68@yahoo.com',
        first_name='Lysanne',
        hub_access_level=shared.HubAccessLevelEnum.ALL_NOTIFICATIONS,
        invited_to_hub=False,
        last_name='Lindgren',
        properties=[
            325685,
        ],
    ),
    id='62f222e9-817e-4e17-8be6-1e6b7b95bc0a',
)

res = s.owner.owner_update(req, operations.OwnerUpdateSecurity(
    pmo_auth2_authentication="",
))

if res.owner is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.OwnerUpdateRequest](../../models/operations/ownerupdaterequest.md)   | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `security`                                                                       | [operations.OwnerUpdateSecurity](../../models/operations/ownerupdatesecurity.md) | :heavy_check_mark:                                                               | The security requirements to use for the request.                                |


### Response

**[operations.OwnerUpdateResponse](../../models/operations/ownerupdateresponse.md)**

