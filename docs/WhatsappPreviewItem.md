# WhatsappPreviewItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_id** | **str** | Stable id: yyyymmddhhmm-&lt;first speaker&gt;[-xN for &gt;2 speakers] | 
**first_at** | **str** | Conversation start (ISO) | 
**last_at** | **str** | Conversation end (ISO) | 
**duration_minutes** | **float** | Conversation duration in minutes | 
**messages** | **int** | Messages in this conversation | 
**characters** | **int** | Characters of this conversation (estimate: media text is only replaced by tokens on extraction) | 
**media** | [**WhatsappPreviewItemMedia**](WhatsappPreviewItemMedia.md) | Media of this conversation | 
**credits** | [**WhatsappPreviewItemCredits**](WhatsappPreviewItemCredits.md) | Credits of this conversation | 

## Example

```python
from falaai_api.models.whatsapp_preview_item import WhatsappPreviewItem

# TODO update the JSON string below
json = "{}"
# create an instance of WhatsappPreviewItem from a JSON string
whatsapp_preview_item_instance = WhatsappPreviewItem.from_json(json)
# print the JSON string representation of the object
print(WhatsappPreviewItem.to_json())

# convert the object into a dict
whatsapp_preview_item_dict = whatsapp_preview_item_instance.to_dict()
# create an instance of WhatsappPreviewItem from a dict
whatsapp_preview_item_from_dict = WhatsappPreviewItem.from_dict(whatsapp_preview_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


