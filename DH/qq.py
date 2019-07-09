#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest
import time
# from DH import login


class Logzin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("http://www.baidu.com")
        self.driver.implicitly_wait(30)  # 隐性等待30秒

    def tearDown(self):
        self.driver.quit()

    def sear(self,username):
        self.driver.find_element_by_id("kw").send_keys(username)
        self.driver.find_element_by_id("su").click()

    def sosuo(self,so):
        self.sear("selenium难度几何", '')
        so = self.driver.find_element_by_css_selector(".searchTool-spanner").text
        self.assertEqual(so, "搜素工具")


if __name__ == '__main__':
    unittest.main()