# RiskAuditParticipantV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interlocutor** | **str** | Speaker label | [optional] 
**name** | **str** | Participant name | [optional] 
**role** | **str** | Role (agent/client/bot/unknown) | [optional] 
**confidence** | **str** | Role inference confidence (high/medium/low) | [optional] 
**source** | **str** | Role source (input/inferred) | [optional] 
**evidence** | **str** | Role inference evidence | [optional] 

## Example

```python
from falaai_api.models.risk_audit_participant_v2 import RiskAuditParticipantV2

# TODO update the JSON string below
json = "{}"
# create an instance of RiskAuditParticipantV2 from a JSON string
risk_audit_participant_v2_instance = RiskAuditParticipantV2.from_json(json)
# print the JSON string representation of the object
print(RiskAuditParticipantV2.to_json())

# convert the object into a dict
risk_audit_participant_v2_dict = risk_audit_participant_v2_instance.to_dict()
# create an instance of RiskAuditParticipantV2 from a dict
risk_audit_participant_v2_from_dict = RiskAuditParticipantV2.from_dict(risk_audit_participant_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


