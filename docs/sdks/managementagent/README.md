# management_agent

### Available Operations

* [management_agent_list](#management_agent_list)
* [management_agent_retrieve](#management_agent_retrieve)

## management_agent_list

### Example Usage

```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.ManagementAgentListRequest(
    x_pm_org=588465,
    limit=725255,
    offset=659669,
    ordering='blanditiis',
)

res = s.management_agent.management_agent_list(req, operations.ManagementAgentListSecurity(
    pmo_auth2_authentication="",
))

if res.paginated_management_agent_serializer_list_list is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ManagementAgentListRequest](../../models/operations/managementagentlistrequest.md)   | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `security`                                                                                       | [operations.ManagementAgentListSecurity](../../models/operations/managementagentlistsecurity.md) | :heavy_check_mark:                                                                               | The security requirements to use for the request.                                                |


### Response

**[operations.ManagementAgentListResponse](../../models/operations/managementagentlistresponse.md)**


## management_agent_retrieve

### Example Usage

```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.ManagementAgentRetrieveRequest(
    x_pm_org=533206,
    id='f3a66997-074b-4a44-a9b6-e2141959890a',
)

res = s.management_agent.management_agent_retrieve(req, operations.ManagementAgentRetrieveSecurity(
    pmo_auth2_authentication="",
))

if res.management_agent_serializer_detail is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.ManagementAgentRetrieveRequest](../../models/operations/managementagentretrieverequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.ManagementAgentRetrieveSecurity](../../models/operations/managementagentretrievesecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.ManagementAgentRetrieveResponse](../../models/operations/managementagentretrieveresponse.md)**

