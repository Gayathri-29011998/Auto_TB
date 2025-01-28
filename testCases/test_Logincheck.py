import configparser
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.Postjobs import Jobs
from pageObjects.loginpage import Login
from utilities.readproperties import ReadConfig
import configparser
from utilities.customLogger import LogGen

config = configparser.ConfigParser()
config.read('C:\\Users\\user\\PycharmProjects\\python framework\\configurations\\config.ini')


class Test_001_Login:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    invalidusername = ReadConfig.getinvalidusername()
    invalidpassword = ReadConfig.getinvalidpassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_login(self, setup):
        self.logger.info("*************** Test_001_Login *************")
        self.logger.info("************** Verifying Home Page Title *************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.l = Login(self.driver)
        self.j = Jobs(self.driver)
        time.sleep(5)
        self.driver.maximize_window()
        self.l.clickSignin()
        time.sleep(3)
        self.driver.refresh()
        self.l.setUsername(self.username)
        time.sleep(3)
        self.l.setPassword(self.password)
        time.sleep(3)
        self.l.clickLogin()
        time.sleep(2)
        # self.j.selectionElement()
        # time.sleep(10)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = toast_msg[0].text
        if result == "Logged In successfully.":
            assert True
            self.logger.info("*************** Login Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Login Test failed *************")

        # act_url = self.driver.current_url
        # print(act_url)
        # if act_url == "https://www.tickbig.com/home":
        #     self.logger.info("Act_url: %s", act_url)
        #     self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_login.png")
        #     print("Screenshot saved.")
        #     assert True
        #     self.logger.info("*************** Home Page URL Test Passed *************")
        # else:
        #     assert False

        time.sleep(3)
        self.l.clickProfiledropdown()
        time.sleep(3)
        #self.l.scrollLogout()
        #time.sleep(3)
        self.l.clickLogout()
        time.sleep(3)
        self.l.clickLogoutYes()
        time.sleep(2)

        act_url = self.driver.current_url
        print(act_url)
        self.logger.info("Act_URL Is: %s", act_url)

        self.logger.info("*************** Sign In URL Test Failed *************")
        self.driver.quit()

    @pytest.mark.sanity
    def test_loginnegative1(self, setup):
        self.logger.info("*************** Test_001_Login *************")
        self.logger.info("************** Verifying Iuput fields *************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.l = Login(self.driver)
        time.sleep(5)
        self.driver.maximize_window()
        self.l.clickSignin()
        time.sleep(3)
        self.driver.refresh()
        self.l.clickLogin()
        time.sleep(2)

        toast_msg = self.driver.find_elements(By.XPATH,"/html/body/div[1]/div[2]/section/main/div/div/section[2]/section/form/div[1]/p")
        result = toast_msg[0].text
        if result == "Email is required":
            self.logger.info("Error Message Is: %s", result)
            self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_login1.png")
            print("Screenshot saved.")
            assert True
            self.logger.info("*************** Username field negative test passed *************")
        else:
            assert False
            self.logger.info("*************** Username field negative test failed *************")

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section/form/div[2]/p")
        result = toast_msg[0].text
        if result == "Password is required":
            self.logger.info("Error Message Is: %s", result)
            # self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_login2.png")
            # print("Screenshot saved.")
            assert True
            self.logger.info("*************** Password field negative test passed *************")
        else:
            assert False

        self.logger.info("*************** Password field negative test failed *************")
        self.driver.quit()

    @pytest.mark.sanity
    def test_loginnegative2(self, setup):
        self.logger.info("*************** Test_001_Login *************")
        self.logger.info("************** Verifying Iuput fields *************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.l = Login(self.driver)
        time.sleep(5)
        self.driver.maximize_window()
        self.l.clickSignin()
        time.sleep(3)
        self.driver.refresh()
        self.l.invalidUsername(self.invalidusername)
        time.sleep(5)
        self.l.invalidPassword(self.invalidpassword)
        time.sleep(5)
        self.l.clickLogin()
        time.sleep(1)

        error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = error_msg[0].text
        if result == "Please provide valid email":
            self.logger.info("Toast Message Is: %s", result)
            #self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_login3.png")
            #print("Screenshot saved.")
            assert True
            self.logger.info("*************** Invalid Inputs Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Invalid Inputs Test Failed *************")

        time.sleep(2)
        self.l.setUsername(self.username)
        time.sleep(3)
        self.l.invalidPassword(self.invalidpassword)
        time.sleep(2)
        self.l.clickLogin()
        time.sleep(1)

        error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = error_msg[0].text
        if result == "Email Id or password is incorrect":
            self.logger.info("Toast Message Is: %s", result)
            # self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_login3.png")
            # print("Screenshot saved.")
            assert True
            self.logger.info("*************** Invalid Inputs Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Invalid Inputs Test Failed *************")

        self.driver.quit()