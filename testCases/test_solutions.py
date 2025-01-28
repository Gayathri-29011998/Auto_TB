import time
from telnetlib import EC

import pytest
import self
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.BrandProfilePage import Brands
from pageObjects.CollegeProfilePage import College
from pageObjects.Postjobs import Jobs
from pageObjects.loginpage import Login
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen
import configparser

class Test_Addsolutions:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    solutiontitle = ReadConfig.getsolutiontitle()
    solutioncontent = ReadConfig.getsolutioncontent()

    logger = LogGen.loggen()

    #@pytest.mark.sanity
    def test_Createsolutionspositive(self, setup):
        self.logger.info("*************** Test_Services *************")
        self.logger.info("************** Create Solutions positive Test *************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.br = Brands(self.driver)
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
        self.br.clickProfileicon()
        time.sleep(3)
        self.br.clickProfilename()
        time.sleep(3)
        self.br.clickNavbarServices()
        time.sleep(2)
        self.br.clickSolutionsIcon()
        time.sleep(3)
        self.br.clickAddSolution()
        time.sleep(3)
        self.br.typeSolutiontitle(self.solutiontitle)
        time.sleep(3)
        self.br.typeSolutioncontent(self.solutioncontent)
        time.sleep(3)
        self.br.scrollSaveSolution()
        time.sleep(3)
        self.br.clickSaveSolution()
        time.sleep(2)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = toast_msg[0].text

        if result == "Solutions updated successfully.":
            self.logger.info("Toast Message Is: %s", result)
            assert True
            self.logger.info("*********** Create Solutions Test Passed ***********")
        else:
            assert False
            self.logger.info("*********** Create Solutions Test Failed ***********")

        time.sleep(2)
        self.br.clickSolutionsIcon()
        time.sleep(2)
        self.br.scrollAddSolution()
        time.sleep(2)
        self.br.clickAddSolution()
        time.sleep(2)
        self.br.typeAddedtitleSolution()
        time.sleep(2)
        self.br.typeAddedcontentSolution()
        time.sleep(2)
        self.br.scrollSaveSolution()
        time.sleep(3)
        self.br.clickSaveSolution()
        time.sleep(2)


        self.logger.info("************** Successfully Create Solutions  positive Test Passed *************")
        self.driver.quit()

    #@pytest.mark.sanity
    def test_DeleteServices(self, setup):
        self.logger.info("*************** Test_Services *************")
        self.logger.info("************** Delete Solutions  positive Test *************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.br = Brands(self.driver)
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
        self.br.clickProfileicon()
        time.sleep(3)
        self.br.clickProfilename()
        time.sleep(3)
        self.br.clickNavbarServices()
        time.sleep(2)
        self.br.clickSolutionsIcon()
        time.sleep(2)
        self.br.clickDeleteSolution()
        time.sleep(2)
        self.br.scrollSaveSolution()
        time.sleep(3)
        self.br.clickSaveSolution()
        time.sleep(3)
        self.br.mouseHoverclickSolution()
        time.sleep(1)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = toast_msg[0].text

        if result == "Client deleted successfully.":
            self.logger.info("Toast Message Is: %s", result)
            self.logger.info("*********** Delete Solutions Test Passed ***********")
            assert True

        else:
            self.logger.info("*********** Delete Solutions Test Failed ***********")
            assert False
        time.sleep(2)

        self.logger.info("************** Successfully Delete Solutions  positive Test Passed *************")
        self.driver.quit()

    #@pytest.mark.sanity
    def test_AddSolutionsnegative(self, setup):
        self.logger.info("*************** Test_Services *************")
        self.logger.info("************** Add Solutions  Negative Test *************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.j = Jobs(self.driver)
        self.br = Brands(self.driver)
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
        self.br.clickProfileicon()
        time.sleep(3)
        self.br.clickProfilename()
        time.sleep(3)
        self.br.clickNavbarServices()
        time.sleep(2)
        self.br.clickSolutionsIcon()
        time.sleep(3)
        self.br.scrollAddSolution()
        time.sleep(3)
        self.br.clickAddSolution()
        time.sleep(3)
        self.br.scrollSaveSolution()
        time.sleep(2)
        self.br.clickSaveSolution()
        time.sleep(3)


        error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/main/section/div[2]/form/div[2]/div/div[1]/div")
        result = error_msg1[0].text
        if result == "solutionTitle is required":
           self.logger.info("Toast Message 1: %s", result)
           assert True
           self.logger.info("********* Solution Title test passed ************")
        else:
           assert False
           self.logger.info("********* Solution Title test passed ************")

        error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/main/section/div[2]/form/div[2]/div/div[2]/div")
        result = error_msg2[0].text
        if result == "solutionContent is required.":
            self.logger.info("Toast Message 2: %s", result)
            assert True
            self.logger.info("********* Solution Content test passed ************")
        else:
            assert False
            self.logger.info("********* Solution Content test passed ************")

        time.sleep(3)
        self.br.lengthServiceContent()
        time.sleep(2)

        error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/main/section/div[2]/form/div[2]/div/div[2]/div")
        result = error_msg[0].text

        if result == "Maximum 150 characters allowed.":
            self.logger.info("Toast Message 2: %s", result)
            assert True
            self.logger.info("********* Solution Content Negative test passed ************")
        else:
            assert False
            self.logger.info("********* Solution Content Negative test passed ************")

        time.sleep(2)
        self.br.shortServiceContent()
        time.sleep(2)

        error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/main/section/div[2]/form/div[2]/div/div[2]/div")
        result = error_msg[0].text

        if result == "solutionContent should be at least 100 characters in length.":
            self.logger.info("Toast Message 2: %s", result)
            assert True
            self.logger.info("********* Solution Content Negative test passed ************")
        else:
            assert False
            self.logger.info("********* Solution Content Negative test passed ************")

        time.sleep(2)
        self.br.invalidServiceTitle()
        time.sleep(2)

        error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/main/section/div[2]/form/div[2]/div/div[1]/div")
        result = error_msg[0].text

        if result == "Invalid Solution Title.":
            self.logger.info("Toast Message 2: %s", result)
            assert True
            self.logger.info("********* Solution Content Negative test passed ************")
        else:
            assert False
            self.logger.info("********* Solution Content Negative test passed ************")


        self.logger.info("*********** Solutions Get the Error Message *************")
        self.logger.info("*********** Solutions Input Fields Negative Test Passed *************")
        self.driver.quit()