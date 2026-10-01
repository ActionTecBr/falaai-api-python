# UpdateWebhookRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Nome identificador | [optional] 
**url** | **str** | URL HTTPS destino | [optional] 
**events** | [**List[WebhookEvent]**](WebhookEvent.md) | Eventos subscritos | [optional] 
**retry_enabled** | **bool** | Habilita retry exponencial | [optional] 
**active** | **bool** | Ativa/desativa sem deletar | [optional] 

## Example

```python
from falaai_api.models.update_webhook_request import UpdateWebhookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWebhookRequest from a JSON string
update_webhook_request_instance = UpdateWebhookRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateWebhookRequest.to_json())

# convert the object into a dict
update_webhook_request_dict = update_webhook_request_instance.to_dict()
# create an instance of UpdateWebhookRequest from a dict
update_webhook_request_from_dict = UpdateWebhookRequest.from_dict(update_webhook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


