*** Settings ***
Library  BuiltIn
Library  JSONLibrary
Library  RequestsLibrary

*** Keywords ***

Login_Post_Call
    [Arguments]    ${user}  ${password}  ${session}
    &{headers}=    Create Dictionary    Content-Type=application/json
    &{data}=  Create Dictionary  user=${user}   password=${password}
    ${response}=  Post Request    ${session}  /rest/Token    headers=${headers}   json=${data}
    ${json_resp}=  to Json   ${response.content}
    [Return]    ${json_resp}