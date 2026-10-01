# EmailAlertListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[EmailAlertItem]**](EmailAlertItem.md) |  | 
**page** | **int** |  | 
**limit** | **int** |  | 

## Example

```python
from falaai_api.models.email_alert_list_response import EmailAlertListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmailAlertListResponse from a JSON string
email_alert_list_response_instance = EmailAlertListResponse.from_json(json)
# print the JSON string representation of the object
print(EmailAlertListResponse.to_json())

# convert the object into a dict
email_alert_list_response_dict = email_alert_list_response_instance.to_dict()
# create an instance of EmailAlertListResponse from a dict
email_alert_list_response_from_dict = EmailAlertListResponse.from_dict(email_alert_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


