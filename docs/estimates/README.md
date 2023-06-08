# estimates

### Available Operations

* [estimates_list](#estimates_list)
* [estimates_retrieve](#estimates_retrieve)

## estimates_list

### Example Usage

```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.EstimatesListRequest(
    x_pm_org=978619,
    estimate_status=[
        operations.EstimatesListEstimateStatus.ESTIMATE_SUBMITTED,
        operations.EstimatesListEstimateStatus.ESTIMATE_SUBMITTED,
    ],
    limit=461479,
    offset=520478,
    ordering='porro',
)

res = s.estimates.estimates_list(req, operations.EstimatesListSecurity(
    pmo_auth2_authentication="",
))

if res.paginated_estimate_serializer_list_list is not None:
    # handle response
```

## estimates_retrieve

### Example Usage

```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.EstimatesRetrieveRequest(
    x_pm_org=678880,
    id='1ba928fc-8167-442c-b739-205929396fea',
)

res = s.estimates.estimates_retrieve(req, operations.EstimatesRetrieveSecurity(
    pmo_auth2_authentication="",
))

if res.estimate_serializer_detail is not None:
    # handle response
```
