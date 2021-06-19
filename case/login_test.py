import os
import unittest

import ddt
import sys
sys.path.append('.')
from business.action import LoginPage
from selenium import webdriver
from util.gettestdata import get_test_data
from util.page_actions import PySele
from util.log import LogMessage
path = os.getcwd()
case_path = os.path.join(path, 'data', 'case.xlsx')
casedata = get_test_data(case_path, 'Login')
@ddt.ddt
class Testlogin(unittest.TestCase):
    def setUp(self):
        self.logs = LogMessage()
        self.driver = webdriver.Chrome()
        self.page = LoginPage(self.driver)
        self.username = ''
        self.pwd = ''
        self.suc = ''
        self.assert_value =''
        self.re_data=''
    @ddt.data(*casedata)
    def test_login_method(self, casedata):
        self.username = casedata['username']
        self.pwd = casedata['pwd']
        self.suc = casedata['suc']
        self.assert_value = casedata['assert']
        self.driver.get_screenshot_as_file(os.path.join(path, 'screenshot', f'{casedata}.png'))
        self.logs.info_log(
            'input data:name:%s,pwd:%s,suc:%s,assert:%s' % (self.username, self.pwd, self.suc, self.assert_value)
        )
        self.re_data = self.page.login(self.suc, self.username, self.pwd)
        self.assertEqual(self.re_data, self.assert_value)
    def tearDown(self):
        self.driver.quit()
