# building

### Available Operations

* [building_list](#building_list)
* [building_retrieve](#building_retrieve)

## building_list

### Example Usage

```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.BuildingListRequest(
    x_pm_org=602763,
    limit=857946,
    offset=544883,
    ordering='illum',
)

res = s.building.building_list(req, operations.BuildingListSecurity(
    pmo_auth2_authentication="",
))

if res.paginated_building_serializer_list_list is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.BuildingListRequest](../../models/operations/buildinglistrequest.md)   | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `security`                                                                         | [operations.BuildingListSecurity](../../models/operations/buildinglistsecurity.md) | :heavy_check_mark:                                                                 | The security requirements to use for the request.                                  |


### Response

**[operations.BuildingListResponse](../../models/operations/buildinglistresponse.md)**


## building_retrieve

### Example Usage

```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.BuildingRetrieveRequest(
    x_pm_org=423655,
    id='9a674e0f-467c-4c87-96ed-151a05dfc2dd',
)

res = s.building.building_retrieve(req, operations.BuildingRetrieveSecurity(
    pmo_auth2_authentication="",
))

if res.building_serializer_detail is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.BuildingRetrieveRequest](../../models/operations/buildingretrieverequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.BuildingRetrieveSecurity](../../models/operations/buildingretrievesecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.BuildingRetrieveResponse](../../models/operations/buildingretrieveresponse.md)**

