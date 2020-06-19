*** Settings ***
Library  BuiltIn
Library  JSONLibrary
Library  RequestsLibrary
Library    Collections
Library     String





*** Keywords ***
Get_Network_Configuration

    [Arguments]   ${session}  ${token}
    &{headers}=  Create Dictionary  Content-Type=application/json   Authorization=Bearer ${token}
    ${resp}=  get request  ${session}    /rest/Configuration/NetworkSettings     headers=${headers}
    [Return]   ${resp}








