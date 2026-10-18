# falaai_api.SpeechApi

All URIs are relative to *https://api01-falaai.action.tec.br*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_transcription_v1_audio_transcriptions_post**](SpeechApi.md#create_transcription_v1_audio_transcriptions_post) | **POST** /v1/audio/transcriptions | Transcribe audio to text


# **create_transcription_v1_audio_transcriptions_post**
> TranscriptionResponse create_transcription_v1_audio_transcriptions_post(file, model=model, language=language, client_reference_id=client_reference_id)

Transcribe audio to text

Transcribes one uploaded audio file into text with speaker diarization and timestamped audio events (laughs, sighs, pauses), returning the full transcript, a turn-by-turn dialog with speaker labels and start/end timestamps, the detected events and the word count. Use it when a recording must become text for analysis, review or storage of the transcript. The required file field takes a single audio upload limited to 1GB and 3 hours, with accepted MIME types audio/mpeg, audio/mp3, audio/mp4, audio/m4a, audio/wav, audio/wave, audio/x-wav, audio/flac, audio/x-flac, audio/ogg, audio/opus, video/ogg, audio/webm, video/webm, audio/aac and audio/x-aac. model is optional and defaults to falaai-transcribe-1, the only supported value; language is an optional two-letter code (pt, en, es, fr, de, it, ja, ko, nl, pl, ru, tr, zh, vi, id, th, ar, hi, cs, da, el, fi, he, hu, ms, no, ro, sk, sv, ta, uk) that forces the audio language and is auto-detected when omitted; client_reference_id is optional, charset A-Za-z0-9 space _/:.- up to 60 chars, echoed verbatim (not idempotency). Billing is 1 credit per second of processed audio with a minimum of 10 credits per request, rounded to 2 decimals; usage reports credits_consumed and processing_ms. Stateless: the audio is processed in memory and never persisted (LGPD). Returns id (tr-), language, language_confidence, duration_seconds, text, dialog, audio_events, event_types, word_count and input metadata (duration, format, codec, sample rate, channels).

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
    language = 'language_example' # str |  (optional)
    client_reference_id = 'client_reference_id_example' # str | Optional client-supplied ID echoed verbatim in the response. Use to correlate/sync with your system. Accepted charset: [A-Za-z0-9 _/:.-], max 60 chars. Not idempotency. (optional)

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
 **language** | **str**|  | [optional] 
 **client_reference_id** | **str**| Optional client-supplied ID echoed verbatim in the response. Use to correlate/sync with your system. Accepted charset: [A-Za-z0-9 _/:.-], max 60 chars. Not idempotency. | [optional] 

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

