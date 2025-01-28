import time
from telnetlib import EC

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.customLogger import LogGen

class Signupinstitute:

    logger = LogGen.loggen()

    btn_register_xpath = "/html/body/div[1]/div[2]/div/div[2]/a[1]"
    box_institute_xpath = "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[1]/div[2]/button[3]"
    input_choosecategory_xpath = "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[1]/div[3]/div"
    txt_college_xpath = "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[1]/div[3]/div[2]/div[1]"
    btn_arrow1_xpath = "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[1]/div[4]/button"
    input_email_xpath = "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[2]/section/form/div[1]/input"
    input_password_xpath = "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[2]/section/form/div[2]/input"
    input_confirmpassword_xpath = "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[2]/section/form/div[3]/input"
    btn_arrow2_xpath = "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[2]/section/form/div[5]/button"
    input_collegename_xpath = "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[3]/section/main/form/div[1]/input"
    input_registername_xpath = "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[3]/section/main/form/div[2]/input"
    input_mobile_xpath = "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[3]/section/main/form/div[3]/div/input"
    input_enabledemail_xpath = "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[3]/section/main/form/div[4]/input"
    input_website_xpath = "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[3]/section/main/form/div[5]/input"
    #btn_agreejoin_xpath = "/html/body/div[1]/div[2]/section/main/div/div/section[2]/section[3]/section/main/form/div[7]/button"
    btn_agreejoin_xpath = "//button[text()='Agree & Join']"
    btn_verifyjoin_xpath = "/html/body/div[1]/section[2]/section/form/div[2]/button"

    def __init__(self, driver):
        self.driver = driver

    def clickRegister(self):
        self.driver.find_element(By.XPATH, self.btn_register_xpath).click()

    def clickInstitute(self):
        self.driver.find_element(By.XPATH, self.box_institute_xpath).click()

    def clickChoosecategory(self):
        self.driver.find_element(By.XPATH, self.input_choosecategory_xpath).click()

    def clickCollege(self):
        self.driver.find_element(By.XPATH, self.txt_college_xpath).click()

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

    def typeCollegename(self, collegename):
        input1=self.driver.find_element(By.XPATH, self.input_collegename_xpath).is_displayed()
        self.logger.info("Is Displayed %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_collegename_xpath).is_enabled()
        self.logger.info("Is Enabled %s", input2)
        self.driver.find_element(By.XPATH, self.input_collegename_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_collegename_xpath).send_keys(collegename)

    def typeRegistername(self, registername):
        input1=self.driver.find_element(By.XPATH, self.input_registername_xpath).is_displayed()
        self.logger.info("Is Displayed %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_registername_xpath).is_enabled()
        self.logger.info("Is Enabled %s", input2)
        self.driver.find_element(By.XPATH, self.input_registername_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_registername_xpath).send_keys(registername)

    def typeMobile(self, mobile):
        input1=self.driver.find_element(By.XPATH, self.input_mobile_xpath).is_displayed()
        self.logger.info("Is Displayed %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_mobile_xpath).is_enabled()
        self.logger.info("Is Enabled %s", input2)
        self.driver.find_element(By.XPATH, self.input_mobile_xpath).click()
        self.driver.find_element(By.XPATH, self.input_mobile_xpath).send_keys(mobile)

    def typeWebsite(self, website):
        input1 = self.driver.find_element(By.XPATH, self.input_website_xpath).is_displayed()
        self.logger.info("Is Displayed %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_website_xpath).is_enabled()
        self.logger.info("Is Enabled %s", input2)
        self.driver.find_element(By.XPATH, self.input_website_xpath).click()
        self.driver.find_element(By.XPATH, self.input_website_xpath).send_keys(website)


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
        self.driver.find_element(By.XPATH, self.input_email_xpath).send_keys("g")

    def typeShortpassword(self):
        self.driver.find_element(By.XPATH, self.input_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_password_xpath).send_keys("g")

    def invalidEmail(self):
        self.driver.find_element(By.XPATH, self.input_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_email_xpath).send_keys("sgdggdgddhsfhv")

    def invalidPassword(self):
        self.driver.find_element(By.XPATH, self.input_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_password_xpath).send_keys("sshshvhsbbshd")


    # signup negative test (Firstname,lastname,mobile number is required) (Invalid firstname,lastname,mobile)

    def typeWithoutcollegename(self):
        self.driver.find_element(By.XPATH, self.input_collegename_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_collegename_xpath).send_keys("       ")

    def typeWithoutregistername(self):
        self.driver.find_element(By.XPATH, self.input_registername_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_registername_xpath).send_keys("        ")

    def typeNumbercollegename(self):
        self.driver.find_element(By.XPATH, self.input_collegename_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_collegename_xpath).send_keys("12345678")

    def typeNumberregistername(self):
        self.driver.find_element(By.XPATH, self.input_registername_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_registername_xpath).send_keys("12345678")

    def typeWithoutmobile(self):
        self.driver.find_element(By.XPATH, self.input_mobile_xpath).click()
        self.driver.find_element(By.XPATH, self.input_mobile_xpath).send_keys("")

    def typeWithoutwebsite(self):
        self.driver.find_element(By.XPATH, self.input_website_xpath).click()
        self.driver.find_element(By.XPATH, self.input_website_xpath).send_keys("")


