import pytest
from selenium import webdriver
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