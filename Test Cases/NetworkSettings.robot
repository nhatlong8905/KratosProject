*** Settings ***
Library    ../py_sources/pythonfw/api/NetworkSettingsAPI.py    
Library    RequestsLibrary    

*** Variables ***
${CONFIGKEY}        user
${CONFIGFILE}    Data/user_conf_networkapi.json
*** Test Cases ***   
Test case 1 View all the Network Configuration
    ${resp}    Get List Network configuration 
    Log To Console  logrepo${resp}       
    
    Status Should Be    200    ${resp}   
    
    Verify List Network Configuration Information    1    /Configuration/NetworkSettings/0    MN300-125-77
    

Test case 2 Update 1st Network Configuration -hostname

    ${resp}    Update Network Configuration Hostname    0    MN300-125-78
    Log To Console  logrepo${resp}       
    
    Status Should Be    200    ${resp}    
    
    ${respUpdate}    Get Network configuration     0 
    
    Status Should Be    200    ${respUpdate}    
    
    Verify Network Configuration Information    /Configuration/NetworkSettings/0    MN300-125-78