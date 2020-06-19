*** Settings ***    
Resource       ../ResourceFiles/BussinessKeywords/init.robot

Suite Setup    init performance test    ${CURDIR}/../Data/add_oper.csv    


*** Test Cases ***
Verify with CSV data file
    FOR    ${record}    IN    @{data}
        Log    ${record}
        Should Be True    ${record["one"]}+${record["two"]}==${record["expect"]}        
    END