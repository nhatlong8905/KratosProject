*** Settings ***
Library    ../py_sources/pythonfw/api/ServerAPI.py    
Library    RequestsLibrary    

*** Variables ***
${CONFIGKEY}        user
${CONFIGFILE}    Data/user_conf.json
${APIKEY}    serverapi
${APIFILE}    Data/server_api.json
*** Test Cases ***   
Test case 1
    ${resp}    Get List Server 
    Log To Console  logrepo${resp}       
    
    Check Status List Server
    
    Verify Server Information         localhost
    
    ${data}    Get Data Api
    Log To Console  logdata${data}       