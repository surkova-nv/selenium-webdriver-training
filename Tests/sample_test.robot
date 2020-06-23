*** Settings ***
Documentation           Test sample
Library                 Selenium2Library
Suite Teardown          Close all browsers

*** Variables ***

*** Test Cases ***
Test our test
    [Documentation]             Trying to open page ya.ru
    open browser                https://ya.ru/          chrome
    wait until page contains    Найти

*** Keywords ***