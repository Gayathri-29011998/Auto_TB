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

class Test_Addplacements:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    percentage = ReadConfig.getpercentage()
    totalpersonplaced = ReadConfig.gettotalpersonplaced()
    editpercentage = ReadConfig.geteditpercentage()
    edittotalpersonplaced = ReadConfig.getedittotalpersonplaced()

    logger = LogGen.loggen()

    #@pytest.mark.sanity
    def test_Addplacementspositive(self, setup):
        self.logger.info("*************** test_placements *************")
        self.logger.info("************** Add Placements  positive Test *************")
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
        self.cp.clickNavbarCertifiedCourse()
        time.sleep(3)
        self.cp.clickAddplacements()
        time.sleep(3)
        self.cp.editPercentage(self.percentage)
        time.sleep(3)
        self.cp.editTotalpersonplaced(self.totalpersonplaced)
        time.sleep(3)
        self.cp.clickSaveplacements()
        time.sleep(2)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = toast_msg[0].text

        if result == "Placement details updated successfully.":
           self.logger.info("Toast Message Is: %s", result)
        else:
            self.logger.info("Add placements Test Failed")

        self.logger.info("************* Successfully Add Placements Positive Test Passed************")
        self.driver.quit()

    #@pytest.mark.sanity
    def test_Editplacementspositive(self, setup):
        self.logger.info("*************** test_placements *************")
        self.logger.info("************** Edit Placements  positive Test *************")
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
        self.cp.clickNavbarCertifiedCourse()
        time.sleep(3)
        self.cp.clickAddplacements()
        time.sleep(3)
        self.cp.editPercentage(self.editpercentage)
        time.sleep(3)
        self.cp.editTotalpersonplaced(self.edittotalpersonplaced)
        time.sleep(3)
        self.cp.clickSaveplacements()
        time.sleep(2)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = toast_msg[0].text

        if result == "Placement details updated successfully.":
            self.logger.info("Toast Message Is: %s", result)
        else:
            self.logger.info("Edit placements Test Failed")
        self.logger.info("************* Successfully Edit Placements Positive Test Passed ************")
        self.driver.quit()



    #@pytest.mark.sanity
    def test_Negativeplacementstest1(self, setup):
        self.logger.info("*************** test_placements *************")
        self.logger.info("************** Placements  Negative Test *************")
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
        self.cp.clickNavbarCertifiedCourse()
        time.sleep(3)
        self.cp.clickAddplacements()
        time.sleep(3)
        self.cp.withoutPercentage()
        time.sleep(2)
        self.cp.withoutTotalpersonplaced()
        time.sleep(2)
        self.cp.clickSaveplacements()
        time.sleep(2)

        toast_msg=self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/main/section/div[2]/form/div[1]/div[1]/p")
        result=toast_msg[0].text

        if result=="Average Placement Rate is required.":
           self.logger.info("Toast Message Is: %s", result)

        else:
            self.logger.info("Percentage Field Negative Test Passed")

        time.sleep(2)

        toast_msg=self.driver.find_elements(By.XPATH,"/html/body/div[3]/div[3]/div/div/main/section/div[2]/form/div[1]/div[2]/p")
        result=toast_msg[0].text

        if result=="Total Persons Placed is required.":
           self.logger.info("Toast Message Is: %s", result)

        else:
            self.logger.info("Total Person Placed Negative Test Failed")

        self.logger.info("************* Successfully  Placements Negative Test Passed ************")
        self.driver.quit()
    #@pytest.mark.sanity
    def test_Negativeplacementstest2(self, setup):  #Invalid Value into th input fields
        self.logger.info("*************** test_placements *************")
        self.logger.info("************** Placements  Negative Test 2  *************")
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
        self.cp.clickNavbarCertifiedCourse()
        time.sleep(3)
        self.cp.clickAddplacements()
        time.sleep(3)
        self.cp.invalidPercentage()
        time.sleep(3)
        self.cp.invalidTotalPersonPlaced()
        time.sleep(3)
        self.cp.clickSaveplacements()
        time.sleep(5)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/main/section/div[2]/form/div[1]/div[1]/p")
        result = toast_msg[0].text

        if result == "Invalid average placement value.":
            self.logger.info("Toast Message Is: %s", result)
            self.logger.info("Percentage Field invalid input negative Test Passed")
        else:
            self.logger.info("Percentage Field invalid input negative Test Passed")

        time.sleep(2)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/main/section/div[2]/form/div[1]/div[2]/p")
        result = toast_msg[0].text

        if result == "Invalid No of placements count.":
            self.logger.info("Toast Message Is: %s", result)
            self.logger.info("Total Person Placed field invalid input Negative Test Passed")

        else:
            self.logger.info("Total Person Placed field invalid input Negative Test Failed")

        self.logger.info("************* Successfully  Placements Negative Test 2 Passed ************")
        self.driver.quit()