# RiskAuditConversationScoresV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consolidated_score** | **float** | Consolidated score | [optional] 
**violation_density_per_min** | **float** | Violation density/min | [optional] 
**sentiment_trend** | **object** | Sentiment trend | [optional] 
**pct_turns_with_violation** | **float** | % turns with violation | [optional] 
**most_critical_turn** | **object** | Most critical turn | [optional] 
**positive_negative_ratio** | **object** | Positive:negative ratio | [optional] 
**global_risk_severity** | **str** | Global risk severity code | [optional] 
**global_risk_severity_label** | **str** | Global risk severity label | [optional] 
**global_risk_severity_color** | **str** | Global risk severity color | [optional] 
**risk_likelihood_avg** | **float** | Risk likelihood avg | [optional] 
**risk_impact_avg** | **float** | Risk impact avg | [optional] 

## Example

```python
from falaai_api.models.risk_audit_conversation_scores_v2 import RiskAuditConversationScoresV2

# TODO update the JSON string below
json = "{}"
# create an instance of RiskAuditConversationScoresV2 from a JSON string
risk_audit_conversation_scores_v2_instance = RiskAuditConversationScoresV2.from_json(json)
# print the JSON string representation of the object
print(RiskAuditConversationScoresV2.to_json())

# convert the object into a dict
risk_audit_conversation_scores_v2_dict = risk_audit_conversation_scores_v2_instance.to_dict()
# create an instance of RiskAuditConversationScoresV2 from a dict
risk_audit_conversation_scores_v2_from_dict = RiskAuditConversationScoresV2.from_dict(risk_audit_conversation_scores_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


