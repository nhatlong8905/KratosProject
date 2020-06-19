*** Settings ***

Library  BuiltIn
Library  JSONLibrary
Library  RequestsLibrary
Resource  ../../ResourceFiles/BussinessKeywords/NetworkConfiguration.robot
Resource       ../../ResourceFiles/BussinessKeywords/init.robot
Resource       ../../ResourceFiles/BussinessKeywords/Login.robot


Suite Setup    initialize

*** Variables ***


*** Test Cases ***
TC_Get_Networks_Configuration_001
     ${username}  set variable  ${credential}[user]
     ${password}  set variable  ${credential}[pass]
     log to console   ${username}
     #login
     ${token}=  Login_Post_Call  ${username}  ${password}  @{session}
     #Get networks info
     ${response}=  Get_Network_Configuration  @{session}   ${token}
     #verify the response
     log to console  ${response.status_code}
     log to console  ${response.content}
     ${json_resp}=  to Json   ${response.content}
     ${ip-response}=  set variable  ${json_resp['items'][0]['data']['ipAddress']}
     log to console  ${ip}
     should be equal as strings  ${response.status_code}  200
     should be equal as strings   ${ip-response}  @{ip}













