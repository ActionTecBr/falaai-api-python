# RiskAuditScoresV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation** | [**RiskAuditConversationScoresV2**](RiskAuditConversationScoresV2.md) | Conversation scores | 
**per_participant** | **Dict[str, object]** | Per-participant KPIs | [optional] 

## Example

```python
from falaai_api.models.risk_audit_scores_v2 import RiskAuditScoresV2

# TODO update the JSON string below
json = "{}"
# create an instance of RiskAuditScoresV2 from a JSON string
risk_audit_scores_v2_instance = RiskAuditScoresV2.from_json(json)
# print the JSON string representation of the object
print(RiskAuditScoresV2.to_json())

# convert the object into a dict
risk_audit_scores_v2_dict = risk_audit_scores_v2_instance.to_dict()
# create an instance of RiskAuditScoresV2 from a dict
risk_audit_scores_v2_from_dict = RiskAuditScoresV2.from_dict(risk_audit_scores_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


