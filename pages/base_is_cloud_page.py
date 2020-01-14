import allure

from common.base_page import BasePage


class IsCloudPage(BasePage):

    def click_save(self):
        '''点击保存按钮'''
        with allure.step('点击保存按钮'):
            elem = self.driver.get_text_element(tag_name='div', text='保存', parent_level=2)
            self.driver.click(elem)

    def click_confirm_alert(self):
        '''点击弹框中的确认按钮'''
        with allure.step('点击弹框中的确认按钮'):
            self.driver.click(self.driver.get_element(by='xpath', value='//div[text()="确定"]/../..'))

    def click_cancel_alert(self):
        '''点击弹框中的取消按钮'''
        with allure.step('点击弹框中的取消按钮'):
            self.driver.click(self.driver.get_element(by='xpath', value='//div[text()="取消"]/../..'))

    def close_alert_tip(self):
        '''关闭操作成功提示'''
        with allure.step('关闭操作提示'):
            self.driver.click(self.driver.get_element(by='xpath', value='//div[text()="关闭"]/../..'))

    def click_main_menu(self):
        with allure.step('点击主菜单'):
            self.driver.click(self.driver.get_text_element(text='menu', tag_name='i'))

    def into_vpool(self):
        self.click_main_menu()
        with allure.step('进入资源池界面'):
            self.driver.click(self.driver.get_text_element(text='资源池', tag_name='div'))

    def into_host_resource(self):
        self.click_main_menu()
        with allure.step('进入主机资源界面'):
            self.driver.click(self.driver.get_text_element(text='主机资源', tag_name='div'))
