# falaai_api.WhatsappApi

All URIs are relative to *https://api01-falaai.action.tec.br*

Method | HTTP request | Description
------------- | ------------- | -------------
[**extract_conversations_v1_whatsapp_extract_conversations_post**](WhatsappApi.md#extract_conversations_v1_whatsapp_extract_conversations_post) | **POST** /v1/whatsapp/extractConversations | Extract and segment WhatsApp conversations from an export


# **extract_conversations_v1_whatsapp_extract_conversations_post**
> WhatsappConversationsResponse extract_conversations_v1_whatsapp_extract_conversations_post(file, start, end, timezone, date_format, gap_minutes=gap_minutes, min_messages=min_messages, chars_per_minute=chars_per_minute, client_reference_id=client_reference_id)

Extract and segment WhatsApp conversations from an export

### Example

* Bearer (fai_xxx) Authentication (ApiKeyAuth):

```python
import falaai_api
from falaai_api.models.whatsapp_conversations_response import WhatsappConversationsResponse
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
    api_instance = falaai_api.WhatsappApi(api_client)
    file = None # bytes | 
    start = 'start_example' # str | 
    end = 'end_example' # str | 
    timezone = 'timezone_example' # str | 
    date_format = 'date_format_example' # str | 
    gap_minutes = 720 # float |  (optional) (default to 720)
    min_messages = 2 # int |  (optional) (default to 2)
    chars_per_minute = 800 # float |  (optional) (default to 800)
    client_reference_id = 'client_reference_id_example' # str |  (optional)

    try:
        # Extract and segment WhatsApp conversations from an export
        api_response = api_instance.extract_conversations_v1_whatsapp_extract_conversations_post(file, start, end, timezone, date_format, gap_minutes=gap_minutes, min_messages=min_messages, chars_per_minute=chars_per_minute, client_reference_id=client_reference_id)
        print("The response of WhatsappApi->extract_conversations_v1_whatsapp_extract_conversations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WhatsappApi->extract_conversations_v1_whatsapp_extract_conversations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytes**|  | 
 **start** | **str**|  | 
 **end** | **str**|  | 
 **timezone** | **str**|  | 
 **date_format** | **str**|  | 
 **gap_minutes** | **float**|  | [optional] [default to 720]
 **min_messages** | **int**|  | [optional] [default to 2]
 **chars_per_minute** | **float**|  | [optional] [default to 800]
 **client_reference_id** | **str**|  | [optional] 

### Return type

[**WhatsappConversationsResponse**](WhatsappConversationsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

