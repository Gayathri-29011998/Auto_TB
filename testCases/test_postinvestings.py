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
    investorname = ReadConfig.getinvestorname()
    invesmentexperience = ReadConfig.getinvesmentexperience()
    totalamountinvest = ReadConfig.gettotalamountinvest()
    noofpreviousinvestcompany = ReadConfig.getnoofpreviousinvestcompany()
    evaluationduration = ReadConfig.getevaluationduration()
    investrangemin = ReadConfig.getinvestrangemin()
    investrangemax = ReadConfig.getinvestrangemax()

    logger = LogGen.loggen()

    #@pytest.mark.sanity
    def test_postinvesting(self, setup):  # Positive Test
        self.logger.info("********** Post Investings Test - Positive **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.j = Jobs(self.driver)
        self.i = Investings(self.driver)
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
        time.sleep(3)
        self.i.clickInvestings()
        time.sleep(2)
        self.i.clickPostInvestingButton()
        time.sleep(2)
        self.i.typeInvestorname(self.investorname)
        time.sleep(2)
        self.i.typeInvestExperience(self.invesmentexperience)
        time.sleep(2)
        self.i.clickInvestorType()
        time.sleep(2)
        self.i.selectInvestorType1()
        time.sleep(2)
        self.i.typeTotalAmountInvest(self.totalamountinvest)
        time.sleep(2)
        self.i.typeNoofpreviousInvCompany(self.noofpreviousinvestcompany)
        time.sleep(2)
        self.i.scrollSector()
        time.sleep(2)
        self.i.clickSector()
        time.sleep(2)
        self.i.selectSectortype1()
        time.sleep(2)
        self.i.clickSector()
        time.sleep(2)
        self.i.clickInvestmentStage()
        time.sleep(2)
        self.i.selectStage1()
        time.sleep(2)
        self.i.selectStage2()
        time.sleep(2)
        self.i.clickInvestmentStage()
        time.sleep(2)
        self.i.typeEvaluationDuration(self.evaluationduration)
        time.sleep(2)
        self.i.clickInvestRange()
        time.sleep(2)
        self.i.selectInvestRangeINR()
        time.sleep(2)
        self.i.typeRangeMin(self.investrangemin)
        time.sleep(2)
        self.i.typeRangeMax(self.investrangemax)
        time.sleep(2)
        self.i.scrollWhoCanApply()
        time.sleep(2)
        self.i.clickWhoCanApply()
        time.sleep(3)
        self.i.selectWhocanapplyAccount7()
        time.sleep(3)
        self.i.selectWhocanapplyAccount6()
        time.sleep(3)
        self.i.selectWhocanapplyAccount5()
        time.sleep(3)
        self.i.selectWhocanapplyAccount4()
        time.sleep(3)
        self.i.selectWhocanapplyAccount3()
        time.sleep(3)
        self.i.selectWhocanapplyAccount2()
        time.sleep(3)
        self.i.selectWhocanapplyAccount1()
        time.sleep(3)
        self.i.clickWhoCanApply()
        time.sleep(3)
        self.i.clickPostInvestingFinalButton()
        time.sleep(1)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = toast_msg[0].text
        if result == "Investing created successfully":
           self.logger.info("Toast Message Is: %s", result)
           assert True
           self.logger.info("*************** Post Job test passed *************")
        else:
           assert False
           self.logger.info("*************** Post Job test failed *************")

        self.logger.info("************** Post Job Test Passed Successfully *************")
        self.driver.quit()

    #@pytest.mark.sanity
    def test_onbehalfofpostinvesting(self, setup):  # Positive Test
        self.logger.info("********** Onbehalfof Post Investings Test - Positive **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.j = Jobs(self.driver)
        self.i = Investings(self.driver)
        self.l.clickSignin()
        time.sleep(1)
        self.driver.refresh()
        self.l.setUsername(self.useremail)
        time.sleep(1)
        self.l.setPassword(self.password)
        time.sleep(1)
        self.l.clickLogin()
        time.sleep(3)
        self.j.selectionElement()
        time.sleep(3)
        self.i.clickInvestings()
        time.sleep(2)
        self.i.clickPostInvestingButton()
        time.sleep(2)
        self.i.typeInvestorname(self.investorname)
        time.sleep(3)
        self.i.typeInvestExperience(self.invesmentexperience)
        time.sleep(3)
        self.i.clickInvestorType()
        time.sleep(2)
        self.i.selectInvestorType1()
        time.sleep(2)
        self.i.typeTotalAmountInvest(self.totalamountinvest)
        time.sleep(2)
        self.i.typeNoofpreviousInvCompany(self.noofpreviousinvestcompany)
        time.sleep(2)
        self.i.scrollSector()
        time.sleep(2)
        self.i.clickSector()
        time.sleep(2)
        self.i.selectSectortype1()
        time.sleep(2)
        self.i.clickSector()
        time.sleep(2)
        self.i.clickInvestmentStage()
        time.sleep(2)
        self.i.selectStage1()
        time.sleep(2)
        self.i.selectStage2()
        time.sleep(2)
        self.i.clickInvestmentStage()
        time.sleep(2)
        self.i.typeEvaluationDuration(self.evaluationduration)
        time.sleep(2)
        self.i.clickInvestRange()
        time.sleep(2)
        self.i.selectInvestRangeINR()
        time.sleep(2)
        self.i.typeRangeMin(self.investrangemin)
        time.sleep(2)
        self.i.typeRangeMax(self.investrangemax)
        time.sleep(2)
        self.i.clickWhoCanApply()
        time.sleep(2)
        self.i.selectWhocanapplyAccount1()
        time.sleep(2)
        self.i.selectWhocanapplyAccount2()
        time.sleep(3)
        self.i.selectWhocanapplyAccount3()
        time.sleep(3)
        self.i.selectWhocanapplyAccount4()
        time.sleep(3)
        self.i.selectWhocanapplyAccount5()
        time.sleep(3)
        self.i.selectWhocanapplyAccount6()
        time.sleep(3)
        self.i.selectWhocanapplyAccount7()
        time.sleep(3)
        self.i.clickWhoCanApply()
        time.sleep(2)
        self.i.clickOnbehalfofToggle()
        time.sleep(2)
        self.i.clickOnbehalfofChoose()
        time.sleep(2)
        self.i.clickOnbehalfofAccount()
        time.sleep(2)
        self.i.scrollPostInvestingFinalButton()
        time.sleep(2)
        self.i.clickPostInvestingFinalButton()
        time.sleep(1)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = toast_msg[0].text
        if result == "Investing created successfully":
           self.logger.info("Toast Message Is: %s", result)
           assert True
           self.logger.info("*************** Post Job test passed *************")
        else:
           assert False
           self.logger.info("*************** Post Job test failed *************")

        self.logger.info("************** Post Job Test Passed Successfully *************")
        self.driver.quit()
    #@pytest.mark.sanity
    def test_postinvestingnegative1(self, setup):  # Negative Test
        self.logger.info("********** Post Investings Test - Negative **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.j = Jobs(self.driver)
        self.i = Investings(self.driver)
        self.l.clickSignin()
        time.sleep(1)
        self.driver.refresh()
        self.l.setUsername(self.useremail)
        time.sleep(1)
        self.l.setPassword(self.password)
        time.sleep(1)
        self.l.clickLogin()
        time.sleep(1)
        self.j.selectionElement()
        time.sleep(4)
        self.i.clickInvestings()
        time.sleep(2)
        self.i.clickPostInvestingButton()
        time.sleep(2)
        self.i.scrollPostInvestingFinalButton()
        time.sleep(2)
        self.i.clickPostInvestingFinalButton()
        time.sleep(3)

        error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[2]/p")
        result = error_msg1[0].text
        if result == "Investor Name is required.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Investor Name is required test passed successfully *************")
        else:
            assert False
            self.logger.info("*************** Investor Name is required test failed *************")

        error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[3]/p")
        result = error_msg2[0].text
        if result == "Investor experience is required":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Investor experience is required test passed successfully *************")
        else:
            assert False
            self.logger.info("*************** Investor experience is required test failed *************")

        error_msg3 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[4]/p")
        result = error_msg3[0].text
        if result == "Investment Type is required":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Investment Type is required test passed successfully *************")
        else:
            assert False
            self.logger.info("*************** Investment Type is required test failed *************")

        error_msg4 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[5]/p")
        result = error_msg4[0].text
        if result == "Total Investment is required":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Total Investment is required test passed successfully *************")
        else:
            assert False
            self.logger.info("*************** Total Investment is required test failed *************")

        error_msg5 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[6]/p")
        result = error_msg5[0].text
        if result == "No. of perviously invested companies is required":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** No. of perviously invested companies is required test passed successfully *************")
        else:
            assert False
            self.logger.info("*************** No. of perviously invested companies is required test failed *************")

        error_msg6 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[7]/p")
        result = error_msg6[0].text
        if result == "Sector is required":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info(
                "*************** Sector is required test passed successfully *************")
        else:
            assert False
            self.logger.info(
                "*************** Sector is required test failed *************")

        error_msg7 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/p[2]")
        result = error_msg7[0].text
        if result == "Evaluation Duration is required":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Evaluation Duration is required test passed successfully *************")
        else:
            assert False
            self.logger.info("*************** Evaluation Duration is required test failed *************")

        error_msg8 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[10]/div/div[1]/p")
        result = error_msg8[0].text
        if result == "Currency is required":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Currency is required test passed successfully *************")
        else:
            assert False
            self.logger.info("*************** Currency is required test failed *************")

        error_msg8 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[10]/p[1]")
        result = error_msg8[0].text
        if result == "Max Investment value is required.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Max Investment value is required test passed successfully *************")
        else:
            assert False
            self.logger.info("*************** Max Investment value is required test failed *************")

        error_msg9 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[10]/p[2]")
        result = error_msg9[0].text
        if result == "Min Investment value is required.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info(
                "*************** Min Investment value is required test passed successfully *************")
        else:
            assert False
            self.logger.info("*************** Min Investment value is required test failed *************")

        error_msg10 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[11]/p")
        result = error_msg10[0].text
        if result == "Who can apply is required":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info(
                "*************** Who can apply is required test passed successfully *************")
        else:
            assert False
            self.logger.info("*************** Who can apply is required test failed *************")

        self.logger.info("************** Post Job Test Passed Successfully *************")
        self.driver.quit()

    #@pytest.mark.sanity
    def test_postinvestingnegative2(self, setup):  # Negative Test - Invalid Input fields
        self.logger.info("********** Post Investings Test - Negative **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.j = Jobs(self.driver)
        self.i = Investings(self.driver)
        self.l.clickSignin()
        time.sleep(1)
        self.driver.refresh()
        self.l.setUsername(self.useremail)
        time.sleep(1)
        self.l.setPassword(self.password)
        time.sleep(1)
        self.l.clickLogin()
        time.sleep(1)
        self.j.selectionElement()
        time.sleep(4)
        self.i.clickInvestings()
        time.sleep(2)
        self.i.clickPostInvestingButton()
        time.sleep(2)
        self.i.invalidInvestorname()
        time.sleep(2)
        self.i.invalidInvestExperience()
        time.sleep(2)
        self.i.invalidTotalAmountInvest()
        time.sleep(2)
        self.i.scrollNoofpreviousInvCompany()
        time.sleep(2)
        self.i.invalidNoofpreviousInvCompany()
        time.sleep(2)
        self.i.invalidEvaluationDuration()
        time.sleep(2)
        self.i.invalidRangeMin()
        time.sleep(2)
        self.i.invalidRangeMax()
        time.sleep(2)
        self.i.scrollPostInvestingFinalButton()
        time.sleep(2)
        self.i.clickPostInvestingFinalButton()
        time.sleep(2)

        error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[2]/p")
        result = error_msg1[0].text
        if result == "Invalid Investor Name":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Invalid Investor Name test passed successfully *************")
        else:
            assert False
            self.logger.info("*************** Invalid Investor Name test failed *************")

        error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[3]/p")
        result = error_msg2[0].text
        if result == "Invalid Investor Experience value.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Invalid Investor Experience test passed successfully *************")
        else:
            assert False
            self.logger.info("*************** Invalid Investor Experience test failed *************")

        error_msg3 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[5]/p")
        result = error_msg3[0].text
        if result == "Invalid total investment value.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Invalid total investment test passed successfully *************")
        else:
            assert False
            self.logger.info("*************** Invalid total investment test failed *************")

        error_msg4 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[6]/p")
        result = error_msg4[0].text
        if result == "No. of previously invested companies is should be a number.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** No. of previously invested companies is should be a number test passed successfully *************")
        else:
            assert False
            self.logger.info("*************** No. of previously invested companies is should be a number test failed *************")

        error_msg5 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/p[2]")
        result = error_msg5[0].text
        if result == "Invalid evaluation duration.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Invalid evaluation duration test passed successfully *************")
        else:
            assert False
            self.logger.info("*************** Invalid evaluation duration test failed *************")

        error_msg6 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[10]/p[1]")
        result = error_msg6[0].text
        if result == "Invalid maximum investment value.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Invalid maximum investment test passed successfully *************")
        else:
            assert False
            self.logger.info("*************** Invalid maximum investment test failed *************")

        error_msg7 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[10]/p[2]")
        result = error_msg7[0].text
        if result == "Invalid minimum investment value.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Invalid minimum investment test passed successfully *************")
        else:
            assert False
            self.logger.info("*************** Invalid minimum investment test failed *************")

        time.sleep(2)
        self.i.lessRangeMin()
        time.sleep(2)
        self.i.lessRangeMax()
        time.sleep(2)

        error_msg7 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[10]/p")
        result = error_msg7[0].text
        if result == "Min value should be less than or equal to Max value":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Min value should be less than or equal to Max value test passed successfully *************")
        else:
            assert False
            self.logger.info("*************** Min value should be less than or equal to Max value test failed *************")

        self.logger.info("************** Post Job Test Passed Successfully *************")
        self.driver.quit()













