# RiskAuditAuditDecisionsV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**risk_origin** | **str** | Risk origin | [optional] 
**has_zero_tolerance_violation** | **bool** | Has zero-tolerance violation | [optional] 
**deterministic_validator_changes** | **List[object]** | Deterministic validator changes | [optional] [default to []]

## Example

```python
from falaai_api.models.risk_audit_audit_decisions_v2 import RiskAuditAuditDecisionsV2

# TODO update the JSON string below
json = "{}"
# create an instance of RiskAuditAuditDecisionsV2 from a JSON string
risk_audit_audit_decisions_v2_instance = RiskAuditAuditDecisionsV2.from_json(json)
# print the JSON string representation of the object
print(RiskAuditAuditDecisionsV2.to_json())

# convert the object into a dict
risk_audit_audit_decisions_v2_dict = risk_audit_audit_decisions_v2_instance.to_dict()
# create an instance of RiskAuditAuditDecisionsV2 from a dict
risk_audit_audit_decisions_v2_from_dict = RiskAuditAuditDecisionsV2.from_dict(risk_audit_audit_decisions_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


