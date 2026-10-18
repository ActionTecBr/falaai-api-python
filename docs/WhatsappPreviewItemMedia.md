# WhatsappPreviewItemMedia


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**figurinha** | **int** | Figurinha occurrences in this conversation (0 quando expression&#x3D;false) | 
**gif** | **int** | GIF occurrences in this conversation (0 quando expression&#x3D;false) | 
**emoji** | **int** | Emoji occurrences in this conversation (0 quando expression&#x3D;false) | 
**ptt** | **int** | Voice/audio/video turns in this conversation (cobra 0,19/segundo SO quando voice_note&#x3D;true) | 
**ptt_seconds** | **float** | Voice/video SECONDS counted in this conversation (0 quando voice_note&#x3D;false) | 
**anexos** | **int** | Image/document turns in this conversation (ANEXO: nunca cobrado) | 
**by_type** | **Dict[str, int]** | Media turns by type in THIS conversation (voz/audio/video/imagem/figurinha/gif/arquivo/oculta/chamada) | 

## Example

```python
from falaai_api.models.whatsapp_preview_item_media import WhatsappPreviewItemMedia

# TODO update the JSON string below
json = "{}"
# create an instance of WhatsappPreviewItemMedia from a JSON string
whatsapp_preview_item_media_instance = WhatsappPreviewItemMedia.from_json(json)
# print the JSON string representation of the object
print(WhatsappPreviewItemMedia.to_json())

# convert the object into a dict
whatsapp_preview_item_media_dict = whatsapp_preview_item_media_instance.to_dict()
# create an instance of WhatsappPreviewItemMedia from a dict
whatsapp_preview_item_media_from_dict = WhatsappPreviewItemMedia.from_dict(whatsapp_preview_item_media_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


