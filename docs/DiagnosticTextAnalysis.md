# DiagnosticTextAnalysis


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**explanation** | **str** | Explanatory text (used in summary and reason) | [optional] 

## Example

```python
from falaai_api.models.diagnostic_text_analysis import DiagnosticTextAnalysis

# TODO update the JSON string below
json = "{}"
# create an instance of DiagnosticTextAnalysis from a JSON string
diagnostic_text_analysis_instance = DiagnosticTextAnalysis.from_json(json)
# print the JSON string representation of the object
print(DiagnosticTextAnalysis.to_json())

# convert the object into a dict
diagnostic_text_analysis_dict = diagnostic_text_analysis_instance.to_dict()
# create an instance of DiagnosticTextAnalysis from a dict
diagnostic_text_analysis_from_dict = DiagnosticTextAnalysis.from_dict(diagnostic_text_analysis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


