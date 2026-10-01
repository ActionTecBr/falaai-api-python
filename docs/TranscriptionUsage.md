# TranscriptionUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audio_seconds** | **float** | Actual audio duration processed in seconds | 
**credits_consumed** | **int** | Number of credits consumed in this request | 
**processing_ms** | **int** | Total processing time in milliseconds | 

## Example

```python
from falaai_api.models.transcription_usage import TranscriptionUsage

# TODO update the JSON string below
json = "{}"
# create an instance of TranscriptionUsage from a JSON string
transcription_usage_instance = TranscriptionUsage.from_json(json)
# print the JSON string representation of the object
print(TranscriptionUsage.to_json())

# convert the object into a dict
transcription_usage_dict = transcription_usage_instance.to_dict()
# create an instance of TranscriptionUsage from a dict
transcription_usage_from_dict = TranscriptionUsage.from_dict(transcription_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


