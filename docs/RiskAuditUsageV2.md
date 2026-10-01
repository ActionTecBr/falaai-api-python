# RiskAuditUsageV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**characters** | **int** | Characters analyzed | 
**credits_consumed** | **int** | Credits consumed | 
**processing_ms** | **int** | Processing time (ms) | 

## Example

```python
from falaai_api.models.risk_audit_usage_v2 import RiskAuditUsageV2

# TODO update the JSON string below
json = "{}"
# create an instance of RiskAuditUsageV2 from a JSON string
risk_audit_usage_v2_instance = RiskAuditUsageV2.from_json(json)
# print the JSON string representation of the object
print(RiskAuditUsageV2.to_json())

# convert the object into a dict
risk_audit_usage_v2_dict = risk_audit_usage_v2_instance.to_dict()
# create an instance of RiskAuditUsageV2 from a dict
risk_audit_usage_v2_from_dict = RiskAuditUsageV2.from_dict(risk_audit_usage_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


