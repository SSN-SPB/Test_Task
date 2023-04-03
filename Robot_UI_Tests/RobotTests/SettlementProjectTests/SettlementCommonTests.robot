*** Settings ***
Documentation    Basic UI tests
Suite Setup      Remove Files    *.png
Test Tags        sanity
Library          OperatingSystem
Resource         ../../Common_Resources/CommonResourceFile.resource
Resource         ../../Common_Resources/PageElements/HealthcarePageElements/HealthcarePageElements.resource


*** Variables ***
${BROWSER}             Chrome


*** Test Cases ***
Check Availability HealthCare
    [Documentation]    This test verifies abiltiy to open site HealthCare
    ...    (positive scenario)
    ...    \n*Ref:*
    ...    (JIRA_TICKET-11 Placeholder)
    [Tags]    healthcare
    [Teardown]    Close All Browsers
    OPEN HEALTHCARE SITE   ${BROWSER}
    CHECK ELEMENTS ON HEALTHCARE ROOT PAGE

Check Availability SocialMap
    [Documentation]    This test verifies abiltiy to open site SocialMap
    ...    (positive scenario)
    ...    \n*Ref:*
    ...    (JIRA_TICKET-11 Placeholder)
    [Tags]    socialmap
    [Teardown]    Close All Browsers
    CHECK SITE AVAILABILITY    ${SOCIAL_MAP_SITE}   ${BROWSER}
