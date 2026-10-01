# RiskAuditDetectionsV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**violations** | [**List[RiskAuditDetectionItemV2]**](RiskAuditDetectionItemV2.md) | Active violations | [optional] [default to []]
**positives** | [**List[RiskAuditDetectionItemV2]**](RiskAuditDetectionItemV2.md) | Active positives | [optional] [default to []]
**client_risk_alerts** | **List[Dict[str, object]]** | Client risk alerts | [optional] [default to []]
**client_behavior_alerts** | **List[Dict[str, object]]** | Client behavior alerts | [optional] [default to []]
**client_negatives** | [**List[RiskAuditDetectionItemV2]**](RiskAuditDetectionItemV2.md) | Client negatives | [optional] [default to []]

## Example

```python
from falaai_api.models.risk_audit_detections_v2 import RiskAuditDetectionsV2

# TODO update the JSON string below
json = "{}"
# create an instance of RiskAuditDetectionsV2 from a JSON string
risk_audit_detections_v2_instance = RiskAuditDetectionsV2.from_json(json)
# print the JSON string representation of the object
print(RiskAuditDetectionsV2.to_json())

# convert the object into a dict
risk_audit_detections_v2_dict = risk_audit_detections_v2_instance.to_dict()
# create an instance of RiskAuditDetectionsV2 from a dict
risk_audit_detections_v2_from_dict = RiskAuditDetectionsV2.from_dict(risk_audit_detections_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


