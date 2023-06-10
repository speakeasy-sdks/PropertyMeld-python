# MeldAPI

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/PropertyMeld-python.git
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.BuildingListRequest(
    x_pm_org=548814,
    limit=592845,
    offset=715190,
    ordering='quibusdam',
)

res = s.building.building_list(req, operations.BuildingListSecurity(
    pmo_auth2_authentication="",
))

if res.paginated_building_serializer_list_list is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [building](docs/sdks/building/README.md)

* [building_list](docs/sdks/building/README.md#building_list)
* [building_retrieve](docs/sdks/building/README.md#building_retrieve)

### [check_token](docs/sdks/checktoken/README.md)

* [check_token_retrieve](docs/sdks/checktoken/README.md#check_token_retrieve) - Used to check the validity of an oauth2 token

### [estimates](docs/sdks/estimates/README.md)

* [estimates_list](docs/sdks/estimates/README.md#estimates_list)
* [estimates_retrieve](docs/sdks/estimates/README.md#estimates_retrieve)

### [expenditure](docs/sdks/expenditure/README.md)

* [expenditure_list](docs/sdks/expenditure/README.md#expenditure_list)
* [expenditure_retrieve](docs/sdks/expenditure/README.md#expenditure_retrieve)

### [floor](docs/sdks/floor/README.md)

* [floor_list](docs/sdks/floor/README.md#floor_list)
* [floor_retrieve](docs/sdks/floor/README.md#floor_retrieve)

### [invoice](docs/sdks/invoice/README.md)

* [invoice_attachment_retrieve](docs/sdks/invoice/README.md#invoice_attachment_retrieve)
* [invoice_list](docs/sdks/invoice/README.md#invoice_list)
* [invoice_retrieve](docs/sdks/invoice/README.md#invoice_retrieve)

### [management_agent](docs/sdks/managementagent/README.md)

* [management_agent_list](docs/sdks/managementagent/README.md#management_agent_list)
* [management_agent_retrieve](docs/sdks/managementagent/README.md#management_agent_retrieve)

### [manager_file](docs/sdks/managerfile/README.md)

* [manager_file_list](docs/sdks/managerfile/README.md#manager_file_list)

### [meld](docs/sdks/meld/README.md)

* [meld_list](docs/sdks/meld/README.md#meld_list)
* [meld_manager_files_list](docs/sdks/meld/README.md#meld_manager_files_list)
* [meld_retrieve](docs/sdks/meld/README.md#meld_retrieve)
* [meld_tenant_files_list](docs/sdks/meld/README.md#meld_tenant_files_list)
* [meld_vendor_files_list](docs/sdks/meld/README.md#meld_vendor_files_list)

### [owner](docs/sdks/owner/README.md)

* [owner_create](docs/sdks/owner/README.md#owner_create)
* [owner_destroy](docs/sdks/owner/README.md#owner_destroy)
* [owner_list](docs/sdks/owner/README.md#owner_list)
* [owner_partial_update](docs/sdks/owner/README.md#owner_partial_update)
* [owner_retrieve](docs/sdks/owner/README.md#owner_retrieve)
* [owner_update](docs/sdks/owner/README.md#owner_update)

### [ping](docs/sdks/ping/README.md)

* [ping_retrieve](docs/sdks/ping/README.md#ping_retrieve) - Used to double check that the api is up an running.

### [project](docs/sdks/project/README.md)

* [project_list](docs/sdks/project/README.md#project_list)
* [project_retrieve](docs/sdks/project/README.md#project_retrieve)

### [property](docs/sdks/property/README.md)

* [property_create](docs/sdks/property/README.md#property_create)
* [property_destroy](docs/sdks/property/README.md#property_destroy)
* [property_list](docs/sdks/property/README.md#property_list)
* [property_partial_update](docs/sdks/property/README.md#property_partial_update)
* [property_retrieve](docs/sdks/property/README.md#property_retrieve)
* [property_update](docs/sdks/property/README.md#property_update)

### [property_group](docs/sdks/propertygroup/README.md)

* [property_group_list](docs/sdks/propertygroup/README.md#property_group_list)
* [property_group_retrieve](docs/sdks/propertygroup/README.md#property_group_retrieve)

### [resident](docs/sdks/resident/README.md)

* [resident_create_form](docs/sdks/resident/README.md#resident_create_form)
* [resident_create_json](docs/sdks/resident/README.md#resident_create_json)
* [resident_create_multipart](docs/sdks/resident/README.md#resident_create_multipart)
* [resident_destroy](docs/sdks/resident/README.md#resident_destroy)
* [resident_list](docs/sdks/resident/README.md#resident_list)
* [resident_partial_update_form](docs/sdks/resident/README.md#resident_partial_update_form)
* [resident_partial_update_json](docs/sdks/resident/README.md#resident_partial_update_json)
* [resident_partial_update_multipart](docs/sdks/resident/README.md#resident_partial_update_multipart)
* [resident_retrieve](docs/sdks/resident/README.md#resident_retrieve)
* [resident_update_form](docs/sdks/resident/README.md#resident_update_form)
* [resident_update_json](docs/sdks/resident/README.md#resident_update_json)
* [resident_update_multipart](docs/sdks/resident/README.md#resident_update_multipart)

### [resident_file](docs/sdks/residentfile/README.md)

* [resident_file_list](docs/sdks/residentfile/README.md#resident_file_list)

### [schema](docs/sdks/schema/README.md)

* [schema_retrieve](docs/sdks/schema/README.md#schema_retrieve) - OpenApi3 schema for this API. Format can be selected via content negotiation.

- YAML: application/vnd.oai.openapi
- JSON: application/vnd.oai.openapi+json

### [unit](docs/sdks/unit/README.md)

* [unit_create](docs/sdks/unit/README.md#unit_create)
* [unit_destroy](docs/sdks/unit/README.md#unit_destroy)
* [unit_list](docs/sdks/unit/README.md#unit_list)
* [unit_partial_update](docs/sdks/unit/README.md#unit_partial_update)
* [unit_retrieve](docs/sdks/unit/README.md#unit_retrieve)
* [unit_update](docs/sdks/unit/README.md#unit_update)

### [vendor](docs/sdks/vendor/README.md)

* [vendor_destroy](docs/sdks/vendor/README.md#vendor_destroy)
* [vendor_list](docs/sdks/vendor/README.md#vendor_list)
* [vendor_retrieve](docs/sdks/vendor/README.md#vendor_retrieve)

### [vendor_file](docs/sdks/vendorfile/README.md)

* [vendor_file_list](docs/sdks/vendorfile/README.md#vendor_file_list)

### [vendor_invite](docs/sdks/vendorinvite/README.md)

* [vendor_invite_create](docs/sdks/vendorinvite/README.md#vendor_invite_create)

### [work_log](docs/sdks/worklog/README.md)

* [work_log_list](docs/sdks/worklog/README.md#work_log_list)
* [work_log_retrieve](docs/sdks/worklog/README.md#work_log_retrieve)
<!-- End SDK Available Operations -->

### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
