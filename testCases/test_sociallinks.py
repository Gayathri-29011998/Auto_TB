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

class Test_Sociallinks:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    facebook = ReadConfig.getfacebooklink()
    twitter = ReadConfig.gettwitterlink()
    linkedin = ReadConfig.getlinkedinlink()
    instagram = ReadConfig.getinstagramlink()
    websitelink = ReadConfig.getwebsitelink()


    logger = LogGen.loggen()

    #@pytest.mark.sanity
    def test_Createsociallinkspositive(self, setup):
        self.logger.info("*************** Test_Social Links *************")
        self.logger.info("************** Create Social Links  positive Test *************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.j = Jobs(self.driver)
        self.cp = College(self.driver)
        time.sleep(3)
        self.l.clickSignin()
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
        self.cp.scrollSociallinksicon()
        time.sleep(3)
        self.cp.clickSociallinksicon()
        time.sleep(3)
        self.cp.typeFacebooklink(self.facebook)
        time.sleep(3)
        self.cp.typeTwitterlink(self.twitter)
        time.sleep(3)
        self.cp.typeLinkedinlink(self.linkedin)
        time.sleep(3)
        self.cp.typeInstagramlink(self.instagram)
        time.sleep(3)
        self.cp.typeWebsitelink(self.websitelink)
        time.sleep(3)
        #self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_Createsociallinkspositive.png")
        time.sleep(3)
        self.cp.clickSavesociallinks()
        time.sleep(2)


        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = toast_msg[0].text

        if result == "Social Media Links updated successfully.":
           self.logger.info("Toast Message Is: %s", result)
           self.logger.info("*********** Create Social Links Test Passed ***********")
           assert True

        else:
           self.logger.info("*********** Create Social Links Test Failed ***********")
           assert False

        self.logger.info("************** Successfully Create Social Links  positive Test Passed *************")
        self.driver.quit()

    #@pytest.mark.sanity
    def test_Opensociallinkspositive(self, setup):
        self.logger.info("*************** Test_Social Links *************")
        self.logger.info("************** Open Social Links  positive Test *************")
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
        self.cp.scrollSociallinksicon()
        time.sleep(10)
        self.cp.clickFBlink()
        time.sleep(10)
        self.cp.clickTwitterlink()
        time.sleep(10)
        self.cp.clickLinkedinlink()
        time.sleep(10)
        self.cp.clickInstalink()
        time.sleep(10)
        self.cp.clickWebsitelink()
        time.sleep(10)
        self.logger.info("************** Successfully Open Social Links  positive Test Passed *************")
        self.driver.quit()

    #@pytest.mark.sanity
    def test_Deletesociallinkspositive(self, setup):
        self.logger.info("*************** Test_Social Links *************")
        self.logger.info("************** Delete Social Links  positive Test *************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.j = Jobs(self.driver)
        self.cp = College(self.driver)
        time.sleep(3)
        self.l.clickSignin()
        time.sleep(2)
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
        self.cp.scrollSociallinksicon()
        time.sleep(3)
        self.cp.clickSociallinksicon()
        time.sleep(3)
        self.cp.withoutFacebooklink()
        time.sleep(3)
        self.cp.withoutTwitterlink()
        time.sleep(3)
        self.cp.withoutLinkedinlink()
        time.sleep(3)
        self.cp.withoutInstagramlink()
        time.sleep(3)
        self.cp.withoutWebsitelink()
        time.sleep(3)
        self.cp.clickSavesociallinks()
        time.sleep(2)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = toast_msg[0].text

        if result == "Social Media Links updated successfully.":
           self.logger.info("Toast Message Is: %s", result)
           self.logger.info("*********** Delete Social Links Test Passed ***********")
           assert True

        else:
           self.logger.info("*********** Delete Social Links Test Failed ***********")
           assert False

        self.logger.info("************** Successfully Delete Social Links  positive Test Passed *************")
        self.driver.quit()
