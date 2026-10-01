# UpdateEmailAlertRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**events** | [**List[EmailEvent]**](EmailEvent.md) |  | [optional] 
**active** | **bool** |  | [optional] 

## Example

```python
from falaai_api.models.update_email_alert_request import UpdateEmailAlertRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateEmailAlertRequest from a JSON string
update_email_alert_request_instance = UpdateEmailAlertRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateEmailAlertRequest.to_json())

# convert the object into a dict
update_email_alert_request_dict = update_email_alert_request_instance.to_dict()
# create an instance of UpdateEmailAlertRequest from a dict
update_email_alert_request_from_dict = UpdateEmailAlertRequest.from_dict(update_email_alert_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


