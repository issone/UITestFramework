import os
import random
import string
import time
from functools import partial

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common import logger
from config.common import SCREENSHOT_DIR, BASE_PATH

LOCATOR_LIST = {
    'css': By.CSS_SELECTOR,
    'id': By.ID,
    'name': By.NAME,
    'xpath': By.XPATH,
    'link_text': By.LINK_TEXT,
    'partial_link_text': By.PARTIAL_LINK_TEXT,
    'tag': By.TAG_NAME,
    'class_name': By.CLASS_NAME,
}


class WebDriver:

    def __init__(self, driver_name=None, driver_path=None, timeout=10):
        driver = None
        if driver_path is None:
            driver_path = os.path.join(BASE_PATH, 'utils', 'chromedriver.exe')
        if driver_name is None:
            driver_name = "chrome"
        if driver_name == "chrome":
            driver = webdriver.Chrome(executable_path=driver_path)
        elif driver_name == 'firefox':
            driver = webdriver.Firefox(executable_path=driver_path)
        elif driver_name == 'ie':
            driver = webdriver.Ie()
        elif driver_path == 'edge':
            driver = webdriver.Edge()

        if driver is None:
            raise NameError(
                "Not found {} browser, You can enter 'ie', 'firefox','edge', 'chrome'.".format(driver_name))
        else:
            self.driver = driver
            self.timeout = timeout
            self.wait = WebDriverWait(self.driver, self.timeout)
            self.logger = logger.Logger().get_logger()

    @property
    def origin(self):
        return self.driver

    def get(self, url):
        '''访问网址'''
        self.driver.get(url)
        self.logger.info("访问网址：" + url)

    def open(self, url):
        """
        打开url
        """
        self.get(url)

    def quit(self):
        '''关闭浏览器'''
        self.driver.quit()
        self.logger.info("退出浏览器")

    def close(self):
        '''
        关闭当前窗口
        :return:
        '''
        self.driver.close()
        self.logger.info("退出浏览器")

    def get_current_url(self):
        '''获取当前url'''
        self.logger.info("获取当前url:" + self.driver.current_url)
        return self.driver.current_url

    def get_title(self):
        '''获取网页title'''
        self.logger.info("获取网页title：" + self.driver.title)
        return self.driver.title

    def max_window(self):
        self.logger.info("窗口最大化")
        self.driver.maximize_window()

    def set_window(self, wide, high):
        self.logger.info("窗口大小设置为，宽：{}，高{}".format(wide, high))
        self.driver.set_window_size(wide, high)

    def get_text_element(self, tag_name='', text='', multi=False, seq=1, parent_level=0, timeout=None,
                         raise_error=True):
        xpath = '//'
        if tag_name:
            xpath += tag_name
        else:
            xpath += '*'

        xpath += '[text()="{}"]'.format(text)

        for i in range(parent_level):
            xpath += '/..'
        elems = self.driver.find_elements_by_xpath(xpath)
        if timeout is None:
            timeout = self.timeout
        start_time = time.time()
        while time.time() - start_time < timeout:
            if elems:
                self.logger.info("找到{}个文字内容为{}的{}标签".format(len(elems), text, tag_name))
                break

            else:
                time.sleep(0.5)
        else:
            error_info = "未找到文字内容为{}的{}标签".format(text, tag_name)
            self.logger.error(error_info)
            if raise_error:
                raise Exception(error_info)
            else:
                return []

        if multi:
            return elems
        else:
            return elems[seq - 1]

    def get_contains_text_element(self, tag_name='', text="", multi=False, parent_level=0, timeout=None):
        if timeout is None:
            timeout = self.timeout
        xpath = '//'
        if tag_name:
            xpath += tag_name
        else:
            xpath += '*'

        xpath += '[contains(text(),"{}")]'.format(text)

        for i in range(parent_level):
            xpath += '/..'

        elems = self.driver.find_elements_by_xpath(xpath)

        start_time = time.time()
        while time.time() - start_time < timeout:
            if elems:
                self.logger.info("找到{}个文字内容包含{}的{}标签".format(len(elems), text, tag_name))
                break

            else:
                time.sleep(0.5)
        else:
            error_info = "未找到文字内容包含{}的{}标签".format(text, tag_name)
            self.logger.error(error_info)
            raise Exception(error_info)

        if multi:
            return elems
        else:
            return elems[0]

    def _find_element(self, locator, timeout):
        """
        Find if the element exists.
        """
        start_time = time.time()
        while time.time() - start_time < timeout:
            elems = self.driver.find_elements(by=locator[0], value=locator[1])
            if elems:
                break
            else:
                time.sleep(0.5)
                print('未找到', locator[0], locator[1])
        else:
            error_info = "定位元素超时，未定位到该元素({},{})".format(locator[0], locator[1])
            self.logger.error(error_info)
            self.save_screenshot()
            raise Exception(error_info)
        self.logger.info("找到{n}个元素 ：{by}={value}".format(n=len(elems), by=locator[0], value=locator[1]))

    def get_element(self, by, value, multi=False, timeout=None):
        """
        Judge element positioning way, and returns the element.
        """
        try:
            LOCATOR_LIST[by]
        except KeyError:
            raise ValueError("Element positioning of type '{}' is not supported. ".format(by))
        if timeout is None:
            timeout = self.timeout
        self._find_element = partial(self._find_element, timeout=timeout)
        if by == "id":
            self._find_element((By.ID, value))
            if multi:
                element = self.driver.find_elements_by_id(value)
            else:
                element = self.driver.find_element_by_id(value)
        elif by == "name":
            self._find_element((By.NAME, value))
            if multi:
                element = self.driver.find_elements_by_name(value)
            else:
                element = self.driver.find_element_by_name(value)
        elif by == "class_name":
            self._find_element((By.CLASS_NAME, value))
            if multi:
                element = self.driver.find_elements_by_class_name(value)

            else:
                element = self.driver.find_element_by_class_name(value)
        elif by == "tag":
            self._find_element((By.TAG_NAME, value))
            if multi:
                element = self.driver.find_elements_by_tag_name(value)

            else:
                element = self.driver.find_element_by_tag_name(value)
        elif by == "link_text":
            self._find_element((By.LINK_TEXT, value))
            if multi:
                element = self.driver.find_elements_by_link_text(value)
            else:
                element = self.driver.find_element_by_link_text(value)
        elif by == "xpath":
            self._find_element((By.XPATH, value))
            if multi:
                element = self.driver.find_elements_by_xpath(value)
            else:
                element = self.driver.find_element_by_xpath(value)
        elif by == "css":
            self._find_element((By.CSS_SELECTOR, value))
            if multi:
                element = self.driver.find_elements_by_css_selector(value)
            else:
                element = self.driver.find_element_by_css_selector(value)
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id_/name/class/tag/link_text/xpath/css'.")
        return element

    def clear(self, **kwargs):
        """
        Clear the contents of the input box.
        Usage:
        self.clear(css="#elem")
        """
        if not kwargs:
            raise ValueError("Please specify a locator")
        if len(kwargs) > 1:
            raise ValueError("Please specify only one locator")
        elem = self.get_element(**kwargs)
        self.logger.info('清空输入值')
        elem.clear()

    def input_text(self, elem, text, clear=False):
        self.logger.info('输入{}'.format(text))
        self.click(elem)
        try:
            if clear:
                self.select_all_clear(elem)

                # self.double_click_clear(elem)
            elem.send_keys(text)
        except Exception as e:
            error_info = "输入{}失败".format(text)
            self.logger.error(error_info)
            self.save_screenshot()
            raise e

    def input_text_by_label(self, label, text, clear=False):
        self.logger.info('查找aria-label属性为{}的input输入框，并输入{}'.format(label, text))
        try:
            elem = self.get_element('xpath', '// input[@aria-label="{}"]'.format(label))
            if clear:
                self.select_all_clear(elem)
            elem.send_keys(text)
        except Exception as e:
            error_info = "输入{}失败".format(text)
            self.logger.error(error_info)
            self.save_screenshot()
            raise e

    def select_all_clear(self, elem):
        '''
        全选删除
        :param elem: 要进行操作的元素
        :return:
        '''
        elem.send_keys(Keys.CONTROL, 'a')  # 全选
        elem.send_keys(Keys.BACKSPACE)
        while elem.text:
            elem.send_keys(Keys.CONTROL, 'a')  # 全选
            elem.send_keys(Keys.BACKSPACE)

        self.logger.info('全选删除')

    def double_click_clear(self, elem):
        '''
        双击删除
        :param elem: 要进行操作的元素
        :return:
        '''
        action_chains = ActionChains(self.origin)
        action_chains.double_click(elem).perform()
        elem.send_keys(Keys.BACKSPACE)  # 删除

    def double_click(self, **kwargs):
        """
        Double click element.
        Usage:
        self.double_click(css="#elem")
        """
        if not kwargs:
            raise ValueError("Please specify a locator")
        if len(kwargs) > 1:
            raise ValueError("Please specify only one locator")
        elem = self.get_element(**kwargs)
        ActionChains(self.driver).double_click(elem).perform()

    def click(self, elem, timeout=None):
        if timeout is None:
            timeout = self.timeout
        start_time = time.time()
        while time.time() - start_time < timeout:
            if elem.is_displayed() and elem.is_enabled():
                elem.click()
                return
            else:
                time.sleep(0.5)

        raise NotImplementedError('无法被点击')

    def refresh(self):
        """
        Refresh the current page.
        Usage:
        self.refresh()
        """
        self.driver.refresh()

    def save_screenshot(self, file_name=time.strftime('%Y-%m-%d_%H-%S-%M', time.localtime(time.time()))):
        '''屏幕截图'''

        self.logger.info("进行截图！！")
        try:
            file_name = file_name + ''.join(random.sample(string.digits, 6)) + '.png'
            file_path = os.path.join(SCREENSHOT_DIR, file_name)

            self.driver.save_screenshot(file_path)
            allure.attach.file(file_path, attachment_type=allure.attachment_type.PNG)
            self.logger.info("已成功生成截图，请确认！")
        except:
            raise Exception("截图失败!")

    def js_replace_text(self, elem, text):
        self.origin.execute_script("arguments[0].innerText = arguments[1]", elem, text)

    def sleep(self, seconds):
        time.sleep(seconds)

    def switch_to_window(self, window_name):
        self.origin.switch_to.window(window_name)
