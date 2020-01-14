from pages.base_is_cloud_page import IsCloudPage


class ModifyPwdPage(IsCloudPage):

    def click_modify_pwd_menu(self):
        self.driver.get_element(by='xpath', value='//button[@title="修改密码"]').click()

    def input_old_password(self, password):
        self.driver.input_text_by_label(text=password, label='原密码')

    def input_new_password(self, password):
        self.driver.input_text_by_label(text=password, label='新密码')

    def input_confirm_password(self, password):
        self.driver.input_text_by_label(text=password, label='确认密码')

    def assert_result(self):
        self.assert_url_contains('/login')

    def input_username(self, username):
        self.driver.input_text_by_label(text=username, label='名称')

    def input_password(self, password):
        self.driver.input_text_by_label(text=password, label='密码')

    def click_login_button(self):
        self.driver.get_element(by='xpath', value='//button').click()
