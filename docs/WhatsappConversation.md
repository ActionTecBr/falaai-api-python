# WhatsappConversation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_id** | **str** | Conversation identifier in the batch | 
**first_at** | **str** | Real start (wall-clock, ISO) | 
**last_at** | **str** | Real end (wall-clock, ISO) | 
**duration_seconds** | **float** | (last - first) + last turn duration | 
**speakers** | [**List[WhatsappSpeaker]**](WhatsappSpeaker.md) | Speakers of THIS conversation (dynamic) | 
**dialog** | **str** | Lines &#39;Speaker N: [HH:MM:SS.mmm - HH:MM:SS.mmm] text&#39; (real offset) | 
**message_count** | **int** | Number of messages | 
**characters** | **int** | Total characters of the conversation | 

## Example

```python
from falaai_api.models.whatsapp_conversation import WhatsappConversation

# TODO update the JSON string below
json = "{}"
# create an instance of WhatsappConversation from a JSON string
whatsapp_conversation_instance = WhatsappConversation.from_json(json)
# print the JSON string representation of the object
print(WhatsappConversation.to_json())

# convert the object into a dict
whatsapp_conversation_dict = whatsapp_conversation_instance.to_dict()
# create an instance of WhatsappConversation from a dict
whatsapp_conversation_from_dict = WhatsappConversation.from_dict(whatsapp_conversation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


