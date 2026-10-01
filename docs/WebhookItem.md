# WebhookItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Webhook id | 
**user_id** | **str** | Owner user id | 
**name** | **str** | Webhook name | 
**url** | **str** | Destination URL | 
**secret** | **str** | HMAC signing secret | 
**events** | **List[str]** | Subscribed events | 
**active** | **bool** | Is active | 
**retry_enabled** | **bool** | Retry enabled | 
**last_delivery_at** | **str** | ISO 8601 of last delivery | [optional] 
**last_status** | **int** | Last HTTP status delivered | [optional] 
**failure_count** | **int** | Consecutive failures | [optional] [default to 0]
**created_at** | **str** | ISO 8601 created | 
**updated_at** | **str** | ISO 8601 updated | 

## Example

```python
from falaai_api.models.webhook_item import WebhookItem

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookItem from a JSON string
webhook_item_instance = WebhookItem.from_json(json)
# print the JSON string representation of the object
print(WebhookItem.to_json())

# convert the object into a dict
webhook_item_dict = webhook_item_instance.to_dict()
# create an instance of WebhookItem from a dict
webhook_item_from_dict = WebhookItem.from_dict(webhook_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


