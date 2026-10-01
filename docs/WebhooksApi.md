# falaai_api.WebhooksApi

All URIs are relative to *https://api01-falaai.action.tec.br*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook_v1_webhooks_post**](WebhooksApi.md#create_webhook_v1_webhooks_post) | **POST** /v1/webhooks | Create webhook
[**delete_webhook_v1_webhooks_webhook_id_delete**](WebhooksApi.md#delete_webhook_v1_webhooks_webhook_id_delete) | **DELETE** /v1/webhooks/{webhook_id} | Delete webhook
[**list_webhooks_v1_webhooks_get**](WebhooksApi.md#list_webhooks_v1_webhooks_get) | **GET** /v1/webhooks | List webhooks
[**update_webhook_v1_webhooks_webhook_id_put**](WebhooksApi.md#update_webhook_v1_webhooks_webhook_id_put) | **PUT** /v1/webhooks/{webhook_id} | Update webhook


# **create_webhook_v1_webhooks_post**
> WebhookItem create_webhook_v1_webhooks_post(create_webhook_request)

Create webhook

Creates a subscription for alert events (10 alerts). Payload delivered: WebhookPayload(event, data, timestamp) with HMAC FalaAI-Signature. To verify the origin, recompute HMAC-SHA256 of "timestamp.body" with your secret.

### Example

* Bearer (fai_xxx) Authentication (ApiKeyAuth):

```python
import falaai_api
from falaai_api.models.create_webhook_request import CreateWebhookRequest
from falaai_api.models.webhook_item import WebhookItem
from falaai_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api01-falaai.action.tec.br
# See configuration.py for a list of all supported configuration parameters.
configuration = falaai_api.Configuration(
    host = "https://api01-falaai.action.tec.br"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (fai_xxx): ApiKeyAuth
configuration = falaai_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with falaai_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = falaai_api.WebhooksApi(api_client)
    create_webhook_request = falaai_api.CreateWebhookRequest() # CreateWebhookRequest | 

    try:
        # Create webhook
        api_response = api_instance.create_webhook_v1_webhooks_post(create_webhook_request)
        print("The response of WebhooksApi->create_webhook_v1_webhooks_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->create_webhook_v1_webhooks_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_webhook_request** | [**CreateWebhookRequest**](CreateWebhookRequest.md)|  | 

### Return type

[**WebhookItem**](WebhookItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook_v1_webhooks_webhook_id_delete**
> MessageResponse delete_webhook_v1_webhooks_webhook_id_delete(webhook_id)

Delete webhook

Deletes a webhook subscription by ID.

### Example

* Bearer (fai_xxx) Authentication (ApiKeyAuth):

```python
import falaai_api
from falaai_api.models.message_response import MessageResponse
from falaai_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api01-falaai.action.tec.br
# See configuration.py for a list of all supported configuration parameters.
configuration = falaai_api.Configuration(
    host = "https://api01-falaai.action.tec.br"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (fai_xxx): ApiKeyAuth
configuration = falaai_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with falaai_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = falaai_api.WebhooksApi(api_client)
    webhook_id = 'webhook_id_example' # str | 

    try:
        # Delete webhook
        api_response = api_instance.delete_webhook_v1_webhooks_webhook_id_delete(webhook_id)
        print("The response of WebhooksApi->delete_webhook_v1_webhooks_webhook_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->delete_webhook_v1_webhooks_webhook_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**|  | 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_webhooks_v1_webhooks_get**
> WebhookListResponse list_webhooks_v1_webhooks_get(page=page, limit=limit)

List webhooks

Lists the authenticated user's webhooks (10 alerts). Paginated. Includes the URL signature secret (always visible to the owner).

### Example

* Bearer (fai_xxx) Authentication (ApiKeyAuth):

```python
import falaai_api
from falaai_api.models.webhook_list_response import WebhookListResponse
from falaai_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api01-falaai.action.tec.br
# See configuration.py for a list of all supported configuration parameters.
configuration = falaai_api.Configuration(
    host = "https://api01-falaai.action.tec.br"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (fai_xxx): ApiKeyAuth
configuration = falaai_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with falaai_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = falaai_api.WebhooksApi(api_client)
    page = 1 # int | Pagina (1-indexed) (optional) (default to 1)
    limit = 20 # int | Itens por pagina (max 100) (optional) (default to 20)

    try:
        # List webhooks
        api_response = api_instance.list_webhooks_v1_webhooks_get(page=page, limit=limit)
        print("The response of WebhooksApi->list_webhooks_v1_webhooks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->list_webhooks_v1_webhooks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Pagina (1-indexed) | [optional] [default to 1]
 **limit** | **int**| Itens por pagina (max 100) | [optional] [default to 20]

### Return type

[**WebhookListResponse**](WebhookListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook_v1_webhooks_webhook_id_put**
> MessageResponse update_webhook_v1_webhooks_webhook_id_put(webhook_id, update_webhook_request)

Update webhook

Updates the webhook's name/url/events/retry_enabled/active. Valid events: 10 alerts.

### Example

* Bearer (fai_xxx) Authentication (ApiKeyAuth):

```python
import falaai_api
from falaai_api.models.message_response import MessageResponse
from falaai_api.models.update_webhook_request import UpdateWebhookRequest
from falaai_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api01-falaai.action.tec.br
# See configuration.py for a list of all supported configuration parameters.
configuration = falaai_api.Configuration(
    host = "https://api01-falaai.action.tec.br"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (fai_xxx): ApiKeyAuth
configuration = falaai_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with falaai_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = falaai_api.WebhooksApi(api_client)
    webhook_id = 'webhook_id_example' # str | 
    update_webhook_request = falaai_api.UpdateWebhookRequest() # UpdateWebhookRequest | 

    try:
        # Update webhook
        api_response = api_instance.update_webhook_v1_webhooks_webhook_id_put(webhook_id, update_webhook_request)
        print("The response of WebhooksApi->update_webhook_v1_webhooks_webhook_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->update_webhook_v1_webhooks_webhook_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**|  | 
 **update_webhook_request** | [**UpdateWebhookRequest**](UpdateWebhookRequest.md)|  | 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

