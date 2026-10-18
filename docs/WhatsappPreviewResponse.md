# WhatsappPreviewResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Object type. Always &#39;whatsapp_preview&#39; | 
**dry_run** | **bool** | Always true (preview: no AI call, no charge) | 
**credits_charged** | **int** | Always 0 in preview | 
**credits_total** | **float** | TOTAL credits &#x3D; exact SUM of the selected conversations (2 decimals, NO rounding up) | 
**params** | [**WhatsappPreviewParams**](WhatsappPreviewParams.md) | Filter parameters actually used (reuse them in the extraction) | 
**windows** | [**List[WhatsappPreviewWindow]**](WhatsappPreviewWindow.md) | Explicit windows used (empty when a single start/end range was used) | 
**items** | [**List[WhatsappPreviewItem]**](WhatsappPreviewItem.md) | Per-conversation detail (send back as &#x60;windows&#x60; to extract only what you want) | 
**warnings** | **List[str]** | Human-readable notices about what would be ignored | 

## Example

```python
from falaai_api.models.whatsapp_preview_response import WhatsappPreviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WhatsappPreviewResponse from a JSON string
whatsapp_preview_response_instance = WhatsappPreviewResponse.from_json(json)
# print the JSON string representation of the object
print(WhatsappPreviewResponse.to_json())

# convert the object into a dict
whatsapp_preview_response_dict = whatsapp_preview_response_instance.to_dict()
# create an instance of WhatsappPreviewResponse from a dict
whatsapp_preview_response_from_dict = WhatsappPreviewResponse.from_dict(whatsapp_preview_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


