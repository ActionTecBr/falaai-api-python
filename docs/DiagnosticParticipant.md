# DiagnosticParticipant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interlocutor** | **str** | Exact speaker label from the dialog (e.g. &#39;Speaker 1&#39;) | 
**name** | **str** | Participant name (optional) | [optional] 
**role** | **str** | agent | client | bot | 

## Example

```python
from falaai_api.models.diagnostic_participant import DiagnosticParticipant

# TODO update the JSON string below
json = "{}"
# create an instance of DiagnosticParticipant from a JSON string
diagnostic_participant_instance = DiagnosticParticipant.from_json(json)
# print the JSON string representation of the object
print(DiagnosticParticipant.to_json())

# convert the object into a dict
diagnostic_participant_dict = diagnostic_participant_instance.to_dict()
# create an instance of DiagnosticParticipant from a dict
diagnostic_participant_from_dict = DiagnosticParticipant.from_dict(diagnostic_participant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


