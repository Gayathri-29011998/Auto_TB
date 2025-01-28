import time

import pytest
import self
from selenium.webdriver.common.by import By

from pageObjects.InstituteSignup import Signupinstitute
from pageObjects.ProfessionalSignup import Signupprofessional
from pageObjects.loginpage import Login
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen
import configparser

config = configparser.ConfigParser()
config.read('C:\\Users\\user\\PycharmProjects\\python framework\\configurations\\config.ini')

class Test_Signupcollege:
    baseurl = ReadConfig.getApplicationURL()
    signupemail = ReadConfig.getemail()
    signuppassword = ReadConfig.getpassword()
    signupconfirmpassword = ReadConfig.getconfirmpassword()
    mobile = ReadConfig.getmobile()
    collegename = ReadConfig.getcollegename()
    registername = ReadConfig.getregistername()
    website = ReadConfig.getwebsite()


    logger = LogGen.loggen()

    # @pytest.mark.sanity
    def test_Signupcollegepositive(self, setup):
        self.logger.info("*************** SignUp Test *************")
        self.logger.info("************** Signup College Positive Test   *************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.si = Signupinstitute(self.driver)
        self.sp = Signupprofessional(self.driver)
        time.sleep(3)
        self.sp.clickRegister()
        time.sleep(3)
        self.si.clickInstitute()
        time.sleep(3)
        self.si.clickChoosecategory()
        time.sleep(3)
        self.si.clickCollege()
        time.sleep(3)
        self.si.clickArrow1()
        time.sleep(3)
        self.si.typeEmail(self.signupemail)
        time.sleep(3)
        self.si.typePassword(self.signuppassword)
        time.sleep(3)
        self.si.typeConfirmpassword(self.signupconfirmpassword)
        time.sleep(3)
        self.si.clickArrow2()
        time.sleep(3)
        self.si.typeCollegename(self.collegename)
        time.sleep(2)
        self.si.typeRegistername(self.registername)
        time.sleep(3)
        self.si.typeMobile(self.mobile)
        time.sleep(2)
        self.si.typeWebsite(self.website)
        time.sleep(3)
        self.si.clickAgreejoin()
        time.sleep(3)
        self.si.clickVerifyjoin()
        time.sleep(1)

        error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = error_msg[0].text
        if result == "Please enter OTP.":
            self.logger.info("Toast Message Is: %s", result)
            assert True
            self.logger.info("*************** Signup test passed successfully *************")
        else:
            assert False
            self.logger.info("*************** Signup test failed *************")

        time.sleep(15)
        self.si.clickVerifyjoin()
        time.sleep(1)

        error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = error_msg[0].text
        if result == "Invalid OTP":
            self.logger.info("Toast Message Is: %s", result)
            assert True
            self.logger.info("*************** Signup test passed successfully *************")
        else:
            assert False
            self.logger.info("*************** Signup test failed *************")

        time.sleep(20)
        self.si.clickVerifyjoin()
        time.sleep(3)

        # toast_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div")
        # result = toast_msg[0].text
        # if result == "":
        #     self.logger.info("Toast Message Is: %s", result)
        #     assert True
        #     self.logger.info("*************** Signup test passed successfully *************")
        # else:
        #     assert False
        #     self.logger.info("*************** Signup test failed *************")

        act_url = self.driver.current_url
        if act_url == "https://www.tickbig.com/signin":
            self.logger.info("Act_url: %s", act_url)
            # self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_login.png")
            # print("Screenshot saved.")
            assert True
            self.logger.info("*************** Sign UP Positive Test Passed *************")
        else:
            assert False

        self.logger.info("************** Signup College Positive Test Passed *************")
        self.driver.quit()

    #@pytest.mark.sanity
    def test_Signupcollegenegative1(self, setup):  # Signup first page(email,password) is required
        self.logger.info("*************** SignUp Test *************")
        self.logger.info("************** Signup College Negative Test 1  *************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.si = Signupinstitute(self.driver)
        self.sp = Signupprofessional(self.driver)
        time.sleep(3)
        self.sp.clickRegister()
        time.sleep(3)
        self.si.clickInstitute()
        time.sleep(3)
        self.si.clickChoosecategory()
        time.sleep(3)
        self.si.clickCollege()
        time.sleep(3)
        self.si.clickArrow1()
        time.sleep(3)
        self.si.clickArrow2()
        self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_signupcollegenegative2.png")
        time.sleep(2)

        error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[2]/section/form/div[1]/p")
        result = error_msg1[0].text
        if result == "email is required":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("*************** Email is required test passed successfully *************")
        else:
           assert False
           self.logger.info("*************** Email is required test failed *************")

        error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[2]/section/form/div[2]/p")
        result = error_msg2[0].text
        if result == "Password is required":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("*************** Password is required test passed successfully *************")
        else:
           assert False
           self.logger.info("*************** Password is required test failed *************")

        error_msg3 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[2]/section/form/div[3]/p")
        result = error_msg3[0].text
        if result == "Confirm Password is required":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("*************** Confirm Password is required test passed successfully *************")
        else:
           assert False
           self.logger.info("*************** Confirm Password is required test failed *************")

        self.logger.info("************** Signup negative 1 test passed *************")
        self.driver.quit()

    #@pytest.mark.sanity
    def test_Signupcollegenegative2(self, setup):  # Signup first page(email,password) is too length
        self.logger.info("*************** SignUp Test *************")
        self.logger.info("************** Signup College Negative Test 2  *************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.si = Signupinstitute(self.driver)
        self.sp = Signupprofessional(self.driver)
        time.sleep(3)
        self.sp.clickRegister()
        time.sleep(3)
        self.si.clickInstitute()
        time.sleep(3)
        self.si.clickChoosecategory()
        time.sleep(3)
        self.si.clickCollege()
        time.sleep(3)
        self.si.clickArrow1()
        time.sleep(3)
        self.si.clickArrow2()
        time.sleep(3)
        self.si.typeLenemail()
        time.sleep(3)
        self.si.typeLenpassword()
        time.sleep(3)
        self.si.typeConfirmpassincorrect()
        time.sleep(2)

        error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[2]/section/form/div[1]/p")
        result = error_msg1[0].text
        if result == "Email Id should not be more than 128 characters.":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("*************** Email length test passed successfully *************")
        else:
           assert False
           self.logger.info("*************** Email length test failed *************")

        error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[2]/section/form/div[2]/p")
        result = error_msg2[0].text
        if result == "Password length should not exceed 128 characters":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Password length test passed successfully *************")
        else:
            assert False
            self.logger.info("*************** Password length test failed *************")

        error_msg3 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[2]/section/form/div[3]/p")
        result = error_msg3[0].text
        if result == "The passwords don't match.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Incorrect confirm password  test passed successfully *************")
        else:
            assert False
            self.logger.info("*************** Incorrect confirm password test failed *************")

        self.logger.info("************** Successfully Signup negative 2 test Passed *************")
        self.driver.quit()

    #@pytest.mark.sanity
    def test_Signupcollegenegative3(self, setup):  # Signup first page(email,password) is too Short & Invalid Email,Password combination Test
        self.logger.info("*************** SignUp Test *************")
        self.logger.info("************** Signup College Negative Test 3  *************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.si = Signupinstitute(self.driver)
        self.sp = Signupprofessional(self.driver)
        time.sleep(3)
        self.sp.clickRegister()
        time.sleep(3)
        self.si.clickInstitute()
        time.sleep(3)
        self.si.clickChoosecategory()
        time.sleep(3)
        self.si.clickCollege()
        time.sleep(3)
        self.si.clickArrow1()
        time.sleep(3)
        self.si.clickArrow2()
        time.sleep(3)
        self.si.typeShortemail()
        time.sleep(3)
        self.si.typeShortpassword()
        time.sleep(3)
        self.si.typeConfirmpassincorrect()
        time.sleep(3)
        self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_sigupnegative3.png")


        error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[2]/section/form/div[1]/p")
        result = error_msg1[0].text
        if result == "Email Id is very short.":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("*************** Email is too short test passed successfully *************")
        else:
           assert False
           self.logger.info("*************** Email is too short test failed *************")

        error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[2]/section/form/div[2]/p")
        result = error_msg2[0].text
        if result == "Password is too short.":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("*************** Password is too short test passed successfully *************")
        else:
           assert False
           self.logger.info("*************** password is too short test failed *************")
           time.sleep(3)

        self.si.invalidEmail()
        time.sleep(6)
        self.si.invalidPassword()
        time.sleep(5)

        error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[2]/section/form/div[1]/p")
        result = error_msg1[0].text
        if result == "Invalid email":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("*************** Invalid Email test passed successfully *************")
        else:
           assert False
           self.logger.info("*************** Invalid Email test failed *************")

        error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[2]/section/form/div[2]/p")
        result = error_msg2[0].text
        if result == "Use 8 or more characters with a mix of letters, numbers, space & symbols":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("*************** Password is mixed & 8 more characters test passed successfully *************")
        else:
           assert False
           self.logger.info("*************** Password is mixed & 8 more characters test failed *************")


        self.logger.info("************** Successfully Signup negative 3 test Passed *************")
        self.driver.quit()

    #@pytest.mark.sanity
    def test_Signupcollegenegative4(self, setup): #Signup second page(Collegename,Registeredname,Mobile,Website) is required
        self.logger.info("*************** SignUp Test *************")
        self.logger.info("************** Signup College Negative Test 4  *************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.si = Signupinstitute(self.driver)
        self.sp = Signupprofessional(self.driver)
        time.sleep(3)
        self.sp.clickRegister()
        time.sleep(3)
        self.si.clickInstitute()
        time.sleep(3)
        self.si.clickChoosecategory()
        time.sleep(3)
        self.si.clickCollege()
        time.sleep(3)
        self.si.clickArrow1()
        time.sleep(3)
        self.si.typeEmail(self.signupemail)
        time.sleep(3)
        self.si.typePassword(self.signuppassword)
        time.sleep(3)
        self.si.typeConfirmpassword(self.signupconfirmpassword)
        time.sleep(3)
        self.si.clickArrow2()
        time.sleep(3)
        self.si.clickAgreejoin()
        self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_signupcollegenegative2.png")
        time.sleep(3)

        error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[3]/section/main/form/div[1]/p")
        result = error_msg1[0].text
        if result == "Your college name is required":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** College name is required Test Passed *************")
        else:
            assert False
            self.logger.info("*************** College name is required Test Failed *************")

        error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[3]/section/main/form/div[2]/p")
        result = error_msg2[0].text
        if result == "College registered name is required":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Registered name  is required Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Registered name is required Test Failed *************")

        error_msg3 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[3]/section/main/form/div[3]/p")
        result = error_msg3[0].text
        if result == "Mobile number is required":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Mobile Number is required Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Mobile Number is required Test Failed *************")

        error_msg4 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[3]/section/main/form/div[5]/p")
        result = error_msg4[0].text
        if result == "Your website is required":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Website is required Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Website is required Test Failed *************")

        self.logger.info("**************  Signup College Negative Test 4 Successfully Passed  *************")
        self.driver.quit()

    #@pytest.mark.sanity
    def test_Signupnegative5(self, setup):  # input combinations,invalid inputs negative test for (collegename,registername)
        self.logger.info("*************** SignUp Test *************")
        self.logger.info("************** Signup professional Negative test 6  *************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.si = Signupinstitute(self.driver)
        self.sp = Signupprofessional(self.driver)
        time.sleep(3)
        self.si.clickRegister()
        time.sleep(3)
        self.si.clickInstitute()
        time.sleep(3)
        self.si.clickChoosecategory()
        time.sleep(3)
        self.si.clickCollege()
        time.sleep(3)
        self.si.clickArrow1()
        time.sleep(3)
        self.si.typeEmail(self.signupemail)
        time.sleep(3)
        self.si.typePassword(self.signuppassword)
        time.sleep(3)
        self.si.typeConfirmpassword(self.signupconfirmpassword)
        time.sleep(3)
        self.si.clickArrow2()
        time.sleep(3)
        self.si.typeWithoutcollegename()  # We run the testcase collegename input fields displayed when manually enter the empty space
        time.sleep(3)
        self.si.typeWithoutregistername() # We run the testcase registername input fields displayed when manually enter the empty space
        time.sleep(3)
        self.si.clickAgreejoin()
        time.sleep(2)

        error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div/div[2]/section/main/div/div/section[2]/section[3]/section/main/form/div[1]/p")
        result = error_msg1[0].text
        if result == "Invalid College Name.":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("*************** College name is Invalid Test Passed *************")
        else:
           assert False
           self.logger.info("*************** College name is Invalid Test Failed *************")

        error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div/div[2]/section/main/div/div/section[2]/section[3]/section/main/form/div[2]/p")
        result = error_msg2[0].text
        if result == "Invalid Registered Name.":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("*************** Register name is Invalid Test Passed *************")
        else:
           assert False
           self.logger.info("*************** Register name is Invalid Test Failed *************")

        time.sleep(3)
        self.si.typeNumbercollegename()   # We run the testcase collegename input fields displayed when manually enter the only Numbers (or) only Special characters
        time.sleep(3)
        self.si.typeNumberregistername()  # We run the testcase registername input fields displayed when manually enter the only Numbers (or) only Special characters
        time.sleep(3)
        self.si.clickAgreejoin()
        time.sleep(2)

        error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[3]/section/main/form/div[1]/p")
        result = error_msg1[0].text
        if result == "Only alphabets & spaces are allowed.":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("*************** College name Combinations Test Passed *************")
        else:
           assert False
           self.logger.info("*************** College name Combinations Test Failed *************")

        error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[3]/section/main/form/div[2]/p")
        result = error_msg2[0].text
        if result == "Only alphabets & spaces are allowed.":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("*************** Register name Combinations Test Passed *************")
        else:
           assert False
           self.logger.info("*************** Register name Combinations Test Failed *************")


        self.logger.info("************** Successfully Signup College Negative 6 test Passed *************")
        self.driver.quit()

    #@pytest.mark.sanity
    def test_Signupnegative6(self, setup):  # already existing user email using signup
        self.logger.info("*************** SignUp Test *************")
        self.logger.info("************** Signup professional Negative test 4  *************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.si = Signupinstitute(self.driver)
        self.sp = Signupprofessional(self.driver)
        time.sleep(3)
        self.sp.clickRegister()
        time.sleep(3)
        self.si.clickInstitute()
        time.sleep(3)
        self.si.clickChoosecategory()
        time.sleep(3)
        self.si.clickCollege()
        time.sleep(3)
        self.si.clickArrow1()
        time.sleep(3)
        self.si.typeEmail(self.signupemail)
        time.sleep(3)
        self.si.typePassword(self.signuppassword)
        time.sleep(3)
        self.si.typeConfirmpassword(self.signupconfirmpassword)
        time.sleep(3)
        self.si.clickArrow2()
        time.sleep(3)
        self.si.typeCollegename(self.collegename)
        time.sleep(3)
        self.si.typeRegistername(self.registername)
        time.sleep(5)
        self.si.typeMobile(self.mobile)
        time.sleep(3)
        self.si.typeWebsite(self.website)
        time.sleep(3)
        self.si.clickAgreejoin()
        time.sleep(1)

        error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = error_msg1[0].text
        if result == "User with the same Email or mobile number already exist.":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("*************** Existing Email Negative Test Passed *************")
        else:
           assert False
           self.logger.info("*************** Existing Email Negative Test Failed *************")

        self.logger.info("************** Signup professional Negative test 6  *************")
        self.driver.quit()











