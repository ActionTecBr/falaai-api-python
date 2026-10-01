# AudioInputMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration_s** | **float** | Exact audio duration sent in seconds | 
**original_format** | **str** | Original file format (wav, mp3, ogg, etc) | 
**codec** | **str** | Audio codec sent | 
**sample_rate** | **int** | Audio sample rate in Hz | 
**channels** | **int** | Number of channels (1&#x3D;mono, 2&#x3D;stereo) | 

## Example

```python
from falaai_api.models.audio_input_meta import AudioInputMeta

# TODO update the JSON string below
json = "{}"
# create an instance of AudioInputMeta from a JSON string
audio_input_meta_instance = AudioInputMeta.from_json(json)
# print the JSON string representation of the object
print(AudioInputMeta.to_json())

# convert the object into a dict
audio_input_meta_dict = audio_input_meta_instance.to_dict()
# create an instance of AudioInputMeta from a dict
audio_input_meta_from_dict = AudioInputMeta.from_dict(audio_input_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


