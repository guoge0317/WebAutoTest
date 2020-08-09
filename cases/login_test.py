import os
import unittest
import ddt
from selenium import webdriver
from function import log
from function.gettestdata import huoqu_test
from comm.funnicgong import Login_tes

path = os.getcwd()
case_path = path + r'\data\case.xlsx'
casedata = huoqu_test(case_path, 3)


@ddt.ddt
class Testlogin(unittest.TestCase):
    def setUp(self):
        self.logs = log.Log()
        self.driver = webdriver.Firefox()
        self.login_fun = Login_tes(self.driver)

    @ddt.data(*casedata)
    def test_login1(self, casedata):
        self.name = casedata['username']
        self.pwd = casedata['pwd']
        self.suc = casedata['suc']
        self.assert_value = casedata['assert']
        self.driver.get_screenshot_as_file(path + '\\screenshot\\%s.png' % casedata)
        self.logs.info_log(
            'input data:name:%s,pwd:%s,suc:%s,assert:%s' % (self.name, self.pwd, self.suc, self.assert_value))
        self.re_data = self.login_fun.login(self.suc, self.name, self.pwd)
        self.assertEqual(self.re_data, self.assert_value)

    def tearDown(self):
        self.driver.quit()
