import time

import pytest
import self
from selenium.webdriver.common.by import By

from pageObjects.ApplyJobs import Applyjob
from pageObjects.OpencloseApplysavedJobs import Opencloseapplysave
from pageObjects.loginpage import Login
from pageObjects.Postjobs import Jobs
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen
import configparser



config = configparser.ConfigParser()
config.read('C:\\Users\\user\\PycharmProjects\\python framework\\configurations\\config.ini')


class Test_OpenCloseApplySave:

    baseURL = ReadConfig.getApplicationURL()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()
    # Project - Open,Close,applied,save
    #@pytest.mark.sanity
    def test_JobOCAS(self, setup): # Open Close Projects Test
        self.logger.info("********** Open Close Applied Saved Test Started **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.j = Jobs(self.driver)
        self.o = Opencloseapplysave(self.driver)
        self.l.clickSignin()
        time.sleep(1)
        self.driver.refresh()
        self.l.setUsername(self.useremail)
        time.sleep(1)
        self.l.setPassword(self.password)
        time.sleep(1)
        self.l.clickLogin()
        time.sleep(5)
        self.j.selectionElement()
        time.sleep(3)
        self.o.clickProfileNavbardropArrow()
        time.sleep(2)
        self.o.clickJobDownArrow()
        time.sleep(1)
        self.o.clickOpenJob()
        time.sleep(1)
        #self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_openjob.png")
        time.sleep(1)
        self.o.clickOpenJob3dots()
        time.sleep(1)
        self.o.clickOpenJobClose()
        time.sleep(1)

        error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = error_msg[0].text
        if result == "Job has been closed successfully.":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("*************** Close One Job Test Passed Successfully  *************")
        else:
           assert False
           self.logger.info("*************** Close One Job Test Failed *************")

        time.sleep(2)
        self.o.clickClosedJobButton()
        time.sleep(1)
        self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_closedjob.png")
        time.sleep(3)
        self.o.clickClosedJobRepost()
        time.sleep(3)
        self.o.scrollJobRepostButton()
        time.sleep(3)
        self.o.clickJobRepostButton()
        time.sleep(1)

        error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = error_msg1[0].text
        if result == "Job created successfully":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("*************** Repost a Job  Test Passed successfully  *************")
        else:
           assert False
           self.logger.info("*************** Repost a Job  Test Failed *************")

        time.sleep(3)
        self.o.clickProfileNavbardropArrow()
        time.sleep(2)
        self.o.clickJobDownArrow()
        time.sleep(3)
        self.o.clickAppliedJob()
        time.sleep(3)
        #self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_appliedjob.png")
        time.sleep(3)
        self.o.clickSavedJob()
        time.sleep(3)
        #self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_savedjob.png")
        
        self.logger.info("************** Open Close Applied Saved Test Ended Successfully *************")
        self.driver.quit()
