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
