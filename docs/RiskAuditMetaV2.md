# RiskAuditMetaV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Analysis id | 
**object** | **str** | Object type | [optional] [default to 'risk_audit']
**call_duration_s** | **float** | Call duration (s) | [optional] 
**analyzed_at** | **str** | ISO 8601 analyzed timestamp | [optional] 
**usage** | [**RiskAuditUsageV2**](RiskAuditUsageV2.md) | Usage block | 
**client_reference_id** | **str** | Echoed client reference id | [optional] 

## Example

```python
from falaai_api.models.risk_audit_meta_v2 import RiskAuditMetaV2

# TODO update the JSON string below
json = "{}"
# create an instance of RiskAuditMetaV2 from a JSON string
risk_audit_meta_v2_instance = RiskAuditMetaV2.from_json(json)
# print the JSON string representation of the object
print(RiskAuditMetaV2.to_json())

# convert the object into a dict
risk_audit_meta_v2_dict = risk_audit_meta_v2_instance.to_dict()
# create an instance of RiskAuditMetaV2 from a dict
risk_audit_meta_v2_from_dict = RiskAuditMetaV2.from_dict(risk_audit_meta_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


