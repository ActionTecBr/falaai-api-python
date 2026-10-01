# DiagnosticUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**characters** | **int** | Total characters analyzed | 
**credits_consumed** | **int** | Credits consumed: max(ceil(chars/500)*3, 3) * 5 | 
**processing_ms** | **int** | Total processing time in milliseconds | 

## Example

```python
from falaai_api.models.diagnostic_usage import DiagnosticUsage

# TODO update the JSON string below
json = "{}"
# create an instance of DiagnosticUsage from a JSON string
diagnostic_usage_instance = DiagnosticUsage.from_json(json)
# print the JSON string representation of the object
print(DiagnosticUsage.to_json())

# convert the object into a dict
diagnostic_usage_dict = diagnostic_usage_instance.to_dict()
# create an instance of DiagnosticUsage from a dict
diagnostic_usage_from_dict = DiagnosticUsage.from_dict(diagnostic_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


