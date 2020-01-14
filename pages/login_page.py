from pages.base_is_cloud_page import IsCloudPage


class LoginPage(IsCloudPage):

    def open(self, url):
        self.driver.get(url)
        self.driver.max_window()

    def input_username(self, username):
        self.driver.input_text_by_label(text=username, label='名称')

    def input_password(self, password):
        self.driver.input_text_by_label(text=password, label='密码')

    def click_login_button(self):
        self.driver.get_element(by='xpath', value='//button').click()

    def assert_result(self):
        self.assert_url_not_contains('/login')
