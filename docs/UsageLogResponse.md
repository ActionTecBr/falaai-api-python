# UsageLogResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UsageLogItem]**](UsageLogItem.md) |  | 
**page** | **int** |  | 
**limit** | **int** |  | 

## Example

```python
from falaai_api.models.usage_log_response import UsageLogResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UsageLogResponse from a JSON string
usage_log_response_instance = UsageLogResponse.from_json(json)
# print the JSON string representation of the object
print(UsageLogResponse.to_json())

# convert the object into a dict
usage_log_response_dict = usage_log_response_instance.to_dict()
# create an instance of UsageLogResponse from a dict
usage_log_response_from_dict = UsageLogResponse.from_dict(usage_log_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


