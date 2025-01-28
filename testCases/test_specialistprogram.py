import time

import pytest
import self
from selenium.webdriver.common.by import By
from pageObjects.CollegeProfilePage import College
from pageObjects.Postjobs import Jobs
from pageObjects.loginpage import Login
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen
import configparser

class Test_Addcertifiedcourse:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    specialprogram = ReadConfig.getspecialprogram()

    logger = LogGen.loggen()

    #@pytest.mark.sanity
    def test_Specializedpgmpositive(self, setup):
        self.logger.info("*************** Test_001_Login *************")
        self.logger.info("************** Specialized Program positive test *************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.j = Jobs(self.driver)
        self.cp = College(self.driver)
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
        time.sleep(5)
        self.cp.clickNavbarAbout()
        time.sleep(2)
        self.cp.viewCertifiedCourse()
        time.sleep(2)
        self.cp.clickNavbarCertifiedCourse()
        time.sleep(2)
        self.cp.clickSpelialistpgmicon()
        time.sleep(3)
        self.cp.clickAddspecialistpgm()
        time.sleep(3)
        self.cp.typeSpecialistpgm(self.specialprogram)
        time.sleep(3)
        self.cp.clickSavespecialistpgm()
        time.sleep(2)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = toast_msg[0].text
        if result == "Special Course updated successfully.":
            self.logger.info("Toast Message Is: %s", result)
            assert True
            self.logger.info("*************** Added One Specialized Program Test Passed ***************")
        else:
            assert False
            self.logger.info("*************** Added One Specialized Program Test Failed ***************")

        self.logger.info("************* Specialized Program Positive Test Passed *******************")
        self.driver.quit()

    #@pytest.mark.sanity
    #Delete the Specialized Program
    def test_DeleteSpecializedpgm(self, setup):
        self.logger.info("*************** Test_001_Login *************")
        self.logger.info("************** Specialized Program Delete test *************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.j = Jobs(self.driver)
        self.cp = College(self.driver)
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
        time.sleep(5)
        self.cp.clickNavbarAbout()
        time.sleep(2)
        self.cp.viewCertifiedCourse()
        time.sleep(2)
        self.cp.clickNavbarCertifiedCourse()
        time.sleep(2)
        self.cp.clickSpelialistpgmicon()
        time.sleep(3)
        self.cp.clickDeletespecialpgm()
        time.sleep(2)
        self.cp.clickSavespecialistpgm()
        time.sleep(2)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = toast_msg[0].text
        if result == "Special Course updated successfully.":
            self.logger.info("Toast Message Is: %s", result)
            assert True
            self.logger.info("*************** Delete One Specialized Program Test Passed ***************")
        else:
            assert False
            self.logger.info("*************** Delete One Specialized Program Test Failed ***************")

        self.logger.info("************* Specialized Program Delete Test Passed *******************")
        self.driver.quit()

    #@pytest.mark.sanity
    #Specialized Program Negative Test (Without Enter Special program and click save)
    def test_Specializedpgmnegative(self, setup):
        self.logger.info("*************** Test_001_Login *************")
        self.logger.info("************** Specialized Program Negative Test *************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.j = Jobs(self.driver)
        self.cp = College(self.driver)
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
        time.sleep(5)
        self.cp.clickNavbarAbout()
        time.sleep(2)
        self.cp.viewCertifiedCourse()
        time.sleep(2)
        self.cp.clickNavbarCertifiedCourse()
        time.sleep(2)
        self.cp.clickSpelialistpgmicon()
        time.sleep(3)
        self.cp.clickAddspecialistpgm()
        time.sleep(3)
        self.cp.clickSavespecialistpgm()
        time.sleep(3)

        error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/main/section/div[2]/form/div[2]/div[1]/div/div")
        result = error_msg[0].text

        if result == "SpecialProgram required":
           self.logger.info("Toast Message Is: %s", result)
           assert True
        else:
           self.logger.info("No Toast Message is Found")
           assert False

        self.logger.info("************ Successfully Completed the Special Program Negative Test Passed **************")
        self.driver.quit()

