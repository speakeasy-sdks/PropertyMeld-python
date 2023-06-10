# property_group

### Available Operations

* [property_group_list](#property_group_list)
* [property_group_retrieve](#property_group_retrieve)

## property_group_list

### Example Usage

```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.PropertyGroupListRequest(
    x_pm_org=888044,
    limit=505866,
    offset=708609,
    ordering='quaerat',
)

res = s.property_group.property_group_list(req, operations.PropertyGroupListSecurity(
    pmo_auth2_authentication="",
))

if res.paginated_property_group_serializer_list_list is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.PropertyGroupListRequest](../../models/operations/propertygrouplistrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.PropertyGroupListSecurity](../../models/operations/propertygrouplistsecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.PropertyGroupListResponse](../../models/operations/propertygrouplistresponse.md)**


## property_group_retrieve

### Example Usage

```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.PropertyGroupRetrieveRequest(
    x_pm_org=277773,
    id='5e80ca55-efd2-40e4-97e1-858b6a89fbe3',
)

res = s.property_group.property_group_retrieve(req, operations.PropertyGroupRetrieveSecurity(
    pmo_auth2_authentication="",
))

if res.property_group_serializer_detail is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PropertyGroupRetrieveRequest](../../models/operations/propertygroupretrieverequest.md)   | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.PropertyGroupRetrieveSecurity](../../models/operations/propertygroupretrievesecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |


### Response

**[operations.PropertyGroupRetrieveResponse](../../models/operations/propertygroupretrieveresponse.md)**

