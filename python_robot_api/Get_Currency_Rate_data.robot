*** Settings ***
Documentation    Suite verifies the validness the data about currencies that is retrieved via API
Suite Setup      Log    the validness the data about currencies that is retrieved via API
Force Tags       code_check
Library          RequestsLibrary
Library          JSONLibrary
Resource         ./Currency_Pairs/Get_Currency_Pairs_Resource.resource


*** Variables ***
${REST_API_ENDPOINT}    /api/live
${API_PARAMETERS}    pairs=USDRUB
${RATE_EURUSD}    pairs=EURUSD
${EXPECTED_RATE_VALUE_EURRUB}    81
@{LIST_OF_PAIRS}    pairs=USDRUB    pairs=EURUSD,USDRUB    pairs=EURUSD


*** Test Cases ***
Check Code For Single Currency Pair
    [Documentation]    This test verifies response code 200 for the singe valid pair
    ...    (positive scenario)
    ...    \n*Ref:*
    ...    (JIRA_TICKET-11 Placeholder)
    [Tags]    single_pair
    [Teardown]    Log    The test ${TEST NAME} is completed
    Do Get Request    ${REST_API_ENDPOINT}    ${API_PARAMETERS}
    Should Be Equal    '${RECEIVED_CODE}'    '[200]'
    Should Be Equal    '${RECEIVED_CODE}[0]'    '200'
    Should Be Equal As Integers   ${RECEIVED_CODE}[0]    200

Check Code For List Of Currency Pair
    [Documentation]    This test verifies response code 200 for the several valid pairs and pairs combinations
    ...    (positive scenario).
    ...    \n*Ref:*
    ...    (JIRA_TICKET-11 Placeholder)
    [Tags]    multipairs
    [Teardown]    Log    The test ${TEST NAME} is completed
    FOR    ${pair}    IN    @{LIST_OF_PAIRS}
        Log Many    Checked pair is ${pair}
        Do Get Request    ${REST_API_ENDPOINT}    ${pair}
        Should Be Equal    '${output_get_request.status_code}'    '200'
    END

Check Ruble Dollar Rate
    [Documentation]    This test verifies that USD/RUB rate less 100
    ...    (positive scenario)
    ...    \n*Ref:*
    ...    (JIRA_TICKET-13 Placeholder)
    [Tags]    single_pair
    [Teardown]    Log    The test ${TEST NAME} is completed
    Do Get Request    ${REST_API_ENDPOINT}    ${API_PARAMETERS}
    Should Be True    ${json_object_get_request['rates']['USDRUB']['rate']} < 100
    Should Contain  ${json_object_get_request['rates']}    USDRUB

Check Ruble Euro Rate
    [Documentation]    This test calculates EUR/RUB and verifies it less 81
    ...    This value is defined by ${EXPECTED_RATE_VALUE_EURRUB}
    ...    (positive scenario)
    ...    \n*Ref:*
    ...    (JIRA_TICKET-13 Placeholder)
    [Tags]    calculated_value
    [Teardown]    Log    The test ${TEST NAME} is completed
    Do Get Request    ${REST_API_ENDPOINT}    ${RATE_EURUSD}
    Set Test Variable    ${RATE_EURO_USD}    ${json_object_get_request['rates']['EURUSD']['rate']}
    Do Get Request    ${REST_API_ENDPOINT}    ${API_PARAMETERS}
    Set Test Variable    ${RATE_USD_RUB}    ${json_object_get_request['rates']['USDRUB']['rate']}
    ${RATE_EURO_RUB} =     Evaluate    ${RATE_EURO_USD}*${RATE_USD_RUB}
    Set Test Variable    ${RATE_EURO_RUB}    ${RATE_EURO_RUB}
    Log Many    ${RATE_EURO_RUB}
    Should Be True    ${RATE_EURO_RUB} < ${EXPECTED_RATE_VALUE_EURRUB}
