# check_token

### Available Operations

* [check_token_retrieve](#check_token_retrieve) - Used to check the validity of an oauth2 token

## check_token_retrieve

Used to check the validity of an oauth2 token

### Example Usage

```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()


res = s.check_token.check_token_retrieve(operations.CheckTokenRetrieveSecurity(
    pmo_auth2_authentication="",
))

if res.check_token_retrieve_200_application_json_object is not None:
    # handle response
```
