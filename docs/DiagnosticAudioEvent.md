# DiagnosticAudioEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | **str** | Audio event type. E.g.: [laughter], [sigh] | 
**start_s** | **float** | Start time in seconds | [optional] 
**end_s** | **float** | End time in seconds | [optional] 
**duration_s** | **float** | Duration in seconds | [optional] 
**formatted_timestamp** | **str** | Formatted timestamp (HH:MM:SS.ms) | [optional] 

## Example

```python
from falaai_api.models.diagnostic_audio_event import DiagnosticAudioEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DiagnosticAudioEvent from a JSON string
diagnostic_audio_event_instance = DiagnosticAudioEvent.from_json(json)
# print the JSON string representation of the object
print(DiagnosticAudioEvent.to_json())

# convert the object into a dict
diagnostic_audio_event_dict = diagnostic_audio_event_instance.to_dict()
# create an instance of DiagnosticAudioEvent from a dict
diagnostic_audio_event_from_dict = DiagnosticAudioEvent.from_dict(diagnostic_audio_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


