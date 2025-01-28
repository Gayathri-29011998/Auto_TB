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

class Test_Addmilestone:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    milestoneyear = ReadConfig.getmilestoneyear()
    milestonedescription = ReadConfig.getmilestonedescri()

    logger = LogGen.loggen()

    #@pytest.mark.sanity
    def test_Createmilestonepositive(self, setup):
        self.logger.info("*************** Test_Milestone *************")
        self.logger.info("************** Create Milestone  positive Test *************")
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
        time.sleep(3)
        self.cp.clickNavbarTrustedCompanies()
        time.sleep(3)
        self.cp.clickMilestoneIcon()
        time.sleep(2)
        self.cp.clickAddMilestone()
        time.sleep(2)
        self.cp.typeMilestoneyear(self.milestoneyear)
        time.sleep(3)
        self.cp.typeMilestonedesc(self.milestonedescription)
        time.sleep(3)
        self.cp.scrollSaveMilestone()
        time.sleep(2)
        self.cp.clickSaveMilestone()
        time.sleep(2)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = toast_msg[0].text

        if result == "Milestone updated successfully.":
            self.logger.info("Toast Message Is: %s", result)
            assert True
            self.logger.info("**************  Create Milestone Test Paseed  *************")
        else:
            assert False
            self.logger.info("************  Create Milestone Test Failed  *************")


        # time.sleep(3)
        # self.cp.clickNavbarTrustedCompanies()
        # time.sleep(3)
        # self.cp.clickMilestoneIcon()
        # time.sleep(2)
        # self.cp.scrollAddMilestone()
        # time.sleep(2)
        # self.cp.clickAddMilestone()
        # time.sleep(2)
        # self.cp.typeaddMilestoneyear()
        # time.sleep(2)
        # self.cp.typeaddMilestonedesc()
        # time.sleep(2)
        # self.cp.scrollSaveMilestone()
        # time.sleep(2)
        # self.cp.clickSaveMilestone()
        # time.sleep(2)

        self.logger.info("************* Successfully  Create Milestone Test Passed************")
        self.driver.quit()

    #@pytest.mark.sanity
    def test_Deletemilestone(self, setup):
        self.logger.info("*************** Test_Milestone *************")
        self.logger.info("************** Delete Milestone  positive Test *************")
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
        self.cp.clickNavbarTrustedCompanies()
        time.sleep(3)
        self.cp.clickMilestoneIcon()
        time.sleep(2)
        self.cp.clickDeletemilestone()
        time.sleep(2)
        self.cp.scrollSaveMilestone()
        time.sleep(3)
        self.cp.clickSaveMilestone()
        time.sleep(2)
        # self.cp.mouseHoverclickMilestone()
        # time.sleep(1)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = toast_msg[0].text

        if result == "Milestone updated successfully.":
            self.logger.info("Toast Message Is: %s", result)
            self.logger.info("*********** Delete Solutions Test Passed ***********")
            assert True

        else:
            self.logger.info("*********** Delete Solutions Test Failed ***********")
            assert False
        time.sleep(2)

        self.logger.info("************** Successfully Delete Solutions  positive Test Passed *************")
        self.driver.quit()

        self.logger.info("*************** Successfully Deleted  *************")
        self.logger.info("************** Delete Milestone  positive Test Passed  *************")

    #@pytest.mark.sanity
    def test_Milestonenegative(self, setup):
        self.logger.info("*************** Test_Milestone *************")
        self.logger.info("************** Milestone  Negative Test *************")
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
        time.sleep(3)
        self.cp.clickNavbarTrustedCompanies()
        time.sleep(3)
        self.cp.clickMilestoneIcon()
        time.sleep(3)
        self.cp.scrollAddMilestone()
        time.sleep(3)
        self.cp.clickAddMilestone()
        time.sleep(3)
        self.cp.scrollSaveMilestone()
        time.sleep(2)
        self.cp.clickSaveMilestone()
        time.sleep(3)


        error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/main/section/div[2]/form/div[2]/div/div[1]/div")
        result = error_msg[0].text

        if result == "Year is required.":
            self.logger.info("Toast Message Is: %s", result)
            assert True
            self.logger.info("**************  Milestone Year Negative Test Passed  *************")
        else:
            assert False
            self.logger.info("************  Milestone Year Negative Test Failed  *************")

        error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/main/section/div[2]/form/div[2]/div/div[2]/div")
        result = error_msg[0].text

        if result == "Description is required.":
            self.logger.info("Toast Message Is: %s", result)
            assert True
            self.logger.info("**************  Milestone Description Negative Test Passed  *************")
        else:
            assert False
            self.logger.info("************  Milestone Description Negative Test Failed  *************")

        time.sleep(2)
        self.cp.invalidAddMilestoneyear()
        time.sleep(2)

        error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/main/section/div[2]/form/div[2]/div/div[1]/div")
        result = error_msg[0].text

        if result == "Invalid Year.":
            self.logger.info("Toast Message Is: %s", result)
            assert True
            self.logger.info("**************  Milestone Year Negative Test Passed  *************")
        else:
            assert False
            self.logger.info("************  Milestone Year Negative Test Failed  *************")

        time.sleep(2)
        self.cp.lengthMilestoneContent()
        time.sleep(2)

        error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/main/section/div[2]/form/div[2]/div/div[2]/div")
        result = error_msg[0].text

        if result == "Maximum 150 characters allowed.":
            self.logger.info("Toast Message Is: %s", result)
            assert True
            self.logger.info("**************  Milestone Description Negative Test Passed  *************")
        else:
            assert False
            self.logger.info("************  Milestone Description Negative Test Failed  *************")

        time.sleep(2)
        self.cp.shortMilestoneContent()
        time.sleep(2)

        error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/main/section/div[2]/form/div[2]/div/div[2]/div")
        result = error_msg[0].text

        if result == "Description should be at least 100 characters in length.":
            self.logger.info("Toast Message Is: %s", result)
            assert True
            self.logger.info("**************  Milestone Description Negative Test Passed  *************")
        else:
            assert False
            self.logger.info("************  Milestone Description Negative Test Failed  *************")

        self.logger.info("************* Successfully Milestone Negative  Test Passed************")
        self.driver.quit()



