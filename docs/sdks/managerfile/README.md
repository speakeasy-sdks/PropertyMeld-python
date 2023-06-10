# manager_file

### Available Operations

* [manager_file_list](#manager_file_list)

## manager_file_list

### Example Usage

```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.ManagerFileListRequest(
    x_pm_org=968962,
    limit=652103,
    offset=320997,
    ordering='eum',
)

res = s.manager_file.manager_file_list(req, operations.ManagerFileListSecurity(
    pmo_auth2_authentication="",
))

if res.paginated_meld_file_list is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ManagerFileListRequest](../../models/operations/managerfilelistrequest.md)   | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.ManagerFileListSecurity](../../models/operations/managerfilelistsecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |


### Response

**[operations.ManagerFileListResponse](../../models/operations/managerfilelistresponse.md)**

