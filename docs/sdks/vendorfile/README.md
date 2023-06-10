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

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.VendorFileListRequest](../../models/operations/vendorfilelistrequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.VendorFileListSecurity](../../models/operations/vendorfilelistsecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.VendorFileListResponse](../../models/operations/vendorfilelistresponse.md)**

