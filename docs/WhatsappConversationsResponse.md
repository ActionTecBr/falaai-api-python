# WhatsappConversationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier. Prefix &#39;wc-&#39; + UUID | 
**object** | **str** | Object type. Always &#39;conversations&#39; | 
**usage** | [**WhatsappUsage**](WhatsappUsage.md) | Usage and processing information | 
**conversations** | [**List[WhatsappConversation]**](WhatsappConversation.md) | Segmented conversations | 
**client_reference_id** | **str** | Client-supplied ID echoed verbatim (if provided) | [optional] 
**meta** | [**WhatsappMeta**](WhatsappMeta.md) | Segmentation parameters and counts | 

## Example

```python
from falaai_api.models.whatsapp_conversations_response import WhatsappConversationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WhatsappConversationsResponse from a JSON string
whatsapp_conversations_response_instance = WhatsappConversationsResponse.from_json(json)
# print the JSON string representation of the object
print(WhatsappConversationsResponse.to_json())

# convert the object into a dict
whatsapp_conversations_response_dict = whatsapp_conversations_response_instance.to_dict()
# create an instance of WhatsappConversationsResponse from a dict
whatsapp_conversations_response_from_dict = WhatsappConversationsResponse.from_dict(whatsapp_conversations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


