# falaai_api.WhatsappApi

All URIs are relative to *https://api01-falaai.action.tec.br*

Method | HTTP request | Description
------------- | ------------- | -------------
[**extract_conversations_v1_whatsapp_extract_conversations_post**](WhatsappApi.md#extract_conversations_v1_whatsapp_extract_conversations_post) | **POST** /v1/whatsapp/extractConversations | Extract and segment WhatsApp conversations from an export


# **extract_conversations_v1_whatsapp_extract_conversations_post**
> ResponseExtractConversationsV1WhatsappExtractconversationsPost extract_conversations_v1_whatsapp_extract_conversations_post(file, timezone, date_format, start=start, end=end, windows=windows, gap_minutes=gap_minutes, min_messages=min_messages, voice_note=voice_note, expression=expression, dry_run=dry_run, client_reference_id=client_reference_id)

Extract and segment WhatsApp conversations from an export

Extracts and segments the conversations of a WhatsApp export (.zip or .txt containing chat.txt in UTF-8 with at least one turn) and, unless it is a preview, resolves each selected conversation with AI by transcribing voice/audio/video notes and describing visual expressions, returning the segmented conversations with speakers, dialogs, counts and usage. Use dry_run=true for a PREVIEW: it validates the file, segments the conversations, counts media and ESTIMATES the credits WITHOUT calling the AI and WITHOUT charging (credits_charged=0), returning object whatsapp_preview with credits_total, the params actually used, the windows, per-conversation items and warnings. The window is given either as a single start/end pair or as windows, a JSON string holding a non-empty list of sub-objects each with start and end; windows must not be combined with start/end, and a windows selection is the deduplicated chronological union of the overlaps, which bypasses the noise filter and keeps conversations that are monologues or below min_messages, while for a single window sending only one of start/end is rejected and empty/all-zeros values select the real period of the export, both being allowed to be omitted in dry_run while outside dry_run both absent is rejected. timezone and date_format are required, where date_format must be day_first, month_first or year_first. gap_minutes is optional (default 720) and splits conversations on idle gaps, min_messages is optional (default 2) and is the minimum messages kept per conversation outside the explicit windows selection, voice_note is optional (default true) and turns voice/audio/video media into text, expression is optional (default true) and describes visual expressions (figurinha, GIF, emoji), and client_reference_id is optional, echoed verbatim, charset A-Za-z0-9 space _/:.- up to 60 chars. Billing outside the preview is 0.15 credit per conversation plus 0.15 per figurinha, 0.18 per GIF and 0.1 per emoji (only with expression=true) plus 0.19 per second of voice/audio/video (only with voice_note=true), rounded to 2 decimals with no rounding up, and the preview credits_total is the same exact sum with 2 decimals; files are limited to 1GB and the endpoint is stateless (export and media processed in memory, temporary files removed, nothing persisted), returning object conversations with id (wc-), usage and the conversations (conversation_id, first_at, last_at, duration_seconds, speakers, dialog, message_count, characters) plus meta.

### Example

* Bearer (fai_xxx) Authentication (ApiKeyAuth):

```python
import falaai_api
from falaai_api.models.response_extract_conversations_v1_whatsapp_extractconversations_post import ResponseExtractConversationsV1WhatsappExtractconversationsPost
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
    timezone = 'timezone_example' # str | 
    date_format = 'date_format_example' # str | 
    start = 'start_example' # str | Inicio da janela. Obrigatorio fora do dry_run; no dry_run ausente = primeiro turno do export. (optional)
    end = 'end_example' # str | Fim da janela. Obrigatorio fora do dry_run; no dry_run ausente = ultimo turno do export. (optional)
    windows = 'windows_example' # str | Selecao explicita por varias janelas: JSON [{\\\"start\\\":\\\"...\\\",\\\"end\\\":\\\"...\\\"}]. Nao combinar com 'start'/'end'. (optional)
    gap_minutes = 720 # float |  (optional) (default to 720)
    min_messages = 2 # int |  (optional) (default to 2)
    voice_note = True # bool | Transcrever mensagens de voz/video gravadas na hora? (optional) (default to True)
    expression = True # bool | Descrever expressoes visuais (figurinha/GIF/imagem)? (optional) (default to True)
    dry_run = False # bool | So analisa o arquivo: valida, segmenta e ESTIMA os creditos SEM chamar a IA e SEM debitar (credits_charged=0). (optional) (default to False)
    client_reference_id = 'client_reference_id_example' # str |  (optional)

    try:
        # Extract and segment WhatsApp conversations from an export
        api_response = api_instance.extract_conversations_v1_whatsapp_extract_conversations_post(file, timezone, date_format, start=start, end=end, windows=windows, gap_minutes=gap_minutes, min_messages=min_messages, voice_note=voice_note, expression=expression, dry_run=dry_run, client_reference_id=client_reference_id)
        print("The response of WhatsappApi->extract_conversations_v1_whatsapp_extract_conversations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WhatsappApi->extract_conversations_v1_whatsapp_extract_conversations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytes**|  | 
 **timezone** | **str**|  | 
 **date_format** | **str**|  | 
 **start** | **str**| Inicio da janela. Obrigatorio fora do dry_run; no dry_run ausente &#x3D; primeiro turno do export. | [optional] 
 **end** | **str**| Fim da janela. Obrigatorio fora do dry_run; no dry_run ausente &#x3D; ultimo turno do export. | [optional] 
 **windows** | **str**| Selecao explicita por varias janelas: JSON [{\\\&quot;start\\\&quot;:\\\&quot;...\\\&quot;,\\\&quot;end\\\&quot;:\\\&quot;...\\\&quot;}]. Nao combinar com &#39;start&#39;/&#39;end&#39;. | [optional] 
 **gap_minutes** | **float**|  | [optional] [default to 720]
 **min_messages** | **int**|  | [optional] [default to 2]
 **voice_note** | **bool**| Transcrever mensagens de voz/video gravadas na hora? | [optional] [default to True]
 **expression** | **bool**| Descrever expressoes visuais (figurinha/GIF/imagem)? | [optional] [default to True]
 **dry_run** | **bool**| So analisa o arquivo: valida, segmenta e ESTIMA os creditos SEM chamar a IA e SEM debitar (credits_charged&#x3D;0). | [optional] [default to False]
 **client_reference_id** | **str**|  | [optional] 

### Return type

[**ResponseExtractConversationsV1WhatsappExtractconversationsPost**](ResponseExtractConversationsV1WhatsappExtractconversationsPost.md)

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

