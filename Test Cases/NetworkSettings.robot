*** Settings ***
Library    ../py_sources/pythonfw/api/NetworkSettingsAPI.py    
Library    RequestsLibrary    

*** Variables ***
${CONFIGKEY}        user
${CONFIGFILE}    Data/user_conf_networkapi.json
*** Test Cases ***   
Test case 1 View all the Network Configuration
    ${resp}    Get Network configuration 
    Log To Console  logrepo${resp}       
    
    Check Status Network Configuration
    
    Verify List Network Configuration Information    1    /Configuration/NetworkSettings/0         bhuvana-Mon300
    

Test case 2 Update 1st Network Configuration -hostname

    ${resp}    Update Network Configuration Hostname    0     bhuvana-101
    Log To Console  logrepo${resp}       
    
    Check Status Network Configuration
    
    Verify Network Configuration Information    /Configuration/NetworkSettings/0         bhuvana-101