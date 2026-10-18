# WhatsappPreviewParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **str** | Window start actually used (file period when start/end are omitted in dry_run) | 
**end** | **str** | Window end actually used (file period when start/end are omitted in dry_run) | 
**timezone** | **str** | Timezone informed | 
**date_format** | **str** | Date order used | 
**gap_minutes** | **float** | Gap used to split conversations | 
**min_messages** | **int** | Minimum messages per conversation | 
**voice_note** | **bool** | Voice/video medias would be transcribed (charge flag) | 
**expression** | **bool** | Visual expressions would be described (charge flag) | 

## Example

```python
from falaai_api.models.whatsapp_preview_params import WhatsappPreviewParams

# TODO update the JSON string below
json = "{}"
# create an instance of WhatsappPreviewParams from a JSON string
whatsapp_preview_params_instance = WhatsappPreviewParams.from_json(json)
# print the JSON string representation of the object
print(WhatsappPreviewParams.to_json())

# convert the object into a dict
whatsapp_preview_params_dict = whatsapp_preview_params_instance.to_dict()
# create an instance of WhatsappPreviewParams from a dict
whatsapp_preview_params_from_dict = WhatsappPreviewParams.from_dict(whatsapp_preview_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


