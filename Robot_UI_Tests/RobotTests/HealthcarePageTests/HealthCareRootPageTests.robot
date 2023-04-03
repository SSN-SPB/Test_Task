*** Settings ***
Documentation    Basic UI tests
Suite Setup      Remove Files    *.png
Test Tags        healthcare
Library          OperatingSystem
Resource         ../../Common_Resources/CommonResourceFile.resource
Resource         ../../Common_Resources/PageElements/HealthcarePageElements/HealthcarePageElements.resource


*** Variables ***
# ${BROWSER}             Chrome
${BROWSER}             Firefox


*** Test Cases ***
Open Find Doctor Subpage
    [Documentation]    This test verifies abiltiy to open site HealthCare
    ...    and navigate to Find Doctor subpage
    ...    (positive scenario)
    ...    \n*Ref:*
    ...    (WKLGAS-XX Placeholder)
    [Tags]    find_doctor
    [Teardown]    Close All Browsers
    OPEN HEALTHCARE SITE   ${BROWSER}
    CHECK ELEMENTS ON HEALTHCARE ROOT PAGE
    OPEN FIND DOCTOR PAGE
    CHECK ELEMENTS ON FIND DOCTOR PAGE

Open Refer Doctor Subpage
    [Documentation]    This test verifies abiltiy to open site HealthCare
    ...    and navigate to Refer Doctor subpage
    ...    (positive scenario)
    ...    \n*Ref:*
    ...    (WKLGAS-XX Placeholder)
    [Tags]    refer_doctor
    [Teardown]    Close All Browsers
    OPEN HEALTHCARE SITE   ${BROWSER}
    CHECK ELEMENTS ON HEALTHCARE ROOT PAGE
    OPEN FIND REFER PAGE
    CHECK ELEMENTS ON REFER DOCTOR PAGE
