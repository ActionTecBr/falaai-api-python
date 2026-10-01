# DiagnosticResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique analysis identifier. Prefix &#39;di-&#39; + UUID | 
**response_language** | **str** | Language used in the response. E.g.: &#39;pt-BR&#39;, &#39;en-US&#39;, &#39;es-ES&#39; | 
**object** | **str** | Object type. Always &#39;analysis&#39; | 
**analysis** | [**DiagnosticAnalysisMap**](DiagnosticAnalysisMap.md) | The 6 conversation analyses (5 + participants) | 
**usage** | [**DiagnosticUsage**](DiagnosticUsage.md) | Usage and processing information | 
**client_reference_id** | **str** | Client-supplied ID echoed verbatim (if provided in request) | [optional] 

## Example

```python
from falaai_api.models.diagnostic_response import DiagnosticResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DiagnosticResponse from a JSON string
diagnostic_response_instance = DiagnosticResponse.from_json(json)
# print the JSON string representation of the object
print(DiagnosticResponse.to_json())

# convert the object into a dict
diagnostic_response_dict = diagnostic_response_instance.to_dict()
# create an instance of DiagnosticResponse from a dict
diagnostic_response_from_dict = DiagnosticResponse.from_dict(diagnostic_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


