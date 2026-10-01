# RiskAuditIndexerV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**suggested_terms_for_bank** | **List[Dict[str, object]]** | Suggested terms for bank | [optional] [default to []]

## Example

```python
from falaai_api.models.risk_audit_indexer_v2 import RiskAuditIndexerV2

# TODO update the JSON string below
json = "{}"
# create an instance of RiskAuditIndexerV2 from a JSON string
risk_audit_indexer_v2_instance = RiskAuditIndexerV2.from_json(json)
# print the JSON string representation of the object
print(RiskAuditIndexerV2.to_json())

# convert the object into a dict
risk_audit_indexer_v2_dict = risk_audit_indexer_v2_instance.to_dict()
# create an instance of RiskAuditIndexerV2 from a dict
risk_audit_indexer_v2_from_dict = RiskAuditIndexerV2.from_dict(risk_audit_indexer_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


