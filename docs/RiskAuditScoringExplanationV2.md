# RiskAuditScoringExplanationV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary** | **str** | Explanation summary | [optional] 
**steps** | **List[object]** | Explanation steps | [optional] [default to []]

## Example

```python
from falaai_api.models.risk_audit_scoring_explanation_v2 import RiskAuditScoringExplanationV2

# TODO update the JSON string below
json = "{}"
# create an instance of RiskAuditScoringExplanationV2 from a JSON string
risk_audit_scoring_explanation_v2_instance = RiskAuditScoringExplanationV2.from_json(json)
# print the JSON string representation of the object
print(RiskAuditScoringExplanationV2.to_json())

# convert the object into a dict
risk_audit_scoring_explanation_v2_dict = risk_audit_scoring_explanation_v2_instance.to_dict()
# create an instance of RiskAuditScoringExplanationV2 from a dict
risk_audit_scoring_explanation_v2_from_dict = RiskAuditScoringExplanationV2.from_dict(risk_audit_scoring_explanation_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


