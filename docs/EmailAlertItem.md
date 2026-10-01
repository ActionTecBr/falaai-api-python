# EmailAlertItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Email alert id | 
**user_id** | **str** | Owner user id | 
**name** | **str** | Email alert name | 
**email** | **str** | Destination email | 
**events** | **List[str]** | Subscribed events | 
**active** | **bool** | Is active | 
**created_at** | **str** | ISO 8601 created | 
**updated_at** | **str** | ISO 8601 updated | 

## Example

```python
from falaai_api.models.email_alert_item import EmailAlertItem

# TODO update the JSON string below
json = "{}"
# create an instance of EmailAlertItem from a JSON string
email_alert_item_instance = EmailAlertItem.from_json(json)
# print the JSON string representation of the object
print(EmailAlertItem.to_json())

# convert the object into a dict
email_alert_item_dict = email_alert_item_instance.to_dict()
# create an instance of EmailAlertItem from a dict
email_alert_item_from_dict = EmailAlertItem.from_dict(email_alert_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


