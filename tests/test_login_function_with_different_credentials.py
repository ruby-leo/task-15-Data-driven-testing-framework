from datetime import date, datetime
from conftest import config_data
from pages.login_page import LoginPage
from utilities.excel_operation import get_username_password_from_excel, write_results_back_into_excel
import pytest

class TestLoginFunction:
    @pytest.mark.parametrize("row_num, username, password", get_username_password_from_excel())
    def test_login_with_different_credentials_from_excel(self, driver, row_num, username, password, config_data):
        login_page = LoginPage(driver)
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login()
        assert login_page.does_url_contain("/dashboard")