import time

import pytest
import self
from selenium.webdriver.common.by import By
from pageObjects.ProfessionalSignup import Signupprofessional
from pageObjects.loginpage import Login
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen
import configparser

config = configparser.ConfigParser()
config.read('C:\\Users\\user\\PycharmProjects\\python framework\\configurations\\config.ini')

class Test_Signupindividual:
    baseurl = ReadConfig.getApplicationURL()
    signupemail = ReadConfig.getemail()
    signuppassword = ReadConfig.getpassword()
    signupconfirmpassword = ReadConfig.getconfirmpassword()
    firstname = ReadConfig.getfirstname()
    lastname = ReadConfig.getlastname()
    mobile = ReadConfig.getmobile()





    logger = LogGen.loggen()

    #@pytest.mark.sanity
    def test_SignupPosNeg(self, setup):#Signup to the professional account type and Without enter otp,invalid otp negative test
        self.logger.info("*************** SignUp Test *************")
        self.logger.info("************** Signup professional positive test *************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.sp = Signupprofessional(self.driver)
        time.sleep(3)
        self.sp.clickRegister()
        time.sleep(3)
        self.sp.clickIndividual()
        time.sleep(3)
        self.sp.clickChoosecategory()
        time.sleep(3)
        self.sp.clickProfessional()
        time.sleep(3)
        self.sp.clickArrow1()
        time.sleep(3)
        self.sp.typeEmail(self.signupemail)
        time.sleep(3)
        self.sp.typePassword(self.signuppassword)
        time.sleep(3)
        self.sp.typeConfirmpassword(self.signupconfirmpassword)
        time.sleep(3)
        self.sp.clickArrow2()
        time.sleep(3)
        self.sp.typeFirstname(self.firstname)
        time.sleep(3)
        self.sp.typeLastname(self.lastname)
        time.sleep(5)
        self.sp.typeMobile(self.mobile)
        time.sleep(3)
        self.sp.clickAgreejoin()
        time.sleep(3)
        self.sp.clickVerifyjoin()
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

        time.sleep(10)
        self.sp.clickVerifyjoin()
        time.sleep(1)

        error_msg = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]")
        result = error_msg[0].text
        if result == "Invalid OTP":
            self.logger.info("Toast Message Is: %s", result)
            assert True
            self.logger.info("*************** Signup Professional test passed successfully *************")
        else:
            assert False
            self.logger.info("*************** Signup Professional test failed *************")

        time.sleep(20)
        self.sp.clickVerifyjoin()
        time.sleep(2)

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
            assert True
            self.logger.info("*************** Sign UP Professional Positive Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Sign UP Professional Positive Test Failed *************")

        self.logger.info("************** Signup Professional Positive Test Passed *************")
        self.driver.quit()


    #@pytest.mark.sanity
    def test_Signupnegative1(self, setup):#Email & Password & Confirm password is required for the signup
        self.logger.info("*************** SignUp Test *************")
        self.logger.info("************** Signup negative 1 test *************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.sp = Signupprofessional(self.driver)
        time.sleep(3)
        self.sp.clickRegister()
        time.sleep(3)
        self.sp.clickIndividual()
        time.sleep(3)
        self.sp.clickChoosecategory()
        time.sleep(3)
        self.sp.clickProfessional()
        time.sleep(3)
        self.sp.clickArrow1()
        time.sleep(3)
        self.sp.clickArrow2()
        time.sleep(3)


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
    def test_Signupnegative2(self, setup):#Email & Password is too length for the signup
        self.logger.info("*************** SignUp Test *************")
        self.logger.info("************** Signup negative 2 test *************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.sp = Signupprofessional(self.driver)
        time.sleep(3)
        self.sp.clickRegister()
        time.sleep(3)
        self.sp.clickIndividual()
        time.sleep(3)
        self.sp.clickChoosecategory()
        time.sleep(3)
        self.sp.clickProfessional()
        time.sleep(3)
        self.sp.clickArrow1()
        time.sleep(3)
        self.sp.clickArrow2()
        time.sleep(3)
        self.sp.typeLenemail()
        time.sleep(3)
        self.sp.typeLenpassword()
        time.sleep(3)
        self.sp.typeConfirmpassincorrect()
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
    def test_Signupnegative3(self, setup):#Email & Password is too short for the signup
        self.logger.info("*************** SignUp Test *************")
        self.logger.info("************** Signup negative 3 test *************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.sp = Signupprofessional(self.driver)
        time.sleep(3)
        self.sp.clickRegister()
        time.sleep(3)
        self.sp.clickIndividual()
        time.sleep(3)
        self.sp.clickChoosecategory()
        time.sleep(3)
        self.sp.clickProfessional()
        time.sleep(3)
        self.sp.clickArrow1()
        time.sleep(3)
        self.sp.clickArrow2()
        time.sleep(3)
        self.sp.typeShortemail()
        time.sleep(3)
        self.sp.typeShortpassword()
        time.sleep(3)


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
        # self.sp.typeWithoutEmail()
        # time.sleep(3)
        self.sp.typeWithoutPassword()
        time.sleep(2)

        # error_msg1 = self.driver.find_elements(By.XPATH,  "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[2]/section/form/div[1]/p")
        # result = error_msg1[0].text
        # if result == "Invalid email":
        #     self.logger.info("Error Message Is: %s", result)
        #     assert True
        #     self.logger.info("*************** Invalid Email test passed successfully *************")
        # else:
        #     assert False
        #     self.logger.info("*************** Invalid Email test failed *************")

        error_msg4 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[2]/section/form/div[2]/p")
        result = error_msg4[0].text
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
    def test_Signupprofessionalnegative4(self, setup): #already existing user email using signup
        self.logger.info("*************** SignUp Test *************")
        self.logger.info("************** Signup professional Negative test 4  *************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.sp = Signupprofessional(self.driver)
        time.sleep(3)
        self.sp.clickRegister()
        time.sleep(3)
        self.sp.clickIndividual()
        time.sleep(3)
        self.sp.clickChoosecategory()
        time.sleep(3)
        self.sp.clickProfessional()
        time.sleep(3)
        self.sp.clickArrow1()
        time.sleep(3)
        self.sp.typeEmail(self.signupemail)
        time.sleep(3)
        self.sp.typePassword(self.signuppassword)
        time.sleep(3)
        self.sp.typeConfirmpassword(self.signupconfirmpassword)
        time.sleep(3)
        self.sp.clickArrow2()
        time.sleep(3)
        self.sp.typeFirstname(self.firstname)
        time.sleep(3)
        self.sp.typeLastname(self.lastname)
        time.sleep(5)
        self.sp.typeMobile(self.mobile)
        time.sleep(3)
        self.sp.clickAgreejoin()
        time.sleep(2)

        error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]")
        result = error_msg1[0].text
        if result == "User with the same Email or mobile number already exist.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Existing Email Negative Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Existing Email Negative Test Failed *************")

        self.logger.info("************** Signup professional Negative test 4  *************")
        self.driver.quit()

    #@pytest.mark.sanity
    def test_Signupprofessionalnegative5(self, setup): #Signup second page(Firstname,Lastname,Mobile) is required
        self.logger.info("*************** SignUp Test *************")
        self.logger.info("************** Signup professional Negative test 5  *************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.l = Login(self.driver)
        self.sp = Signupprofessional(self.driver)
        time.sleep(3)
        self.sp.clickRegister()
        time.sleep(3)
        self.sp.clickIndividual()
        time.sleep(3)
        self.sp.clickChoosecategory()
        time.sleep(3)
        self.sp.clickProfessional()
        time.sleep(3)
        self.sp.clickArrow1()
        time.sleep(3)
        self.sp.typeEmail(self.signupemail)
        time.sleep(3)
        self.sp.typePassword(self.signuppassword)
        time.sleep(3)
        self.sp.typeConfirmpassword(self.signupconfirmpassword)
        time.sleep(3)
        self.sp.clickArrow2()
        time.sleep(3)
        self.sp.clickAgreejoin()

        error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[3]/section/main/form/div[1]/p")
        result = error_msg1[0].text
        if result == "Your first name is required":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("*************** Firstname is required Test Passed *************")
        else:
           assert False
           self.logger.info("*************** Firstname is required Test Failed *************")

        error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[3]/section/main/form/div[2]/p")
        result = error_msg2[0].text
        if result == "Your last name is required":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("*************** Lastname is required Test Passed *************")
        else:
           assert False
           self.logger.info("*************** Lastname is required Test Failed *************")

        error_msg3 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[3]/section/main/form/div[3]/p")
        result = error_msg3[0].text
        if result == "Mobile number is required":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("*************** Mobile Number is required Test Passed *************")
        else:
           assert False
           self.logger.info("*************** Mobile Number is required Test Failed *************")

        #Only alphabets are allowed in the Firstname & Lastname

        time.sleep(3)
        self.sp.typeFnnegative1()
        time.sleep(3)
        self.sp.typeLnnegative1()
        time.sleep(3)


        error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[3]/section/main/form/div[1]/p")
        result = error_msg1[0].text
        if result == "Only alphabets & spaces are allowed.":
            self.logger.info("Error Message Is: %s", result)
            assert True
            self.logger.info("*************** Firstname is only alphabets Test Passed *************")
        else:
            assert False
            self.logger.info("*************** Firstname is only alphabets Test Failed *************")

        error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[3]/section/main/form/div[2]/p")
        result = error_msg2[0].text
        if result == "Only alphabets & spaces are allowed.":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("*************** Lastname is only alphabets Test Passed *************")
        else:
           assert False
           self.logger.info("*************** Lastname is only alphabets Test Failed *************")

        #Invalid Firstname & Lastname

        time.sleep(3)
        self.sp.typeWithoutFirstname()
        time.sleep(3)
        self.sp.typeWithoutlastname()
        time.sleep(3)


        error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[3]/section/main/form/div[1]/p")
        result = error_msg1[0].text
        if result == "Invalid Firstname.":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("*************** Firstname is Invalid Test Passed *************")
        else:
           assert False
           self.logger.info("*************** Firstname is Invalid Test Failed *************")

        error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[3]/section/main/form/div[2]/p")
        result = error_msg2[0].text
        if result == "Invalid Lastname.":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("*************** Lastname is Invalid Test Passed *************")
        else:
           assert False
           self.logger.info("*************** Lastname is Invalid Test Failed *************")

        #Firstname & Lastname should be accept only 100 characters
        time.sleep(3)
        self.sp.typeFnnegative3()
        time.sleep(3)
        self.sp.typeLnnegative3()
        time.sleep(2)


        error_msg1 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[3]/section/main/form/div[1]/p")
        result = error_msg1[0].text
        if result == "Name should not exceed 20 letters.":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("*************** Firstname is only accept 100 Characters Test Passed *************")
        else:
           assert False
           self.logger.info("*************** Firstname is only accept 100 Characters Test Failed *************")

        error_msg2 = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[3]/section/main/form/div[2]/p")
        result = error_msg2[0].text
        if result == "Last Name should not exceed 20 letters.":
           self.logger.info("Error Message Is: %s", result)
           assert True
           self.logger.info("*************** Lastname is only accept 100 Characters Test Passed *************")
        else:
           assert False
           self.logger.info("*************** Lastname is only accept 100 Characters Test Failed *************")

        self.logger.info("************** Signup professional Negative test 5 Passed Successfully *************")
        self.driver.quit()

























