from datetime import date, datetime

import pytest
from selenium import webdriver

from utilities.excel_operation import write_results_back_into_excel
from utilities.read_json import get_config

@pytest.fixture(scope="function")
def driver(config_data):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(config_data["base_url"])
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def config_data():
    return get_config()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call":
        params = item.callspec.params
        row_num = params.get("row_num")
        test_result = "Passed" if report.passed else "Failed"
        config_data = item._request.getfixturevalue("config_data")
        write_results_back_into_excel(row_num, date.today(), datetime.now().time(), config_data["name_of_the_tester"], test_result)