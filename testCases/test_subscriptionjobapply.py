import time

import pytest
import self
from selenium.webdriver.common.by import By

from pageObjects.ApplyJobs import Applyjob
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
    def test_subscriptionjobapply(self, setup):  # Subscription Apply Test
        self.logger.info("********** Subscription Apply Test- Positive **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.j = Jobs(self.driver)
        self.aj = Applyjob(self.driver)
        self.l.clickSignin()
        time.sleep(1)
        self.l.setUsername(self.useremail)
        time.sleep(1)
        self.l.setPassword(self.password)
        time.sleep(1)
        self.l.clickLogin()
        time.sleep(1)
        self.j.selectionElement()
        time.sleep(3)
        self.j.clickJobButton()
        time.sleep(2)
        self.aj.clickJobApplyButton()
        time.sleep(2)
        self.aj.clickOnbehalfofJobapplytoggle()
        time.sleep(2)
        self.aj.clickJobapplyPdfupload()
        time.sleep(2)
        self.aj.clickJobapplyZipfileupload()
        time.sleep(2)
        self.aj.typeDescriptionjobapply()
        time.sleep(2)
        self.aj.clickOnbehalfchooseone_JobApply()
        time.sleep(2)
        self.aj.selectOnbehalfofAccount()
        time.sleep(2)
        self.aj.clickSubmitjobapply()
        time.sleep(1)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = toast_msg[0].text
        if result == "You need subscription to apply this job.":
            self.logger.info("Toast Message Is: %s", result)
            assert True
            self.logger.info("*************** Need Subscription for Onbehalfof Job Apply test passed *************")
        else:
            assert False
            self.logger.info("*************** Need Subscription for Onbehalfof Job Apply test failed *************")

        self.logger.info(
            "************** Need Subscription for Onbehalfof Job Apply Test Passed Successfully *************")
        self.driver.quit()