from selenium.webdriver.chrome.webdriver import WebDriver

def test_open_browser():
    driver = WebDriver(executable_path='C://WorkFiles//chromedriver.exe')
    driver.get("https://ya.ru")
    driver.quit()