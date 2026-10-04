# WhatsappSpeaker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Speaker label (e.g. &#39;Speaker 1&#39;) | 
**name** | **str** | Participant name from the export | 

## Example

```python
from falaai_api.models.whatsapp_speaker import WhatsappSpeaker

# TODO update the JSON string below
json = "{}"
# create an instance of WhatsappSpeaker from a JSON string
whatsapp_speaker_instance = WhatsappSpeaker.from_json(json)
# print the JSON string representation of the object
print(WhatsappSpeaker.to_json())

# convert the object into a dict
whatsapp_speaker_dict = whatsapp_speaker_instance.to_dict()
# create an instance of WhatsappSpeaker from a dict
whatsapp_speaker_from_dict = WhatsappSpeaker.from_dict(whatsapp_speaker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


