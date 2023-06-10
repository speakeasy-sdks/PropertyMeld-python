# invoice

### Available Operations

* [invoice_attachment_retrieve](#invoice_attachment_retrieve)
* [invoice_list](#invoice_list)
* [invoice_retrieve](#invoice_retrieve)

## invoice_attachment_retrieve

### Example Usage

```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.InvoiceAttachmentRetrieveRequest(
    id='e6e13b99-d488-4e1e-91e4-50ad2abd4426',
)

res = s.invoice.invoice_attachment_retrieve(req, operations.InvoiceAttachmentRetrieveSecurity(
    pmo_auth2_authentication="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.InvoiceAttachmentRetrieveRequest](../../models/operations/invoiceattachmentretrieverequest.md)   | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `security`                                                                                                   | [operations.InvoiceAttachmentRetrieveSecurity](../../models/operations/invoiceattachmentretrievesecurity.md) | :heavy_check_mark:                                                                                           | The security requirements to use for the request.                                                            |


### Response

**[operations.InvoiceAttachmentRetrieveResponse](../../models/operations/invoiceattachmentretrieveresponse.md)**


## invoice_list

### Example Usage

```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.InvoiceListRequest(
    x_pm_org=586513,
    created_gte='quos',
    created_interval='perferendis',
    created_lte='magni',
    declined=operations.InvoiceListDeclined.FALSE,
    limit=369808,
    offset=4695,
    ordering='fugit',
    paid=operations.InvoiceListPaid.TRUE,
    payment_requested_gte='excepturi',
    payment_requested_interval='tempora',
    payment_requested_lte='facilis',
    status=operations.InvoiceListStatus.APPROVED,
    vendor='labore',
    vendors='delectus',
)

res = s.invoice.invoice_list(req, operations.InvoiceListSecurity(
    pmo_auth2_authentication="",
))

if res.paginated_meld_invoice_serializer_list_list is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.InvoiceListRequest](../../models/operations/invoicelistrequest.md)   | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `security`                                                                       | [operations.InvoiceListSecurity](../../models/operations/invoicelistsecurity.md) | :heavy_check_mark:                                                               | The security requirements to use for the request.                                |


### Response

**[operations.InvoiceListResponse](../../models/operations/invoicelistresponse.md)**


## invoice_retrieve

### Example Usage

```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.InvoiceRetrieveRequest(
    x_pm_org=433288,
    id='3c969e9a-3efa-477d-bb14-cd66ae395efb',
)

res = s.invoice.invoice_retrieve(req, operations.InvoiceRetrieveSecurity(
    pmo_auth2_authentication="",
))

if res.meld_invoice_serializer_detail is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.InvoiceRetrieveRequest](../../models/operations/invoiceretrieverequest.md)   | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.InvoiceRetrieveSecurity](../../models/operations/invoiceretrievesecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |


### Response

**[operations.InvoiceRetrieveResponse](../../models/operations/invoiceretrieveresponse.md)**

