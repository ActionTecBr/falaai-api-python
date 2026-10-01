# RiskAuditAppliedActionV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_type** | **str** | Action type code | 
**label** | **str** | Action label | 
**description** | **str** | Action description | 
**priority** | **str** | CRITICO/ALTO/MEDIO/BAIXO | 
**color** | **str** | Color | [optional] [default to '']
**icon** | **str** | Icon | [optional] [default to '']
**condition** | **str** | Condition | [optional] 
**reason** | **str** | Reason | [optional] [default to '']

## Example

```python
from falaai_api.models.risk_audit_applied_action_v2 import RiskAuditAppliedActionV2

# TODO update the JSON string below
json = "{}"
# create an instance of RiskAuditAppliedActionV2 from a JSON string
risk_audit_applied_action_v2_instance = RiskAuditAppliedActionV2.from_json(json)
# print the JSON string representation of the object
print(RiskAuditAppliedActionV2.to_json())

# convert the object into a dict
risk_audit_applied_action_v2_dict = risk_audit_applied_action_v2_instance.to_dict()
# create an instance of RiskAuditAppliedActionV2 from a dict
risk_audit_applied_action_v2_from_dict = RiskAuditAppliedActionV2.from_dict(risk_audit_applied_action_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


