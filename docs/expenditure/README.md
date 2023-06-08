# expenditure

### Available Operations

* [expenditure_list](#expenditure_list)
* [expenditure_retrieve](#expenditure_retrieve)

## expenditure_list

### Example Usage

```python
import meldapi
import dateutil.parser
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.ExpenditureListRequest(
    x_pm_org=449950,
    created_gte=dateutil.parser.isoparse('2022-05-22T05:33:50.280Z'),
    created_interval=dateutil.parser.isoparse('2022-02-05T15:25:35.140Z'),
    created_lte=dateutil.parser.isoparse('2022-10-20T12:36:28.767Z'),
    limit=60225,
    offset=969810,
    ordering='est',
    status=[
        operations.ExpenditureListStatus.HOLD,
        operations.ExpenditureListStatus.APPROVED,
        operations.ExpenditureListStatus.BILLED,
    ],
)

res = s.expenditure.expenditure_list(req, operations.ExpenditureListSecurity(
    pmo_auth2_authentication="",
))

if res.paginated_meld_expenditures_list_view_serializer_list_list is not None:
    # handle response
```

## expenditure_retrieve

### Example Usage

```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.ExpenditureRetrieveRequest(
    x_pm_org=358152,
    id='2c595590-7aff-41a3-a2fa-9467739251aa',
)

res = s.expenditure.expenditure_retrieve(req, operations.ExpenditureRetrieveSecurity(
    pmo_auth2_authentication="",
))

if res.meld_expenditures_list_view_serializer_detail is not None:
    # handle response
```
