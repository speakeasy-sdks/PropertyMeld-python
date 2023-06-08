# vendor_file

### Available Operations

* [vendor_file_list](#vendor_file_list)

## vendor_file_list

### Example Usage

```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.VendorFileListRequest(
    x_pm_org=480061,
    limit=664965,
    offset=522176,
    ordering='eligendi',
)

res = s.vendor_file.vendor_file_list(req, operations.VendorFileListSecurity(
    pmo_auth2_authentication="",
))

if res.paginated_vendor_meld_file_list is not None:
    # handle response
```
