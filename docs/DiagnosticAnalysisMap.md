# DiagnosticAnalysisMap


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dialogue_summary** | [**DiagnosticTextAnalysis**](DiagnosticTextAnalysis.md) | Detailed conversation summary | 
**contact_reason** | [**DiagnosticTextAnalysis**](DiagnosticTextAnalysis.md) | Initial contact reason | 
**identified_action** | [**DiagnosticCategoricalAnalysis**](DiagnosticCategoricalAnalysis.md) | Action taken / resolution | 
**identified_label** | [**DiagnosticCategoricalAnalysis**](DiagnosticCategoricalAnalysis.md) | Theme classification | 
**sentiment** | [**DiagnosticCategoricalAnalysis**](DiagnosticCategoricalAnalysis.md) | Predominant sentiment | 
**participants_identified** | [**List[ParticipantDiagnostic]**](ParticipantDiagnostic.md) | Identified participants and roles (same field names as auditoria) | [optional] [default to []]

## Example

```python
from falaai_api.models.diagnostic_analysis_map import DiagnosticAnalysisMap

# TODO update the JSON string below
json = "{}"
# create an instance of DiagnosticAnalysisMap from a JSON string
diagnostic_analysis_map_instance = DiagnosticAnalysisMap.from_json(json)
# print the JSON string representation of the object
print(DiagnosticAnalysisMap.to_json())

# convert the object into a dict
diagnostic_analysis_map_dict = diagnostic_analysis_map_instance.to_dict()
# create an instance of DiagnosticAnalysisMap from a dict
diagnostic_analysis_map_from_dict = DiagnosticAnalysisMap.from_dict(diagnostic_analysis_map_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


