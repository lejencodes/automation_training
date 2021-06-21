import os
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as waiter
from selenium.webdriver.support import expected_conditions as EC
import yaml

sys.path.append(".")
from util.log import LogMessage

path = os.getcwd()

class LoginPage():
    def __init__(self, driver):
        # super().__init__('Chrome')
        self.driver = driver
        self.logs = LogMessage()
        self.file = open(os.path.join(path, 'data', 'page_data.yaml'), "r", encoding="utf-8")
        self.data = yaml.safe_load(self.file)
        self.file.close()
        self.login_url = self.data['login'].get('url')
        self.login_btn = self.data['login'].get('login_btn')
        self.username = self.data['login'].get('username')
        self.password = self.data['login'].get('password')
        self.submit = self.data['login'].get('submit_btn')
        self.login_err = self.data['login'].get('login_err')
        self.login_suc = self.data['login'].get('login_suc')
        self.driver.get(self.login_url)
        # self.driver.open(self.login_url)
        self.status =''

    def login(self, suc, username, password):
        try:
            xpath ='/html/body/div/div[2]/div/div[3]/div/h1'
            waiter(self.driver, 10, 1).until(EC.presence_of_element_located((By.XPATH, xpath)))
            self.driver.find_element_by_id(self.username).clear()
            self.driver.find_element_by_id(self.username).send_keys(username)
            self.driver.find_element_by_id(self.password).click()
            self.driver.find_element_by_id(self.password).send_keys(password)
            self.driver.find_element_by_id(self.submit).click()
            if suc == '1':
                # wait for page change
                xpath ='//h1[@class="page-heading" and contains(text(),"My account")]'
                waiter(self.driver,10,1).until(EC.presence_of_element_located((By.XPATH, xpath)))
                self.status = self.driver.find_element_by_xpath(self.login_suc).text
                return self.status
            if suc == '0':
                # wait for page change
                xpath='//div[@class="alert alert-danger"]'
                waiter(self.driver,10,1).until(EC.presence_of_all_elements_located((By.XPATH,xpath)))
                self.status = self.driver.find_element_by_xpath(self.login_err).text
                return self.status
        except Exception as e:
            self.logs.error_log(f'Test Failed，Error：{e}')
        finally:
            self.driver.quit()


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        title = '注册模块'
        self.logs = LogMessage()
        self.file = open(os.path.join(path, 'data', 'page_data.yaml'), "r", encoding="utf-8")
        self.data = yaml.load(self.file)
        self.file.close()
        self.reg_url = self.data['register'].get('url')
        self.reg_btn = self.data['register'].get('register_btn')
        self.reg_user = self.data['register'].get('username')
        self.reg_pwd = self.data['register'].get('password')
        self.reg_pwd1 = self.data['register'].get('password1')
        self.reg_mobile = self.data['register'].get('mobile')
        self.reg_email = self.data['register'].get('email')
        self.reg_submit_btn = self.data['register'].get('submit_btn')
        self.reg_suc = self.data['register'].get('register_suc')
        self.reg_err = self.data['register'].get('register_err')
        self.driver.get(self.reg_url)

    def register(self, suc, username, password, password1, mobile, email):
        try:
            self.driver.find_element_by_link_text(self.reg_btn).click()
            self.driver.find_element_by_class_name(self.reg_user).clear()
            self.driver.find_element_by_class_name(self.reg_user).send_keys(username)
            self.driver.find_element_by_class_name(self.reg_pwd).clear()
            self.driver.find_element_by_class_name(self.reg_pwd).send_keys(password)
            self.driver.find_element_by_class_name(self.reg_pwd1).clear()
            self.driver.find_element_by_class_name(self.reg_pwd1).send_keys(password1)
            self.driver.find_element_by_class_name(self.reg_mobile).clear()
            self.driver.find_element_by_class_name(self.reg_mobile).send_keys(mobile)
            self.driver.find_element_by_class_name(self.reg_email).clear()
            self.driver.find_element_by_class_name(self.reg_email).send_keys(email)
            self.driver.find_element_by_class_name(self.reg_submit_btn).click()
            if suc == "1":
                self.reg_status = self.driver.find_element_by_id(self.reg_suc).text
                return self.reg_status
            if suc == '0':
                self.reg_status = self.driver.find_element_by_xpath(self.reg_err).text
                return self.reg_status
        except Exception as e:
            self.logs.error_log(f'Test Failed，Error：{e}')
        finally:
            self.driver.quit()


class ForgotPasswordPage:
    def __init__(self, driver):
        self.driver = driver
        self.logs = LogMessage()
        self.file = open(os.path.join(path, 'data', 'page_data.yaml'), "r", encoding="utf-8")
        self.data = yaml.load(self.file)
        self.file.close()
        self.reset_url = self.data['forgotpassword'].get('url')
        self.reset_username = self.data['forgotpassword'].get('username')
        self.reset_email = self.data['forgotpassword'].get('email')
        self.reset_submit_btn = self.data['forgotpassword'].get('submit_btn')
        self.reset_err = self.data['forgotpassword'].get('rec_err')
        self.reset_suc = self.data['forgotpassword'].get('rec_suc')
        self.driver.get(self.reset_url)

    def retrieve(self, suc, name, eamil):
        try:
            self.driver.find_element_by_css_selector(self.reset_username).clear()
            self.driver.find_element_by_css_selector(self.reset_username).send_keys(name)
            self.driver.find_element_by_css_selector(self.reset_email).clear()
            self.driver.find_element_by_css_selector(self.reset_email).send_keys(eamil)
            self.driver.find_element_by_css_selector(self.reset_submit_btn).click()
            if suc == '1':
                self.reset_suc = self.driver.find_element_by_css_selector(self.reset_suc).text
                return self.reset_suc
            if suc == "0":
                self.reset_suc = self.driver.find_element_by_xpath(self.reset_err).text
                return self.reset_suc
        except Exception as e:
            self.logs.error_log(f'Test Failed，Error：{e}')
        finally:
            self.driver.quit()


class ChangePasswordPage:
    def __init__(self, driver):
        title = '修改模块'
        self.logs = LogMessage()
        self.driver = driver
        self.file = open(os.path.join(path, 'data', 'page_data.yaml'), "r", encoding="utf-8")
        self.data = yaml.load(self.file)
        self.file.close()
        self.url = self.data['changepassword'].get('url')
        self.pwd = self.data['changepassword'].get('password')
        self.pwd1 = self.data['changepassword'].get('newpassword')
        self.pwd2 = self.data['changepassword'].get('confirmpassword')
        self.submit_btn = self.data['changepassword'].get('submit_btn')
        self.change_suc = self.data['changepassword'].get('suc')
        self.change_err = self.data['changepassword'].get('err')
        self.driver.get(self.url)

    def change_pwd(self, suc, ori_pass, new_pwd, confirm_pwd):
        try:
            self.driver.find_element_by_css_selector(self.pwd).clear()
            self.driver.find_element_by_css_selector(self.pwd).send_keys(ori_pass)
            self.driver.find_element_by_css_selector(self.pwd1).clear()
            self.driver.find_element_by_css_selector(self.pwd1).send_keys(new_pwd)
            self.driver.find_element_by_css_selector(self.pwd2).clear()
            self.driver.find_element_by_css_selector(self.pwd2).send_keys(confirm_pwd)
            self.driver.find_element_by_link_text(self.submit_btn).click()
            if suc == '1':
                self.change_status = self.driver.find_element_by_id(self.change_suc).text
                return self.change_status
            if suc == '0':
                self.change_status = self.driver.find_element_by_xpath(self.change_err).text
                return self.change_status
        except Exception as e:
            self.logs.error_log(f'Test Failed，Error：{e}')
        finally:
            self.driver.quit()
