*** Settings ***
Documentation    The currency pairs resource
Library          Collections
Library          String
Library          JSONLibrary
Library          RequestsLibrary


*** Variables ***
${ENV_URL}    https://www.freeforexapi.com


*** Keywords ***
Do Get Request
    [Arguments]    ${api_endpoint}    ${get_parameters}
    [Documentation]    Keyword makes a get request ${api_endpoint}
    ...    and assigns the response to test variable ${json_object_get_request}.
    ...
    ...    *Arguments*
    ...    - ${api_endpoint} - _String_ Endpoint link
    ...    - ${get_parameters} - _String_ parameters of url
    Create Session    API    ${ENV_URL}   verify=true
    ${output_req} =    GET On Session    API    ${api_endpoint}    params=${get_parameters}
    ${response_code} =    Get Value From Json    ${output_req.json()}    code
    Set Test Variable    ${JSON_OBJECT_GET_REQUEST}    ${output_req.json()}
    Set Test Variable    ${OUTPUT_GET_REQUEST}    ${output_req}
    Set Test Variable    ${RECEIVED_CODE}    ${response_code}
