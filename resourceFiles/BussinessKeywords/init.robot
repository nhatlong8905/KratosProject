

*** Settings ***
Library  BuiltIn
Library  JSONLibrary
Library  RequestsLibrary


*** Keywords ***
initialize
    set global variable  @{BaseURL}  https://10.244.125.77
    set global variable  &{credential}    user=admin   pass=Krt123Krt123@#
    create session   appdata  @{BaseURL}
    set global variable  @{session}  appdata
    set global variable  @{ip}  10.244.125.77