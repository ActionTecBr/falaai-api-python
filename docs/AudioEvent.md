# AudioEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | **str** | Type of identified audio event. Ex: [riso], [suspiro], [pausa], [tosse] | 
**start_s** | **float** | Start time of audio event in seconds | 
**end_s** | **float** | End time of audio event in seconds | 
**duration_s** | **float** | Event duration in seconds | 
**formatted_timestamp** | **str** | Formatted timestamp HH:MM:SS.mmm of event start | 

## Example

```python
from falaai_api.models.audio_event import AudioEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AudioEvent from a JSON string
audio_event_instance = AudioEvent.from_json(json)
# print the JSON string representation of the object
print(AudioEvent.to_json())

# convert the object into a dict
audio_event_dict = audio_event_instance.to_dict()
# create an instance of AudioEvent from a dict
audio_event_from_dict = AudioEvent.from_dict(audio_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


