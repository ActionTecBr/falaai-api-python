# RiskAuditRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** | Analysis model. Always &#39;falaai-risk-audit-1&#39; | [optional] [default to 'falaai-risk-audit-1']
**text** | **str** | Plain transcript (fallback if dialog is empty). At least one of &#39;dialog&#39; or &#39;text&#39; required. Max 300,000 characters | [optional] [default to '']
**dialog** | **str** | Diarized transcript with speaker turns. PRIMARY source. Speaker labels accepted (any case): &#39;Speaker N&#39;, &#39;Interlocutor N&#39;, &#39;Hablante N&#39;, &#39;Locutor N&#39;, &#39;Orador N&#39; (space or underscore). Normalized internally to &#39;Speaker N&#39; in the response. Max 300,000 characters | [optional] [default to '']
**audio_events** | [**List[DiagnosticAudioEvent]**](DiagnosticAudioEvent.md) | Audio events with timestamps (correlated with turns when diarization is present) | [optional] [default to []]
**duration_seconds** | **float** | Total audio duration in seconds. Required. Max 3h (10800s). | 
**language** | **str** | Language of the transcript being analyzed. Must match the dialog/text language. Accepted: pt-BR, en-US, es-ES. | 
**response_language** | **str** | Language for analysis results (labels, categories, levels, actions, HTML report). Can differ from &#39;language&#39;. Accepted: pt-BR, en-US, es-ES. | 
**call_direction** | **str** | Who originated the call. inbound&#x3D;client called, outbound&#x3D;company called. If omitted, LLM infers from context. | [optional] 
**participants** | [**List[Participant]**](Participant.md) | Explicit participant roles. If omitted, LLM infers from dialog (Lei 17). When provided, used as ground truth — no inference. | [optional] 
**response_format** | **str** | Response format version. Only &#39;v2&#39; (structured EN-US blocks) is available today. | [optional] [default to 'v2']
**client_reference_id** | **str** | Optional client-supplied ID echoed verbatim in the response. Use to correlate/sync with your system. Accepted charset: [A-Za-z0-9._:-], max 128 chars. Not idempotency. | [optional] 

## Example

```python
from falaai_api.models.risk_audit_request import RiskAuditRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RiskAuditRequest from a JSON string
risk_audit_request_instance = RiskAuditRequest.from_json(json)
# print the JSON string representation of the object
print(RiskAuditRequest.to_json())

# convert the object into a dict
risk_audit_request_dict = risk_audit_request_instance.to_dict()
# create an instance of RiskAuditRequest from a dict
risk_audit_request_from_dict = RiskAuditRequest.from_dict(risk_audit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


