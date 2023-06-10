# schema

### Available Operations

* [schema_retrieve](#schema_retrieve) - OpenApi3 schema for this API. Format can be selected via content negotiation.

- YAML: application/vnd.oai.openapi
- JSON: application/vnd.oai.openapi+json

## schema_retrieve

OpenApi3 schema for this API. Format can be selected via content negotiation.

- YAML: application/vnd.oai.openapi
- JSON: application/vnd.oai.openapi+json

### Example Usage

```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.SchemaRetrieveRequest(
    x_pm_org=425402,
    format=operations.SchemaRetrieveFormat.JSON,
)

res = s.schema.schema_retrieve(req, operations.SchemaRetrieveSecurity(
    pmo_auth2_authentication="",
))

if res.schema_retrieve_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.SchemaRetrieveRequest](../../models/operations/schemaretrieverequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.SchemaRetrieveSecurity](../../models/operations/schemaretrievesecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.SchemaRetrieveResponse](../../models/operations/schemaretrieveresponse.md)**

