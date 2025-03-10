import random

from selenium.webdriver.common.by import By
from selenium_ui.jsm.pages.customer_selectors import RequestSelectors

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium_ui.jira.pages.pages import Login
from util.conf import JIRA_SETTINGS


def app_specific_action(webdriver, datasets):
    page = BasePage(webdriver)
    issue_key = random.randint(1, 200)

    # To run action as specific user uncomment code bellow.
    # NOTE: If app_specific_action is running as specific user, make sure that app_specific_action is running
    # just before test_2_selenium_z_log_out action
    #
    # @print_timing("selenium_app_specific_user_login")
    # def measure():
    #     def app_specific_user_login(username='admin', password='admin'):
    #         login_page = Login(webdriver)
    #         login_page.delete_all_cookies()
    #         login_page.go_to()
    #         login_page.set_credentials(username=username, password=password)
    #         if login_page.is_first_login():
    #             login_page.first_login_setup()
    #         if login_page.is_first_login_second_page():
    #             login_page.first_login_second_page_setup()
    #         login_page.wait_for_page_loaded()
    #     app_specific_user_login(username='admin', password='admin')
    # measure()

    @print_timing("selenium_app_custom_action")
    def measure():
        @print_timing("selenium_app_custom_action:push_to_testmanager")
        def sub_measure():
            # page.go_to_url(f"{JIRA_SETTINGS.server_url}/browse/{issue_key}")
            page.go_to_url(
                f"{JIRA_SETTINGS.server_url}/browse/AANES-{issue_key}")
            page.wait_until_visible((By.ID, "summary-val"))
            page.wait_until_clickable(
                page.get_selector(RequestSelectors.more_button))
            page.get_element(page.get_selector(
                RequestSelectors.more_button)).click()
            page.wait_until_clickable(page.get_selector(
                RequestSelectors.push_to_tmh_button))
            page.get_element(page.get_selector(
                RequestSelectors.push_to_tmh_button)).click()
            page.wait_until_clickable(page.get_selector(
                RequestSelectors.tmh_cancel_button))
            page.get_element(page.get_selector(
                RequestSelectors.tmh_cancel_button)).click()

        sub_measure()
    measure()
