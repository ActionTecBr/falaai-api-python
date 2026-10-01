# RiskAuditTimelineV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**turns_sentiment** | **List[Dict[str, object]]** | Per-turn sentiment | [optional] [default to []]
**audio_events** | **List[Dict[str, object]]** | Audio events (i18n) | [optional] [default to []]
**audio_groups_found** | **List[Dict[str, object]]** | Audio groups found | [optional] [default to []]

## Example

```python
from falaai_api.models.risk_audit_timeline_v2 import RiskAuditTimelineV2

# TODO update the JSON string below
json = "{}"
# create an instance of RiskAuditTimelineV2 from a JSON string
risk_audit_timeline_v2_instance = RiskAuditTimelineV2.from_json(json)
# print the JSON string representation of the object
print(RiskAuditTimelineV2.to_json())

# convert the object into a dict
risk_audit_timeline_v2_dict = risk_audit_timeline_v2_instance.to_dict()
# create an instance of RiskAuditTimelineV2 from a dict
risk_audit_timeline_v2_from_dict = RiskAuditTimelineV2.from_dict(risk_audit_timeline_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


