# falaai_api.VersionApi

All URIs are relative to *https://api01-falaai.action.tec.br*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_version_api_version_get**](VersionApi.md#get_version_api_version_get) | **GET** /api/version | Get Version


# **get_version_api_version_get**
> VersionResponse get_version_api_version_get()

Get Version

### Example


```python
import falaai_api
from falaai_api.models.version_response import VersionResponse
from falaai_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api01-falaai.action.tec.br
# See configuration.py for a list of all supported configuration parameters.
configuration = falaai_api.Configuration(
    host = "https://api01-falaai.action.tec.br"
)


# Enter a context with an instance of the API client
with falaai_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = falaai_api.VersionApi(api_client)

    try:
        # Get Version
        api_response = api_instance.get_version_api_version_get()
        print("The response of VersionApi->get_version_api_version_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VersionApi->get_version_api_version_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**VersionResponse**](VersionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

