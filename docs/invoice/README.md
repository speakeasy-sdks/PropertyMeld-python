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
