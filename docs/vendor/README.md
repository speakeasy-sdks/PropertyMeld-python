# vendor

### Available Operations

* [vendor_destroy](#vendor_destroy)
* [vendor_list](#vendor_list)
* [vendor_retrieve](#vendor_retrieve)

## vendor_destroy

### Example Usage

```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.VendorDestroyRequest(
    id='e189dbb3-0fcb-433e-a055-b197cd44e2f5',
)

res = s.vendor.vendor_destroy(req, operations.VendorDestroySecurity(
    pmo_auth2_authentication="",
))

if res.status_code == 200:
    # handle response
```

## vendor_list

### Example Usage

```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.VendorListRequest(
    x_pm_org=164532,
    limit=813880,
    offset=512905,
    ordering='odit',
)

res = s.vendor.vendor_list(req, operations.VendorListSecurity(
    pmo_auth2_authentication="",
))

if res.paginated_vendor_list is not None:
    # handle response
```

## vendor_retrieve

### Example Usage

```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.VendorRetrieveRequest(
    id='d3513bb6-f48b-4656-bcdb-35ff2e4b2753',
)

res = s.vendor.vendor_retrieve(req, operations.VendorRetrieveSecurity(
    pmo_auth2_authentication="",
))

if res.vendor is not None:
    # handle response
```
