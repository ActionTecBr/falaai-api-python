# UsageByKeyItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | **str** | API key id | 
**key_name** | **str** | API key name | 
**total_credits** | **int** | Total credits consumed by the key | 
**request_count** | **int** | Number of requests | 
**last_used** | **str** | ISO 8601 of last use (null if never) | [optional] 

## Example

```python
from falaai_api.models.usage_by_key_item import UsageByKeyItem

# TODO update the JSON string below
json = "{}"
# create an instance of UsageByKeyItem from a JSON string
usage_by_key_item_instance = UsageByKeyItem.from_json(json)
# print the JSON string representation of the object
print(UsageByKeyItem.to_json())

# convert the object into a dict
usage_by_key_item_dict = usage_by_key_item_instance.to_dict()
# create an instance of UsageByKeyItem from a dict
usage_by_key_item_from_dict = UsageByKeyItem.from_dict(usage_by_key_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


