import json
import time
import os
import allure
import pytest

from common.driver import WebDriver
from pages.host_resource_page import HostResourcePage
from pages.login_page import LoginPage
from pages.modify_pwd_page import ModifyPwdPage
from pages.vpool_page import VPoolPage
from config.page_config import *


class TestISCloud(object):
    '''
       1、用fixture在所有用例开始前初始化测试对象、在所有用例结束后销毁测试对象
       2、yield是用于生成器，与return不同！所有用例执行完后，会执行yield后面的代码，
           无论用例是否执行成功，该代码都会执行（相当于teardown）
       3、在一个文件中，用例的执行顺序是从上到下的

       '''

    def setup_class(self):  # 执行前运行一次
        self.driver = WebDriver()

    def teardown_class(self):  # 执行完毕后运行一次
        self.driver.quit()

    @allure.feature('测试登录')
    @allure.story('测试登录')
    @allure.title('测试登录')
    # @pytest.mark.skip(reason="跳过登录")
    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.open(LOGIN_URL)
        login_page.input_username(USERNAME)
        login_page.input_password(PASSWORD)
        login_page.click_login_button()
        login_page.assert_result()

    @allure.feature('修改密码测试')
    @allure.story('修改密码')
    @allure.title('修改测试')
    @pytest.mark.skip(reason="修改密码已测试完毕")   # 跳过测试用例
    def test_modify_pwd(self):

        page = ModifyPwdPage(self.driver)
        page.click_modify_pwd_menu()
        page.input_old_password(PASSWORD)
        page.input_new_password(NEW_PASSWORD)
        page.input_confirm_password(NEW_PASSWORD)
        page.click_save()
        page.click_confirm_alert()
        page.assert_result()
        self.test_login()

    @allure.feature('资源池测试')
    @allure.story('增加')
    @allure.title('增加资源池')
    @pytest.mark.skip(reason="测试完毕")
    def test_add_vpool(self):
        page = VPoolPage(self.driver)
        page.into_vpool()
        page.click_sub_menu()
        page.click_add_menu()
        page.input_pool_name(POOL_NAME)
        page.input_pool_desc(POOL_DESC)
        page.click_save()
        page.assert_result(action='add', pool_name=POOL_NAME)
        page.close_alert_tip()

    @allure.feature('资源池测试')
    @allure.story('修改')
    @allure.title('修改资源池')
    @pytest.mark.skip(reason="测试完毕")
    def test_update_vpool(self):
        page = VPoolPage(self.driver)
        page.into_vpool()
        page.select_pool(POOL_NAME)
        page.click_sub_menu()
        page.click_update_menu()
        page.input_pool_name(NEW_POOL_NAME, clear=True)
        page.input_pool_desc(NEW_POOL_DESC, clear=True)
        page.click_save()
        page.assert_result(action='update', pool_name=NEW_POOL_NAME)
        page.close_alert_tip()

    @allure.feature('资源池测试')
    @allure.story('删除')
    @allure.title('删除资源池')
    @pytest.mark.skip(reason="测试完毕")
    def test_del_vpool(self):
        page = VPoolPage(self.driver)
        page.into_vpool()
        page.select_pool(NEW_POOL_NAME)
        page.click_sub_menu()
        page.click_del_menu()
        page.click_confirm_alert()
        page.assert_result(action='del', pool_name='资源池')
        page.close_alert_tip()

    @allure.feature('主机资源测试')
    @allure.story('增加')
    @allure.title('增加单台主机')
    # @pytest.mark.skip(reason="测试完毕")
    def test_add_single_host_resource(self):
        page = HostResourcePage(self.driver)
        page.into_host_resource()
        page.click_sub_menu()
        page.click_add_menu()
        page.input_ip_addr(IP_ADDR)
        page.input_hostname(HOST_NAME)
        page.select_vpool(POOL_NAME)
        page.select_host_type(HOST_TYPE_NAME)
        page.click_save()
        page.assert_result(action='add')

    @allure.feature('主机资源测试')
    @allure.story('增加')
    @allure.title('批量增加主机')
    @pytest.mark.skip(reason="测试完毕")
    def test_batch_add_host_resource(self):
        page = HostResourcePage(self.driver)
        page.into_host_resource()
        page.click_sub_menu()
        page.click_add_menu(batch=True)
        page.select_vpool(POOL_NAME)
        page.select_host_type(HOST_TYPE_NAME)
        page.input_start_and_end_ip(start_ip=START_IP_ADDR, end_ip=END_IP_ADDR)
        page.click_scan()
        page.click_save()
        page.assert_result(action='batch_add')

    @allure.feature('主机资源测试')
    @allure.title('修改主机信息')
    @allure.story('修改')
    @pytest.mark.skip(reason="测试完毕")
    def test_update_single_host_resource(self):
        page = HostResourcePage(self.driver)
        page.into_host_resource()
        page.select_host_click_sub_menu(HOST_NAME)
        page.click_update_menu()
        page.input_hostname(hostname=NEW_HOST_NAME, clear=True)
        page.select_vpool(pool_name=NEW_POOL_NAME)
        page.select_host_type(host_type_name=NEW_HOST_TYPE_NAME)
        page.click_save()
        page.assert_result(action='update')

    @allure.feature('主机资源测试')
    @allure.story('删除')
    @allure.title('删除主机')
    @pytest.mark.skip(reason="测试完毕")
    def test_del_single_host_resource(self):
        page = HostResourcePage(self.driver)
        page.into_host_resource()
        page.select_host_click_sub_menu(HOST_NAME)
        page.click_del_menu()
        page.click_confirm_alert()
        page.assert_result(action='del')

    @allure.feature('主机资源测试')
    @allure.story('删除')
    @allure.title('批量删除主机')
    @pytest.mark.skip(reason="测试完毕")
    def test_batch_del_host_resource(self):
        page = HostResourcePage(self.driver)
        page.into_host_resource()
        for hostname in HOST_NAME_LIST:
            page.select_host(hostname)
        page.click_sub_menu()
        page.click_del_menu()
        page.click_confirm_alert()
        page.assert_result(action='del')

    @allure.feature('主机资源测试')
    @allure.story('详细')
    @allure.title('查看主机详情')
    @pytest.mark.skip(reason="测试完毕")
    def test_detail_host_resource(self):
        page = HostResourcePage(self.driver)
        page.into_host_resource()
        page.select_host_click_sub_menu(HOST_NAME)
        page.click_detail_menu()
        try:
            self.driver.get_text_element("div", "概要")
        except Exception as e:
            page.final_assert(e)
        else:
            page.final_assert(True)

    @allure.feature('主机资源测试')
    @allure.story('物理网卡')
    @allure.title('查看物理网卡列表')
    @pytest.mark.skip(reason="测试完毕")
    def test_get_physical_adapter_list(self):
        page = HostResourcePage(self.driver)
        page.into_host_resource()
        page.select_host_click_sub_menu(HOST_NAME)
        page.click_physical_adapter_menu()
        try:
            self.driver.get_contains_text_element("th", "IPv4地址")
        except Exception as e:
            page.final_assert(e)
        else:
            page.final_assert(True)

    @allure.feature('主机资源测试')
    @allure.story('物理网卡')
    @allure.title('网卡识别')
    @pytest.mark.skip(reason="测试完毕")
    def test_nic_discern(self):

        page = HostResourcePage(self.driver)
        page.into_host_resource()
        page.select_host_click_sub_menu(HOST_NAME)
        page.click_physical_adapter_menu()
        page.check_first_nic()
        page.click_nic_discern()

        try:
            self.driver.get_text_element("div", "网卡识别成功。")
        except Exception as e:
            page.final_assert(e)
        else:
            page.final_assert(True)

    @allure.feature('主机资源测试')
    @allure.story('虚拟网卡')
    @allure.title('查看虚拟网卡列表')
    @pytest.mark.skip(reason="测试完毕")
    def test_get_virtul_adapter_list(self):
        page = HostResourcePage(self.driver)
        page.into_host_resource()
        page.select_host_click_sub_menu(HOST_NAME)
        page.click_virtul_adapter_menu()
        try:
            self.driver.get_contains_text_element("th", "IPv4地址")
        except Exception as e:
            page.final_assert(e)
        else:
            page.final_assert(True)

    @allure.feature('主机资源测试')
    @allure.story('虚拟网卡')
    @allure.title('创建虚拟网卡')
    @pytest.mark.skip(reason="测试完毕")
    def test_add_virtul_adapter(self):
        page = HostResourcePage(self.driver)
        page.into_host_resource()
        page.select_host_click_sub_menu(HOST_NAME)
        page.click_virtul_adapter_menu()
        page.click_sub_menu()
        page.click_add_menu()
        page.select_nic(VIRTUL_NIC_NAME_LIST)
        page.input_ipv4_addr(IPV4_ADDR)
        page.input_ipv4_subnet_mask(IPV4_SUBNET_MASK)
        page.select_nic_type(VIRTUL_NIC_TYPE)
        page.click_save()
        try:
            self.driver.get_text_element("div", "创建虚拟网卡成功")
        except Exception as e:
            page.final_assert(e)
        else:
            page.final_assert(True)

    @allure.feature('主机资源测试')
    @allure.story('虚拟网卡')
    @allure.title('删除虚拟网卡')
    @pytest.mark.skip(reason="测试完毕")
    def test_del_virtul_adapter(self):
        page = HostResourcePage(self.driver)
        page.into_host_resource()
        page.select_host_click_sub_menu(HOST_NAME)
        page.click_virtul_adapter_menu()
        page.check_first_nic()
        page.click_sub_menu()
        page.click_del_menu()
        page.click_confirm_alert()
        try:
            self.driver.get_text_element("div", "删除虚拟网卡成功")
        except Exception as e:
            page.final_assert(e)
        else:
            page.final_assert(True)

    @allure.feature('主机资源测试')
    @allure.story('SSH客户端')
    @allure.title('SSH客户端测试')
    @pytest.mark.skip(reason="不确定")
    def test_terminal(self):
        page = HostResourcePage(self.driver)
        page.into_host_resource()
        page.select_host_click_sub_menu(HOST_NAME)
        page.click_terminal_menu()
        try:
            self.driver.get_element("xpath", '//div[@id="terminal-container"]', timeout=30)
        except Exception as e:
            page.final_assert(e)
        else:
            page.final_assert(True)

    @allure.feature('主机资源测试')
    @allure.story('操作日志')
    @allure.title('查看操作日志列表')
    @pytest.mark.skip(reason="测试完毕")
    def test_get_operation_log_list(self):
        page = HostResourcePage(self.driver)
        page.into_host_resource()
        page.select_host_click_sub_menu(HOST_NAME)
        page.click_operation_log_menu()
        try:
            self.driver.get_contains_text_element("th", "操作日志")
        except Exception as e:
            page.final_assert(e)
        else:
            page.final_assert(True)

    @allure.feature('主机资源测试')
    @allure.story('报警日志')
    @allure.title('查看报警日志列表')
    @pytest.mark.skip(reason="测试完毕")
    def test_get_warn_log_list(self):
        page = HostResourcePage(self.driver)
        page.into_host_resource()
        page.select_host_click_sub_menu(HOST_NAME)
        page.click_warn_log_menu()
        try:
            self.driver.get_contains_text_element("th", "报警日志")
        except Exception as e:
            page.final_assert(e)
        else:
            page.final_assert(True)
