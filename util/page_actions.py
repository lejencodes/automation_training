import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from config import settings


class PySele:
    def __init__(self, browser):
        if browser in ['firefox', 'Firefox', 'f', 'F']:
            driver = webdriver.Firefox()
        elif browser in ['Ie', 'ie', 'i', 'I']:
            driver = webdriver.Ie()
        elif browser in ['Chrome', 'chrome', 'Ch', 'ch']:
            driver = webdriver.Chrome()
        elif browser in ['PhantomJS', 'phantomjs', 'ph', 'phjs']:
            driver = webdriver.PhantomJS()
        elif browser in ['Edge', 'edge', 'Ed', 'ed']:
            driver = webdriver.Edge()
        elif browser in ['Opera', 'opera', 'op', 'OP']:
            driver = webdriver.Opera()
        elif browser in ['Safari', 'safari', 'sa', 'saf']:
            driver = webdriver.Safari()
        else:
            raise NameError('Please select from: Firefox,Ie,Chrome,PhantomJS,Edge,Opera,Safari')
        self.driver = driver

    def element(self, by, selector):  # single
        if by == 'id':
            element = self.driver.find_element_by_id(selector)
        elif by == "name":
            element = self.driver.find_element_by_name(selector)
        elif by == "class":
            element = self.driver.find_element_by_class_name(selector)
        elif by == "link_text":
            element = self.driver.find_element_by_link_text(selector)
        elif by == "xpath":
            element = self.driver.find_element_by_xpath(selector)
        elif by == "tag":
            element = self.driver.find_element_by_tag_name(selector)
        elif by == "css":
            element = self.driver.find_element_by_css_selector(selector)
        else:
            raise NameError("Please enter the  elements,'id','name','class','link_text','xpath','css','tag'.")
        return element

    def elements(self, by, selector):  # group
        if by == 'id':
            element = self.driver.find_elements_by_id(selector)
        elif by == "name":
            element = self.driver.find_elements_by_name(selector)
        elif by == "class":
            element = self.driver.find_elements_by_class_name(selector)
        elif by == "link_text":
            element = self.driver.find_elements_by_link_text(selector)
        elif by == "xpath":
            element = self.driver.find_elements_by_xpath(selector)
        elif by == "tag":
            element = self.driver.find_elements_by_tag_name(selector)
        elif by == "css":
            element = self.driver.find_elements_by_css_selector(selector)
        else:
            raise NameError("Please enter the  elements,'id','name','class','link_text','xpath','css','tag'.")
        return element

    def wait_for_element(self, by, selector, timeout=6):
        if by == "id":
            WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located((By.ID, selector)))
        elif by == "name":
            WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located((By.NAME, selector)))
        elif by == "class":
            WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located((By.CLASS_NAME, selector)))
        elif by == "link_text":
            WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located((By.LINK_TEXT, selector)))
        elif by == "xpath":
            WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located((By.XPATH, selector)))
        elif by == "css":
            WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
        else:
            raise NameError("Please enter the  elements,'id','name','class','link_text','xpath','css'.")

    def wait_for_element_present(self, selector, by=By.CSS_SELECTOR, timeout=settings.LARGE_TIMEOUT):
        """
        Searches for the specified element by the given selector. Returns the
        element object if it exists in the HTML. (The element can be invisible.)
        Raises NoSuchElementException if the element does not exist in the HTML
        within the specified timeout.
        @Params
        driver - the webdriver object
        selector - the locator for identifying the page element (required)
        by - the type of selector being used (Default: By.CSS_SELECTOR)
        timeout - the time to wait for elements in seconds
        @Returns
        A web element object
        """
        element = None
        start_ms = time.time() * 1000.0
        stop_ms = start_ms + (timeout * 1000.0)
        for _ in range(int(timeout * 10)):
            try:
                element = self.driver.find_element(by=by, value=selector)
                return element
            except Exception:
                now_ms = time.time() * 1000.0
                if now_ms >= stop_ms:
                    break
                time.sleep(0.1)
        plural = "s"
        if timeout == 1:
            plural = ""
        if not element:
            message = "Element {%s} was not present after %s second%s!" % (
                selector,
                timeout,
                plural,
            )
            print(message)
            raise NoSuchElementException()

    def open(self, url):
        '''
        Open URL
        '''
        self.driver.get(url)

    def maximize_window(self):
        self.driver.maximize_window()

    def set_window_size(self, wide, hight):
        self.driver.set_window_size(wide, hight)

    def send_key(self, by, selector, text):
        self.element(by, selector)
        el = self.element(by, selector)
        el.clear()
        el.send_keys(text)

    def clear(self, by, selector):
        self.wait_for_element(by, selector)
        el = self.element(by, selector)
        el.clear()

    def click(self, by, selector):
        self.wait_for_element(by, selector)
        el = self.element(by, selector)
        el.click()

    def right_click(self, by, selector):
        self.wait_for_element(by, selector)
        el = self.element(by, selector)
        ActionChains(self.driver).context_click(el).perform()

    def move_element(self, by, selector):
        self.wait_for_element(by, selector)
        el = self.element(by, selector)
        ActionChains(self.driver).move_to_element(el).perform()

    def double_click(self, by, selector):
        self.wait_for_element(selector, by)
        el = self.element(by, selector)
        ActionChains(self.driver).double_click(el).perform()

    def drag_and_drop(self, selector1, el, selector2, e2):  # 从e1到e2
        self.wait_for_element(selector1, el)
        eme1 = self.element(selector1, el)
        self.wait_for_element(selector2, e2)
        eme2 = self.element(selector2, e2)
        ActionChains(self.driver).drag_and_drop(eme1, eme2).perform()

    def click_text(self, text):  # 点击文字
        self.driver.find_element_by_link_text(text).click()

    def close(self):  # 关闭
        self.driver.close()

    def kill(self):  # 退出
        self.driver.quit()

    def submit(self, by, selector):  # 提交
        self.wait_for_element(by, selector)
        el = self.element(by, selector)
        el.submit()

    def f5(self):  # 刷新
        self.driver.refresh()

    def js(self, js_script):  # 执行js
        self.driver.execute_script(js_script)

    def get_attribute(self, by, selector, attribute):
        el = self.element(by, selector)
        return el.get_attribute(attribute)

    def get_text(self, by, selector):
        self.wait_for_element(by, selector)
        el = self.element(by, selector)
        return el.text

    def get_is_dis(self, by, selector):
        self.wait_for_element(by, selector)
        el = self.element(by, selector)
        return el.is_displayed()

    def get_page_title(self):
        self.wait_for_element_present("title")
        return self.driver.title

    def get_title(self):
        """ The shorter version of self.get_page_title() """
        return self.get_page_title()

    def get_screen(self, file_path):
        self.driver.get_screenshot_as_file(file_path)

    def wait(self, by, selector):
        self.driver.implicitly_wait((by, selector))

    def accept(self):
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        self.driver.switch_to.alert.dismiss()

    def switch_to_frame(self, by, selector):
        self.wait_for_element(by, selector)
        if1 = self.element(by, selector)
        self.driver.switch_to.frame(if1)
