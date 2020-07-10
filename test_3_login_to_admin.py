import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def finally_logged_in(driver):
    return driver.find_element_by_css_selector("div.logotype")


def test_3_login_to_admin(driver):
    driver.get("http://localhost:8080/litecart/admin")
    driver.find_element_by_xpath("//input[contains(@name,'username')]").send_keys("admin")
    driver.find_element_by_xpath("//input[contains(@name,'password')]").send_keys("admin")
    driver.find_element_by_xpath("//button[@type='submit']").click()
    WebDriverWait(driver, 10, 0.5).until(finally_logged_in)
