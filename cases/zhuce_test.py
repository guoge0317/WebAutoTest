# -*- coding: utf-8 -*-
# @Author  : leizi
from comm.funnicgong import Zhuce_tes
import unittest,time,os,ddt
from function import log
from selenium import webdriver
path=os.getcwd()
from function.gettestdata import huoqu_test
case_path=path+'\\data\\cases.xlsx'
casedata=huoqu_test(case_path,1)
@ddt.ddt
class Testzhuce(unittest.TestCase):
    def setUp(self):
        self.logs = log.Log()
        self.derve=webdriver.Firefox()
        self.zhuce_fun=Zhuce_tes(self.derve)
    @ddt.data(*casedata)
    def test_zhuce_1(self,casedata):
        self.name=casedata['username']
        self.password=casedata['mima']
        self.passwordque=casedata['nima2']
        self.shoujihao=casedata['shoujihao']
        self.youxiang=casedata['youxiang']
        self.suc=casedata['suc']
        self.assert_vale=casedata['assert_vale']
        self.re_data=self.zhuce_fun.zhuce(self.name,self.password,self.passwordque,self.shoujihao,self.youxiang,self.suc)
        self.derve.get_screenshot_as_file(path+'\\screenshot\\%s.png'%casedata[id])
        self.logs.info_log("input:name:%s password:%s,passwordque:%s,shoujihao:%s,youxiang:%s ,assert:%s"%(self.name,self.password,self.passwordque,self.shoujihao,self.youxiang,self.assert_vale))
        time.sleep(1)
        self.assertEqual(self.re_data, self.assert_vale)
    def tearDown(self):
        self.derve.quit()