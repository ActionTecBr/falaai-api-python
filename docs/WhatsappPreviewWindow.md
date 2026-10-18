# WhatsappPreviewWindow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **str** | Window start used | 
**end** | **str** | Window end used | 
**selected** | **int** | Conversations matched by THIS window (before the union dedupe) | 

## Example

```python
from falaai_api.models.whatsapp_preview_window import WhatsappPreviewWindow

# TODO update the JSON string below
json = "{}"
# create an instance of WhatsappPreviewWindow from a JSON string
whatsapp_preview_window_instance = WhatsappPreviewWindow.from_json(json)
# print the JSON string representation of the object
print(WhatsappPreviewWindow.to_json())

# convert the object into a dict
whatsapp_preview_window_dict = whatsapp_preview_window_instance.to_dict()
# create an instance of WhatsappPreviewWindow from a dict
whatsapp_preview_window_from_dict = WhatsappPreviewWindow.from_dict(whatsapp_preview_window_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


