# resident

### Available Operations

* [resident_create_form](#resident_create_form)
* [resident_create_json](#resident_create_json)
* [resident_create_multipart](#resident_create_multipart)
* [resident_destroy](#resident_destroy)
* [resident_list](#resident_list)
* [resident_partial_update_form](#resident_partial_update_form)
* [resident_partial_update_json](#resident_partial_update_json)
* [resident_partial_update_multipart](#resident_partial_update_multipart)
* [resident_retrieve](#resident_retrieve)
* [resident_update_form](#resident_update_form)
* [resident_update_json](#resident_update_json)
* [resident_update_multipart](#resident_update_multipart)

## resident_create_form

### Example Usage

```python
import meldapi
from meldapi.models import operations, shared

s = meldapi.MeldAPI()

req = shared.ResidentInput1(
    address='dolorum',
    contact=shared.Contact(
        business_phone='nostrum',
        business_phone_ext='officia',
        cell_phone='dolorum',
        cell_phone_ext='corrupti',
        fax='accusamus',
        home_phone='tempora',
        home_phone_ext='atque',
        primary_email='Easter63@gmail.com',
        secondary_email='Elinor.Adams@hotmail.com',
        tertiary_email='Justine.Lynch8@gmail.com',
    ),
    first_name='Jo',
    invite=False,
    last_name='Jaskolski',
    middle_name='sed',
    notes='sit',
    notification_settings=shared.NotificationSettingsInput(
        incoming_meld_frequency=shared.IncomingMeldFrequencyEnum.DAILY,
        sms_notifications=False,
        successful_meld_frequency=shared.SuccessfulMeldFrequencyEnum.DAILY,
        timezone=shared.TimezoneEnum.PACIFIC_GAMBIER,
    ),
    units=[
        8511,
        279068,
        968865,
    ],
)

res = s.resident.resident_create_form(req, operations.ResidentCreateFormSecurity(
    pmo_auth2_authentication="",
))

if res.resident is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [shared.ResidentInput1](../../models/shared/residentinput1.md)                                 | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.ResidentCreateFormSecurity](../../models/operations/residentcreateformsecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |


### Response

**[operations.ResidentCreateFormResponse](../../models/operations/residentcreateformresponse.md)**


## resident_create_json

### Example Usage

```python
import meldapi
from meldapi.models import operations, shared

s = meldapi.MeldAPI()

req = shared.ResidentInput(
    address=shared.ResidentAddress(
        city='Lake Bettie',
        country='Bhutan',
        county_province='occaecati',
        line_1='labore',
        line_2='quidem',
        line_3='atque',
        postcode='79302-6469',
    ),
    contact=shared.Contact(
        business_phone='provident',
        business_phone_ext='repellendus',
        cell_phone='delectus',
        cell_phone_ext='voluptates',
        fax='perferendis',
        home_phone='est',
        home_phone_ext='quidem',
        primary_email='Raquel_Pfannerstill@yahoo.com',
        secondary_email='Alessia.Schiller54@yahoo.com',
        tertiary_email='Yvette_Leannon@yahoo.com',
    ),
    first_name='Rae',
    invite=False,
    last_name='Borer',
    middle_name='esse',
    notes='amet',
    notification_settings=shared.NotificationSettingsInput(
        incoming_meld_frequency=shared.IncomingMeldFrequencyEnum.NEVER,
        sms_notifications=False,
        successful_meld_frequency=shared.SuccessfulMeldFrequencyEnum.DAILY,
        timezone=shared.TimezoneEnum.ASIA_THIMPHU,
    ),
    units=[
        887265,
        886961,
        880107,
    ],
)

res = s.resident.resident_create_json(req, operations.ResidentCreateJSONSecurity(
    pmo_auth2_authentication="",
))

if res.resident is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [shared.ResidentInput](../../models/shared/residentinput.md)                                   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.ResidentCreateJSONSecurity](../../models/operations/residentcreatejsonsecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |


### Response

**[operations.ResidentCreateJSONResponse](../../models/operations/residentcreatejsonresponse.md)**


## resident_create_multipart

### Example Usage

```python
import meldapi
from meldapi.models import operations, shared

s = meldapi.MeldAPI()

req = shared.ResidentInput1(
    address='natus',
    contact=shared.Contact(
        business_phone='minima',
        business_phone_ext='aspernatur',
        cell_phone='ex',
        cell_phone_ext='maiores',
        fax='corrupti',
        home_phone='at',
        home_phone_ext='error',
        primary_email='Genevieve_Walker@yahoo.com',
        secondary_email='Theresia.Parisian96@gmail.com',
        tertiary_email='Tevin10@gmail.com',
    ),
    first_name='Chandler',
    invite=False,
    last_name='Halvorson',
    middle_name='laboriosam',
    notes='velit',
    notification_settings=shared.NotificationSettingsInput(
        incoming_meld_frequency=shared.IncomingMeldFrequencyEnum.NEVER,
        sms_notifications=False,
        successful_meld_frequency=shared.SuccessfulMeldFrequencyEnum.DAILY,
        timezone=shared.TimezoneEnum.AMERICA_PANAMA,
    ),
    units=[
        160467,
        580107,
        886305,
        597937,
    ],
)

res = s.resident.resident_create_multipart(req, operations.ResidentCreateMultipartSecurity(
    pmo_auth2_authentication="",
))

if res.resident is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [shared.ResidentInput1](../../models/shared/residentinput1.md)                                           | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.ResidentCreateMultipartSecurity](../../models/operations/residentcreatemultipartsecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.ResidentCreateMultipartResponse](../../models/operations/residentcreatemultipartresponse.md)**


## resident_destroy

### Example Usage

```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.ResidentDestroyRequest(
    id='73e922a5-7a15-4be3-a060-807e2b6e3ab8',
)

res = s.resident.resident_destroy(req, operations.ResidentDestroySecurity(
    pmo_auth2_authentication="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ResidentDestroyRequest](../../models/operations/residentdestroyrequest.md)   | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.ResidentDestroySecurity](../../models/operations/residentdestroysecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |


### Response

**[operations.ResidentDestroyResponse](../../models/operations/residentdestroyresponse.md)**


## resident_list

### Example Usage

```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.ResidentListRequest(
    limit=523006,
    offset=304446,
    ordering='ad',
)

res = s.resident.resident_list(req, operations.ResidentListSecurity(
    pmo_auth2_authentication="",
))

if res.paginated_resident_list is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.ResidentListRequest](../../models/operations/residentlistrequest.md)   | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `security`                                                                         | [operations.ResidentListSecurity](../../models/operations/residentlistsecurity.md) | :heavy_check_mark:                                                                 | The security requirements to use for the request.                                  |


### Response

**[operations.ResidentListResponse](../../models/operations/residentlistresponse.md)**


## resident_partial_update_form

### Example Usage

```python
import meldapi
from meldapi.models import operations, shared

s = meldapi.MeldAPI()

req = operations.ResidentPartialUpdateFormRequest(
    patched_resident_input1=shared.PatchedResidentInput1(
        address='repellat',
        contact=shared.Contact(
            business_phone='alias',
            business_phone_ext='corporis',
            cell_phone='perspiciatis',
            cell_phone_ext='nihil',
            fax='mollitia',
            home_phone='voluptas',
            home_phone_ext='alias',
            primary_email='Waldo.Daniel@hotmail.com',
            secondary_email='Marilyne92@gmail.com',
            tertiary_email='Elsa.Kreiger@yahoo.com',
        ),
        first_name='Loren',
        invite=False,
        last_name='Ferry',
        middle_name='debitis',
        notes='laudantium',
        notification_settings=shared.NotificationSettingsInput(
            incoming_meld_frequency=shared.IncomingMeldFrequencyEnum.DAILY,
            sms_notifications=False,
            successful_meld_frequency=shared.SuccessfulMeldFrequencyEnum.DAILY,
            timezone=shared.TimezoneEnum.PACIFIC_NIUE,
        ),
        units=[
            592081,
            337477,
        ],
    ),
    id='6f9251a5-a9da-4660-bf57-bfaad4f9efc1',
)

res = s.resident.resident_partial_update_form(req, operations.ResidentPartialUpdateFormSecurity(
    pmo_auth2_authentication="",
))

if res.resident is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.ResidentPartialUpdateFormRequest](../../models/operations/residentpartialupdateformrequest.md)   | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `security`                                                                                                   | [operations.ResidentPartialUpdateFormSecurity](../../models/operations/residentpartialupdateformsecurity.md) | :heavy_check_mark:                                                                                           | The security requirements to use for the request.                                                            |


### Response

**[operations.ResidentPartialUpdateFormResponse](../../models/operations/residentpartialupdateformresponse.md)**


## resident_partial_update_json

### Example Usage

```python
import meldapi
from meldapi.models import operations, shared

s = meldapi.MeldAPI()

req = operations.ResidentPartialUpdateJSONRequest(
    patched_resident_input=shared.PatchedResidentInput(
        address=shared.PatchedResidentAddress(
            city='Goldnerborough',
            country='Belgium',
            county_province='fugit',
            line_1='cumque',
            line_2='quae',
            line_3='perferendis',
            postcode='14258',
        ),
        contact=shared.Contact(
            business_phone='impedit',
            business_phone_ext='eos',
            cell_phone='sapiente',
            cell_phone_ext='eum',
            fax='dicta',
            home_phone='minima',
            home_phone_ext='beatae',
            primary_email='Lambert_Weber84@yahoo.com',
            secondary_email='Tremaine_Metz39@gmail.com',
            tertiary_email='Geo76@hotmail.com',
        ),
        first_name='Marlene',
        invite=False,
        last_name='Dickens',
        middle_name='animi',
        notes='necessitatibus',
        notification_settings=shared.NotificationSettingsInput(
            incoming_meld_frequency=shared.IncomingMeldFrequencyEnum.NEVER,
            sms_notifications=False,
            successful_meld_frequency=shared.SuccessfulMeldFrequencyEnum.IMMEDIATELY,
            timezone=shared.TimezoneEnum.AMERICA_ANTIGUA,
        ),
        units=[
            497777,
        ],
    ),
    id='996312fd-e047-4717-b8ff-61d017476360',
)

res = s.resident.resident_partial_update_json(req, operations.ResidentPartialUpdateJSONSecurity(
    pmo_auth2_authentication="",
))

if res.resident is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.ResidentPartialUpdateJSONRequest](../../models/operations/residentpartialupdatejsonrequest.md)   | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `security`                                                                                                   | [operations.ResidentPartialUpdateJSONSecurity](../../models/operations/residentpartialupdatejsonsecurity.md) | :heavy_check_mark:                                                                                           | The security requirements to use for the request.                                                            |


### Response

**[operations.ResidentPartialUpdateJSONResponse](../../models/operations/residentpartialupdatejsonresponse.md)**


## resident_partial_update_multipart

### Example Usage

```python
import meldapi
from meldapi.models import operations, shared

s = meldapi.MeldAPI()

req = operations.ResidentPartialUpdateMultipartRequest(
    patched_resident_input1=shared.PatchedResidentInput1(
        address='laborum',
        contact=shared.Contact(
            business_phone='sunt',
            business_phone_ext='nostrum',
            cell_phone='fugiat',
            cell_phone_ext='expedita',
            fax='aliquid',
            home_phone='officia',
            home_phone_ext='suscipit',
            primary_email='Alanis_Kemmer@yahoo.com',
            secondary_email='Anthony_Muller65@yahoo.com',
            tertiary_email='Mollie.Hane@hotmail.com',
        ),
        first_name='Bernie',
        invite=False,
        last_name='Skiles',
        middle_name='ex',
        notes='quo',
        notification_settings=shared.NotificationSettingsInput(
            incoming_meld_frequency=shared.IncomingMeldFrequencyEnum.DAILY,
            sms_notifications=False,
            successful_meld_frequency=shared.SuccessfulMeldFrequencyEnum.IMMEDIATELY,
            timezone=shared.TimezoneEnum.AMERICA_REGINA,
        ),
        units=[
            29950,
            561577,
            737254,
        ],
    ),
    id='61891baa-0fe1-4ade-808e-6f8c5f350d8c',
)

res = s.resident.resident_partial_update_multipart(req, operations.ResidentPartialUpdateMultipartSecurity(
    pmo_auth2_authentication="",
))

if res.resident is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.ResidentPartialUpdateMultipartRequest](../../models/operations/residentpartialupdatemultipartrequest.md)   | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |
| `security`                                                                                                             | [operations.ResidentPartialUpdateMultipartSecurity](../../models/operations/residentpartialupdatemultipartsecurity.md) | :heavy_check_mark:                                                                                                     | The security requirements to use for the request.                                                                      |


### Response

**[operations.ResidentPartialUpdateMultipartResponse](../../models/operations/residentpartialupdatemultipartresponse.md)**


## resident_retrieve

### Example Usage

```python
import meldapi
from meldapi.models import operations

s = meldapi.MeldAPI()

req = operations.ResidentRetrieveRequest(
    id='db5a3418-1430-4104-a181-3d5208ece7e2',
)

res = s.resident.resident_retrieve(req, operations.ResidentRetrieveSecurity(
    pmo_auth2_authentication="",
))

if res.resident is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ResidentRetrieveRequest](../../models/operations/residentretrieverequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.ResidentRetrieveSecurity](../../models/operations/residentretrievesecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.ResidentRetrieveResponse](../../models/operations/residentretrieveresponse.md)**


## resident_update_form

### Example Usage

```python
import meldapi
from meldapi.models import operations, shared

s = meldapi.MeldAPI()

req = operations.ResidentUpdateFormRequest(
    resident_input1=shared.ResidentInput1(
        address='veniam',
        contact=shared.Contact(
            business_phone='nesciunt',
            business_phone_ext='expedita',
            cell_phone='eum',
            cell_phone_ext='vel',
            fax='voluptatum',
            home_phone='magnam',
            home_phone_ext='exercitationem',
            primary_email='Oswald.Jones92@gmail.com',
            secondary_email='Alessia.Heller39@gmail.com',
            tertiary_email='Shaina.Orn98@hotmail.com',
        ),
        first_name='Terrence',
        invite=False,
        last_name='Rowe',
        middle_name='occaecati',
        notes='nemo',
        notification_settings=shared.NotificationSettingsInput(
            incoming_meld_frequency=shared.IncomingMeldFrequencyEnum.DAILY,
            sms_notifications=False,
            successful_meld_frequency=shared.SuccessfulMeldFrequencyEnum.DAILY,
            timezone=shared.TimezoneEnum.CANADA_SASKATCHEWAN,
        ),
        units=[
            254025,
            364912,
        ],
    ),
    id='84273a84-18d1-4623-89fb-0929921aefb9',
)

res = s.resident.resident_update_form(req, operations.ResidentUpdateFormSecurity(
    pmo_auth2_authentication="",
))

if res.resident is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ResidentUpdateFormRequest](../../models/operations/residentupdateformrequest.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.ResidentUpdateFormSecurity](../../models/operations/residentupdateformsecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |


### Response

**[operations.ResidentUpdateFormResponse](../../models/operations/residentupdateformresponse.md)**


## resident_update_json

### Example Usage

```python
import meldapi
from meldapi.models import operations, shared

s = meldapi.MeldAPI()

req = operations.ResidentUpdateJSONRequest(
    resident_input=shared.ResidentInput(
        address=shared.ResidentAddress(
            city='Framingham',
            country='Liechtenstein',
            county_province='maxime',
            line_1='magnam',
            line_2='temporibus',
            line_3='quos',
            postcode='94592',
        ),
        contact=shared.Contact(
            business_phone='nam',
            business_phone_ext='vero',
            cell_phone='voluptatem',
            cell_phone_ext='ipsam',
            fax='vel',
            home_phone='alias',
            home_phone_ext='quasi',
            primary_email='Wilford_Hamill@gmail.com',
            secondary_email='Jaden_Hickle@yahoo.com',
            tertiary_email='Kiana_Thompson90@yahoo.com',
        ),
        first_name='Zachariah',
        invite=False,
        last_name='Jakubowski',
        middle_name='voluptas',
        notes='debitis',
        notification_settings=shared.NotificationSettingsInput(
            incoming_meld_frequency=shared.IncomingMeldFrequencyEnum.NEVER,
            sms_notifications=False,
            successful_meld_frequency=shared.SuccessfulMeldFrequencyEnum.IMMEDIATELY,
            timezone=shared.TimezoneEnum.EUROPE_SARATOV,
        ),
        units=[
            675689,
            231070,
            244889,
        ],
    ),
    id='83c2beb4-7737-43c8-972f-64d1db1f2c43',
)

res = s.resident.resident_update_json(req, operations.ResidentUpdateJSONSecurity(
    pmo_auth2_authentication="",
))

if res.resident is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ResidentUpdateJSONRequest](../../models/operations/residentupdatejsonrequest.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.ResidentUpdateJSONSecurity](../../models/operations/residentupdatejsonsecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |


### Response

**[operations.ResidentUpdateJSONResponse](../../models/operations/residentupdatejsonresponse.md)**


## resident_update_multipart

### Example Usage

```python
import meldapi
from meldapi.models import operations, shared

s = meldapi.MeldAPI()

req = operations.ResidentUpdateMultipartRequest(
    resident_input1=shared.ResidentInput1(
        address='illo',
        contact=shared.Contact(
            business_phone='accusantium',
            business_phone_ext='vel',
            cell_phone='ea',
            cell_phone_ext='beatae',
            fax='vero',
            home_phone='excepturi',
            home_phone_ext='eum',
            primary_email='Ed.Metz77@gmail.com',
            secondary_email='Leonora39@hotmail.com',
            tertiary_email='Deangelo22@hotmail.com',
        ),
        first_name='Jayne',
        invite=False,
        last_name='Bailey',
        middle_name='doloremque',
        notes='consequatur',
        notification_settings=shared.NotificationSettingsInput(
            incoming_meld_frequency=shared.IncomingMeldFrequencyEnum.DAILY,
            sms_notifications=False,
            successful_meld_frequency=shared.SuccessfulMeldFrequencyEnum.NEVER,
            timezone=shared.TimezoneEnum.ASIA_ASHKHABAD,
        ),
        units=[
            377406,
            705148,
            809365,
        ],
    ),
    id='9b8f759e-ac55-4a97-81d3-11352965bb8a',
)

res = s.resident.resident_update_multipart(req, operations.ResidentUpdateMultipartSecurity(
    pmo_auth2_authentication="",
))

if res.resident is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.ResidentUpdateMultipartRequest](../../models/operations/residentupdatemultipartrequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.ResidentUpdateMultipartSecurity](../../models/operations/residentupdatemultipartsecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.ResidentUpdateMultipartResponse](../../models/operations/residentupdatemultipartresponse.md)**

