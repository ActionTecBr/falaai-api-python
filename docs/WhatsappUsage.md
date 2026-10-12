# WhatsappUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversations** | **int** | Number of conversations returned | 
**characters** | **int** | Total characters across conversations | 
**expressions** | **int** | Expression tokens across conversations (sticker/emoji/gif) | 
**voice_notes** | **int** | Voice notes (PTT) resolved to text | 
**conversation_credits** | **int** | Credits for conversations (2 each) | 
**expression_credits** | **float** | Credits for expressions (0.2 each) | 
**audio_credits** | **float** | Credits for audio duration (0.2 per second) | 
**credits_consumed** | **int** | Total credits &#x3D; ceil(conversation_credits + expression_credits + audio_credits) | 
**processing_ms** | **int** | Total processing time in milliseconds | 

## Example

```python
from falaai_api.models.whatsapp_usage import WhatsappUsage

# TODO update the JSON string below
json = "{}"
# create an instance of WhatsappUsage from a JSON string
whatsapp_usage_instance = WhatsappUsage.from_json(json)
# print the JSON string representation of the object
print(WhatsappUsage.to_json())

# convert the object into a dict
whatsapp_usage_dict = whatsapp_usage_instance.to_dict()
# create an instance of WhatsappUsage from a dict
whatsapp_usage_from_dict = WhatsappUsage.from_dict(whatsapp_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


