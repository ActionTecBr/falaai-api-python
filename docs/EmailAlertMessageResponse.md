# EmailAlertMessageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Operation result message | 

## Example

```python
from falaai_api.models.email_alert_message_response import EmailAlertMessageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmailAlertMessageResponse from a JSON string
email_alert_message_response_instance = EmailAlertMessageResponse.from_json(json)
# print the JSON string representation of the object
print(EmailAlertMessageResponse.to_json())

# convert the object into a dict
email_alert_message_response_dict = email_alert_message_response_instance.to_dict()
# create an instance of EmailAlertMessageResponse from a dict
email_alert_message_response_from_dict = EmailAlertMessageResponse.from_dict(email_alert_message_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


