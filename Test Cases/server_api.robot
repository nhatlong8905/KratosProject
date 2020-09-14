*** Settings ***
Library    ../py_sources/pythonfw/api/ServerAPI.py    
Library    RequestsLibrary    

*** Variables ***
${CONFIGKEY}        user
${CONFIGFILE}    Data/user_conf.json
*** Test Cases ***   
Test case 1
    ${resp}    Get List Server 
    Log To Console  logrepo${resp}       
    
    Check Status List Server
    
    
    Verify Server Information    localhost
    
    Verify Network Configuration Information More    /server/server/1    None         192.168.1.1
   