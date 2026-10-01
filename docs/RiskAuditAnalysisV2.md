# RiskAuditAnalysisV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**global_metrics** | **Dict[str, object]** | Global metrics | [optional] 
**final_analysis** | **Dict[str, object]** | Final analysis | [optional] 
**frameworks** | **Dict[str, object]** | Frameworks (COPC/ISO/Kirkpatrick/CES) | [optional] 

## Example

```python
from falaai_api.models.risk_audit_analysis_v2 import RiskAuditAnalysisV2

# TODO update the JSON string below
json = "{}"
# create an instance of RiskAuditAnalysisV2 from a JSON string
risk_audit_analysis_v2_instance = RiskAuditAnalysisV2.from_json(json)
# print the JSON string representation of the object
print(RiskAuditAnalysisV2.to_json())

# convert the object into a dict
risk_audit_analysis_v2_dict = risk_audit_analysis_v2_instance.to_dict()
# create an instance of RiskAuditAnalysisV2 from a dict
risk_audit_analysis_v2_from_dict = RiskAuditAnalysisV2.from_dict(risk_audit_analysis_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


