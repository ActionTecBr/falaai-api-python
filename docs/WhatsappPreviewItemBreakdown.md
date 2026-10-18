# WhatsappPreviewItemBreakdown


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation** | **float** | Conversation credit (0,15) | 
**figurinha** | **float** | Figurinha credits of this conversation | 
**gif** | **float** | GIF credits of this conversation | 
**emoji** | **float** | Emoji credits of this conversation | 
**audio** | **float** | Audio credits of this conversation | 

## Example

```python
from falaai_api.models.whatsapp_preview_item_breakdown import WhatsappPreviewItemBreakdown

# TODO update the JSON string below
json = "{}"
# create an instance of WhatsappPreviewItemBreakdown from a JSON string
whatsapp_preview_item_breakdown_instance = WhatsappPreviewItemBreakdown.from_json(json)
# print the JSON string representation of the object
print(WhatsappPreviewItemBreakdown.to_json())

# convert the object into a dict
whatsapp_preview_item_breakdown_dict = whatsapp_preview_item_breakdown_instance.to_dict()
# create an instance of WhatsappPreviewItemBreakdown from a dict
whatsapp_preview_item_breakdown_from_dict = WhatsappPreviewItemBreakdown.from_dict(whatsapp_preview_item_breakdown_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


