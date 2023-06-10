# work_log

### Available Operations

* [work_log_list](#work_log_list)
* [work_log_retrieve](#work_log_retrieve)

## work_log_list

### Example Usage

```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.WorkLogListRequest(
    x_pm_org=491201,
    limit=729828,
    offset=72350,
    ordering='ab',
)

res = s.work_log.work_log_list(req, operations.WorkLogListSecurity(
    pmo_auth2_authentication="",
))

if res.paginated_work_entry_serializer_list_list is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.WorkLogListRequest](../../models/operations/workloglistrequest.md)   | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `security`                                                                       | [operations.WorkLogListSecurity](../../models/operations/workloglistsecurity.md) | :heavy_check_mark:                                                               | The security requirements to use for the request.                                |


### Response

**[operations.WorkLogListResponse](../../models/operations/workloglistresponse.md)**


## work_log_retrieve

### Example Usage

```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.WorkLogRetrieveRequest(
    x_pm_org=280114,
    id='eeb52ff7-85fc-4378-94d4-c98e0c2bb89e',
)

res = s.work_log.work_log_retrieve(req, operations.WorkLogRetrieveSecurity(
    pmo_auth2_authentication="",
))

if res.work_entry_serializer_detail is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.WorkLogRetrieveRequest](../../models/operations/worklogretrieverequest.md)   | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.WorkLogRetrieveSecurity](../../models/operations/worklogretrievesecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |


### Response

**[operations.WorkLogRetrieveResponse](../../models/operations/worklogretrieveresponse.md)**

