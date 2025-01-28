import configparser
import pytest
import time

import self
from selenium.webdriver.common.by import By

from pageObjects.AdminPage import Adminpage
from pageObjects.ApplyInvestings import ApplyInvest
from pageObjects.ApplyJobs import Applyjob
from pageObjects.HomePage import HomePage
from pageObjects.OpencloseApplysavedJobs import Opencloseapplysave
from pageObjects.Postinvestiing import Investings
from pageObjects.loginpage import Login
from pageObjects.Postjobs import Jobs
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen
import configparser

config = configparser.ConfigParser()
config.read('C:\\Users\\user\\PycharmProjects\\python framework\\configurations\\config.ini')


class Test_Jobs:

    baseURL = ReadConfig.getApplicationURL()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    #@pytest.mark.sanity
    def test_homepageJobsLock(self, setup):
        self.logger.info("********** Home Page Jobs Lock Test **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.ad = Adminpage(self.driver)
        self.hp = HomePage(self.driver)
        self.l.clickSignin()
        time.sleep(2)
        self.l.setUsername(self.useremail)
        time.sleep(3)
        self.l.setPassword(self.password)
        time.sleep(3)
        self.l.clickLogin()
        time.sleep(3)
        self.hp.clickJobsLock()
        time.sleep(1)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = toast_msg[0].text
        if result == "Default route has been updated.":
            self.logger.info("Toast Message Is: %s", result)
            assert True
            self.logger.info("*********** Jobs Lock Test Passed ***********")
        else:
            assert False
            self.logger.info("*********** Jobs Lock Test Failed ***********")

        time.sleep(2)
        self.hp.clickProfileIcon()
        time.sleep(2)
        self.hp.clickLogout()
        time.sleep(2)
        self.hp.clickLogoutYes()
        time.sleep(3)
        self.l.setUsername(self.useremail)
        time.sleep(3)
        self.l.setPassword(self.password)
        time.sleep(3)
        self.l.clickLogin()
        time.sleep(3)

        act_url = self.driver.current_url
        print(act_url)
        if act_url == "https://www.tickbig.com/jobs":
            self.logger.info("Act_url: %s", act_url)
            print("Screenshot saved.")
            assert True
            self.logger.info("*************** Home Page URL Test Passed *************")
        else:
            assert False

        time.sleep(2)
        self.hp.clickJPFIHomepageIcon()
        time.sleep(2)
        self.hp.clickJobsLock()
        time.sleep(3)
        self.logger.info("********** Home Page Jobs Lock Test Passed **********")
        self.driver.quit()

    def test_homepageProjectsLock(self, setup):
        self.logger.info("********** Home Page Projects Lock Test **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.ad = Adminpage(self.driver)
        self.hp = HomePage(self.driver)
        self.l.clickSignin()
        time.sleep(2)
        self.l.setUsername(self.useremail)
        time.sleep(3)
        self.l.setPassword(self.password)
        time.sleep(3)
        self.l.clickLogin()
        time.sleep(3)
        self.hp.clickProjectsLock()
        time.sleep(1)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = toast_msg[0].text
        if result == "Default route has been updated.":
            self.logger.info("Toast Message Is: %s", result)
            assert True
            self.logger.info("*********** Projects Lock Test Passed ***********")
        else:
            assert False
            self.logger.info("*********** Projects Lock Test Failed ***********")

        time.sleep(2)
        self.hp.clickProfileIcon()
        time.sleep(2)
        self.hp.clickLogout()
        time.sleep(2)
        self.hp.clickLogoutYes()
        time.sleep(3)
        self.l.setUsername(self.useremail)
        time.sleep(3)
        self.l.setPassword(self.password)
        time.sleep(3)
        self.l.clickLogin()
        time.sleep(3)

        act_url = self.driver.current_url
        print(act_url)
        if act_url == "https://www.tickbig.com/projects":
            self.logger.info("Act_url: %s", act_url)
            print("Screenshot saved.")
            assert True
            self.logger.info("*************** Home Page URL Test Passed *************")
        else:
            assert False

        time.sleep(2)
        self.hp.clickJPFIHomepageIcon()
        time.sleep(2)
        self.hp.clickProjectsLock()
        time.sleep(2)
        self.logger.info("********** Home Page Projects Lock Test Passed **********")
        self.driver.quit()


    def test_homepageFundingLock(self, setup):
        self.logger.info("********** Home Page Funding Lock Test **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.ad = Adminpage(self.driver)
        self.hp = HomePage(self.driver)
        self.l.clickSignin()
        time.sleep(2)
        self.l.setUsername(self.useremail)
        time.sleep(3)
        self.l.setPassword(self.password)
        time.sleep(3)
        self.l.clickLogin()
        time.sleep(3)
        self.hp.clickFundingLock()
        time.sleep(1)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = toast_msg[0].text
        if result == "Default route has been updated.":
            self.logger.info("Toast Message Is: %s", result)
            assert True
            self.logger.info("*********** Projects Lock Test Passed ***********")
        else:
            assert False
            self.logger.info("*********** Projects Lock Test Failed ***********")

        time.sleep(2)
        self.hp.clickProfileIcon()
        time.sleep(2)
        self.hp.clickLogout()
        time.sleep(2)
        self.hp.clickLogoutYes()
        time.sleep(3)
        self.l.setUsername(self.useremail)
        time.sleep(3)
        self.l.setPassword(self.password)
        time.sleep(3)
        self.l.clickLogin()
        time.sleep(3)

        act_url = self.driver.current_url
        print(act_url)
        if act_url == "https://www.tickbig.com/fundraisings":
            self.logger.info("Act_url: %s", act_url)
            print("Screenshot saved.")
            assert True
            self.logger.info("*************** Home Page URL Test Passed *************")
        else:
            assert False

        time.sleep(2)
        self.hp.clickJPFIHomepageIcon()
        time.sleep(2)
        self.hp.clickFundingLock()
        time.sleep(2)
        self.logger.info("********** Home Page Funding Lock Test Passed **********")
        self.driver.quit()

    def test_homepageInvestLock(self, setup):
        self.logger.info("********** Home Page Investing Lock Test **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.ad = Adminpage(self.driver)
        self.hp = HomePage(self.driver)
        self.l.clickSignin()
        time.sleep(2)
        self.l.setUsername(self.useremail)
        time.sleep(3)
        self.l.setPassword(self.password)
        time.sleep(3)
        self.l.clickLogin()
        time.sleep(3)
        self.hp.clickInvestingLock()
        time.sleep(1)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = toast_msg[0].text
        if result == "Default route has been updated.":
            self.logger.info("Toast Message Is: %s", result)
            assert True
            self.logger.info("*********** Projects Lock Test Passed ***********")
        else:
            assert False
            self.logger.info("*********** Projects Lock Test Failed ***********")

        time.sleep(2)
        self.hp.clickProfileIcon()
        time.sleep(2)
        self.hp.clickLogout()
        time.sleep(2)
        self.hp.clickLogoutYes()
        time.sleep(3)
        self.l.setUsername(self.useremail)
        time.sleep(3)
        self.l.setPassword(self.password)
        time.sleep(3)
        self.l.clickLogin()
        time.sleep(3)

        act_url = self.driver.current_url
        print(act_url)
        if act_url == "https://www.tickbig.com/investings":
            self.logger.info("Act_url: %s", act_url)
            print("Screenshot saved.")
            assert True
            self.logger.info("*************** Home Page URL Test Passed *************")
        else:
            assert False

        time.sleep(2)
        self.hp.clickJPFIHomepageIcon()
        time.sleep(2)
        self.hp.clickInvestingLock()
        time.sleep(2)
        self.logger.info("********** Home Page Investing Lock Test Passed **********")
        self.driver.quit()



