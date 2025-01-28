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

class Test_Trustedcompanies:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    client = ReadConfig.getclient()

    logger = LogGen.loggen()

    #@pytest.mark.sanity
    def test_Trustedcompaniespositive(self, setup):
        self.logger.info("*************** Test_Trusted Companies *************")
        self.logger.info("************** Trusted Companies Add Clients Positive Test *************")
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
        self.cp.clickNavbarPlacements()
        time.sleep(3)
        self.cp.clickTrustedcompanyicon()
        time.sleep(3)
        self.cp.typeClientname(self.client)
        time.sleep(3)
        self.cp.clickAddcompany()
        time.sleep(3)
        self.logger.info("Client 1 Added")
        self.cp.typeClientname1()
        time.sleep(7)
        self.cp.clickAddcompany()
        time.sleep(3)
        self.logger.info("Client 2 Added")
        self.cp.clickSaveclients()
        time.sleep(2)


        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = toast_msg[0].text

        if result == "Clients updated successfully.":
           self.logger.info("Toast Message Is: %s", result)
           self.logger.info("Add Clients Test Passed")
        else:
            self.logger.info("Add Clients Test Failed")


        self.logger.info("************** Trusted Companies Add Clients Positive Test Successfully Completed *****************")
        self.driver.quit()

    #@pytest.mark.sanity
    def test_Trustedcompaniesdelete(self, setup):
        self.logger.info("*************** Test_Trusted Companies *************")
        self.logger.info("************** Trusted Companies delete Clients Positive Test *************")
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
        self.cp.clickNavbarPlacements()
        time.sleep(3)
        self.cp.mouseHoverclick()
        time.sleep(2)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = toast_msg[0].text

        if result == "Client deleted successfully.":
           self.logger.info("Toast Message Is: %s", result)
           assert True
           self.logger.info("Delete Clients Test Passed")
        else:
            assert False
            self.logger.info("Delete Clients Test Failed")


        self.logger.info("************** Trusted Companies Delete Clients Positive Test Successfully Completed *****************")
        self.driver.quit()

