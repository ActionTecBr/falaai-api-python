# RiskAuditSummaryV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_turns** | **int** | Total turns | [optional] 
**total_calibrated** | **int** | Total calibrated detections | [optional] 
**active** | **int** | Active detections | [optional] 
**tolerated** | **int** | Tolerated detections | [optional] 
**blocked** | **int** | Blocked detections | [optional] 
**audio_events_used** | **int** | Audio events used | [optional] 
**audio_events_aggravated** | **int** | Audio events aggravated | [optional] 
**mac_audio_applied** | **object** | MAC audio applied | [optional] 
**mvad_applied** | **object** | MVAD applied | [optional] 
**total_participants** | **int** | Total participants | [optional] 
**total_agents** | **int** | Total agents | [optional] 
**total_clients** | **int** | Total clients | [optional] 
**total_bots** | **int** | Total bots | [optional] 
**total_unknown** | **int** | Total unknown | [optional] 
**client_risk_alerts_count** | **int** | Client risk alerts count | [optional] 
**client_behavior_alerts_count** | **int** | Client behavior alerts count | [optional] 

## Example

```python
from falaai_api.models.risk_audit_summary_v2 import RiskAuditSummaryV2

# TODO update the JSON string below
json = "{}"
# create an instance of RiskAuditSummaryV2 from a JSON string
risk_audit_summary_v2_instance = RiskAuditSummaryV2.from_json(json)
# print the JSON string representation of the object
print(RiskAuditSummaryV2.to_json())

# convert the object into a dict
risk_audit_summary_v2_dict = risk_audit_summary_v2_instance.to_dict()
# create an instance of RiskAuditSummaryV2 from a dict
risk_audit_summary_v2_from_dict = RiskAuditSummaryV2.from_dict(risk_audit_summary_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


