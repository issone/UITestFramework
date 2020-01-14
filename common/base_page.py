import allure

from common.driver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def assert_title_is(self, text):
        try:
            assert self.driver.get_title() == text
        except Exception as e:
            with allure.step('失败截图'):
                self.driver.save_screenshot()
                raise e
        else:
            with allure.step('成功截图'):
                self.driver.save_screenshot()

    def assert_title_contains(self, text):
        try:
            assert text in self.driver.get_title()
        except Exception as e:
            with allure.step('失败截图'):
                self.driver.save_screenshot()
                raise e
        else:
            with allure.step('成功截图'):
                self.driver.save_screenshot()

    def assert_url_is(self, url):
        try:
            assert self.driver.get_title() == url
        except Exception as e:
            with allure.step('失败截图'):
                self.driver.save_screenshot()
                raise e
        else:
            with allure.step('成功截图'):
                self.driver.save_screenshot()

    def assert_url_contains(self, url):
        try:
            assert url in self.driver.get_current_url()
        except Exception as e:
            with allure.step('失败截图'):
                self.driver.save_screenshot()
                raise e
        else:
            with allure.step('成功截图'):
                self.driver.save_screenshot()

    def assert_url_not_contains(self, url):
        try:
            assert url not in self.driver.get_current_url()
        except Exception as e:
            with allure.step('失败截图'):
                self.driver.save_screenshot()
                raise e
        else:
            with allure.step('成功截图'):
                self.driver.save_screenshot()

    def final_assert(self, result):
        if isinstance(result, Exception):
            with allure.step('失败截图'):
                self.driver.save_screenshot()
                raise result
        else:
            with allure.step('成功截图'):
                self.driver.save_screenshot()
