# RiskAuditAudioEventModelV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** | MAC model text (i18n) | [optional] [default to '']
**description** | **str** | MAC description (i18n) | [optional] [default to '']
**windows_s** | **Dict[str, object]** | Temporal windows (s) | [optional] 

## Example

```python
from falaai_api.models.risk_audit_audio_event_model_v2 import RiskAuditAudioEventModelV2

# TODO update the JSON string below
json = "{}"
# create an instance of RiskAuditAudioEventModelV2 from a JSON string
risk_audit_audio_event_model_v2_instance = RiskAuditAudioEventModelV2.from_json(json)
# print the JSON string representation of the object
print(RiskAuditAudioEventModelV2.to_json())

# convert the object into a dict
risk_audit_audio_event_model_v2_dict = risk_audit_audio_event_model_v2_instance.to_dict()
# create an instance of RiskAuditAudioEventModelV2 from a dict
risk_audit_audio_event_model_v2_from_dict = RiskAuditAudioEventModelV2.from_dict(risk_audit_audio_event_model_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


