# WhatsappMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **str** | Uploaded file name | 
**chat_txt** | **str** | chat.txt entry name inside the export | 
**format** | **str** | Detected format: Android | iOS | 
**date_format** | **str** | Date order used | 
**timezone** | **str** | Timezone informed | 
**start** | **str** | Window start (ISO) | 
**end** | **str** | Window end (ISO) | 
**gap_minutes** | **float** | Gap used to split conversations | 
**min_messages** | **int** | Minimum messages per conversation | 
**chars_per_minute** | **float** | Chars per minute used to estimate duration | 
**turns** | **int** | Total parsed turns | 
**system_lines** | **int** | System lines ignored | 
**conversations_total** | **int** | Conversations before window filter | 
**conversations_in_window** | **int** | Conversations overlapping the window | 
**monologues_dropped** | **int** | Single-speaker conversations dropped | 
**conversations_selected** | **int** | Final conversations returned | 

## Example

```python
from falaai_api.models.whatsapp_meta import WhatsappMeta

# TODO update the JSON string below
json = "{}"
# create an instance of WhatsappMeta from a JSON string
whatsapp_meta_instance = WhatsappMeta.from_json(json)
# print the JSON string representation of the object
print(WhatsappMeta.to_json())

# convert the object into a dict
whatsapp_meta_dict = whatsapp_meta_instance.to_dict()
# create an instance of WhatsappMeta from a dict
whatsapp_meta_from_dict = WhatsappMeta.from_dict(whatsapp_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


