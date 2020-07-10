import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_8_check_stikers(driver):
    driver.get("http://localhost:8080/litecart/en/")
    item = 0
    while item < len(driver.find_elements_by_css_selector("li.product")):
        goods = driver.find_elements_by_css_selector("li.product")[item]
        label_count = len(goods.find_elements_by_css_selector("div.sticker"))
        assert label_count == 1
        item += 1
