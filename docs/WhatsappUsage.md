# WhatsappUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversations** | **int** | Number of conversations returned | 
**characters** | **int** | Total characters across conversations | 
**expressions** | **int** | Chargeable expression occurrences (figurinha+GIF+emoji); 0 quando expression&#x3D;false | 
**expressions_figurinha** | **int** | Figurinha occurrences (cobra 0,15 cada quando expression&#x3D;true) | 
**expressions_gif** | **int** | GIF occurrences (cobra 0,18 cada quando expression&#x3D;true) | 
**expressions_emoji** | **int** | Emoji occurrences (cobra 0,1 cada quando expression&#x3D;true) | 
**voice_notes** | **int** | Voice notes (PTT) resolved to text | 
**conversation_credits** | **float** | Credits for conversations (0,15 each) | 
**expression_credits** | **float** | Credits for expressions (figurinha 0,15 / GIF 0,18 / emoji 0,1) | 
**audio_credits** | **float** | Credits for transcribed voice seconds (0,19 per second; 0 quando voice_note&#x3D;false) | 
**credits_consumed** | **float** | Total credits &#x3D; round(conversation_credits + expression_credits + audio_credits, 2) | 
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


