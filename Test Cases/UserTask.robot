*** Settings ***
Library    ../py_sources/pythonfw/locust/UserTask.py 
Library    RequestsLibrary    

*** Test Cases ***   
Test case 1
    On Start
    Get List Server