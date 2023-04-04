*** Settings ***
Documentation    The SETTLEMENT project common resources
Library          Selenium2Library


*** Variables ***
${SOCIAL_MAP_SITE}        https://ecsa004054e1.epam.com:8001/
${HEALTHCARE_SITE}        https://montenegrohealthcare.azureedge.net/
${REALTY_DEV_SITE}        http://10.253.218.125/
${REALTY_STAGING_SITE}    http://10.253.219.161/
${REALTY_PROD_SITE}       http://10.253.222.1/
# passwords and logons


*** Keywords ***
CHECK SITE AVAILABILITY
    [Arguments]    ${site_url}    ${selected_browser}
    [Documentation]    This step verifies abiltiy to open required site
    ...    (positive scenario)
    ...    \n*Ref:*
    ...    (JIRA_TICKET-11 Placeholder)
    Open Browser    ${site_url}   ${selected_browser}
