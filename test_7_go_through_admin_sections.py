import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def do_login(driver):
    driver.get("http://localhost:8080/litecart/admin")
    driver.find_element_by_xpath("//input[contains(@name,'username')]").send_keys("admin")
    driver.find_element_by_xpath("//input[contains(@name,'password')]").send_keys("admin")
    driver.find_element_by_xpath("//button[@type='submit']").click()
    driver.find_element_by_css_selector("div.logotype")


def do_check_section(driver):
    return len(driver.find_elements_by_css_selector("h1")) > 0


def test_7_go_through_admin_sections(driver):
    do_login(driver)
    menu_items_count = len(driver.find_elements_by_css_selector("ul#box-apps-menu>li"))
    step = 1
    while step <= menu_items_count:
        driver.find_elements_by_css_selector("ul#box-apps-menu>li")[step - 1].click()
        assert do_check_section(driver)

        submenu_items_count = len(
            driver.find_elements_by_css_selector("ul#box-apps-menu>li:nth-child(" + str(step) + ")>ul.docs>li"))

        step_into_submenu = 1
        while step_into_submenu <= submenu_items_count:
            driver.find_elements_by_css_selector("ul#box-apps-menu>li:nth-child(" + str(step) +
                                                 ")>ul.docs>li")[step_into_submenu - 1].click()
            assert do_check_section(driver)
            step_into_submenu += 1

        step += 1
