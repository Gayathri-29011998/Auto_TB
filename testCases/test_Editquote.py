import configparser
import time
# from telnetlib import EC

import pytest
import self
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.Postjobs import Jobs
from pageObjects.loginpage import Login
from utilities.readproperties import ReadConfig
import configparser
from utilities.customLogger import LogGen
from pageObjects.CollegeProfilePage import College

config = configparser.ConfigParser()
config.read('C:\\Users\\user\\PycharmProjects\\python framework\\configurations\\config.ini')


class Test_Editquote:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    quote = ReadConfig.getquote()

    logger = LogGen.loggen()

    #@pytest.mark.sanity
    def test_Editquotepositive(self, setup): # positive test
        self.logger.info("*************** Test_001_Login *************")
        self.logger.info("************** Verifying Home Page Title *************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.l = Login(self.driver)
        self.j = Jobs(self.driver)
        self.cp = College(self.driver)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        self.l.clickSignin()
        time.sleep(3)
        self.l.setUsername(self.username)
        time.sleep(3)
        self.l.setPassword(self.password)
        time.sleep(3)
        self.l.clickLogin()
        time.sleep(3)
        self.j.selectionElement()
        time.sleep(3)
        self.cp.clickProfileicon()
        time.sleep(3)
        self.cp.clickProfilename()
        time.sleep(3)
        self.cp.clickEditquote()
        time.sleep(3)
        self.cp.typeQuotes(self.quote)
        time.sleep(3)
        self.cp.clickSave()
        time.sleep(2)

        toast_msg = self.driver.find_elements(By.XPATH,"/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = toast_msg[0].text
        print(result)
        if result == "Quote updated successfully.":
            assert True
        else:
            assert False

        self.logger.info("*************** Edit Quote test passed *************")
        self.driver.close()

    #Negativetest 1
    #@pytest.mark.sanity
    def test_Editquotenegative(self, setup):  #Quote is required
        self.logger.info("*************** Test_001_Login *************")
        self.logger.info("************** Verifying Home Page Title *************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.l = Login(self.driver)
        self.j = Jobs(self.driver)
        self.cp = College(self.driver)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        self.l.clickSignin()
        time.sleep(3)
        self.l.setUsername(self.username)
        time.sleep(3)
        self.l.setPassword(self.password)
        time.sleep(3)
        self.l.clickLogin()
        time.sleep(3)
        self.j.selectionElement()
        time.sleep(3)
        self.cp.clickProfileicon()
        time.sleep(3)
        self.cp.clickProfilename()
        time.sleep(3)
        self.cp.clickEditquote()
        time.sleep(3)
        self.cp.clickSave()
        time.sleep(2)

        toast_msg = self.driver.find_elements(By.XPATH,"/html/body/div[3]/div[3]/div/div/main/section/form/p")
        result = toast_msg[0].text
        print(result)
        if result == "Quote is required.":
            assert True
        else:
            assert False

        self.logger.info("*************** Edit quote Negative1 test passed *************")
        self.driver.close()

        # Negativetest 2
    #@pytest.mark.sanity
    def test_Editquotenegative2(self, setup): #quote is too short
            self.logger.info("*************** Test_001_Login *************")
            self.logger.info("************** Verifying Home Page Title *************")
            self.driver = setup
            self.driver.get(self.baseurl)
            self.l = Login(self.driver)
            self.j = Jobs(self.driver)
            self.cp = College(self.driver)
            time.sleep(3)
            self.driver.maximize_window()
            time.sleep(3)
            self.l.clickSignin()
            time.sleep(3)
            self.l.setUsername(self.username)
            time.sleep(3)
            self.l.setPassword(self.password)
            time.sleep(3)
            self.l.clickLogin()
            time.sleep(3)
            self.j.selectionElement()
            time.sleep(3)
            self.cp.clickProfileicon()
            time.sleep(3)
            self.cp.clickProfilename()
            time.sleep(3)
            self.cp.clickEditquote()
            time.sleep(3)
            self.cp.shortQuote()
            time.sleep(5 )
            self.cp.clickSave()
            time.sleep(2)

            toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/main/section/form/p")
            result = toast_msg[0].text
            print(result)
            if result == "Quote is too short.":
                assert True
            else:
                assert False

            self.logger.info("*************** Edit quote Negative2 test passed *************")
            self.driver.close()
    # Negativetest 3
    #@pytest.mark.sanity
    def test_Editquotenegative3(self, setup): #quote is too long
            self.logger.info("*************** Test_001_Login *************")
            self.logger.info("************** Verifying Home Page Title *************")
            self.driver = setup
            self.driver.get(self.baseurl)
            self.l = Login(self.driver)
            self.j = Jobs(self.driver)
            self.cp = College(self.driver)
            time.sleep(3)
            self.driver.maximize_window()
            time.sleep(3)
            self.l.clickSignin()
            time.sleep(3)
            self.l.setUsername(self.username)
            time.sleep(3)
            self.l.setPassword(self.password)
            time.sleep(3)
            self.l.clickLogin()
            time.sleep(3)
            self.j.selectionElement()
            time.sleep(3)
            self.cp.clickProfileicon()
            time.sleep(3)
            self.cp.clickProfilename()
            time.sleep(3)
            self.cp.clickEditquote()
            time.sleep(3)
            self.cp.lengthQuote()
            time.sleep(3)
            self.cp.clickSave()
            time.sleep(2)

            toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/main/section/form/p")
            result = toast_msg[0].text
            print(result)
            if result == "Quote is too long.":
                assert True
            else:
                assert False

            self.logger.info("*************** Edit quote Negative3 test passed *************")
            self.driver.close()
