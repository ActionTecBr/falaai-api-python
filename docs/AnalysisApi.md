# falaai_api.AnalysisApi

All URIs are relative to *https://api01-falaai.action.tec.br*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_diagnostic_v1_analyze_diagnostic_post**](AnalysisApi.md#create_diagnostic_v1_analyze_diagnostic_post) | **POST** /v1/analyze/diagnostic | Analyze a call transcript — 5 parallel analyses
[**create_risk_audit_v1_analyze_risk_audit_post**](AnalysisApi.md#create_risk_audit_v1_analyze_risk_audit_post) | **POST** /v1/analyze/riskAudit | Compliance Risk Audit — conversation compliance analysis


# **create_diagnostic_v1_analyze_diagnostic_post**
> DiagnosticResponse create_diagnostic_v1_analyze_diagnostic_post(diagnostic_request)

Analyze a call transcript — 5 parallel analyses

Analyzes a call transcript and returns six structured blocks: dialogue summary, contact reason, identified action, theme label, predominant sentiment and identified participants with roles, names, confidence and evidence; use it for a fast, generic diagnosis of what happened in a call, and use /v1/analyze/riskAudit instead when the goal is compliance violation auditing. Provide at least one of dialog (primary source: diarized transcript in the format 'Speaker 1: [00:00:00.540 - 00:00:01.139] text', speaker labels accepted in any case as Speaker, Interlocutor, Hablante, Locutor or Orador plus number) or text (plain transcript fallback), each up to 300,000 characters; when dialog is used duration_seconds is required by the schema and, when provided, must be >= the last turn end time. Required: language; optional: model (always 'falaai-diagnostic-1'), audio_events, response_language (language of the results, defaulting to language), participants (up to 10 with interlocutor and optional name and role agent/client/bot, ground truth when the role is informed and otherwise inferred), call_direction (inferred when omitted), client_reference_id (echoed verbatim, charset [A-Za-z0-9 _/:.-], max 60). Returns id, object 'analysis', response_language, analysis with the six blocks, usage (characters, credits_consumed, processing_ms) and html_report (base64 gzip) only when dialog is provided; with text-only input the participant roles are forced to confidence 'low'. Credits are charged per character of the transcript (0.03/char, counted without speaker labels, timestamps and inline expression tokens, minimum 500 characters, plus 50 characters per audio event) and the amount charged is returned in usage.credits_consumed. Stateless: neither the transcript nor the analysis is persisted (only billing and usage metadata is logged), protecting personal data under LGPD.

### Example

* Bearer (fai_xxx) Authentication (ApiKeyAuth):

```python
import falaai_api
from falaai_api.models.diagnostic_request import DiagnosticRequest
from falaai_api.models.diagnostic_response import DiagnosticResponse
from falaai_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api01-falaai.action.tec.br
# See configuration.py for a list of all supported configuration parameters.
configuration = falaai_api.Configuration(
    host = "https://api01-falaai.action.tec.br"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (fai_xxx): ApiKeyAuth
configuration = falaai_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with falaai_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = falaai_api.AnalysisApi(api_client)
    diagnostic_request = falaai_api.DiagnosticRequest() # DiagnosticRequest | 

    try:
        # Analyze a call transcript — 5 parallel analyses
        api_response = api_instance.create_diagnostic_v1_analyze_diagnostic_post(diagnostic_request)
        print("The response of AnalysisApi->create_diagnostic_v1_analyze_diagnostic_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysisApi->create_diagnostic_v1_analyze_diagnostic_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **diagnostic_request** | [**DiagnosticRequest**](DiagnosticRequest.md)|  | 

### Return type

[**DiagnosticResponse**](DiagnosticResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_risk_audit_v1_analyze_risk_audit_post**
> RiskAuditV2Response create_risk_audit_v1_analyze_risk_audit_post(risk_audit_request)

Compliance Risk Audit — conversation compliance analysis

Runs a compliance risk audit on a diarized call transcript, detecting violations and positives, applying the ISO 31000 risk matrix, classifying the conversation into a level and returning the verdict with the applied actions and the NIST/OWASP risk framework enquadramento; use it for compliance and quality audits of company-agent-to-client calls, not for generic conversation summarization. Required fields: dialog (diarized transcript in the format 'Speaker 1: [00:00:00.540 - 00:00:01.139] text', speaker labels accepted in any case as Speaker, Interlocutor, Hablante, Locutor or Orador plus number; plain text is not accepted; max 300,000 characters), duration_seconds (total audio duration in seconds, must be >= the last turn end time) and language plus response_language (only pt-BR, en-US or es-ES). Optional: model (always 'falaai-risk-audit-1'), audio_events (up to 500, each requiring event and start_s), participants (up to 10 with interlocutor and role agent/client/bot, ground truth when provided, else inferred), call_direction (inbound/outbound, inferred when omitted), response_format (only 'v2'), client_reference_id (echoed verbatim, charset [A-Za-z0-9 _/:.-], max 60). Returns response (V2) with meta+usage, participants, verdict with level and applied actions, scores, detections (violations, positives, client alerts), analysis frameworks, timeline, categories_summary, executive summary, scoring explanation and an HTML report (gzip+base64). Credits are charged per character of the spoken transcript (0.09/char, counted without speaker labels and inline expression tokens, minimum 1,000 characters, plus 50 characters per audio event) and a minimum-cost guard may raise the final amount, so response.meta.usage.credits_consumed is the amount actually charged. Stateless: neither the transcript nor the analysis is persisted (only billing and usage metadata is logged), protecting personal data under LGPD.

### Example

* Bearer (fai_xxx) Authentication (ApiKeyAuth):

```python
import falaai_api
from falaai_api.models.risk_audit_request import RiskAuditRequest
from falaai_api.models.risk_audit_v2_response import RiskAuditV2Response
from falaai_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api01-falaai.action.tec.br
# See configuration.py for a list of all supported configuration parameters.
configuration = falaai_api.Configuration(
    host = "https://api01-falaai.action.tec.br"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (fai_xxx): ApiKeyAuth
configuration = falaai_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with falaai_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = falaai_api.AnalysisApi(api_client)
    risk_audit_request = falaai_api.RiskAuditRequest() # RiskAuditRequest | 

    try:
        # Compliance Risk Audit — conversation compliance analysis
        api_response = api_instance.create_risk_audit_v1_analyze_risk_audit_post(risk_audit_request)
        print("The response of AnalysisApi->create_risk_audit_v1_analyze_risk_audit_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysisApi->create_risk_audit_v1_analyze_risk_audit_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **risk_audit_request** | [**RiskAuditRequest**](RiskAuditRequest.md)|  | 

### Return type

[**RiskAuditV2Response**](RiskAuditV2Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

