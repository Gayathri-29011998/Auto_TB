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
    course = ReadConfig.getcourse()


    logger = LogGen.loggen()

    #@pytest.mark.sanity
    def test_Certifiedcoursepositive(self, setup):
        self.logger.info("*************** Test_001_Login *************")
        self.logger.info("************** Add Certified course Positive *************")
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
        self.cp.clickNavbarAbout()
        time.sleep(3)
        self.cp.clickCertifiedcourseicon()
        time.sleep(3)
        self.cp.scrollAddcourse()
        time.sleep(3)
        self.cp.clickAddcourse()
        time.sleep(5)
        self.cp.typeCourse(self.course)
        time.sleep(5)
        self.cp.clickSavecourse()
        time.sleep(1)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = toast_msg[0].text
        if result == "Courses updated successfully.":
           assert True
           self.logger.info("Toast Message: %s", result)
        else:
           self.logger.info("No toast message found")
           assert False
        self.logger.info("*************** Add Certified courses positive Test Passed *************")
        self.driver.quit()

    #@pytest.mark.sanity
    #delete Test(positive)
    def test_Certifiedcoursedelete(self, setup):
        self.logger.info("*************** Test_001_Login *************")
        self.logger.info("************** Delete Certified course Positive *************")
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
        self.cp.clickNavbarAbout()
        time.sleep(3)
        self.cp.clickCertifiedcourseicon()
        time.sleep(3)
        self.cp.clickDeletecourse()
        time.sleep(2)
        self.cp.clickSavecourse()
        time.sleep(2)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = toast_msg[0].text
        if result == "Courses updated successfully.":
           self.logger.info("Toast Message Is %s", result)
           assert True
           self.logger.info("*********** Course Delete Test Passed ************")
        else:
           assert False
           self.logger.info("*********** Course Delete Test Failed ************")

        self.logger.info("*************** Delete Certified Courses Positive Test Passed *************")
        self.driver.quit()

    # #Negative Test - Without enter the course name
    #@pytest.mark.sanity
    def test_Certifiedcoursenegative1(self, setup):
        self.logger.info("*************** Test_001_Login *************")
        self.logger.info("************** Add Certified course Negative 1 Test *************")
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
        self.cp.clickNavbarAbout()
        time.sleep(3)
        self.cp.clickCertifiedcourseicon()
        time.sleep(3)
        self.cp.scrollAddcourse()
        time.sleep(3)
        self.cp.clickAddcourse()
        time.sleep(5)
        self.cp.clickSavecourse()
        time.sleep(2)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/main/section/div[2]/form/div/div[1]/div/div")
        result = toast_msg[0].text
        if result == "Course required":
           self.logger.info("Toast Message Is %s", result)
           self.logger.info("*********** Course Required Test Passed ************")
           assert True
        else:
           assert False
           self.logger.info("*********** Course Required Test Failed ************")

        self.logger.info("*************** Add Certified courses negative  Test Passed *************")
        self.driver.quit()


    #Edit Course
    #@pytest.mark.sanity
    def test_edit_existdelete(self,setup):
        self.logger.info("*************** Test_001_Login *************")
        self.logger.info("************** Edit Exist Course *************")
        self.logger.info("************** Exist Course Delete *************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.driver.refresh()
        self.l = Login(self.driver)
        self. j = Jobs(self.driver)
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
        time.sleep(3)
        self.cp.clickCertifiedcourseicon()
        time.sleep(3)
        self.cp.editCourse()
        time.sleep(3)
        # self.cp.existCoursedelete()
        # time.sleep(3)
        self.cp.clickSavecourse()
        time.sleep(3)


        self.logger.info("************ Edit Exist Course Test Passed **************")
        self.logger.info("************ Exist Course Delete Test Passed **************")
        self.driver.close()


