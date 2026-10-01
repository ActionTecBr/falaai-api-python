# falaai_api.EmailAlertsApi

All URIs are relative to *https://api01-falaai.action.tec.br*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_email_alert_v1_email_alerts_post**](EmailAlertsApi.md#create_email_alert_v1_email_alerts_post) | **POST** /v1/email-alerts | Create email alert
[**delete_email_alert_v1_email_alerts_alert_id_delete**](EmailAlertsApi.md#delete_email_alert_v1_email_alerts_alert_id_delete) | **DELETE** /v1/email-alerts/{alert_id} | Delete email alert
[**list_email_alerts_v1_email_alerts_get**](EmailAlertsApi.md#list_email_alerts_v1_email_alerts_get) | **GET** /v1/email-alerts | List email alerts
[**update_email_alert_v1_email_alerts_alert_id_put**](EmailAlertsApi.md#update_email_alert_v1_email_alerts_alert_id_put) | **PUT** /v1/email-alerts/{alert_id} | Update email alert


# **create_email_alert_v1_email_alerts_post**
> EmailAlertItem create_email_alert_v1_email_alerts_post(create_email_alert_request)

Create email alert

### Example

* Bearer (fai_xxx) Authentication (ApiKeyAuth):

```python
import falaai_api
from falaai_api.models.create_email_alert_request import CreateEmailAlertRequest
from falaai_api.models.email_alert_item import EmailAlertItem
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
    api_instance = falaai_api.EmailAlertsApi(api_client)
    create_email_alert_request = falaai_api.CreateEmailAlertRequest() # CreateEmailAlertRequest | 

    try:
        # Create email alert
        api_response = api_instance.create_email_alert_v1_email_alerts_post(create_email_alert_request)
        print("The response of EmailAlertsApi->create_email_alert_v1_email_alerts_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAlertsApi->create_email_alert_v1_email_alerts_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_email_alert_request** | [**CreateEmailAlertRequest**](CreateEmailAlertRequest.md)|  | 

### Return type

[**EmailAlertItem**](EmailAlertItem.md)

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

# **delete_email_alert_v1_email_alerts_alert_id_delete**
> EmailAlertMessageResponse delete_email_alert_v1_email_alerts_alert_id_delete(alert_id)

Delete email alert

### Example

* Bearer (fai_xxx) Authentication (ApiKeyAuth):

```python
import falaai_api
from falaai_api.models.email_alert_message_response import EmailAlertMessageResponse
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
    api_instance = falaai_api.EmailAlertsApi(api_client)
    alert_id = 'alert_id_example' # str | 

    try:
        # Delete email alert
        api_response = api_instance.delete_email_alert_v1_email_alerts_alert_id_delete(alert_id)
        print("The response of EmailAlertsApi->delete_email_alert_v1_email_alerts_alert_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAlertsApi->delete_email_alert_v1_email_alerts_alert_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **str**|  | 

### Return type

[**EmailAlertMessageResponse**](EmailAlertMessageResponse.md)

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

# **list_email_alerts_v1_email_alerts_get**
> EmailAlertListResponse list_email_alerts_v1_email_alerts_get(page=page, limit=limit)

List email alerts

### Example

* Bearer (fai_xxx) Authentication (ApiKeyAuth):

```python
import falaai_api
from falaai_api.models.email_alert_list_response import EmailAlertListResponse
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
    api_instance = falaai_api.EmailAlertsApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    limit = 20 # int |  (optional) (default to 20)

    try:
        # List email alerts
        api_response = api_instance.list_email_alerts_v1_email_alerts_get(page=page, limit=limit)
        print("The response of EmailAlertsApi->list_email_alerts_v1_email_alerts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAlertsApi->list_email_alerts_v1_email_alerts_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **limit** | **int**|  | [optional] [default to 20]

### Return type

[**EmailAlertListResponse**](EmailAlertListResponse.md)

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

# **update_email_alert_v1_email_alerts_alert_id_put**
> EmailAlertMessageResponse update_email_alert_v1_email_alerts_alert_id_put(alert_id, update_email_alert_request)

Update email alert

### Example

* Bearer (fai_xxx) Authentication (ApiKeyAuth):

```python
import falaai_api
from falaai_api.models.email_alert_message_response import EmailAlertMessageResponse
from falaai_api.models.update_email_alert_request import UpdateEmailAlertRequest
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
    api_instance = falaai_api.EmailAlertsApi(api_client)
    alert_id = 'alert_id_example' # str | 
    update_email_alert_request = falaai_api.UpdateEmailAlertRequest() # UpdateEmailAlertRequest | 

    try:
        # Update email alert
        api_response = api_instance.update_email_alert_v1_email_alerts_alert_id_put(alert_id, update_email_alert_request)
        print("The response of EmailAlertsApi->update_email_alert_v1_email_alerts_alert_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAlertsApi->update_email_alert_v1_email_alerts_alert_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **str**|  | 
 **update_email_alert_request** | [**UpdateEmailAlertRequest**](UpdateEmailAlertRequest.md)|  | 

### Return type

[**EmailAlertMessageResponse**](EmailAlertMessageResponse.md)

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

