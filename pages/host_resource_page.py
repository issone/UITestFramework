import allure

from pages.base_is_cloud_page import IsCloudPage


class HostResourcePage(IsCloudPage):

    def click_sub_menu(self):
        with allure.step('点击子菜单'):
            self.driver.click(self.driver.get_text_element(tag_name='i', text="more_vert", parent_level=2))

    def click_add_menu(self, batch=False):
        with allure.step('点击增加'):
            self.driver.click(self.driver.get_text_element(text='增加', tag_name='div'))
        if batch:
            with allure.step('批量增加'):
                self.driver.click(self.driver.get_text_element(text='批量增加', tag_name='div', parent_level=2))
                self.driver.sleep(1)

    def click_del_menu(self):
        with allure.step('点击删除'):
            self.driver.click(self.driver.get_text_element(text='删除', tag_name='div'))

    def click_update_menu(self):
        with allure.step('点击修改'):
            self.driver.click(self.driver.get_text_element(text='修改', tag_name='div'))

    def click_detail_menu(self):
        with allure.step('点击详细'):
            self.driver.click(self.driver.get_text_element(text='详细', tag_name='div'))

    def click_physical_adapter_menu(self):
        with allure.step('点击物理网卡'):
            self.driver.click(self.driver.get_text_element(text='物理网卡', tag_name='div'))

    def click_virtul_adapter_menu(self):
        with allure.step('点击虚拟网卡'):
            self.driver.click(self.driver.get_text_element(text='虚拟网卡', tag_name='div'))

    def click_terminal_menu(self):
        with allure.step('点击SSH客户端'):
            self.driver.click(self.driver.get_text_element(text='SSH客户端', tag_name='div'))
            self.driver.sleep(2)
            # 获得当前所有打开的窗口的句柄
            all_handles = self.driver.origin.window_handles
            print('all_handles', all_handles)
            terminal_handles = all_handles[-1]
            self.driver.switch_to_window(terminal_handles)

    def click_operation_log_menu(self):
        with allure.step('点击操作日志'):
            self.driver.click(self.driver.get_text_element(text='操作日志', tag_name='div'))

    def click_warn_log_menu(self):
        with allure.step('点击报警日志'):
            self.driver.click(self.driver.get_text_element(text='报警日志', tag_name='div'))

    def input_start_and_end_ip(self, start_ip, end_ip):
        self.driver.input_text_by_label(label="起始IP地址", text=start_ip)
        self.driver.input_text_by_label(label="结束IP地址", text=end_ip, clear=True)

    def click_scan(self):
        self.driver.click(self.driver.get_text_element(tag_name="div", text="扫描", parent_level=2))
        self.driver.sleep(2)
        while self.driver.get_text_element(tag_name="div", text="正在获取主机名...", raise_error=False):
            self.driver.sleep(0.5)
        if self.driver.get_text_element("div", "未扫描到可用的主机IP地址。", timeout=2, raise_error=False):
            self.driver.logger.error("未扫描到可用的主机IP地址。")
            raise NotImplementedError("未扫描到可用的主机IP地址。")

    def select_host(self, hostname):
        """选择主机"""
        with allure.step('选择主机-{}'.format(hostname)):
            host_xpath = f'//div[contains(@class,"q-splitter__panel q-splitter__after")]//div[@title="{hostname}"]'
            self.driver.click(self.driver.get_element('xpath', host_xpath))

    def select_host_click_sub_menu(self, hostname):
        """选中主机的同时点击其菜单"""
        with allure.step('选择主机-{},并点开菜单栏'.format(hostname)):
            host_xpath = f'//div[contains(@class,"q-splitter__panel q-splitter__after")]//div[@title="{hostname}"]'
            host_menu_xpath = host_xpath + '/../../../../..//i[text()="more_vert"]/../..'
            self.driver.click(self.driver.get_element('xpath', host_xpath))
            self.driver.click(self.driver.get_element('xpath', host_menu_xpath))

    def select_vpool(self, pool_name):
        with  allure.step('选择所属资源池-{}'.format(pool_name)):
            self.driver.click(self.driver.get_text_element(text='所属资源池*', tag_name='div', parent_level=4))

            self.driver.click(self.driver.get_element('xpath',
                                                      f'//div[@class="q-virtual-scroll__content"]//div[text()="{pool_name}"]'))

    def select_host_type(self, host_type_name):
        with  allure.step('选择主机型号'):
            self.driver.click(self.driver.get_contains_text_element(text='主机型号', tag_name='div', parent_level=4))
            self.driver.click(self.driver.get_element('xpath',
                                                      f'//div[@class="q-virtual-scroll__content"]//div[text()="{host_type_name}"]'))

    def check_first_nic(self):
        '''勾选第一个网卡'''

        with allure.step('勾选第一个网卡'):
            first_tr_td_list = self.driver.get_element('xpath', '(//tr[not(@style)])[2]/td', multi=True)
            first_tr_td_list[0].click()

    def select_nic(self, nic_name_list):
        '''下拉选择网卡'''
        with allure.step('点击下拉选择网卡'):
            self.driver.click(self.driver.get_text_element("div", '网卡', parent_level=4))
            for nic_name in nic_name_list:
                self.driver.click(self.driver.get_text_element("div", nic_name, parent_level=2))

    def input_ipv4_addr(self, ipv4_addr, clear=False):
        '''输入IPv4地址'''
        with allure.step('输入IPv4地址'):
            self.driver.input_text_by_label('IPv4地址*', ipv4_addr, clear)

    def input_ipv4_subnet_mask(self, ipv4_subnet_mask, clear=False):
        '''IPv4子网掩码'''
        with allure.step('IPv4子网掩码'):
            self.driver.input_text_by_label('IPv4子网掩码*', ipv4_subnet_mask, clear)

    def input_ipv4_gateway(self, ipv4_gateway, clear=False):
        '''输入IPv4网关'''
        with allure.step('输入IPv4网关'):
            self.driver.input_text_by_label('IPv4网关', ipv4_gateway, clear)

    def select_nic_type(self, nic_type_name):
        '''选择网卡类型'''
        with allure.step('选择网卡类型'):
            self.driver.click(self.driver.get_text_element("div", '类型', parent_level=1))
            self.driver.click(self.driver.get_text_element("div", nic_type_name, parent_level=1))

    def click_nic_discern(self):
        '''点击网卡识别'''
        with allure.step('点击网卡识别'):
            self.click_sub_menu()
            self.driver.click(self.driver.get_text_element('div', '网卡识别', parent_level=2))
            self.click_confirm_alert()
            self.close_alert_tip()

    def input_ip_addr(self, ip_addr, clear=False):
        with allure.step('输入IP地址'):
            self.driver.input_text_by_label(text=ip_addr, label='IP地址*', clear=clear)

    def input_hostname(self, hostname, clear=False):
        with allure.step('输入主机名'):
            self.driver.input_text_by_label(text=hostname, label='主机名*', clear=clear)

    def assert_result(self, action):
        if action == 'add':
            desc = '增加'
        elif action == 'batch_add':
            desc = '批量增加'
        elif action == 'update':
            desc = '修改'
        elif action == 'del':
            desc = '删除'

        else:
            raise ValueError('action必须为 add , batch_add , update ,del 中的一个，不能为{}'.format(action))
        try:
            self.driver.get_element(by='xpath', value=f'//div[text()="{desc}主机成功。"]')
        except Exception as e:
            with allure.step('失败截图'):
                self.driver.save_screenshot()
                raise e
        else:
            with allure.step('成功截图'):
                self.driver.save_screenshot()
