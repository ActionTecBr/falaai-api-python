# ParticipantDiagnostic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interlocutor** | **str** | Exact speaker label from the dialog (e.g. &#39;Speaker 1&#39;) | 
**role** | **str** | Role: agent | client | bot | agent_requester | agent_custodian | 
**name** | **str** | Participant name if mentioned in the dialogue | [optional] 
**confidence** | **str** | high | medium | low | [optional] 
**evidence** | **str** | Exact verbatim quote supporting the role (no timestamps) | [optional] 

## Example

```python
from falaai_api.models.participant_diagnostic import ParticipantDiagnostic

# TODO update the JSON string below
json = "{}"
# create an instance of ParticipantDiagnostic from a JSON string
participant_diagnostic_instance = ParticipantDiagnostic.from_json(json)
# print the JSON string representation of the object
print(ParticipantDiagnostic.to_json())

# convert the object into a dict
participant_diagnostic_dict = participant_diagnostic_instance.to_dict()
# create an instance of ParticipantDiagnostic from a dict
participant_diagnostic_from_dict = ParticipantDiagnostic.from_dict(participant_diagnostic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


