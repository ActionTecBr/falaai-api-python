# ResponseExtractConversationsV1WhatsappExtractconversationsPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier. Prefix &#39;wc-&#39; + UUID | 
**object** | **str** | Object type. Always &#39;whatsapp_preview&#39; | 
**usage** | [**WhatsappUsage**](WhatsappUsage.md) | Usage and processing information | 
**conversations** | [**List[WhatsappConversation]**](WhatsappConversation.md) | Segmented conversations | 
**client_reference_id** | **str** | Client-supplied ID echoed verbatim (if provided) | [optional] 
**meta** | [**WhatsappMeta**](WhatsappMeta.md) | Segmentation parameters and counts | 
**dry_run** | **bool** | Always true (preview: no AI call, no charge) | 
**credits_charged** | **int** | Always 0 in preview | 
**credits_total** | **float** | TOTAL credits &#x3D; exact SUM of the selected conversations (2 decimals, NO rounding up) | 
**params** | [**WhatsappPreviewParams**](WhatsappPreviewParams.md) | Filter parameters actually used (reuse them in the extraction) | 
**windows** | [**List[WhatsappPreviewWindow]**](WhatsappPreviewWindow.md) | Explicit windows used (empty when a single start/end range was used) | 
**items** | [**List[WhatsappPreviewItem]**](WhatsappPreviewItem.md) | Per-conversation detail (send back as &#x60;windows&#x60; to extract only what you want) | 
**warnings** | **List[str]** | Human-readable notices about what would be ignored | 

## Example

```python
from falaai_api.models.response_extract_conversations_v1_whatsapp_extractconversations_post import ResponseExtractConversationsV1WhatsappExtractconversationsPost

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseExtractConversationsV1WhatsappExtractconversationsPost from a JSON string
response_extract_conversations_v1_whatsapp_extractconversations_post_instance = ResponseExtractConversationsV1WhatsappExtractconversationsPost.from_json(json)
# print the JSON string representation of the object
print(ResponseExtractConversationsV1WhatsappExtractconversationsPost.to_json())

# convert the object into a dict
response_extract_conversations_v1_whatsapp_extractconversations_post_dict = response_extract_conversations_v1_whatsapp_extractconversations_post_instance.to_dict()
# create an instance of ResponseExtractConversationsV1WhatsappExtractconversationsPost from a dict
response_extract_conversations_v1_whatsapp_extractconversations_post_from_dict = ResponseExtractConversationsV1WhatsappExtractconversationsPost.from_dict(response_extract_conversations_v1_whatsapp_extractconversations_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


