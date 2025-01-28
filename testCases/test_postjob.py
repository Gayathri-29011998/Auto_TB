import configparser
import pytest
import time

import self
from selenium.webdriver.common.by import By
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
    jobdescription  = ReadConfig.getjobdescription()
    jobresponsiblities = ReadConfig.getjobresponsiblities()
    skill = ReadConfig.getskill()

    logger = LogGen.loggen()

    #@pytest.mark.sanity
    def test_postjob(self, setup):  # Positive Test
        self.logger.info("********** Post Jobs Test - Positive **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.j = Jobs(self.driver)
        self.l.clickSignin()
        time.sleep(3)
        self.driver.refresh()
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
        #self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_postpositive.png")
        time.sleep(2)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = toast_msg[0].text
        if result == "Job created successfully":
           self.logger.info("Toast Message Is: %s", result)
           assert True
           self.logger.info("*************** Post Job test passed *************")
        else:
           assert False
           self.logger.info("*************** Post Job test failed *************")



        self.logger.info("************** Post Job Test Passed Successfully *************")
        self.driver.quit()

    #@pytest.mark.sanity
    def test_onbehalfofpostjob(self, setup):  # Positive Test
        self.logger.info("********** Onbehalfof Post Jobs Test - Positive **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.j = Jobs(self.driver)
        self.l.clickSignin()
        time.sleep(1)
        self.driver.refresh()
        self.l.setUsername(self.useremail)
        time.sleep(1)
        self.l.setPassword(self.password)
        time.sleep(1)
        self.l.clickLogin()
        time.sleep(2)
        self.j.selectionElement()
        time.sleep(3)
        self.j.clickJobButton()
        time.sleep(1)
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
        time.sleep(5)
        self.j.scrollJobDescription()
        time.sleep(3)
        self.j.typeJobResponsiblities(self.jobresponsiblities)
        time.sleep(5)
        self.j.typeSkill(self.skill)
        time.sleep(3)
        self.j.scrollPostJobFinalButton()
        time.sleep(3)
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
        self.j.clickWhocanapplySelect()
        time.sleep(3)
        self.j.clickOnbehalfofToggle()
        time.sleep(2)
        self.j.clickOnbehalfofChoose()
        time.sleep(2)
        self.j.clickOnbehalfofChooseAccount()
        time.sleep(2)
        self.j.scrollPostJobFinalButton()
        time.sleep(2)
        self.j.clickPostJobFinalButton()
        time.sleep(2)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = toast_msg[0].text
        if result == "Job created successfully":
            self.logger.info("Toast Message Is: %s", result)
            assert True
            self.logger.info("*************** Onbehalfof Post Job test passed *************")
        else:
            assert False
            self.logger.info("*************** Onbehalfof Post Job test failed *************")

        self.logger.info("************** Onbehalfof Post Job Test Passed Successfully *************")
        self.driver.quit()




    #@pytest.mark.sanity
    def test_jobsnegative1(self, setup):
        self.logger.info("********** Post Jobs Test - Negative **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.j = Jobs(self.driver)
        self.l.clickSignin()
        time.sleep(2)
        self.driver.refresh()
        self.l.setUsername(self.useremail)
        time.sleep(1)
        self.l.setPassword(self.password)
        time.sleep(1)
        self.l.clickLogin()
        time.sleep(3)
        self.j.selectionElement()
        time.sleep(2)
        self.j.clickJobButton()
        time.sleep(1)
        self.j.clickPostJobButton()
        time.sleep(3)
        self.j.scrollPostJobFinalButton()
        time.sleep(3)
        self.j.typeSkill(self.skill)
        time.sleep(3)
        self.j.clickPostJobFinalButton()
        time.sleep(2)
        #self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_postjobnegative1.png")
        #Designation
        error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[1]/p")
        result = error_msg1[0].text
        if result == "Designation is required.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Designation is required test passed successfully *************")
        else:
            assert False
            self.logger.info("*************** Designation is required test failed *************")
        #Experience Min
        error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[2]/p[1]")
        result = error_msg2[0].text
        if result == "Experience Min is required.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Experience Min is required test passed successfully *************")
        else:
            assert False
            self.logger.info("*************** Experience Min is required test failed *************")
        # Experience Max
        error_msg3 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[2]/p[2]")
        result = error_msg3[0].text
        if result == "Experience Max is required.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Experience Max is required test passed successfully *************")
        else:
            assert False
            self.logger.info("*************** Experience Max is required test failed *************")

        #Joining
        error_msg4 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[3]/p")
        result = error_msg4[0].text
        if result == "Joining is required":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Joining is required test passed successfully *************")
        else:
            assert False
            self.logger.info("*************** Joining is required test failed *************")
        #Employment Type
        error_msg5 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[4]/p")
        result = error_msg5[0].text
        if result == "Employment Type is required":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Employment Type required test passed successfully *************")
        else:
            assert False
            self.logger.info("*************** Employment Type required test failed *************")
        #Location
        error_msg6 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[5]/p")
        result = error_msg6[0].text
        if result == "Location is required.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Location required test passed successfully *************")
        else:
            assert False
            self.logger.info("*************** Location required test failed *************")
        #Currency
        error_msg7 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[6]/p[1]")
        result = error_msg7[0].text
        if result == "Currency is required":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Currency required test passed successfully *************")
        else:
            assert False
            self.logger.info("*************** Currency required test failed *************")
        #Salary Min
        error_msg8 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[6]/p[2]")
        result = error_msg8[0].text
        if result == "Salary Min value is required.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Salary Min value required test passed successfully *************")
        else:
            assert False
            self.logger.info("*************** Salary Min value required test failed *************")
        # Salary Max
        error_msg9 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[6]/p[3]")
        result = error_msg9[0].text
        if result == "Max Salary is required.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Max Salary required test passed successfully *************")
        else:
            assert False
            self.logger.info("*************** Max Salary required test failed *************")
        #Requirement
        error_msg10 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[7]/div[1]/p")
        result = error_msg10[0].text
        if result == "Requirement should not be blank.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Requirement required test passed successfully *************")
        else:
            assert False
            self.logger.info("*************** Requirement required test failed *************")
        #Responsiblities
        error_msg11 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[7]/div[2]/p")
        result = error_msg11[0].text
        if result == "Responsibility is required.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Responsibility required test passed successfully *************")
        else:
            assert False
            self.logger.info("*************** Responsibility required test failed *************")
        #Who Can Apply
        error_msg12 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[10]/p")
        result = error_msg12[0].text
        if result == "Who can apply is required":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Who can apply is required test passed successfully *************")
        else:
            assert False
            self.logger.info("*************** Who can apply is required test failed *************")

        self.logger.info("*************** Successfully Location Negative Test Passed ***************")
        self.driver.quit()

    #@pytest.mark.sanity
    def test_designationnegative(self, setup):  # Negative Test for Designation (very short,max 100 characters,invalid designation)
        self.logger.info("********** Post Jobs Test - Negative 2 **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.j = Jobs(self.driver)
        self.l.clickSignin()
        time.sleep(2)
        self.driver.refresh()
        time.sleep(1)
        self.l.setUsername(self.useremail)
        time.sleep(1)
        self.l.setPassword(self.password)
        time.sleep(1)
        self.l.clickLogin()
        time.sleep(2)
        self.j.selectionElement()
        time.sleep(2)
        self.j.clickJobButton()
        time.sleep(1)
        self.j.clickPostJobButton()
        time.sleep(3)
        self.j.scrollPostJobFinalButton()
        time.sleep(3)
        self.j.typeSkill(self.skill)
        time.sleep(5)
        self.j.clickPostJobFinalButton()
        time.sleep(3)
        # self.j.scrollDesignation()
        # time.sleep(2)
        self.j.shortDesignation()  #designation field  one character
        time.sleep(1)

        error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[1]/p")
        result = error_msg1[0].text
        if result == "Designation Title is very short.":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("*************** Designation Title is very short test passed successfully *************")
        else:
           assert False
           self.logger.info("*************** Designation Title is very short test failed *************")

        time.sleep(5)
        self.j.lengthDesignation()  #designation field  more than 100 character
        time.sleep(5)

        error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[1]/p")
        result = error_msg1[0].text
        if result == "Designation Title should not exceed 100 letters.":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("*************** Designation Title should 100 letters test passed successfully *************")
        else:
           assert False
           self.logger.info("*************** Designation Title should 100 letters test failed *************")

        time.sleep(5)
        self.j.invalidDesignation()  #designation field  onlynumbers (or) onlyspecial characters (or) onlyempty space
        time.sleep(10)

        error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[1]/p")
        result = error_msg1[0].text
        if result == "Invalid Designation.":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("*************** Designation is Invalid test passed successfully *************")
        else:
           assert False
           self.logger.info("*************** Designation is Invalid test failed *************")

        self.logger.info("************** Designation Test Passed Successfully *************")
        self.driver.quit()

    #@pytest.mark.sanity
    def test_experiencenegative(self, setup):  # Negative Test for Experience (max value greater than min valueinvalid designation)
        self.logger.info("********** Post Jobs Test Experience - Negative  **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.j = Jobs(self.driver)
        self.l.clickSignin()
        time.sleep(1)
        self.driver.refresh()
        time.sleep(1)
        self.l.setUsername(self.useremail)
        time.sleep(1)
        self.l.setPassword(self.password)
        time.sleep(1)
        self.l.clickLogin()
        time.sleep(2)
        self.j.selectionElement()
        time.sleep(2)
        self.j.clickJobButton()
        time.sleep(1)
        self.j.clickPostJobButton()
        time.sleep(3)
        self.j.scrollPostJobFinalButton()
        time.sleep(3)
        self.j.typeSkill(self.skill)
        time.sleep(5)
        self.j.clickPostJobFinalButton()
        time.sleep(3)
        self.j.scrollDesignation()
        time.sleep(2)
        self.j.typeInvalidExperienceMin()
        time.sleep(2)
        self.j.typeInvalidExperienceMax()
        time.sleep(2)

        error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[2]/p[1]")
        result = error_msg1[0].text
        if result == "Invalid minimum Experience value.":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("*************** Invalid minimum Experience test passed successfully *************")
        else:
           assert False
           self.logger.info("*************** Invalid minimum Experience test failed *************")

        error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[2]/p[2]")
        result = error_msg2[0].text
        if result == "Invalid maximum experience value.":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("*************** Invalid maximum experience test passed successfully *************")
        else:
           assert False
           self.logger.info("*************** Invalid maximum experience test failed *************")

        time.sleep(3)
        self.j.typeExperienceMin(self.experiencemin)
        time.sleep(3)
        self.j.lessExperiencemax()
        time.sleep(2)

        error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[2]/p")
        result = error_msg1[0].text
        if result == "Min value should be less than or equal to Max value":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("*************** Min value should be less than or equal to Max value test passed successfully *************")
        else:
           assert False
           self.logger.info("*************** Min value should be less than or equal to Max value test failed *************")

        self.logger.info("*************** Successfully Experience Min & Max Negative Test Passed ***************")
        self.driver.quit()

    #@pytest.mark.sanity
    def test_locationnegative(self, setup):  # Negative Test for Location (alphabets only accepted)
        self.logger.info("********** Post Jobs Test Location - Negative  **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.j = Jobs(self.driver)
        self.l.clickSignin()
        time.sleep(1)
        self.driver.refresh()
        time.sleep(1)
        self.l.setUsername(self.useremail)
        time.sleep(1)
        self.l.setPassword(self.password)
        time.sleep(1)
        self.l.clickLogin()
        time.sleep(2)
        self.j.selectionElement()
        time.sleep(2)
        self.j.clickJobButton()
        time.sleep(1)
        self.j.clickPostJobButton()
        time.sleep(3)
        self.j.scrollPostJobFinalButton()
        time.sleep(3)
        self.j.typeSkill(self.skill)
        time.sleep(5)
        self.j.clickPostJobFinalButton()
        time.sleep(3)
        self.j.scrollEmploymenttype()
        time.sleep(3)
        self.j.invalidLocation()
        time.sleep(2)

        error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[5]/p")
        result = error_msg1[0].text
        if result == "Location should contain only alphabets.":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("*************** Location should contain only alphabets test passed successfully *************")
        else:
           assert False
           self.logger.info("*************** Location should contain only alphabets test failed *************")

        self.logger.info("*************** Successfully Location Negative Test Passed ***************")
        self.driver.quit()

    #@pytest.mark.sanity
    def test_salaryminmaxnegative(self, setup):  # Negative Test for Location (alphabets only accepted)
        self.logger.info("********** Post Jobs Test Salary Min & Max - Negative  **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.j = Jobs(self.driver)
        self.l.clickSignin()
        time.sleep(1)
        self.driver.refresh()
        time.sleep(1)
        self.l.setUsername(self.useremail)
        time.sleep(1)
        self.l.setPassword(self.password)
        time.sleep(1)
        self.l.clickLogin()
        time.sleep(2)
        self.j.selectionElement()
        time.sleep(2)
        self.j.clickJobButton()
        time.sleep(1)
        self.j.clickPostJobButton()
        time.sleep(3)
        self.j.scrollPostJobFinalButton()
        time.sleep(3)
        self.j.typeSkill(self.skill)
        time.sleep(5)
        self.j.clickPostJobFinalButton()
        time.sleep(3)
        self.j.scrollLocation()
        time.sleep(3)
        self.j.invalidSalaryMin()
        time.sleep(1)
        self.j.invalidSalaryMax()
        time.sleep(1)

        error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[6]/p[2]")
        result = error_msg1[0].text
        if result == "Invalid minimum salary value.":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("*************** Invalid minimum salary value test passed successfully *************")
        else:
           assert False
           self.logger.info("*************** Invalid minimum salary value test failed *************")

        error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[6]/p[3]")
        result = error_msg2[0].text
        if result == "Invalid maximum salary value.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Invalid maximum salary value test passed successfully *************")
        else:
            assert False
            self.logger.info("*************** Invalid maximum salary value test failed *************")

        time.sleep(2)
        self.j.typeSalaryMin(self.salarymin)
        time.sleep(3)
        self.j.lessSalaryMax()
        time.sleep(1)

        error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[6]/p[2]")
        result = error_msg1[0].text
        if result == "Price Min value should be less than or equal to Max value":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("*************** Price Min value should be less than or equal to Max value test passed successfully *************")
        else:
           assert False
           self.logger.info("*************** Price Min value should be less than or equal to Max value test failed *************")

        self.logger.info("*************** Successfully Salary Min & Max Negative Test Passed ***************")
        self.driver.quit()

    #@pytest.mark.sanity
    def test_requirementresponsiblitiesnegative(self, setup):  # Negative Test for Location (alphabets only accepted)
        self.logger.info("********** Post Jobs Test Requirements & Responsiblities - Negative  **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.j = Jobs(self.driver)
        self.l.clickSignin()
        time.sleep(1)
        self.driver.refresh()
        time.sleep(1)
        self.l.setUsername(self.useremail)
        time.sleep(1)
        self.l.setPassword(self.password)
        time.sleep(1)
        self.l.clickLogin()
        time.sleep(2)
        self.j.selectionElement()
        time.sleep(2)
        self.j.clickJobButton()
        time.sleep(1)
        self.j.clickPostJobButton()
        time.sleep(3)
        self.j.scrollPostJobFinalButton()
        time.sleep(3)
        self.j.typeSkill(self.skill)
        time.sleep(5)
        self.j.clickPostJobFinalButton()
        time.sleep(3)
        self.j.scrollSalaryType()
        time.sleep(3)
        self.j.invalidJobDescription()
        time.sleep(2)

        error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[7]/div[1]/p")
        result = error_msg1[0].text
        if result == "Job Requirement should be at least 100 characters long.":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("*************** Job Requirement should be at least 100 characters long test passed successfully *************")
        else:
           assert False
           self.logger.info("*************** Job Requirement should be at least 100 characters long test failed *************")

        time.sleep(2)
        self.j.emptyJobDescription()
        time.sleep(10)

        error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[7]/div[1]/p")
        result = error_msg2[0].text
        if result == "Requirement should not be empty.":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("*************** Requirement should not be empty test passed successfully *************")
        else:
           assert False
           self.logger.info("*************** Requirement should not be empty test failed *************")

        time.sleep(3)
        self.j.scrollJobDescription()
        time.sleep(2)
        self.j.invalidJobResponsiblities()
        time.sleep(2)
        self.j.scrollPostJobFinalButton()
        time.sleep(1)
        self.j.clickPostJobFinalButton()
        time.sleep(2)
        self.j.scrollJobDescription()
        time.sleep(2)

        error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[7]/div[2]/p")
        result = error_msg1[0].text
        if result == "Responsibility is very short. Required at least 100 characters.":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("*************** Responsibility is very short. Required at least 100 characters test passed successfully *************")
        else:
           assert False
           self.logger.info("*************** Responsibility is very short. Required at least 100 characters test failed *************")

        self.logger.info("*************** Successfully Requirements & Responsiblities Negative Test Passed ***************")
        self.driver.quit()








