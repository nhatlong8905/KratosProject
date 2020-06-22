*** Settings ***
Library    BuiltIn
Library        ../ResourceFiles/CommonKeywords/datetime.py
Resource       ../ResourceFiles/BussinessKeywords/GetLogKeywords.robot
Resource       ../ResourceFiles/BussinessKeywords/init.robot


Suite Setup    initialize
Suite Teardown    Log    Clean up when suite is done    
Test Setup    Log    Run before each test starts    
Test Teardown    Log    Run after each test is done    

Default Tags    Smoke

*** Test Cases ***
TC 002 Hello World
    [Tags]    P1  
    should be true  '${account_credential}[user]'=='admin1'
    log     ${account_credential}[password]

# set global variable in a test, up comming test can access it
Test 1
    [Tags]    P2
    ${test}=    evaluate    9
    set global variable     ${test}     10
    
# it's not good 
Test 2   
    # access a global variable declared in previous test
    [Tags]    P3
    log     ${test}

Test with Python Keyword
    [Tags]    Python
    ${localtime}=    get current time
    Log    ${localtime}  
# execute with tag in cmd
# robot -i P1 -i P2 [path to test suite file]
# robot --settag=P1 [path to test suite file]
# robot -i smoke* [path to test suite file]
# -e --exclude  -i --include
# robot -e smoke* [path to test suite file]