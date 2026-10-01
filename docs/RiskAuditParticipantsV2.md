# RiskAuditParticipantsV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identified** | [**List[RiskAuditParticipantV2]**](RiskAuditParticipantV2.md) | Identified participants | [optional] [default to []]
**call_direction** | **str** | inbound/outbound | [optional] 
**role_inference_reliable** | **bool** | Role inference reliability | [optional] [default to True]
**identification_status** | **str** | Identification status | [optional] [default to 'none']
**unidentified_items_count** | **int** | Unidentified items count | [optional] [default to 0]

## Example

```python
from falaai_api.models.risk_audit_participants_v2 import RiskAuditParticipantsV2

# TODO update the JSON string below
json = "{}"
# create an instance of RiskAuditParticipantsV2 from a JSON string
risk_audit_participants_v2_instance = RiskAuditParticipantsV2.from_json(json)
# print the JSON string representation of the object
print(RiskAuditParticipantsV2.to_json())

# convert the object into a dict
risk_audit_participants_v2_dict = risk_audit_participants_v2_instance.to_dict()
# create an instance of RiskAuditParticipantsV2 from a dict
risk_audit_participants_v2_from_dict = RiskAuditParticipantsV2.from_dict(risk_audit_participants_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


