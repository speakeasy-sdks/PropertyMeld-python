# ping

### Available Operations

* [ping_retrieve](#ping_retrieve) - Used to double check that the api is up an running.

## ping_retrieve

Used to double check that the api is up an running.

### Example Usage

```python
import meldapi


s = meldapi.MeldAPI()


res = s.ping.ping_retrieve()

if res.ping_retrieve_200_application_json_object is not None:
    # handle response
```


### Response

**[operations.PingRetrieveResponse](../../models/operations/pingretrieveresponse.md)**

