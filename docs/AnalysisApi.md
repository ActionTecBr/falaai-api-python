# falaai_api.AnalysisApi

All URIs are relative to *https://api01-falaai.action.tec.br*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_diagnostic_v1_analyze_diagnostic_post**](AnalysisApi.md#create_diagnostic_v1_analyze_diagnostic_post) | **POST** /v1/analyze/diagnostic | Analyze a call transcript — 5 parallel analyses
[**create_risk_audit_v1_analyze_risk_audit_post**](AnalysisApi.md#create_risk_audit_v1_analyze_risk_audit_post) | **POST** /v1/analyze/riskAudit | Compliance Risk Audit — conversation compliance analysis


# **create_diagnostic_v1_analyze_diagnostic_post**
> DiagnosticResponse create_diagnostic_v1_analyze_diagnostic_post(diagnostic_request)

Analyze a call transcript — 5 parallel analyses

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

