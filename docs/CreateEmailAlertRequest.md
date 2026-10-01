# CreateEmailAlertRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Nome identificador | 
**email** | **str** | Email destino | 
**events** | [**List[EmailEvent]**](EmailEvent.md) | Eventos subscritos | 

## Example

```python
from falaai_api.models.create_email_alert_request import CreateEmailAlertRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEmailAlertRequest from a JSON string
create_email_alert_request_instance = CreateEmailAlertRequest.from_json(json)
# print the JSON string representation of the object
print(CreateEmailAlertRequest.to_json())

# convert the object into a dict
create_email_alert_request_dict = create_email_alert_request_instance.to_dict()
# create an instance of CreateEmailAlertRequest from a dict
create_email_alert_request_from_dict = CreateEmailAlertRequest.from_dict(create_email_alert_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


