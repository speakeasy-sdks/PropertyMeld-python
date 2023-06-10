# vendor_invite

### Available Operations

* [vendor_invite_create](#vendor_invite_create)

## vendor_invite_create

### Example Usage

```python
import meldapi
from meldapi.models import operations, shared

s = meldapi.MeldAPI()

req = operations.VendorInviteCreateRequest(
    vendor_invite=shared.VendorInvite(
        company_name='fugiat',
        company_phone='unde',
        email='Jeromy62@hotmail.com',
        first_name='Owen',
        last_name='Brown',
        line_1='dignissimos',
        postcode='83139',
    ),
    x_pm_org=482584,
)

res = s.vendor_invite.vendor_invite_create(req, operations.VendorInviteCreateSecurity(
    pmo_auth2_authentication="",
))

if res.vendor_invite is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.VendorInviteCreateRequest](../../models/operations/vendorinvitecreaterequest.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.VendorInviteCreateSecurity](../../models/operations/vendorinvitecreatesecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |


### Response

**[operations.VendorInviteCreateResponse](../../models/operations/vendorinvitecreateresponse.md)**

