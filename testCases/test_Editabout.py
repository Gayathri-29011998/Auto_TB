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

class Test_Editabout:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    aboutdescription = ReadConfig.getabout()

    logger = LogGen.loggen()

    #@pytest.mark.sanity
    def test_Editaboutpositive(self, setup):
        self.logger.info("*************** Test_001_Login *************")
        self.logger.info("************** Edit About Positive *************")
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
        self.cp.clickAbouticon()
        time.sleep(5)
        self.cp.clickOpenconsult()
        time.sleep(3)
        self.cp.clickHiring()
        time.sleep(3)
        self.cp.clickRaisingfund()
        time.sleep(3)
        self.cp.clickOpeninvest()
        time.sleep(3)
        self.cp.typeAboutdesc(self.aboutdescription)
        time.sleep(3)
        self.cp.clickSaveabout()
        time.sleep(1)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = toast_msg[0].text
        if result == "Profile updated successfully.":
            self.logger.info("Error Message Is: %s", result)
            assert True
        else:
            assert False

        self.logger.info("************** Edit About Positive test passed *************")
        self.driver.quit()

    #Negative Editabout1
    #@pytest.mark.sanity
    def test_Editaboutnegative1(self, setup):
        self.logger.info("*************** Test_001_Login *************")
        self.logger.info("************** Edit About Negative *************")
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
        self.cp.clickAbouticon()
        time.sleep(5)
        self.cp.clickOpenconsult()
        time.sleep(3)
        self.cp.clickHiring()
        time.sleep(3)
        self.cp.clickRaisingfund()
        time.sleep(3)
        self.cp.clickOpeninvest()
        time.sleep(3)
        self.cp.withoutaboutdescription()
        time.sleep(3)
        self.cp.clickSaveabout()

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/main/section/div[2]/form/div[3]/p")
        result = toast_msg[0].text
        if result == "Description is required.":
            self.logger.info("Error Message Is: %s", result)
            assert True
        else:
            assert False

        self.logger.info("************** Edit About Negative 1 test passed *************")
        self.driver.quit()


    # Negative Edit about2
    #@pytest.mark.sanity
    def test_Editaboutnegative2(self, setup):
            self.logger.info("*************** Test_001_Login *************")
            self.logger.info("************** Edit About Negative 2 *************")
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
            self.cp.clickAbouticon()
            time.sleep(5)
            self.cp.clickOpenconsult()
            time.sleep(3)
            self.cp.clickHiring()
            time.sleep(3)
            self.cp.clickRaisingfund()
            time.sleep(3)
            self.cp.clickOpeninvest()
            time.sleep(3)
            self.cp.lengthaboutdescription()
            time.sleep(3)
            self.cp.clickSaveabout()
            time.sleep(2)

            toast_msg = self.driver.find_elements(By.XPATH,"/html/body/div[3]/div[3]/main/section/div[2]/form/div[3]/p")
            result = toast_msg[0].text
            if result == "Maximum 500 characters allowed.":
                self.logger.info("Error Message Is: %s", result)
                assert True
            else:
                assert False

            self.logger.info("************** Edit About Negative 2 test passed *************")
            self.driver.quit()

