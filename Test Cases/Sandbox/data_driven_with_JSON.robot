*** Settings ***
Resource       ../ResourceFiles/BussinessKeywords/init.robot

# parse file config, read data to intake dictionary
# global variable dictionary key=test case name, value= path to datadriven file
Suite Setup    init performance test    ${CURDIR}/../Data/data.json
    

*** Test Cases ***
test with JSON data
    FOR    ${item}    IN    @{data}
        Log               ${item}
        Should Be True    '${item['sat']}'=='Eagle'    
    END 