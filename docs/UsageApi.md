# falaai_api.UsageApi

All URIs are relative to *https://api01-falaai.action.tec.br*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_usage_by_key_v1_usage_by_key_get**](UsageApi.md#get_usage_by_key_v1_usage_by_key_get) | **GET** /v1/usage/by-key | Get Usage By Key
[**get_usage_log_v1_usage_log_get**](UsageApi.md#get_usage_log_v1_usage_log_get) | **GET** /v1/usage/log | Get Usage Log


# **get_usage_by_key_v1_usage_by_key_get**
> List[UsageByKeyItem] get_usage_by_key_v1_usage_by_key_get(key_id=key_id)

Get Usage By Key

### Example

* Bearer (fai_xxx) Authentication (ApiKeyAuth):

```python
import falaai_api
from falaai_api.models.usage_by_key_item import UsageByKeyItem
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
    api_instance = falaai_api.UsageApi(api_client)
    key_id = 'key_id_example' # str |  (optional)

    try:
        # Get Usage By Key
        api_response = api_instance.get_usage_by_key_v1_usage_by_key_get(key_id=key_id)
        print("The response of UsageApi->get_usage_by_key_v1_usage_by_key_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->get_usage_by_key_v1_usage_by_key_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**|  | [optional] 

### Return type

[**List[UsageByKeyItem]**](UsageByKeyItem.md)

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

# **get_usage_log_v1_usage_log_get**
> UsageLogResponse get_usage_log_v1_usage_log_get(page=page, limit=limit, api_key_id=api_key_id)

Get Usage Log

### Example

* Bearer (fai_xxx) Authentication (ApiKeyAuth):

```python
import falaai_api
from falaai_api.models.usage_log_response import UsageLogResponse
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
    api_instance = falaai_api.UsageApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    limit = 20 # int |  (optional) (default to 20)
    api_key_id = 'api_key_id_example' # str |  (optional)

    try:
        # Get Usage Log
        api_response = api_instance.get_usage_log_v1_usage_log_get(page=page, limit=limit, api_key_id=api_key_id)
        print("The response of UsageApi->get_usage_log_v1_usage_log_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->get_usage_log_v1_usage_log_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **limit** | **int**|  | [optional] [default to 20]
 **api_key_id** | **str**|  | [optional] 

### Return type

[**UsageLogResponse**](UsageLogResponse.md)

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

