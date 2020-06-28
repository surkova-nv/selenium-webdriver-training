from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element

def test_3_login_to_admin():
    driver = WebDriver(executable_path='C://WorkFiles//chromedriver.exe')
    driver.get("http://localhost:8080/litecart/admin")
    login_input = driver.find_element_by_xpath("//input[contains(@name,'username')]")
    pass_input = driver.find_element_by_xpath("//input[contains(@name,'password')]")
    submit_button = driver.find_element_by_xpath("//button[@type='submit']")
    login_input.send_keys("admin")
    pass_input.send_keys("admin")

    def finally_logged_in(driver):
        return driver.find_element_by_link_text("Appearence")

    try:
        submit_button.click()
        WebDriverWait(driver, 10, 0.5).until(finally_logged_in)
    finally:
        driver.quit()
