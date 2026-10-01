# RiskAuditDetectionItemV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**turn** | **int** | Turn number | [optional] 
**interlocutor** | **str** | Speaker | [optional] 
**role** | **str** | Role | [optional] 
**timestamp_start_s** | **float** | Start (s) | [optional] 
**timestamp_end_s** | **float** | End (s) | [optional] 
**timestamp_formatted** | **str** | Formatted timestamp | [optional] 
**term_text** | **str** | Detected term | [optional] 
**suggested_term_for_bank** | **object** | Suggested term for bank | [optional] 
**category** | **str** | Category code | [optional] 
**category_label** | **str** | Category label (i18n) | 
**category_color** | **str** | Category color | [optional] 
**category_icon** | **str** | Category icon | [optional] 
**criticality** | **str** | Criticality | [optional] 
**category_threshold** | **float** | Category threshold | [optional] 
**category_type** | **str** | Category type | [optional] 
**category_group** | **str** | Category group label (i18n) | 
**nature** | **str** | Nature | [optional] 
**llm_confidence** | **float** | LLM confidence | [optional] 
**reason** | **str** | Reason | [optional] 
**is_valid_context** | **bool** | Valid context | [optional] 
**risk_probability** | **float** | Risk probability | [optional] 
**risk_impact** | **float** | Risk impact | [optional] 
**category_weight** | **float** | Category weight | [optional] 
**turn_sentiment** | **str** | Turn sentiment | [optional] 
**intensity** | **object** | Intensity | [optional] 
**mod_applied** | **float** | Total modifier applied | [optional] 
**mac_applied** | **float** | Audio modifier applied | [optional] 
**mvad_applied** | **float** | Intensity modifier applied | [optional] 
**mod_formula** | **str** | Modifier formula | [optional] 
**mac_details** | **List[Dict[str, object]]** | MAC details | [optional] [default to []]
**calibration_reason** | **str** | Calibration reason | [optional] 
**final_score** | **float** | Final score | [optional] 
**final_score_formula** | **str** | Final score formula | [optional] 
**conversation_limit** | **object** | Conversation limit | [optional] 
**apply_saturation** | **bool** | Apply saturation | [optional] 
**block_repetition** | **bool** | Block repetition | [optional] 
**status** | **str** | Status | [optional] 
**effective_impact** | **float** | Effective impact | [optional] 
**saturation_factor** | **float** | Saturation factor | [optional] 
**saturation_formula** | **str** | Saturation formula | [optional] 
**threshold_formula** | **str** | Threshold formula | [optional] 
**blocked_formula** | **str** | Blocked formula | [optional] 
**reconciliation_note** | **str** | Reconciliation note | [optional] 
**violated_frameworks** | **List[object]** | Violated frameworks | [optional] [default to []]
**citation_fidelity** | **bool** | Citation fidelity | [optional] [default to True]
**subcategory** | **str** | Subcategory code | [optional] 
**subcategory_label** | **str** | Subcategory label (i18n) | [optional] 

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


