import allure

from pages.base_is_cloud_page import IsCloudPage


class VPoolPage(IsCloudPage):

    def click_sub_menu(self):
        with allure.step('点击子菜单'):
            self.driver.click(self.driver.get_text_element(tag_name='i', text="more_vert", parent_level=2))

    def click_add_menu(self):
        with allure.step('点击增加'):
            self.driver.click(self.driver.get_text_element(text='增加', tag_name='div'))

    def click_del_menu(self):
        with allure.step('点击删除'):
            self.driver.click(self.driver.get_text_element(text='删除', tag_name='div'))

    def click_update_menu(self):
        with allure.step('点击修改'):
            self.driver.click(self.driver.get_text_element(text='修改', tag_name='div'))

    def select_pool(self, pool_name):
        with allure.step('选中{}资源池'.format(pool_name)):
            self.driver.click(self.driver.get_text_element(text=pool_name, tag_name='div'))

    def input_pool_name(self, name, clear=False):
        with allure.step('输入资源池名称'):
            self.driver.input_text_by_label(text=name, label='资源池名称*', clear=clear)

    def input_pool_desc(self, desc, clear=False):
        with allure.step('输入资源池描述信息'):
            el = self.driver.get_element(by='xpath', value='//div[@class="q-editor__content"]')
            self.driver.input_text(el, text=desc, clear=clear)

    def assert_result(self, action, pool_name):
        if action == 'add':
            desc = '增加'
        elif action == 'update':
            desc = '修改'
        elif action == 'del':
            desc = '删除'
        else:
            raise ValueError('action必须为 add , update ,del 中的一个，不能为{}'.format(action))
        try:
            self.driver.get_element(by='xpath', value=f'//div[text()="{desc}{pool_name}成功"]')
        except Exception as e:
            with allure.step('失败截图'):
                self.driver.save_screenshot()
                raise e
        else:
            with allure.step('成功截图'):
                self.driver.save_screenshot()
