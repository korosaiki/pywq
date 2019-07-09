from DHSM import login
#
# class denglu():
    def login(self,username,password,yanzm):
        yanzm = input("请输入验证码")
        self.driver.find_element_by_xpath("//input[@id='user']").send_keys(username)
        self.driver.find_element_by_xpath("//input[@id='password']").send_keys(password)
        self.driver.find_element_by_xpath("//input[@id='yanZ']").send_keys(yanzm)
        self.driver.find_element_by_css_selector(".class='sub'").click()

    def test_loginsSuccess(self):
        # '''登录成功'''
        self.login('admin', '1','yanzm')
        tip = self.driver.find_element_by_css_selector(".title-ct > div:nth-child(2)").text
        print(tip)
        self.assertNotEqual(tip, '后台管理系统')

    def test_error(self):
        # 输入错误账号或密码
        yanzm = input("请输入验证码")
        error_user = input("请输入账号")
        error_passwd = input("请输入密码:")
        self.login(error_user,error_passwd,yanzm)
        self.driver.find_element_by_css_selector(".class='sub'").click()
        time.sleep(2)
