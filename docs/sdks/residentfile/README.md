# resident_file

### Available Operations

* [resident_file_list](#resident_file_list)

## resident_file_list

### Example Usage

```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.ResidentFileListRequest(
    x_pm_org=487676,
    limit=144691,
    offset=545,
    ordering='magni',
)

res = s.resident_file.resident_file_list(req, operations.ResidentFileListSecurity(
    pmo_auth2_authentication="",
))

if res.paginated_tenant_meld_file_list is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ResidentFileListRequest](../../models/operations/residentfilelistrequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.ResidentFileListSecurity](../../models/operations/residentfilelistsecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.ResidentFileListResponse](../../models/operations/residentfilelistresponse.md)**

