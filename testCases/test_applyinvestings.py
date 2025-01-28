import time

import pytest
import self
from selenium.webdriver.common.by import By

from pageObjects.ApplyInvestings import ApplyInvest
from pageObjects.ApplyJobs import Applyjob
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

    logger = LogGen.loggen()

    #@pytest.mark.sanity
    def test_applyinvestingpositive(self,setup):  #Positive Test for Investings Apply
        self.logger.info("********** Apply Investings Test - Positive **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.j = Jobs(self.driver)
        self.inv = Investings(self.driver)
        self.ai = ApplyInvest(self.driver)
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
        time.sleep(5)
        self.inv.clickInvestings()
        time.sleep(3)
        self.ai.clickPitchButton()
        time.sleep(2)
        self.ai.typeInvestFundRequired()
        time.sleep(2)
        self.ai.clickStage()
        time.sleep(2)
        self.ai.selectStage1()
        time.sleep(2)
        self.ai.clickSector()
        time.sleep(2)
        self.ai.selectSector1()
        time.sleep(2)
        self.ai.typeDescription()
        time.sleep(3)
        self.ai.clickPDFUpload()
        time.sleep(2)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = toast_msg[0].text
        if result == "Successfully Uploaded":
            self.logger.info("Toast Message Is: %s", result)
            assert True
            self.logger.info("*********** PDF Upload Test Passed ***********")
        else:
            assert False

        time.sleep(3)
        self.ai.clickApplyInvestSubmitButton()
        time.sleep(2)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = toast_msg[0].text
        if result == "You have successfully pitched to this investing":
            self.logger.info("Toast Message Is: %s", result)
            assert True
            self.logger.info("*********** You have successfully pitched to this investing Test Passed ***********")
        else:
            assert False
            self.logger.info("*********** You have successfully pitched to this investing Test Failed ***********")

        self.logger.info("********** Apply Investing Test Successfully Passed **********")
        self.driver.quit()

    #@pytest.mark.sanity
    def test_applyinvestingonbehalfof(self, setup):  # Positive Test for Investings Onbehalfof Apply
        self.logger.info("********** Apply Investings Onbehalfof Test - Positive **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.j = Jobs(self.driver)
        self.inv = Investings(self.driver)
        self.ai = ApplyInvest(self.driver)
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
        time.sleep(5)
        self.inv.clickInvestings()
        time.sleep(3)
        self.ai.clickPitchButton()
        time.sleep(2)
        self.ai.typeInvestFundRequired()
        time.sleep(2)
        self.ai.clickStage()
        time.sleep(2)
        self.ai.selectStage1()
        time.sleep(2)
        self.ai.clickSector()
        time.sleep(2)
        self.ai.selectSector1()
        time.sleep(2)
        self.ai.typeDescription()
        time.sleep(2)
        self.ai.clickPDFUpload()
        time.sleep(2)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = toast_msg[0].text
        if result == "Successfully Uploaded":
            self.logger.info("Toast Message Is: %s", result)
            assert True
            self.logger.info("*********** PDF Upload Test Passed ***********")
        else:
            assert False

        time.sleep(2)
        self.ai.clickOnbehalfofToggle()
        time.sleep(2)
        self.ai.clickOnbehalfofChoose()
        time.sleep(2)
        self.ai.clickOnbehalfofAccount()
        time.sleep(2)
        self.ai.clickApplyInvestSubmitButton()
        time.sleep(2)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = toast_msg[0].text
        if result == "You have successfully pitched to this investing":
            self.logger.info("Toast Message Is: %s", result)
            assert True
            self.logger.info("*********** You have successfully pitched to this investing Test Passed ***********")
        else:
            assert False
            self.logger.info("*********** You have successfully pitched to this investing Test Failed ***********")

        self.logger.info("********** Apply Investing Test Successfully Passed **********")
        self.driver.quit()

    #@pytest.mark.sanity
    def test_applyinvestingnegative(self,setup):  #Negative Test
        self.logger.info("********** Apply Investings Test - Negative **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.j = Jobs(self.driver)
        self.inv = Investings(self.driver)
        self.ai = ApplyInvest(self.driver)
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
        self.inv.clickInvestings()
        time.sleep(2)
        self.ai.clickPitchButton()
        time.sleep(2)
        self.ai.clickApplyInvestSubmitButton()
        time.sleep(2)

        error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[4]/div[3]/form/p[2]")
        result = error_msg1[0].text
        if result == "Amount is required":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Amount is required Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Amount is required Test Failed *************")

        error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[4]/div[3]/form/div[2]/div[1]/p[2]")
        result = error_msg2[0].text
        if result == "Stage is required":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Stage is required Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Stage is required Test Failed *************")

        error_msg3 = self.driver.find_elements(By.XPATH, "/html/body/div[4]/div[3]/form/div[2]/div[2]/p[2]")
        result = error_msg3[0].text
        if result == "Sector is required":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Sector is required Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Sector is required Test Failed *************")

        error_msg4 = self.driver.find_elements(By.XPATH, "/html/body/div[4]/div[3]/form/p[3]")
        result = error_msg4[0].text
        if result == "Description is required":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Description is required Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Description is required Test Failed *************")

        time.sleep(2)
        self.ai.typeInvestFundRequired()
        time.sleep(2)
        self.ai.clickStage()
        time.sleep(2)
        self.ai.selectStage1()
        time.sleep(2)
        self.ai.clickSector()
        time.sleep(2)
        self.ai.selectSector1()
        time.sleep(2)
        self.ai.typeDescription()
        time.sleep(2)
        self.ai.clickApplyInvestSubmitButton()
        time.sleep(1)

        error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = error_msg[0].text
        if result == "Pitch Deck document is required":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("*************** Pitch Deck document is required Test Passed *************")
        else:
           assert False
           self.logger.info("*************** Pitch Deck document is required Test Failed *************")

        time.sleep(2)
        self.ai.clickPDFUpload()
        time.sleep(2)
        self.ai.clickOnbehalfofToggle()
        time.sleep(2)
        self.ai.clickApplyInvestSubmitButton()
        time.sleep(1)

        error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = error_msg[0].text
        if result == "Select On Behalf of dropdown.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Select On Behalf of dropdown. Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Select On Behalf of dropdown. Test Failed *************")

        self.logger.info("********** Apply Investing Negative1 Test Successfully Passed **********")
        self.driver.quit()

    #@pytest.mark.sanity
    def test_Saveinvesting(self,setup):
        self.logger.info("********** Save & Unsave Investings Test **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.j = Jobs(self.driver)
        self.inv = Investings(self.driver)
        self.ai = ApplyInvest(self.driver)
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
        self.inv.clickInvestings()
        time.sleep(2)
        self.ai.clickInvestThreedots()
        time.sleep(2)
        self.ai.clickInvestsave()
        time.sleep(1)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = toast_msg[0].text
        if result == "You have successfully saved this investing":
            self.logger.info("Toast Message Is: %s", result)
            assert True
            self.logger.info("*********** Investing Save Test Passed ***********")
        else:
            assert False

        time.sleep(2)
        self.ai.clickInvestThreedots()
        time.sleep(2)
        self.ai.clickInvestsave()
        time.sleep(1)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = toast_msg[0].text
        if result == "You have successfully unsaved this investing":
            self.logger.info("Toast Message Is: %s", result)
            assert True
            self.logger.info("*********** Investing Unsave Test Passed ***********")
        else:
            assert False

        self.logger.info("********** Save & Unsave Investing Test Successfully Passed **********")
        self.driver.quit()

    #@pytest.mark.sanity
    def test_copylinkinvesting(self,setup):
        self.logger.info("********** Copy Link Investings Test **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.j = Jobs(self.driver)
        self.inv = Investings(self.driver)
        self.ai = ApplyInvest(self.driver)
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
        time.sleep(3)
        self.inv.clickInvestings()
        time.sleep(2)
        self.ai.clickInvestThreedots()
        time.sleep(2)
        self.ai.clickInvestcopylink()
        time.sleep(1)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = toast_msg[0].text
        if result == "Link copied":
            self.logger.info("Toast Message Is: %s", result)
            assert True
            self.logger.info("*********** Investing Copy link Test Passed ***********")
        else:
            assert False

        self.logger.info("********** Copy Link Investing Test Successfully Passed **********")
        self.driver.quit()

    #@pytest.mark.sanity
    def test_reviewinvesting(self,setup):
        self.logger.info("**********  Write a Review Investings Test - Positive & Negative  **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.j = Jobs(self.driver)
        self.inv = Investings(self.driver)
        self.ai = ApplyInvest(self.driver)
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
        self.inv.clickInvestings()
        time.sleep(2)
        self.ai.clickInvestThreedots()
        time.sleep(2)
        self.ai.clickInvestreview()
        time.sleep(2)
        self.ai.clickInvestreviewsubmit()
        time.sleep(1)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = toast_msg[0].text
        if result == "Rating is required":
            self.logger.info("Toast Message Is: %s", result)
            assert True
            self.logger.info("*********** Rating is required Test Passed ***********")
        else:
            assert False

        time.sleep(2)
        self.ai.clickInvestrating()
        time.sleep(2)
        self.ai.clickInvestreviewsubmit()
        time.sleep(1)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = toast_msg[0].text
        if result == "Review comment is required.":
            self.logger.info("Toast Message Is: %s", result)
            assert True
            self.logger.info("*********** Review comment is required Test Passed ***********")
        else:
            assert False

        time.sleep(2)
        self.ai.clickInvestreviewtext()
        time.sleep(2)
        self.ai.clickInvestreviewsubmit()
        time.sleep(2)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = toast_msg[0].text
        if result == "Investing Reviewed successfully":
            self.logger.info("Toast Message Is: %s", result)
            assert True
            self.logger.info("*********** Investing Reviewed successfully  ***********")
        else:
            assert False

        self.logger.info("********** Review Investing Successfully Passed **********")
        self.driver.quit()

    #@pytest.mark.sanity
    def test_reportinvesting(self,setup):
        self.logger.info("**********  Report Investings Test - Positive & Negative  **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.j = Jobs(self.driver)
        self.inv = Investings(self.driver)
        self.ai = ApplyInvest(self.driver)
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
        self.inv.clickInvestings()
        time.sleep(2)
        self.ai.clickInvestThreedots()
        time.sleep(2)
        self.ai.clickInvestreport()
        time.sleep(2)
        self.ai.clickInvestreportsubmit()
        time.sleep(1)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = toast_msg[0].text
        if result == "Please type your comment.":
            self.logger.info("Toast Message Is: %s", result)
            assert True
            self.logger.info("*********** Report Comment is required Test Passed ***********")
        else:
            assert False

        time.sleep(2)
        self.ai.clickInvestreporttext()
        time.sleep(2)
        self.ai.clickInvestreportsubmit()
        time.sleep(1)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = toast_msg[0].text
        if result == "Investing Reported successfully.":
            self.logger.info("Toast Message Is: %s", result)
            assert True
            self.logger.info("*********** Investing Reported successfully. Test Passed ***********")
        else:
            assert False

        self.logger.info("********** Report Investing Test Successfully Passed **********")
        self.driver.quit()

    #@pytest.mark.sanity
    def test_notinterestinvesting(self,setup):
        self.logger.info("**********  Not Interested Investings Test - Positive  **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.j = Jobs(self.driver)
        self.inv = Investings(self.driver)
        self.ai = ApplyInvest(self.driver)
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
        self.inv.clickInvestings()
        time.sleep(2)
        self.ai.clickInvestThreedots()
        time.sleep(2)
        self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_Investings1.png")
        time.sleep(3)
        self.ai.clickInvestnotinterest()
        time.sleep(2)
        self.ai.clickInvestnotinterestyes()
        time.sleep(1)

        toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = toast_msg[0].text
        if result == "Investing not interested successfully.":
            self.logger.info("Toast Message Is: %s", result)
            assert True
            self.logger.info("*********** Not Interested Investing Test Passed ***********")
        else:
            assert False

        self.logger.info("********** Not Interested Investing Test  Passed Successfully **********")
        self.driver.quit()
















