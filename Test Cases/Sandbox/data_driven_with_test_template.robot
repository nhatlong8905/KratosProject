*** Settings ***
Library  BuiltIn
Library  JSONLibrary
Library  RequestsLibrary
Library  urllib3
Resource       ../../ResourceFiles/BussinessKeywords/init.robot
Suite Setup    initialize
***Variable***



*** Keywords ***

Checkmultiple_Login
     [Arguments]    ${user}  ${password}

     #login
    disable_warnings
    &{headers}=    Create Dictionary    Content-Type=application/json
    &{data}=  Create Dictionary  user=${user}   password=${password}
    ${response}=  Post Request  @{session}  /rest/Token    headers=${headers}   json=${data}
    should be equal as strings  ${response.status_code}  200



*** Test Cases ***
Tests_sample_datadriven
    [Template]   Checkmultiple_Login
    admin  Krt123Krt123@#
    admin  Krt123Krt123@#











