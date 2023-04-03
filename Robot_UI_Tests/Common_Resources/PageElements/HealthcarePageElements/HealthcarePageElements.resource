*** Settings ***
Documentation    The Healthcare pages variables and locators
Library          Selenium2Library
Resource         ../../../Common_Resources/CommonResourceFile.resource


*** Variables ***
${HEALTHCARE_ROOT_TEXT_HEADER_HEALTHCARE}       Healthcare
${HEALTHCARE_ROOT_TEXT_CARD_FIND_DOCTOR}        Find doctor
${HEALTHCARE_ROOT_TEXT_CARD_REFER_DOCTOR}       Refer doctor
${HEALTHCARE_ROOT_FIND_DOCTOR_CARD_CSS}                  css=#root > div.App_app__GuJBs > main > div > div._3A38f._2rjCO._2l2Ul._28bJK.MainPage_content_container__9yFhD._3b-XQ.DyvCE > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(1) > h2
${HEALTHCARE_ROOT_FIND_DOCTOR_CARD_XPATH}                xpath=//*[@id="root"]/div[1]/main/div/div[2]/div[1]/div/div[1]/div[1]/h2
${HEALTHCARE_ROOT_REFER_DOCTOR_CARD_XPATH}               xpath=//*[@id="root"]/div[1]/main/div/div[2]/div[1]/div/div[2]/div[1]/h2
${HEALTHCARE_FIND_DOCTOR_TEXT_HEADER_FIND_DOCTOR}        Find doctor
${HEALTHCARE_FIND_DOCTOR_TEXT_HEADER_TEXT}               HERE YOU CAN FIND A DOCTOR FOR YOU AND YOUR FAMILY
${HEALTHCARE_REFER_DOCTOR_TEXT_HEADER_FIND_DOCTOR}       Refer doctor
${HEALTHCARE_REFER_DOCTOR_TEXT_HEADER_TEXT}              HERE YOU CAN REFER A DOCTOR OF ANY SPECIALTY TO OTHER USERS
${HEALTHCARE_REFER_DOCTOR_TEXT_DOCTOR_CONTACT_TITLE}     Doctor contacts


*** Keywords ***
OPEN HEALTHCARE SITE
    [Arguments]    ${selected_browser}
    [Documentation]    This step opens healthcare site with require browser
    ...    (positive scenario)
    ...    \n*Ref:*
    ...    (WKLGAS-XX Placeholder)
    Open Browser    ${HEALTHCARE_SITE}   ${selected_browser}

CHECK ELEMENTS ON HEALTHCARE ROOT PAGE
    [Documentation]    This step verifies elements on the healthcare root pate
    ...    (positive scenario)
    ...    \n*Ref:*
    ...    (WKLGAS-XX Placeholder)
    Wait Until Page Contains    ${HEALTHCARE_ROOT_TEXT_HEADER_HEALTHCARE}
    Wait Until Page Contains    ${HEALTHCARE_ROOT_TEXT_CARD_FIND_DOCTOR}
    Wait Until Page Contains    ${HEALTHCARE_ROOT_TEXT_CARD_REFER_DOCTOR}

OPEN FIND DOCTOR PAGE
    [Documentation]    This step opens the "Find Doctor " page
    ...    (positive scenario)
    ...    \n*Ref:*
    ...    (WKLGAS-XX Placeholder)
    Click Element    ${HEALTHCARE_ROOT_FIND_DOCTOR_CARD_XPATH}

CHECK ELEMENTS ON FIND DOCTOR PAGE
    [Documentation]    This step verifies elements on the "Find Doctor " page
    ...    (positive scenario)
    ...    \n*Ref:*
    ...    (WKLGAS-XX Placeholder)
    Wait Until Page Contains    ${HEALTHCARE_FIND_DOCTOR_TEXT_HEADER_FIND_DOCTOR}
    Wait Until Page Contains    ${HEALTHCARE_FIND_DOCTOR_TEXT_HEADER_TEXT}

OPEN FIND REFER PAGE
    [Documentation]    This step opens the "Find Doctor " page
    ...    (positive scenario)
    ...    \n*Ref:*
    ...    (WKLGAS-XX Placeholder)
    Click Element    ${HEALTHCARE_ROOT_REFER_DOCTOR_CARD_XPATH}

CHECK ELEMENTS ON REFER DOCTOR PAGE
    [Documentation]    This step verifies elements on the "Find Doctor " page
    ...    (positive scenario)
    ...    \n*Ref:*
    ...    (WKLGAS-XX Placeholder)
    Wait Until Page Contains    ${HEALTHCARE_REFER_DOCTOR_TEXT_HEADER_FIND_DOCTOR}
    Wait Until Page Contains    ${HEALTHCARE_REFER_DOCTOR_TEXT_HEADER_TEXT}
    Wait Until Page Contains    ${HEALTHCARE_REFER_DOCTOR_TEXT_DOCTOR_CONTACT_TITLE}
