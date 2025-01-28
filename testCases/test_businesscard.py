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

class Test_Businesscard:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    tagline = ReadConfig.gettagline()
    foundedyear = ReadConfig.getfoundedyear()
    noofstudents = ReadConfig.getnoofstudents()
    noofcourses = ReadConfig.getnoofcourses()
    noofcompaniestrusting = ReadConfig.getnoofcompaniestrusting()
    summary = ReadConfig.getsummary()
    address1 = ReadConfig.getaddress1()
    address2 = ReadConfig.getaddress2()
    city = ReadConfig.getcity()
    state = ReadConfig.getstate()
    country = ReadConfig.getcountry()
    pincode = ReadConfig.getpincode()



    logger = LogGen.loggen()
    #
    # #@pytest.mark.sanity
    # def test_Editbusinesscardpositive(self, setup):
    #     self.logger.info("*************** Test_Businesscard *************")
    #     self.logger.info("************** Edit Businesscard  positive Test *************")
    #     self.driver = setup
    #     self.driver.get(self.baseurl)
    #     self.driver.maximize_window()
    #     self.l = Login(self.driver)
    #     self.j = Jobs(self.driver)
    #     self.cp = College(self.driver)
    #     time.sleep(3)
    #     self.l.clickSignin()
    #     time.sleep(3)
    #     self.l.setUsername(self.username)
    #     time.sleep(3)
    #     self.l.setPassword(self.password)
    #     time.sleep(3)
    #     self.l.clickLogin()
    #     time.sleep(3)
    #     self.j.selectionElement()
    #     time.sleep(3)
    #     self.cp.clickProfileicon()
    #     time.sleep(3)
    #     self.cp.clickProfilename()
    #     time.sleep(5)
    #     self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_Editbusinesscard1.png")
    #     time.sleep(3)
    #     self.cp.clickEditbusinesscard()
    #     time.sleep(3)
    #     self.cp.typeInstitutename()
    #     time.sleep(3)
    #     self.cp.typeTagline(self.tagline)
    #     time.sleep(3)
    #     self.cp.typeFoundedyear(self.foundedyear)
    #     time.sleep(3)
    #     self.cp.typeNoofstudents(self.noofstudents)
    #     time.sleep(3)
    #     self.cp.typeNoofcourses(self.noofcourses)
    #     time.sleep(3)
    #     self.cp.typeNoofcompaniestrusting(self.noofcompaniestrusting)
    #     time.sleep(3)
    #     self.cp.typeSummary(self.summary)
    #     time.sleep(3)
    #     self.cp.typeAddress1(self.address1)
    #     time.sleep(3)
    #     self.cp.typeAddress2(self.address2)
    #     time.sleep(3)
    #     self.cp.typeCity(self.city)
    #     time.sleep(3)
    #     self.cp.typeState(self.state)
    #     time.sleep(3)
    #     self.cp.typeCountry(self.country)
    #     time.sleep(3)
    #     self.cp.typePincode(self.pincode)
    #     time.sleep(3)
    #     self.cp.typeMobile()
    #     time.sleep(3)
    #     self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_Editbusinesscard2.png")
    #     time.sleep(2)
    #     self.cp.clickSavebusinesscard()
    #     time.sleep(2)
    #
    #     toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
    #     result = toast_msg[0].text
    #
    #     if result == "Business Card details updated Successfully.":
    #         self.logger.info("Toast Message Is: %s", result)
    #         self.logger.info("*********** Edit Businesscard Test Passed ***********")
    #         assert True
    #
    #     else:
    #         self.logger.info("*********** Edit Businesscard Test Failed ***********")
    #         assert False
    #
    #     self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_Editbusinesscard3.png")
    #     self.logger.info("Screenshot Saved")
    #
    #     self.logger.info("************** Successfully Edit Businesscard  Positive Test Passed *************")
    #     self.driver.quit()
    #
    # #@pytest.mark.sanity
    # def test_Editbusinesscardnegative(self, setup):
    #     self.logger.info("*************** Test_Businesscard *************")
    #     self.logger.info("************** Edit Businesscard  Negative Test *************")
    #     self.driver = setup
    #     self.driver.get(self.baseurl)
    #     self.driver.maximize_window()
    #     self.l = Login(self.driver)
    #     self.j = Jobs(self.driver)
    #     self.cp = College(self.driver)
    #     time.sleep(3)
    #     self.l.clickSignin()
    #     time.sleep(3)
    #     self.l.setUsername(self.username)
    #     time.sleep(3)
    #     self.l.setPassword(self.password)
    #     time.sleep(3)
    #     self.l.clickLogin()
    #     time.sleep(3)
    #     self.j.selectionElement()
    #     time.sleep(3)
    #     self.cp.clickProfileicon()
    #     time.sleep(3)
    #     self.cp.clickProfilename()
    #     time.sleep(5)
    #     self.cp.clickEditbusinesscard()
    #     time.sleep(3)
    #     self.cp.withoutTagline()
    #     time.sleep(1)
    #     self.cp.withoutFoundedyear()
    #     time.sleep(1)
    #     self.cp.withoutNoofstudents()
    #     time.sleep(1)
    #     self.cp.withoutNoofcourses()
    #     time.sleep(1)
    #     self.cp.withoutNoofcompaniestrusting()
    #     time.sleep(1)
    #     self.cp.withoutSummary()
    #     time.sleep(1)
    #     self.cp.withoutAddress1()
    #     time.sleep(1)
    #     self.cp.withoutAddress2()
    #     time.sleep(1)
    #     self.cp.withoutCity()
    #     time.sleep(1)
    #     self.cp.withoutState()
    #     time.sleep(1)
    #     self.cp.withoutCountry()
    #     time.sleep(1)
    #     self.cp.withoutPincode()
    #     time.sleep(3)
    #     self.cp.clickSavebusinesscard()
    #     time.sleep(2)
    #
    #     #Tagline
    #     error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/form/p[1]")
    #     result = error_msg[0].text
    #     if result == "TagLine is required.":
    #         self.logger.info("Error Message Is: %s", result)
    #         assert True
    #         self.logger.info("********** TagLine Negative Test passed *********")
    #     else:
    #         assert False
    #         self.logger.info("********** TagLine Negative Test failed *********")
    #
    #     #Founded Year
    #     error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/form/p[2]")
    #     result = error_msg1[0].text
    #     if result == "Year is required":
    #         self.logger.info("Error Message Is: %s", result)
    #         assert True
    #         self.logger.info("********** Founded Year Negative Test passed *********")
    #     else:
    #         assert False
    #         self.logger.info("********** Founded Year Negative Test failed *********")
    #
    #     #No.Of.Students
    #     error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/form/p[3]")
    #     result = error_msg2[0].text
    #     print(result)
    #     if result == "Total Number of students is required.":
    #         self.logger.info("Error Message Is: %s", result)
    #         assert True
    #         self.logger.info("********** Total Number of students Negative Test passed *********")
    #     else:
    #         assert False
    #         self.logger.info("********** Total Number of students Negative Test failed *********")
    #
    #
    #     #Total No.of Courses
    #     error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/form/p[4]")
    #     result = error_msg2[0].text
    #
    #     if result == "Total Number of Courses offered is required.":
    #         self.logger.info("Error Message Is: %s", result)
    #         assert True
    #         self.logger.info("********** Total Number of Courses Negative Test passed *********")
    #     else:
    #         assert False
    #         self.logger.info("********** Total Number of Courses Negative Test failed *********")
    #
    #     #No.of Companies Trusting us
    #     error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/form/p[5]")
    #     result = error_msg1[0].text
    #     if result == "Total Number of companies trusting is required.":
    #         self.logger.info("Error Message Is: %s", result)
    #         assert True
    #         self.logger.info("********** Total Number of companies trusting Negative Test passed *********")
    #     else:
    #         assert False
    #         self.logger.info("********** Total Number of companies trusting Negative Test failed *********")
    #
    #     # Summary
    #     error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/form/p[6]")
    #     result = error_msg2[0].text
    #     if result == "Summary is required.":
    #        self.logger.info("Error Message Is: %s", result)
    #        assert True
    #        self.logger.info("********** Summary Negative Test passed *********")
    #     else:
    #         assert False
    #         self.logger.info("********** Summary Negative Test failed *********")
    #
    #
    #
    #     # Address1
    #     error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/form/p[7]")
    #     result = error_msg2[0].text
    #     if result == "Address Line 1 is required.":
    #        self.logger.info("Error Message Is: %s", result)
    #        assert True
    #        self.logger.info("********** Address Line 1 Negative Test passed *********")
    #     else:
    #        assert False
    #        self.logger.info("********** Address Line 1 Negative Test failed *********")
    #
    #
    #
    #     # Address2
    #     error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/form/p[8]")
    #     result = error_msg2[0].text
    #     if result == "Address Line 2 is required.":
    #        self.logger.info("Error Message Is: %s", result)
    #        assert True
    #        self.logger.info("********** Address Line 2 Negative Test passed *********")
    #     else:
    #        assert False
    #        self.logger.info("********** Address Line 2 Negative Test failed *********")
    #
    #
    #
    #     # City
    #     error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/form/div[11]/div[1]/p")
    #     result = error_msg2[0].text
    #     if result == "City is required.":
    #        self.logger.info("Error Message Is: %s", result)
    #        assert True
    #        self.logger.info("********** City Negative Test passed *********")
    #     else:
    #        assert False
    #        self.logger.info("********** City Negative Test failed *********")
    #
    #
    #     # State
    #     error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/form/div[11]/div[2]/p")
    #     result = error_msg2[0].text
    #     if result == "state is required.":
    #        self.logger.info("Error Message Is: %s", result)
    #        assert True
    #        self.logger.info("********** State Negative Test Test passed *********")
    #     else:
    #        assert False
    #        self.logger.info("********** State Negative Test failed *********")
    #
    #
    #     # Country
    #     error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/form/div[11]/div[3]/p")
    #     result = error_msg2[0].text
    #     if result == "Country is required.":
    #        self.logger.info("Error Message Is: %s", result)
    #        assert True
    #        self.logger.info("********** Country Negative Test passed *********")
    #     else:
    #        assert False
    #        self.logger.info("********** Country Negative Test failed *********")
    #
    #     # Pincode
    #     error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/form/div[11]/div[4]/p")
    #     result = error_msg[0].text
    #     if result == "Pincode is required.":
    #        self.logger.info("Error Message Is: %s", result)
    #        assert True
    #        self.logger.info("********** Pincode Negative Test passed *********")
    #     else:
    #        assert False
    #        self.logger.info("********** Pincode Negative Test failed *********")
    #
    #
    #     time.sleep(2)
    #     self.logger.info("*************** Edit Businesscard Negative Test Completed Successfully *************")
    #     self.driver.quit()

    def test_Editbusinesscardnegative2(self, setup):
        self.logger.info("*************** Test_Businesscard *************")
        self.logger.info("************** Edit Businesscard  Negative Test 2 *************")
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
        self.cp.clickEditbusinesscard()
        time.sleep(3)
        self.cp.invalidTagline()
        time.sleep(1)
        self.cp.invalidFoundedyear()
        time.sleep(1)
        self.cp.invalidNoofstudents()
        time.sleep(1)
        self.cp.invalidNoofcourses()
        time.sleep(1)
        self.cp.invalidNoofcompaniestrusting()
        time.sleep(1)
        self.cp.invalidSummary()
        time.sleep(1)
        self.cp.invalidAddress1()
        time.sleep(1)
        self.cp.invalidAddress2()
        time.sleep(1)
        self.cp.invalidCity()
        time.sleep(1)
        self.cp.invalidState()
        time.sleep(1)
        self.cp.invalidCountry()
        time.sleep(1)
        self.cp.clickSavebusinesscard()
        time.sleep(2)

        #Tagline
        error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/form/p[1]")
        result = error_msg[0].text
        if result == "Invalid Tagline":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("********** TagLine Negative Test passed *********")
        else:
            assert False
            self.logger.info("********** TagLine Negative Test failed *********")

        #Founded Year
        error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/form/p[2]")
        result = error_msg1[0].text
        if result == "Invalid Year.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("********** Founded Year Negative Test passed *********")
        else:
            assert False
            self.logger.info("********** Founded Year Negative Test failed *********")

        #No.Of.Students
        error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/form/p[3]")
        result = error_msg2[0].text
        print(result)
        if result == "Invalid format. Only numbers are allowed.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("********** Total Number of students Negative Test passed *********")
        else:
            assert False
            self.logger.info("********** Total Number of students Negative Test failed *********")


        #Total No.of Courses
        error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/form/p[4]")
        result = error_msg2[0].text

        if result == "Invalid format. Only numbers are allowed.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("********** Total Number of Courses Negative Test passed *********")
        else:
            assert False
            self.logger.info("********** Total Number of Courses Negative Test failed *********")

        #No.of Companies Trusting us
        error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/form/p[5]")
        result = error_msg1[0].text
        if result == "Only Numbers are allowed.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("********** Total Number of companies trusting Negative Test passed *********")
        else:
            assert False
            self.logger.info("********** Total Number of companies trusting Negative Test failed *********")

        # Summary
        error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/form/p[6]")
        result = error_msg2[0].text
        if result == "Summary should not be blank.":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("********** Summary Negative Test passed *********")
        else:
            assert False
            self.logger.info("********** Summary Negative Test failed *********")



        # Address1
        error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/form/p[7]")
        result = error_msg2[0].text
        if result == "Invalid Address Line 1.":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("********** Address Line 1 Negative Test passed *********")
        else:
           assert False
           self.logger.info("********** Address Line 1 Negative Test failed *********")



        # Address2
        error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/form/p[8]")
        result = error_msg2[0].text
        if result == "Invalid Address Line 2.":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("********** Address Line 2 Negative Test passed *********")
        else:
           assert False
           self.logger.info("********** Address Line 2 Negative Test failed *********")



        # City
        error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/form/div[11]/div[1]/p")
        result = error_msg2[0].text
        if result == "Invalid City.":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("********** City Negative Test passed *********")
        else:
           assert False
           self.logger.info("********** City Negative Test failed *********")


        # State
        error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/form/div[11]/div[2]/p")
        result = error_msg2[0].text
        if result == "Invalid State.":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("********** State Negative Test Test passed *********")
        else:
           assert False
           self.logger.info("********** State Negative Test failed *********")


        # Country
        error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/form/div[11]/div[3]/p")
        result = error_msg2[0].text
        if result == "Invalid Country.":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("********** Country Negative Test passed *********")
        else:
           assert False
           self.logger.info("********** Country Negative Test failed *********")



        time.sleep(3)
        self.cp.invalidPincode()
        time.sleep(2)

        # Pincode
        error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/form/div[11]/div[4]/p")
        result = error_msg[0].text
        if result == "Invalid Pincode.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("********** Pincode Negative Test passed *********")
        else:
            assert False
            self.logger.info("********** Pincode Negative Test failed *********")

        time.sleep(2)
        self.cp.numberState()
        time.sleep(2)
        self.cp.numberCountry()
        time.sleep(2)

        # State
        error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/form/div[11]/div[2]/p")
        result = error_msg2[0].text
        if result == "State should contain only alphabets.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("********** State Negative Test Test passed *********")
        else:
            assert False
            self.logger.info("********** State Negative Test failed *********")

        # Country
        error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div[3]/div/div/form/div[11]/div[3]/p")
        result = error_msg2[0].text
        if result == "Country should contain only alphabets.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("********** Country Negative Test passed *********")
        else:
            assert False
            self.logger.info("********** Country Negative Test failed *********")

        self.logger.info("*************** Edit Businesscard Negative Test Completed Successfully *************")
        self.driver.quit()




