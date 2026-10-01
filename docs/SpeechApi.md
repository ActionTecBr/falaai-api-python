# falaai_api.SpeechApi

All URIs are relative to *https://api01-falaai.action.tec.br*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_transcription_v1_audio_transcriptions_post**](SpeechApi.md#create_transcription_v1_audio_transcriptions_post) | **POST** /v1/audio/transcriptions | Transcribe audio to text


# **create_transcription_v1_audio_transcriptions_post**
> TranscriptionResponse create_transcription_v1_audio_transcriptions_post(file, model=model, language=language, client_reference_id=client_reference_id)

Transcribe audio to text

### Example

* Bearer (fai_xxx) Authentication (ApiKeyAuth):

```python
import falaai_api
from falaai_api.models.transcription_response import TranscriptionResponse
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
    api_instance = falaai_api.SpeechApi(api_client)
    file = None # bytes | 
    model = 'falaai-transcribe-1' # str |  (optional) (default to 'falaai-transcribe-1')
    language = 'pt' # str |  (optional) (default to 'pt')
    client_reference_id = 'client_reference_id_example' # str | Optional client-supplied ID echoed verbatim in the response. Use to correlate/sync with your system. Accepted charset: [A-Za-z0-9._:-]. Not idempotency. (optional)

    try:
        # Transcribe audio to text
        api_response = api_instance.create_transcription_v1_audio_transcriptions_post(file, model=model, language=language, client_reference_id=client_reference_id)
        print("The response of SpeechApi->create_transcription_v1_audio_transcriptions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpeechApi->create_transcription_v1_audio_transcriptions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytes**|  | 
 **model** | **str**|  | [optional] [default to &#39;falaai-transcribe-1&#39;]
 **language** | **str**|  | [optional] [default to &#39;pt&#39;]
 **client_reference_id** | **str**| Optional client-supplied ID echoed verbatim in the response. Use to correlate/sync with your system. Accepted charset: [A-Za-z0-9._:-]. Not idempotency. | [optional] 

### Return type

[**TranscriptionResponse**](TranscriptionResponse.md)

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

