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


def test_9_countries_sorting(driver):
    do_login(driver)

    # go to Countries list page
    driver.get("http://localhost:8080/litecart/admin/?app=countries&doc=countries")
    # get list of all countries
    elemAsIs = driver.find_elements_by_xpath("//table[@class='dataTable']//tr[@class='row']//td/a[not(@title)]")

    # arrays to store the data
    countryArrayAsIs = []
    contriesSorted = []
    tz_count_is_not_zero = []

    # flags for the final assert
    is_list_of_countries_sorted = True
    is_time_zones_sorted = True

    # go through the list of countries
    i = 0
    while i < len(elemAsIs):
        countryArrayAsIs.insert(i, elemAsIs[i].text)
        tz_count = driver.find_elements_by_xpath('//table[@class="dataTable"]//tr[@class="row"][' + str(i + 1)
                                                 + ']//td/a[not(@title)]//..//following-sibling::td[1]')[0]
        if int(tz_count.text) > 0:
            tz_count_is_not_zero.insert(i, elemAsIs[i].get_attribute('href'))
        i += 1

    contriesSorted = countryArrayAsIs
    contriesSorted.sort()

    if len(tz_count_is_not_zero) > 0:
        tzAsIs = []
        tzSorted = []
        item = 0
        while item < len(tz_count_is_not_zero):
            driver.get(tz_count_is_not_zero[item])
            tzAsIs = driver.find_elements_by_xpath("//table[@class='dataTable']//tr[@class='row']//td/a[not(@title)]")
            tzSorted = tzAsIs
            tzSorted.sort()
            if tzSorted != tzAsIs:
                is_time_zones_sorted = False
            item += 1

    if contriesSorted != countryArrayAsIs:
        is_list_of_countries_sorted = False

    assert is_list_of_countries_sorted and is_time_zones_sorted


def test_9_geo_zones_sorting(driver):
    driver.get("http://localhost:8080/litecart/admin/?app=geo_zones&doc=geo_zones")
    countries = driver.find_elements_by_xpath("//table[@class='dataTable']//tr[@class='row']//td/a[not(@title)]")

    is_sorted = True

    countries_urls = []
    item = 0
    while item < len(countries):
        countries_urls.insert(item, countries[item].get_attribute('href'))
        item += 1

    zones_array = []
    item = 0
    while item < len(countries_urls):
        driver.get(countries_urls[item])
        zonesAsIs = driver.find_elements_by_xpath("//select[contains(@name, 'zone_code')]/option[@selected]")
        zones_array = []

        i = 1
        while i < len(zonesAsIs):
            zones_array.insert(i, zonesAsIs[i].text)
            i += 1

        zones_sorted = zones_array
        zones_sorted.sort()

        if zones_sorted != zones_array:
            is_sorted = False

        item += 1

    assert is_sorted
