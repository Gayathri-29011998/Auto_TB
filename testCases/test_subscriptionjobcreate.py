import configparser
import pytest
import time

import self
from selenium.webdriver.common.by import By

from pageObjects.Postinvestiing import Investings
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
    designation = ReadConfig.getdesignation()
    experiencemin = ReadConfig.getexperiencemin()
    experiencemax = ReadConfig.getexperiencemax()
    location = ReadConfig.getlocation()
    salarymin = ReadConfig.getsalarymin()
    salarymax = ReadConfig.getsalarymax()
    jobdescription = ReadConfig.getjobdescription()
    jobresponsiblities = ReadConfig.getjobresponsiblities()
    skill = ReadConfig.getskill()

    logger = LogGen.loggen()

    #@pytest.mark.sanity
    def test_jobsubscription(self, setup):  # Subscription For Job Create
        self.logger.info("********** Subscription For Job Create Test - Positive **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.j = Jobs(self.driver)
        self.i = Investings(self.driver)
        self.l.clickSignin()
        time.sleep(3)
        self.l.setUsername(self.useremail)
        time.sleep(1)
        self.l.setPassword(self.password)
        time.sleep(1)
        self.l.clickLogin()
        time.sleep(3)
        self.j.selectionElement()
        time.sleep(3)
        self.j.clickJobButton()
        time.sleep(2)
        self.j.clickPostJobButton()
        time.sleep(3)
        self.j.typeDesignation(self.designation)
        time.sleep(3)
        self.j.typeExperienceMin(self.experiencemin)
        time.sleep(3)
        self.j.typeExperienceMax(self.experiencemax)
        time.sleep(3)
        self.j.clickJoiningSelect()
        time.sleep(2)
        self.j.clickJoiningType1()
        time.sleep(2)
        self.j.clickEmploymentSelect()
        time.sleep(2)
        self.j.clickEmploymentType1()
        time.sleep(2)
        self.j.typeLocation(self.location)
        time.sleep(3)
        self.j.scrollLocation()
        time.sleep(3)
        self.j.clickSalarytypeSelect()
        time.sleep(2)
        self.j.clickSalaryType1()
        time.sleep(2)
        self.j.typeSalaryMin(self.salarymin)
        time.sleep(3)
        self.j.typeSalaryMax(self.salarymax)
        time.sleep(3)
        self.j.typeJobDescription(self.jobdescription)
        time.sleep(3)
        self.j.scrollJobResponsiblities()
        time.sleep(3)
        self.j.typeJobResponsiblities(self.jobresponsiblities)
        time.sleep(3)
        self.j.typeSkill(self.skill)
        time.sleep(3)
        # self.j.clickAddSkillIcon()
        # time.sleep(5)
        self.j.clickWhocanapplySelect()
        time.sleep(3)
        self.j.selectWhocanapplyAccount1()
        time.sleep(3)
        self.j.selectWhocanapplyAccount2()
        time.sleep(3)
        self.j.selectWhocanapplyAccount3()
        time.sleep(3)
        self.j.selectWhocanapplyAccount4()
        time.sleep(3)
        self.j.selectWhocanapplyAccount5()
        time.sleep(3)

        self.j.clickPostJobFinalButton()
        time.sleep(1)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = toast_msg[0].text
        if result == "Please subscribe to create a new job.":
           self.logger.info("Toast Message Is: %s", result)
           assert True
           self.logger.info("*************** Please subscribe to create a new job test passed *************")
        else:
           assert False
           self.logger.info("*************** Please subscribe to create a new job test failed *************")



        self.logger.info("************** Need Subscription For Job Post Test Passed Successfully *************")
        self.driver.quit()