from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class BrowserTypeError(Exception):
    pass


class MethodError(Exception):
    pass


class Browser:
    """Create a browser instance"""

    # 打开浏览器并初始化
    def __init__(self, browser, method="xpath"):
        if browser == 'firefox' or browser == 'Firefox' or browser == 'f' or browser == 'F':
            driver = webdriver.Firefox()
        elif browser == 'Ie' or browser == 'ie' or browser == 'i' or browser == 'I':
            driver = webdriver.Ie()
        elif browser == 'Chrome' or browser == 'chrome' or browser == 'Ch' or browser == 'ch':
            driver = webdriver.Chrome()
        elif browser == 'PhantomJS' or browser == 'phantomjs' or browser == 'ph' or browser == 'phjs':
            driver = webdriver.PhantomJS()
        elif browser == 'Edge' or browser == 'edge' or browser == 'Ed' or browser == 'ed':
            driver = webdriver.Edge()
        elif browser == 'Opera' or browser == 'opera' or browser == 'op' or browser == 'OP':
            driver = webdriver.Opera()
        elif browser == 'Safari' or browser == 'safari' or browser == 'sa' or browser == 'saf':
            driver = webdriver.Safari()
        else:
            raise BrowserTypeError(u'当前仅支持 Firefox,Ie,Chrome,PhantomJS,Edge,Opera,Safari 等浏览器')
        self.driver = driver
        self.driver.maximize_window()
        self.method = method

    # 选择元素定位方式
    def loc_method_select(self, method):
        methods = ["id", "name", "class", "link_text", "xpath", "tag", "css"]
        if method in methods:
            self.method = method
        else:
            raise MethodError("Method not correct")

    # 定位元素
    def loc_element(self, key):
        if self.method == 'id':
            element = self.driver.find_element_by_id(key)
        elif self.method == "name":
            element = self.driver.find_element_by_name(key)
        elif self.method == "class":
            element = self.driver.find_element_by_class_name(key)
        elif self.method == "link_text":
            element = self.driver.find_element_by_link_text(key)
        elif self.method == "xpath":
            element = self.driver.find_element_by_xpath(key)
        elif self.method == "tag":
            element = self.driver.find_element_by_tag_name(key)
        elif self.method == "css":
            element = self.driver.find_element_by_css_selector(key)
        return element

    # 定位多个元素
    def loc_elements(self, key):
        if self.method == 'id':
            element = self.driver.find_elements_by_id(key)
        elif self.method == "name":
            element = self.driver.find_elements_by_name(key)
        elif self.method == "class":
            element = self.driver.find_elements_by_class_name(key)
        elif self.method == "link_text":
            element = self.driver.find_elements_by_link_text(key)
        elif self.method == "xpath":
            element = self.driver.find_elements_by_xpath(key)
        elif self.method == "tag":
            element = self.driver.find_elements_by_tag_name(key)
        elif self.method == "css":
            element = self.driver.find_elements_by_css_selector(key)
        return element

    # 检查页面元素是否存在
    def wait_in_position(self, key, timeout=5):
        if self.method == "id":
            WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located((By.ID, key)))
        elif self.method == "name":
            WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located((By.NAME, key)))
        elif self.method == "class":
            WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located((By.CLASS_NAME, key)))
        elif self.method == "link_text":
            WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located((By.LINK_TEXT, key)))
        elif self.method == "xpath":
            WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located((By.XPATH, key)))
        elif self.method == "css":
            WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located((By.CSS_SELECTOR, key)))

    # 打开URL页面
    def open(self, url):
        self.driver.get(url)

    # 发送指定内容
    def send_key(self, key, text):
        element = self.loc_element(key)
        element.clear()
        element.send_keys(text)

    # 清空输入框
    def clear(self, key):
        self.wait_in_position(key)
        element = self.loc_element(key)
        element.clear()
    
    # 单击
    def click(self, key):
        self.wait_in_position(key)
        element = self.loc_element(key)
        element.click()

    # 右击
    def right_click(self, key):
        self.wait_in_position(key)
        element = self.loc_element(key)
        ActionChains(self.driver).context_click(element).perform()

    # 移动
    def move_element(self, key):
        self.wait_in_position(key)
        element = self.loc_element(key)
        ActionChains(self.driver).move_to_element(element).perform()

    # 双击
    def double_click(self, key):
        self.wait_in_position(key)
        element = self.loc_element(key)
        ActionChains(self.driver).double_click(element).perform()

    # 拖放
    def drag_and_drop(self, source, destination):
        self.wait_in_position(source)
        src_elem = self.loc_element(source)
        self.wait_in_position(destination)
        dst_elem = self.loc_element(destination)
        ActionChains(self.driver).drag_and_drop(src_elem, dst_elem).perform()

    # 点击文字
    def click_text(self, text):
        self.driver.find_element_by_link_text(text).click()

    # 关闭URL页面
    def close(self):
        self.driver.close()

    # 退出浏览器
    def quit(self):
        self.driver.quit()

    # 提交
    def submit(self, key):
        self.wait_in_position(key)
        element = self.loc_element(key)
        element.submit()

    # 刷新页面
    def refresh(self):
        self.driver.refresh()

    # 执行js命令
    def execute_js(self, cmd):
        self.driver.execute_script(cmd)

    # 获取元素属性
    def get_attribute(self, key, attribute):
        element = self.loc_element(key)
        return element.get_attribute(attribute)

    # 获取文字
    def get_text(self, key):
        self.wait_in_position(key)
        element = self.loc_element(key)
        return element.text

    # 判断元素是否可见
    def is_visible(self, key):
        self.wait_in_position(key)
        element = self.loc_element(key)
        return element.is_displayed()

    # 获取title
    def get_title(self):
        return self.driver.title

    # 截屏
    def screenshot(self, file_path):
        self.driver.get_screenshot_as_file(file_path)

    # 等待
    def wait(self, timeout):
        self.driver.implicitly_wait(timeout)

    # 接受弹窗告警
    def accept(self):
        self.driver.switch_to.alert.accept()

    # 取消弹窗告警
    def dismiss(self):
        self.driver.switch_to.alert.dismiss()

    # 切换至表单内嵌页面
    def switch_to_frame(self, key):
        self.wait_in_position(key)
        element = self.loc_element(key)
        self.driver.switch_to.frame(element)
