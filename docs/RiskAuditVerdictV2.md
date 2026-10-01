# RiskAuditVerdictV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Human-readable verdict | [optional] 
**level_code** | **str** | Classification level code | [optional] 
**color** | **str** | Level color | [optional] 
**icon** | **str** | Level icon | [optional] 
**risk_matrix** | **Dict[str, object]** | Risk matrix | [optional] 
**applied_actions** | [**List[RiskAuditAppliedActionV2]**](RiskAuditAppliedActionV2.md) | Applied actions | [optional] [default to []]
**decision_details** | **object** | Decision details | [optional] 

## Example

```python
from falaai_api.models.risk_audit_verdict_v2 import RiskAuditVerdictV2

# TODO update the JSON string below
json = "{}"
# create an instance of RiskAuditVerdictV2 from a JSON string
risk_audit_verdict_v2_instance = RiskAuditVerdictV2.from_json(json)
# print the JSON string representation of the object
print(RiskAuditVerdictV2.to_json())

# convert the object into a dict
risk_audit_verdict_v2_dict = risk_audit_verdict_v2_instance.to_dict()
# create an instance of RiskAuditVerdictV2 from a dict
risk_audit_verdict_v2_from_dict = RiskAuditVerdictV2.from_dict(risk_audit_verdict_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


