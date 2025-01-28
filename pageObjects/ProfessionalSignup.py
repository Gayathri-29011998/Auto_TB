import time
from telnetlib import EC

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.customLogger import LogGen

class Signupprofessional:

    logger = LogGen.loggen()

    btn_register_xpath = "/html/body/div[1]/div[2]/div/div[2]/a[1]"
    box_individual_xpath = "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[1]/div[2]/button[1]"
    input_choosecategory_xpath = "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[1]/div[3]/div"
    txt_professional_xpath = "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[1]/div[3]/div[2]/div[1]"
    btn_arrow1_xpath = "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[1]/div[4]/button"
    input_email_xpath = "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[2]/section/form/div[1]/input"
    input_password_xpath = "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[2]/section/form/div[2]/input"
    input_confirmpassword_xpath = "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[2]/section/form/div[3]/input"
    btn_arrow2_xpath = "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[2]/section/form/div[5]/button"
    input_firstname_xpath = "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[3]/section/main/form/div[1]/input"
    input_lastname_xpath = "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[3]/section/main/form/div[2]/input"
    input_mobile_xpath = "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[3]/section/main/form/div[3]/div/input"
    input_enabledemail_xpath = "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[3]/section/main/form/div[4]/input"
    btn_agreejoin_xpath = "//button[text()= 'Agree & Join']"
    btn_verifyjoin_xpath = "/html/body/div[1]/section[2]/section/form/div[2]/button"

    def __init__(self, driver):
        self.driver = driver

    def clickRegister(self):
        self.driver.find_element(By.XPATH, self.btn_register_xpath).click()

    def clickIndividual(self):
        self.driver.find_element(By.XPATH, self.box_individual_xpath).click()

    def clickChoosecategory(self):
        self.driver.find_element(By.XPATH, self.input_choosecategory_xpath).click()

    def clickProfessional(self):
        self.driver.find_element(By.XPATH, self.txt_professional_xpath).click()

    def clickArrow1(self):
        self.driver.find_element(By.XPATH, self.btn_arrow1_xpath).click()

    def typeEmail(self, signupemail):
        input1=self.driver.find_element(By.XPATH, self.input_email_xpath).is_displayed()
        self.logger.info("Is Displayed %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_email_xpath).is_enabled()
        self.logger.info("Is Enabled %s", input2)
        self.driver.find_element(By.XPATH, self.input_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_email_xpath).send_keys(signupemail)

    def typePassword(self, signuppassword):
        input1=self.driver.find_element(By.XPATH, self.input_password_xpath).is_displayed()
        self.logger.info("Is Displayed %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_password_xpath).is_enabled()
        self.logger.info("Is Enabled %s", input2)
        self.driver.find_element(By.XPATH, self.input_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_password_xpath).send_keys(signuppassword)

    def typeConfirmpassword(self, signupconfirmpassword):
        input1=self.driver.find_element(By.XPATH, self.input_confirmpassword_xpath).is_displayed()
        self.logger.info("Is Displayed %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_confirmpassword_xpath).is_enabled()
        self.logger.info("Is Enabled %s", input2)
        self.driver.find_element(By.XPATH, self.input_confirmpassword_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_confirmpassword_xpath).send_keys(signupconfirmpassword)

    def clickArrow2(self):
        self.driver.find_element(By.XPATH, self.btn_arrow2_xpath).click()

    def typeFirstname(self, firstname):
        input1=self.driver.find_element(By.XPATH, self.input_firstname_xpath).is_displayed()
        self.logger.info("Is Displayed %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_firstname_xpath).is_enabled()
        self.logger.info("Is Enabled %s", input2)
        self.driver.find_element(By.XPATH, self.input_firstname_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_firstname_xpath).send_keys(firstname)

    def typeLastname(self, lastname):
        input1=self.driver.find_element(By.XPATH, self.input_lastname_xpath).is_displayed()
        self.logger.info("Is Displayed %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_lastname_xpath).is_enabled()
        self.logger.info("Is Enabled %s", input2)
        self.driver.find_element(By.XPATH, self.input_lastname_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_lastname_xpath).send_keys(lastname)

    def typeMobile(self, mobile):
        input1=self.driver.find_element(By.XPATH, self.input_mobile_xpath).is_displayed()
        self.logger.info("Is Displayed %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_mobile_xpath).is_enabled()
        self.logger.info("Is Enabled %s", input2)
        self.driver.find_element(By.XPATH, self.input_mobile_xpath).click()
        self.driver.find_element(By.XPATH, self.input_mobile_xpath).send_keys(mobile)


    def clickAgreejoin(self):
        self.driver.find_element(By.XPATH, self.btn_agreejoin_xpath).click()

    def clickVerifyjoin(self):
        self.driver.find_element(By.XPATH, self.btn_verifyjoin_xpath).click()

    #signup negative test (more than 128 characters in the email and password) (email and password is too short)
    def typeLenemail(self):
        self.driver.find_element(By.XPATH, self.input_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_email_xpath).send_keys("sdhfbhgfgfshhcbhcvgcvgv@yvdvscsshfsgygygygycuncfcgddff.ffdvcfyvfbgfbeycgfbfgfgfurgfuegcenejfhxeifuerfgeybcehgfuegyxnsxnbbshgfdygfyrgrfu")

    def typeLenpassword(self):
        self.driver.find_element(By.XPATH, self.input_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_password_xpath).send_keys("dxdcscsds214254@@@@@@@@@@@@@@@22dhschvcgdvgcvgcvdhcshdhbdsnjsbjchsbchbgyrfgrpofrihnucgyvcgvgsvhxsvchschsbsbycbb gygyfcgdvgsdvvvvvvvvvvvvvvvvvvv")

    def typeConfirmpassincorrect(self):
        self.driver.find_element(By.XPATH, self.input_confirmpassword_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_confirmpassword_xpath).send_keys(" ")

    # signup negative test (email and password is too short)
    def typeShortemail(self):
        self.driver.find_element(By.XPATH, self.input_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_email_xpath).send_keys("d")

    def typeShortpassword(self):
        self.driver.find_element(By.XPATH, self.input_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_password_xpath).send_keys("d")

    # signup negative test (Firstname,lastname,mobile number is required) (Invalid firstname,lastname,mobile)
    def typeWithoutEmail(self):
        self.driver.find_element(By.XPATH, self.input_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_email_xpath).send_keys("      ")

    def typeWithoutPassword(self):
        self.driver.find_element(By.XPATH, self.input_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_password_xpath).send_keys("                                     ")

    def typeWithoutFirstname(self):
        self.driver.find_element(By.XPATH, self.input_firstname_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_firstname_xpath).send_keys("      ")

    def typeWithoutlastname(self):
        self.driver.find_element(By.XPATH, self.input_lastname_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_lastname_xpath).send_keys("      ")

    def typeWithoutmobile(self):
        self.driver.find_element(By.XPATH, self.input_mobile_xpath).click()
        self.driver.find_element(By.XPATH, self.input_mobile_xpath).send_keys("")

    def typeFnnegative1(self):
        self.driver.find_element(By.XPATH, self.input_firstname_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_firstname_xpath).send_keys("12133333334")

    def typeLnnegative1(self):
        self.driver.find_element(By.XPATH, self.input_lastname_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_lastname_xpath).send_keys("33235345545")

    def typeFnnegative2(self):
        self.driver.find_element(By.XPATH, self.input_firstname_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_firstname_xpath).send_keys("          ")

    def typeLnnegative2(self):
        self.driver.find_element(By.XPATH, self.input_lastname_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_lastname_xpath).send_keys("           ")

    def typeFnnegative3(self):
        self.driver.find_element(By.XPATH, self.input_firstname_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_firstname_xpath).send_keys("sdhfbhgfgfshhcbhcvgcvgv@yvdvscsshfsgygygygycuncfcgddff.ffdvcfyvfbgfbeycgfbfgfgfurgfuegcenejfhxeifuerfgeybcehgfuegyxnsxnbbshgfdygfyrgrfu")

    def typeLnnegative3(self):
        self.driver.find_element(By.XPATH, self.input_lastname_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_lastname_xpath).send_keys("dxdcscsds214254@@@@@@@@@@@@@@@22dhschvcgdvgcvgcvdhcshdhbdsnjsbjchsbchbgyrfgrpofrihnucgyvcgvgsvhxsvchschsbsbycbb gygyfcgdvgsdvvvvvvvvvvvvvvvvvvv")














