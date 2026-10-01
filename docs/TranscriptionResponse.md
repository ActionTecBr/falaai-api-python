# TranscriptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique transcription identifier. Prefix &#39;tr-&#39; followed by UUID | 
**object** | **str** | Returned object type. Always &#39;transcription&#39; | 
**model** | **str** | Model used for transcription. Ex: &#39;falaai-transcribe-1&#39; | 
**filename** | **str** | Original audio file name uploaded | 
**processed_at** | **str** | Processing datetime in ISO 8601 UTC format | 
**usage** | [**TranscriptionUsage**](TranscriptionUsage.md) | Usage and processing information | 
**language** | **str** | ISO 639-3 language code detected in audio. Ex: &#39;por&#39; (Portuguese), &#39;eng&#39; (English), &#39;spa&#39; (Spanish) | 
**language_confidence** | **float** | Language detection confidence level (0.0 to 1.0). Higher is more reliable | [optional] 
**duration_seconds** | **float** | Total audio duration in seconds | 
**text** | **str** | Full transcription as plain text, including audio events in brackets | 
**dialog** | **str** | Turn-by-turn formatted transcript with speaker identification and start/end timestamps | 
**audio_events** | [**List[AudioEvent]**](AudioEvent.md) | List of detected audio events (laughs, sighs, pauses, etc) with timestamps and duration | 
**event_types** | **List[str]** | Unique audio event types found in transcription, alphabetically sorted | 
**word_count** | **int** | Total number of recognized words in transcription | 
**input** | [**AudioInputMeta**](AudioInputMeta.md) | Metadados do arquivo de audio enviado (duracao, formato, codec, sample rate, canais) | 
**client_reference_id** | **str** | Client-supplied ID echoed verbatim (if provided in request) | [optional] 

## Example

```python
from falaai_api.models.transcription_response import TranscriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TranscriptionResponse from a JSON string
transcription_response_instance = TranscriptionResponse.from_json(json)
# print the JSON string representation of the object
print(TranscriptionResponse.to_json())

# convert the object into a dict
transcription_response_dict = transcription_response_instance.to_dict()
# create an instance of TranscriptionResponse from a dict
transcription_response_from_dict = TranscriptionResponse.from_dict(transcription_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


