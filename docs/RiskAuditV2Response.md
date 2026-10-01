# RiskAuditV2Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**RiskAuditV2**](RiskAuditV2.md) | Public response V2 — always returned | 

## Example

```python
from falaai_api.models.risk_audit_v2_response import RiskAuditV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of RiskAuditV2Response from a JSON string
risk_audit_v2_response_instance = RiskAuditV2Response.from_json(json)
# print the JSON string representation of the object
print(RiskAuditV2Response.to_json())

# convert the object into a dict
risk_audit_v2_response_dict = risk_audit_v2_response_instance.to_dict()
# create an instance of RiskAuditV2Response from a dict
risk_audit_v2_response_from_dict = RiskAuditV2Response.from_dict(risk_audit_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


