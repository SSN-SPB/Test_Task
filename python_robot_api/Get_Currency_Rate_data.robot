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