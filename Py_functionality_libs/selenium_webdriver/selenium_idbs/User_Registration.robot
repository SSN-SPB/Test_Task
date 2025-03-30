*** Settings ***
Documentation     Test Suite verifies login to User Management in Admin Portal.
Suite Teardown  Close All Browsers
Force Tags        all
Library             Selenium2Library
Library             SeleniumLibrary


*** Variables ***
${URL}              http://www.google.com
${BROWSER}          Chrome

*** Test Cases ***
01 - Login
    [Documentation]    *Description*
    ...
    ...    Verifies that the internal colleague user can be added to the User's table via 'Add user' button.
    ...
    ...
    ...    - *Given:* A user with valid permisions who is already logged in (or has a valid prior session, i.e. has logged into the Admin Portal in the current browser before)
    ...    - *When:* the user navigates to user management and clicks on Add New User Button
    ...    - *Then:* the user is able to add Full name, User ID, Email address, Department, Collaborator, Select IDP, User groups, User roles and Save the details successfully.
    [Tags]    open_browser    USER REGISTRATION
    Open Browser    ${URL}   ${BROWSER}
    Wait     10 s
