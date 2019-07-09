from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest, time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
# driver = webdriver.Firefox()
#登陆模块（函数）
from selenium.webdriver.firefox.webdriver import WebDriver
driver = webdriver.Firefox()
driver.get("http://company.dhsm.perealtech.com")
driver.maximize_window()
driver.find_element_by_css_selector("div.form-item:nth-child(1) > input:nth-child(2)").send_keys("lys")
driver.find_element_by_css_selector("div.form-item:nth-child(2) > input:nth-child(2)").send_keys("123456")
driver.find_element_by_css_selector(".el-button").click()
time.sleep(3)
driver.find_element_by_css_selector("div.menu-wrapper:nth-child(3) > a:nth-child(1) > li:nth-child(1) > span:nth-child(2)").click()
time.sleep(2)
driver.find_element_by_css_selector("html body div#app div.app-wrapper.openSidebar div.main-container section.app-main div.manage-orders div.section-top-btns form.el-form.el-form--inline div.el-form-item.el-form-item--small div.el-form-item__content div.input-width.el-input.el-input--small input.el-input__inner").send_keys("JU")
driver.find_element_by_css_selector(".el-button--primary > span:nth-child(1)").click()
time.sleep(2)
driver.find_element_by_css_selector("html body div#app div.app-wrapper.openSidebar div.main-container section.app-main div.manage-orders div.section-top-btns form.el-form.el-form--inline div.el-form-item.el-form-item--small div.el-form-item__content div.input-width.el-input.el-input--small input.el-input__inner").clear()
time.sleep(1)
driver.find_element_by_css_selector("div.el-form-item:nth-child(2) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)").send_keys("成")
driver.find_element_by_css_selector(".el-button--primary > span:nth-child(1)").click()
time.sleep(2)
driver.find_element_by_css_selector("div.el-form-item:nth-child(2) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)").clear()
driver.find_element_by_css_selector("div.el-form-item:nth-child(3) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)").send_keys("373")
driver.find_element_by_css_selector(".el-button--primary > span:nth-child(1)").click()
time.sleep(2)
driver.find_element_by_css_selector("div.el-form-item:nth-child(3) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)").clear()
driver.find_element_by_css_selector("input.el-range-input:nth-child(2)").click()
time.sleep(2)
driver.find_element_by_css_selector("div.el-picker-panel__content:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(7) > div:nth-child(1) > span:nth-child(1)").click()
driver.find_element_by_css_selector("div.el-picker-panel__content:nth-child(2) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(6) > td:nth-child(4) > div:nth-child(1) > span:nth-child(1)").click()

#
# def login(self):

# driver = self.driver

