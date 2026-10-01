# DiagnosticCategoricalAnalysis


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list_choice** | **str** | Selected value from classification list (used in action, label, sentiment) | [optional] 
**justification** | **str** | Justification for the choice | [optional] 
**evidence_phrases** | **List[str]** | Verbatim transcript excerpts supporting the analysis | [optional] [default to []]

## Example

```python
from falaai_api.models.diagnostic_categorical_analysis import DiagnosticCategoricalAnalysis

# TODO update the JSON string below
json = "{}"
# create an instance of DiagnosticCategoricalAnalysis from a JSON string
diagnostic_categorical_analysis_instance = DiagnosticCategoricalAnalysis.from_json(json)
# print the JSON string representation of the object
print(DiagnosticCategoricalAnalysis.to_json())

# convert the object into a dict
diagnostic_categorical_analysis_dict = diagnostic_categorical_analysis_instance.to_dict()
# create an instance of DiagnosticCategoricalAnalysis from a dict
diagnostic_categorical_analysis_from_dict = DiagnosticCategoricalAnalysis.from_dict(diagnostic_categorical_analysis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


