<!-- Start SDK Example Usage -->
```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.BuildingListRequest(
    x_pm_org=548814,
    limit=592845,
    offset=715190,
    ordering='quibusdam',
)

res = s.building.building_list(req, operations.BuildingListSecurity(
    pmo_auth2_authentication="",
))

if res.paginated_building_serializer_list_list is not None:
    # handle response
```
<!-- End SDK Example Usage -->