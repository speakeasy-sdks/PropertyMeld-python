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
