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

    # #@pytest.mark.sanity
    # def test_applyjobpositive(self,setup):  #Positive Test for Job Apply
    #     self.logger.info("********** Apply Jobs Test - Positive **********")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.driver.maximize_window()
    #     self.l = Login(self.driver)
    #     self.j = Jobs(self.driver)
    #     self.aj = Applyjob(self.driver)
    #     self.l.clickSignin()
    #     time.sleep(2)
    #     self.driver.refresh()
    #     self.l.setUsername(self.useremail)
    #     time.sleep(2)
    #     self.l.setPassword(self.password)
    #     time.sleep(2)
    #     self.l.clickLogin()
    #     time.sleep(2)
    #     # self.j.selectionElement()
    #     # time.sleep(3)
    #     self.j.clickJobButton()
    #     time.sleep(3)
    #     self.aj.clickJobApplyButton()
    #     time.sleep(3)
    #     self.aj.clickOnbehalfofJobapplytoggle()
    #     time.sleep(3)
    #     self.aj.clickJobapplyPdfupload()
    #     time.sleep(1)
    #
    #     toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
    #     result = toast_msg[0].text
    #     if result == "Successfully Uploaded":
    #         self.logger.info("Toast Message Is: %s", result)
    #         assert True
    #         self.logger.info("*********** PDF Upload Test Passed ***********")
    #     else:
    #         assert False
    #
    #     time.sleep(3)
    #     self.aj.clickJobapplyZipfileupload()
    #     time.sleep(1)
    #
    #     toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
    #     result = toast_msg[0].text
    #     if result == "Successfully Uploaded":
    #         self.logger.info("Toast Message Is: %s", result)
    #         assert True
    #         self.logger.info("*********** PDF Upload Test Passed ***********")
    #     else:
    #         assert False
    #
    #     time.sleep(3)
    #     self.aj.typeDescriptionjobapply()
    #     time.sleep(5)
    #     self.aj.clickOnbehalfchooseone_JobApply()
    #     time.sleep(3)
    #     self.aj.selectOnbehalfofAccount()
    #     time.sleep(3)
    #     self.aj.clickSubmitjobapply()
    #     time.sleep(1)
    #
    #     toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
    #     result = toast_msg[0].text
    #     if result == "Applied to a Job successfully":
    #        self.logger.info("Toast Message Is: %s", result)
    #        assert True
    #        self.logger.info("*************** Onbehalfof Job Apply test passed *************")
    #     else:
    #        assert False
    #        self.logger.info("*************** Onbehalfof Job Apply test failed *************")
    #
    #     time.sleep(2)
    #     self.driver.refresh()
    #     time.sleep(5)
    #     self.aj.clickJobApplyButton()
    #     time.sleep(2)
    #     self.aj.clickNextJobApplyButton()
    #     time.sleep(1)
    #
    #     toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
    #     result = toast_msg[0].text
    #     if result == "Job applied successfully":
    #         self.logger.info("Toast Message Is: %s", result)
    #         assert True
    #         self.logger.info("*************** Job Apply test passed *************")
    #     else:
    #         assert False
    #         self.logger.info("*************** Job Apply test failed *************")
    #
    #     self.logger.info("************** Apply Job Test Passed Successfully *************")
    #     self.driver.quit()
    #@pytest.mark.sanity
    # def test_applyjobnegative(self, setup): # Apply Job Negative Test
    #     self.logger.info("********** Apply Jobs Test - Positive **********")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.driver.maximize_window()
    #     self.l = Login(self.driver)
    #     self.j = Jobs(self.driver)
    #     self.aj = Applyjob(self.driver)
    #     self.l.clickSignin()
    #     time.sleep(3)
    #     self.driver.refresh()
    #     self.l.setUsername(self.useremail)
    #     time.sleep(2)
    #     self.l.setPassword(self.password)
    #     time.sleep(2)
    #     self.l.clickLogin()
    #     time.sleep(2)
    #     # self.j.selectionElement()
    #     # time.sleep(3)
    #     self.j.clickJobButton()
    #     time.sleep(3)
    #     self.aj.clickJobApplyButton()
    #     time.sleep(3)
    #     self.aj.clickOnbehalfofJobapplytoggle()
    #     time.sleep(2)
    #     self.aj.clickSubmitjobapply()
    #     time.sleep(1)
    #
    #     error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
    #     result = error_msg[0].text
    #     if result == "Resume Zip file is required.":
    #        self.logger.info("Error Message Is: %s", result)
    #        assert True
    #        self.logger.info("*************** Resume Zip file Negative Test Passed *************")
    #     else:
    #        assert False
    #        self.logger.info("*************** Resume Zip file Negative Test Failed *************")
    #
    #     time.sleep(2)
    #     self.aj.clickJobapplyZipfileupload()
    #     time.sleep(3)
    #     self.aj.clickSubmitjobapply()
    #     time.sleep(1)
    #
    #     error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
    #     result = error_msg[0].text
    #     if result == "Profile Tracker is required.":
    #        self.logger.info("Error Message Is: %s", result)
    #        assert True
    #        self.logger.info("*************** Profile Tracker Negative Test Passed *************")
    #     else:
    #        assert False
    #        self.logger.info("*************** Profile Tracker Negative Test Failed *************")
    #
    #     time.sleep(2)
    #     self.aj.clickJobapplyPdfupload()
    #     time.sleep(3)
    #     self.aj.clickSubmitjobapply()
    #     time.sleep(1)
    #
    #     error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
    #     result = error_msg[0].text
    #     if result == "Please enter description":
    #        self.logger.info("Error Message Is: %s", result)
    #        assert True
    #        self.logger.info("*************** Description Negative Test Passed *************")
    #     else:
    #        assert False
    #        self.logger.info("*************** Description Negative Test Failed *************")
    #
    #     time.sleep(2)
    #     self.aj.typeDescriptionjobapply()
    #     time.sleep(3)
    #     self.aj.clickSubmitjobapply()
    #     time.sleep(1)
    #
    #     error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
    #     result = error_msg[0].text
    #     if result == "Please select OnBehalf of account.":
    #        self.logger.info("Error Message Is: %s", result)
    #        assert True
    #        self.logger.info("*************** Please select OnBehalf of account Negative Test Passed *************")
    #     else:
    #        assert False
    #        self.logger.info("*************** Please select OnBehalf of account Negative Test Failed *************")
    #
    #     self.logger.info("************** Apply Job Negative  Test Passed Successfully *************")
    #     self.driver.quit()

    #@pytest.mark.sanity
    # def test_savejob(self, setup): # Save Job & UnSave Job Positive
    #     self.logger.info("********** Apply Job Test - Negative **********")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.driver.maximize_window()
    #     self.l = Login(self.driver)
    #     self.j = Jobs(self.driver)
    #     self.aj = Applyjob(self.driver)
    #     self.l.clickSignin()
    #     time.sleep(1)
    #     self.driver.refresh()
    #     self.l.setUsername(self.useremail)
    #     time.sleep(1)
    #     self.l.setPassword(self.password)
    #     time.sleep(1)
    #     self.l.clickLogin()
    #     time.sleep(1)
    #     # self.j.selectionElement()
    #     # time.sleep(3)
    #     self.j.clickJobButton()
    #     time.sleep(3)
    #     self.aj.clickJobSave()
    #     time.sleep(1)
    #
    #     toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
    #     result = toast_msg[0].text
    #     if result == "Job saved successfully":
    #         self.logger.info("Toast Message Is: %s", result)
    #         assert True
    #         self.logger.info("*************** Job Save test passed *************")
    #     else:
    #         assert False
    #         self.logger.info("*************** Job Save test failed *************")
    #
    #
    #     time.sleep(3)
    #     self.aj.clickJobSave()
    #     time.sleep(1)
    #
    #     toast_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
    #     result = toast_msg1[0].text
    #     if result == "Job unsaved successfully":
    #         self.logger.info("Toast Message Is: %s", result)
    #         assert True
    #         self.logger.info("*************** Job Apply test passed *************")
    #     else:
    #         assert False
    #         self.logger.info("*************** Job Apply test failed *************")
    #
    #     self.logger.info("************* Save Job & UnSave Jobs Test Successfully Passed *************")
    #     self.driver.quit()
    #
    # #@pytest.mark.sanity
    # def test_copylinkjob(self, setup):  # Job Copy Link Positive
    #     self.logger.info("********** Save Jobs & UnSave Jobs Test - Positive **********")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.driver.maximize_window()
    #     self.l = Login(self.driver)
    #     self.j = Jobs(self.driver)
    #     self.aj = Applyjob(self.driver)
    #     self.l.clickSignin()
    #     time.sleep(1)
    #     self.driver.refresh()
    #     self.l.setUsername(self.useremail)
    #     time.sleep(1)
    #     self.l.setPassword(self.password)
    #     time.sleep(1)
    #     self.l.clickLogin()
    #     time.sleep(1)
    #     # self.j.selectionElement()
    #     # time.sleep(3)
    #     self.j.clickJobButton()
    #     time.sleep(3)
    #     self.aj.clickJobThreedots()
    #     time.sleep(2)
    #     self.aj.clickJobCopylink()
    #     time.sleep(1)
    #
    #     toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
    #     result = toast_msg[0].text
    #     if result == "Link copied":
    #         self.logger.info("Error Message Is: %s", result)
    #         assert True
    #         self.logger.info("*************** Link copied Test Passed *************")
    #     else:
    #         assert False
    #         self.logger.info("*************** Link copied Test Failed *************")
    #
    #     self.logger.info("************* Copy Link Test Successfully Passed *************")
    #     self.driver.quit()
    #
    # #@pytest.mark.sanity
    # def test_reviewjob(self, setup):  # Job Review Positive & Negative
    #     self.logger.info("********** Review Job Test - Positive & Negative  **********")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.driver.maximize_window()
    #     self.l = Login(self.driver)
    #     self.j = Jobs(self.driver)
    #     self.aj = Applyjob(self.driver)
    #     self.l.clickSignin()
    #     time.sleep(1)
    #     self.driver.refresh()
    #     self.l.setUsername(self.useremail)
    #     time.sleep(1)
    #     self.l.setPassword(self.password)
    #     time.sleep(1)
    #     self.l.clickLogin()
    #     time.sleep(1)
    #     # self.j.selectionElement()
    #     # time.sleep(3)
    #     self.j.clickJobButton()
    #     time.sleep(3)
    #     self.aj.clickJobThreedots()
    #     time.sleep(2)
    #     self.aj.clickJobReview()
    #     time.sleep(3)
    #     self.aj.clickJobReviewSubmit()
    #     time.sleep(1)
    #
    #     error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
    #     result = error_msg[0].text
    #     if result == "Rating is required":
    #         self.logger.info("Error Message Is: %s", result)
    #         assert True
    #         self.logger.info("*************** Job Rating Negative Test Passed *************")
    #     else:
    #         assert False
    #         self.logger.info("*************** Job Rating Negative Test Failed *************")
    #
    #     time.sleep(2)
    #     self.aj.clickJobRating()
    #     time.sleep(2)
    #     self.aj.clickJobReviewSubmit()
    #     time.sleep(1)
    #
    #     error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
    #     result = error_msg1[0].text
    #     if result == "Review comment is required.":
    #         self.logger.info("Error Message Is: %s", result)
    #         assert True
    #         self.logger.info("*************** Job Review Negative Test Passed *************")
    #     else:
    #         assert False
    #         self.logger.info("*************** Job Review Negative Test Failed *************")
    #
    #     time.sleep(2)
    #     self.aj.clickJobReviewtxt()
    #     time.sleep(3)
    #     self.aj.clickJobReviewSubmit()
    #     time.sleep(2)
    #
    #     toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
    #     result = toast_msg[0].text
    #     if result == "Review added.":
    #         self.logger.info("Toast Message Is: %s", result)
    #         assert True
    #         self.logger.info("*************** Review Job Test Passed *************")
    #     else:
    #         assert False
    #         self.logger.info("*************** Review Job  Test Failed *************")
    #
    #     self.logger.info("************* Job Review Positive & Negative Test Successfully Passed *************")
    #     self.driver.quit()
    #
    # #@pytest.mark.sanity
    # def testreportjob(self, setup): # Report Job Positive & Negative
    #     self.logger.info("********** Report Job Test - Positive **********")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.driver.maximize_window()
    #     self.l = Login(self.driver)
    #     self.j = Jobs(self.driver)
    #     self.aj = Applyjob(self.driver)
    #     self.l.clickSignin()
    #     time.sleep(1)
    #     self.driver.refresh()
    #     self.l.setUsername(self.useremail)
    #     time.sleep(1)
    #     self.l.setPassword(self.password)
    #     time.sleep(1)
    #     self.l.clickLogin()
    #     time.sleep(1)
    #     # self.j.selectionElement()
    #     # time.sleep(3)
    #     self.j.clickJobButton()
    #     time.sleep(3)
    #     self.aj.clickJobThreedots()
    #     time.sleep(2)
    #     self.aj.clickJobReport()
    #     time.sleep(3)
    #     self.aj.clickJobReportSubmit()
    #     time.sleep(1)
    #
    #     error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
    #     result = error_msg[0].text
    #     if result == "Please type your comment.":
    #        self.logger.info("Error Message Is: %s", result)
    #        assert True
    #        self.logger.info("*************** Job Report Negative Test Passed *************")
    #     else:
    #        assert False
    #        self.logger.info("*************** Job Report Negative Test Failed *************")
    #
    #     time.sleep(2)
    #     self.aj.typeJobReportTxt()
    #     time.sleep(3)
    #     self.aj.clickJobReportSubmit()
    #     time.sleep(1)
    #
    #     toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
    #     result = toast_msg[0].text
    #     if result == "Job has been Reported":
    #        self.logger.info("Toast Message Is: %s", result)
    #        assert True
    #        self.logger.info("*************** Job Report Positive Test Passed *************")
    #     else:
    #        assert False
    #        self.logger.info("*************** Job Report Positive Test Failed *************")
    #
    #     self.logger.info("************* Job Report Positive & Negative Test Successfully Passed *************")
    #     self.driver.quit()
    #
    # #@pytest.mark.sanity
    # def test_notinterestjob(self, setup): # Not Intesrest The Job Positive
    #     self.logger.info("********** Not Interest Job Test - Positive **********")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.driver.maximize_window()
    #     self.l = Login(self.driver)
    #     self.j = Jobs(self.driver)
    #     self.aj = Applyjob(self.driver)
    #     self.l.clickSignin()
    #     time.sleep(1)
    #     self.driver.refresh()
    #     self.l.setUsername(self.useremail)
    #     time.sleep(1)
    #     self.l.setPassword(self.password)
    #     time.sleep(1)
    #     self.l.clickLogin()
    #     time.sleep(1)
    #     # self.j.selectionElement()
    #     # time.sleep(3)
    #     self.j.clickJobButton()
    #     time.sleep(3)
    #     self.aj.clickJobThreedots()
    #     time.sleep(2)
    #     self.aj.clickJobNotInterest()
    #     time.sleep(2)
    #     self.aj.clickjobNotInterestYesButton()
    #     time.sleep(1)
    #
    #     error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
    #     result = error_msg[0].text
    #     if result == "Not Interested successfully.":
    #        self.logger.info("Error Message Is: %s", result)
    #        assert True
    #        self.logger.info("*************** Job Not Interested Test Passed *************")
    #     else:
    #        assert False
    #        self.logger.info("*************** Job Not Interested Test Failed *************")
    #
    #     self.logger.info("************* Job Not Interest Test Successfully Passed *************")
    #     self.driver.quit()





