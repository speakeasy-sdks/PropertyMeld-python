# floor

### Available Operations

* [floor_list](#floor_list)
* [floor_retrieve](#floor_retrieve)

## floor_list

### Example Usage

```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.FloorListRequest(
    x_pm_org=317202,
    limit=138183,
    offset=778346,
    ordering='sequi',
)

res = s.floor.floor_list(req, operations.FloorListSecurity(
    pmo_auth2_authentication="",
))

if res.paginated_floor_serializer_list_list is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.FloorListRequest](../../models/operations/floorlistrequest.md)   | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `security`                                                                   | [operations.FloorListSecurity](../../models/operations/floorlistsecurity.md) | :heavy_check_mark:                                                           | The security requirements to use for the request.                            |


### Response

**[operations.FloorListResponse](../../models/operations/floorlistresponse.md)**


## floor_retrieve

### Example Usage

```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.FloorRetrieveRequest(
    x_pm_org=949572,
    id='5ad019da-1ffe-478f-897b-0074f15471b5',
)

res = s.floor.floor_retrieve(req, operations.FloorRetrieveSecurity(
    pmo_auth2_authentication="",
))

if res.floor_serializer_detail is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.FloorRetrieveRequest](../../models/operations/floorretrieverequest.md)   | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [operations.FloorRetrieveSecurity](../../models/operations/floorretrievesecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |


### Response

**[operations.FloorRetrieveResponse](../../models/operations/floorretrieveresponse.md)**

