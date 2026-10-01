# UsageLogItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Usage log entry id | 
**endpoint** | **str** | Endpoint called | 
**credits_cost** | **int** | Credits consumed | 
**status** | **str** | Result status | 
**errors_count** | **int** | Errors count | 
**created_at** | **str** | ISO 8601 timestamp | 

## Example

```python
from falaai_api.models.usage_log_item import UsageLogItem

# TODO update the JSON string below
json = "{}"
# create an instance of UsageLogItem from a JSON string
usage_log_item_instance = UsageLogItem.from_json(json)
# print the JSON string representation of the object
print(UsageLogItem.to_json())

# convert the object into a dict
usage_log_item_dict = usage_log_item_instance.to_dict()
# create an instance of UsageLogItem from a dict
usage_log_item_from_dict = UsageLogItem.from_dict(usage_log_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


