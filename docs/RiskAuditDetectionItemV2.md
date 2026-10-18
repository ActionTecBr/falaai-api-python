# RiskAuditDetectionItemV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**turn** | **int** | Turn number | [optional] 
**interlocutor** | **str** | Speaker | [optional] 
**role** | **str** | Role | [optional] 
**timestamp_formatted** | **str** | Formatted timestamp | [optional] 
**term_text** | **str** | Detected term | [optional] 
**category_label** | **str** | Category label (i18n) | 
**subcategory_label** | **str** | Subcategory label (i18n) | [optional] 
**criticality** | **str** | Criticality | [optional] 
**status** | **str** | Status | [optional] 
**reason** | **str** | Reason | [optional] 
**final_score** | **float** | Final score | [optional] 
**violated_frameworks** | **List[object]** | Violated frameworks | [optional] [default to []]

## Example

```python
from falaai_api.models.risk_audit_detection_item_v2 import RiskAuditDetectionItemV2

# TODO update the JSON string below
json = "{}"
# create an instance of RiskAuditDetectionItemV2 from a JSON string
risk_audit_detection_item_v2_instance = RiskAuditDetectionItemV2.from_json(json)
# print the JSON string representation of the object
print(RiskAuditDetectionItemV2.to_json())

# convert the object into a dict
risk_audit_detection_item_v2_dict = risk_audit_detection_item_v2_instance.to_dict()
# create an instance of RiskAuditDetectionItemV2 from a dict
risk_audit_detection_item_v2_from_dict = RiskAuditDetectionItemV2.from_dict(risk_audit_detection_item_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


