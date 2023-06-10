# project

### Available Operations

* [project_list](#project_list)
* [project_retrieve](#project_retrieve)

## project_list

### Example Usage

```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.ProjectListRequest(
    x_pm_org=731398,
    limit=240020,
    offset=766964,
    ordering='consequuntur',
)

res = s.project.project_list(req, operations.ProjectListSecurity(
    pmo_auth2_authentication="",
))

if res.paginated_project_list_view_list is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ProjectListRequest](../../models/operations/projectlistrequest.md)   | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `security`                                                                       | [operations.ProjectListSecurity](../../models/operations/projectlistsecurity.md) | :heavy_check_mark:                                                               | The security requirements to use for the request.                                |


### Response

**[operations.ProjectListResponse](../../models/operations/projectlistresponse.md)**


## project_retrieve

### Example Usage

```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.ProjectRetrieveRequest(
    x_pm_org=9766,
    id='c4f3789f-d871-4f99-9d2e-fd121aa6f1e6',
)

res = s.project.project_retrieve(req, operations.ProjectRetrieveSecurity(
    pmo_auth2_authentication="",
))

if res.pm_api_project_detail is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ProjectRetrieveRequest](../../models/operations/projectretrieverequest.md)   | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.ProjectRetrieveSecurity](../../models/operations/projectretrievesecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |


### Response

**[operations.ProjectRetrieveResponse](../../models/operations/projectretrieveresponse.md)**

