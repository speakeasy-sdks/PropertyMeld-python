# meld

### Available Operations

* [meld_list](#meld_list)
* [meld_manager_files_list](#meld_manager_files_list)
* [meld_retrieve](#meld_retrieve)
* [meld_tenant_files_list](#meld_tenant_files_list)
* [meld_vendor_files_list](#meld_vendor_files_list)

## meld_list

### Example Usage

```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.MeldListRequest(
    x_pm_org=221262,
    ack_approval=operations.MeldListAckApproval.FALSE,
    assigned_to_me='odit',
    categories=operations.MeldListCategories.GENERAL,
    comments_gte='quasi',
    comments_lte='iure',
    completed_gte='doloribus',
    completed_interval='debitis',
    completed_lte='eius',
    created_gte='maxime',
    created_interval='deleniti',
    created_lte='facilis',
    created_offset_lte='in',
    due_date_choice=operations.MeldListDueDateChoice.OVERDUE,
    due_date_gte='architecto',
    due_date_lte='repudiandae',
    ever_been_assigned=operations.MeldListEverBeenAssigned.TRUE,
    exp=operations.MeldListExp.FALSE,
    exp_s='nihil',
    files_gte='repellat',
    files_lte='quibusdam',
    has_estimates=operations.MeldListHasEstimates.FALSE,
    invoice_s='saepe',
    limit=868126,
    maint='accusantium',
    maint_type=operations.MeldListMaintType.ONE,
    marked_complete_gte='praesentium',
    marked_complete_interval='natus',
    marked_complete_lte='magni',
    meldinvoice=operations.MeldListMeldinvoice.TRUE,
    offset=779051,
    order_by=operations.MeldListOrderBy.MINUS_OWNER_APPROVAL_REQUEST_DATE,
    owner_approval=operations.MeldListOwnerApproval.OWNER_APPROVAL_REQUESTED_ESTIMATES,
    pg='maxime',
    priority=operations.MeldListPriority.MEDIUM,
    project='excepturi',
    project_assigned=operations.MeldListProjectAssigned.TRUE,
    prop='ea',
    rating=operations.MeldListRating.ONE,
    recurring=operations.MeldListRecurring.TRUE,
    recurring_meld='maiores',
    remindees='quidem',
    reminder_choice=operations.MeldListReminderChoice.TODAY,
    reminder_gte='voluptate',
    reminder_lte='autem',
    scheduled_gte='nam',
    scheduled_interval='eaque',
    scheduled_lte='pariatur',
    scheduling='nemo',
    status=operations.MeldListStatus.PENDING_ASSIGNMENT,
    tags='perferendis',
    tags_ex='fugiat',
    tpr=operations.MeldListTpr.FALSE,
    unit='aut',
    updated_gte='cumque',
    updated_interval='corporis',
    updated_lte='hic',
    updated_offset_lte='libero',
    vendor_scheduled_gte='nobis',
    vendor_scheduled_interval='dolores',
    vendor_scheduled_lte='quis',
    wl_gte='totam',
    wl_lte='dignissimos',
)

res = s.meld.meld_list(req, operations.MeldListSecurity(
    pmo_auth2_authentication="",
))

if res.paginated_meld_serializer_list_list is not None:
    # handle response
```

## meld_manager_files_list

### Example Usage

```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.MeldManagerFilesListRequest(
    x_pm_org=54338,
    id='53202c73-d5fe-49b9-8c28-909b3fe49a8d',
    limit=589910,
    offset=750844,
    ordering='libero',
)

res = s.meld.meld_manager_files_list(req, operations.MeldManagerFilesListSecurity(
    pmo_auth2_authentication="",
))

if res.paginated_pm_api_meldfile_list is not None:
    # handle response
```

## meld_retrieve

### Example Usage

```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.MeldRetrieveRequest(
    x_pm_org=964490,
    id='48633323-f9b7-47f3-a410-0674ebf69280',
)

res = s.meld.meld_retrieve(req, operations.MeldRetrieveSecurity(
    pmo_auth2_authentication="",
))

if res.meld_serializer_detail is not None:
    # handle response
```

## meld_tenant_files_list

### Example Usage

```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.MeldTenantFilesListRequest(
    x_pm_org=854614,
    id='1ba77a89-ebf7-437a-a420-3ce5e6a95d8a',
    limit=55,
    offset=872651,
    ordering='quaerat',
)

res = s.meld.meld_tenant_files_list(req, operations.MeldTenantFilesListSecurity(
    pmo_auth2_authentication="",
))

if res.paginated_pm_api_tenant_meld_list is not None:
    # handle response
```

## meld_vendor_files_list

### Example Usage

```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.MeldVendorFilesListRequest(
    x_pm_org=273542,
    id='6ce2af7a-73cf-43be-853f-870b326b5a73',
    limit=277628,
    offset=186458,
    ordering='cupiditate',
)

res = s.meld.meld_vendor_files_list(req, operations.MeldVendorFilesListSecurity(
    pmo_auth2_authentication="",
))

if res.paginated_pm_api_vendor_meld_file_list is not None:
    # handle response
```
