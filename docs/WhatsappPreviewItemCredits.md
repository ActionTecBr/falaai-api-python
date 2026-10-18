# WhatsappPreviewItemCredits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** | Credits of THIS conversation (2 decimals, exact fraction — the charge is ONE ceil on the batch total) | 
**breakdown** | [**WhatsappPreviewItemBreakdown**](WhatsappPreviewItemBreakdown.md) | Credits by component for THIS conversation | 

## Example

```python
from falaai_api.models.whatsapp_preview_item_credits import WhatsappPreviewItemCredits

# TODO update the JSON string below
json = "{}"
# create an instance of WhatsappPreviewItemCredits from a JSON string
whatsapp_preview_item_credits_instance = WhatsappPreviewItemCredits.from_json(json)
# print the JSON string representation of the object
print(WhatsappPreviewItemCredits.to_json())

# convert the object into a dict
whatsapp_preview_item_credits_dict = whatsapp_preview_item_credits_instance.to_dict()
# create an instance of WhatsappPreviewItemCredits from a dict
whatsapp_preview_item_credits_from_dict = WhatsappPreviewItemCredits.from_dict(whatsapp_preview_item_credits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


