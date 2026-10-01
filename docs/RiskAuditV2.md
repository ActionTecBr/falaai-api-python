# RiskAuditV2

Response V2 (build_public_response_v2) — blocos logicos EN-US. Fonte: response_builder.py.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**RiskAuditMetaV2**](RiskAuditMetaV2.md) | Identification + usage | 
**participants** | [**RiskAuditParticipantsV2**](RiskAuditParticipantsV2.md) | Participants/roles/direction | 
**verdict** | [**RiskAuditVerdictV2**](RiskAuditVerdictV2.md) | Verdict + level + applied actions | 
**scores** | [**RiskAuditScoresV2**](RiskAuditScoresV2.md) | Consolidated + per-participant scores | 
**detections** | [**RiskAuditDetectionsV2**](RiskAuditDetectionsV2.md) | violations/positives/client alerts | 
**analysis** | [**RiskAuditAnalysisV2**](RiskAuditAnalysisV2.md) | global_metrics + final_analysis + frameworks | 
**timeline** | [**RiskAuditTimelineV2**](RiskAuditTimelineV2.md) | turns_sentiment + audio_events + groups | 
**audio_event_model** | [**RiskAuditAudioEventModelV2**](RiskAuditAudioEventModelV2.md) | MAC audio event semantics | 
**categories_summary** | **Dict[str, object]** | Per-category summary (keyed by category) | 
**indexer** | [**RiskAuditIndexerV2**](RiskAuditIndexerV2.md) | Suggested terms for bank | 
**summary** | [**RiskAuditSummaryV2**](RiskAuditSummaryV2.md) | Executive summary counts | 
**actions_i18n** | **Dict[str, object]** | Used actions i18n catalog (keyed by action) | 
**audit_decisions** | [**RiskAuditAuditDecisionsV2**](RiskAuditAuditDecisionsV2.md) | Risk origin + validator changes | 
**scoring_explanation** | [**RiskAuditScoringExplanationV2**](RiskAuditScoringExplanationV2.md) | Score composition explanation | 
**html_report** | **str** | HTML report (base64 gzip) | 

## Example

```python
from falaai_api.models.risk_audit_v2 import RiskAuditV2

# TODO update the JSON string below
json = "{}"
# create an instance of RiskAuditV2 from a JSON string
risk_audit_v2_instance = RiskAuditV2.from_json(json)
# print the JSON string representation of the object
print(RiskAuditV2.to_json())

# convert the object into a dict
risk_audit_v2_dict = risk_audit_v2_instance.to_dict()
# create an instance of RiskAuditV2 from a dict
risk_audit_v2_from_dict = RiskAuditV2.from_dict(risk_audit_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


