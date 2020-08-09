# -*- coding: utf-8 -*-
# @Author  : leizi
from comm.funnicgong import Xiugai_tes
from selenium import webdriver
import unittest,time,os,ddt
from function import log
from function.gettestdata import huoqu_test
path=os.getcwd()
case_path=path+'\\data\\cases.xlsx'
casedata=huoqu_test(case_path,3)
@ddt.ddt
class Test_xiugai(unittest.TestCase):
    def setUp(self):
        self.logs = log.Log()
        self.derve=webdriver.Fi()
        self.xiugai_fun=Xiugai_tes(self.derve)
    @ddt.data(*casedata)
    def test_xiugai_1(self,casedata):
        self.password=casedata['yuanmi']
        self.xiugaimi=casedata['xiugaimi']
        self.xiugaimi1=casedata['xiugaimi1']
        self.suc=casedata['suc']
        self.assert_vale=casedata['assert_vale']
        self.return_data=self.xiugai_fun.xiugai(self.suc,self.password,self.xiugaimi,self.xiugaimi1)
        self.logs.info_log("input: password:%s,xiugaimima:%s,xiugaimima1:%s,assert:%s"%(self.password,self.xiugaimi,self.xiugaimi1,self.assert_vale))
        time.sleep(1)
        self.assertAlmostEqual(self.return_data,self.assert_vale)
    def tearDown(self):
        self.derve.quit()
