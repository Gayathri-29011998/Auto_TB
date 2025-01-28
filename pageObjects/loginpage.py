from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Login:
    btn_signin_xpath = "/html/body/div[1]/div[2]/div/div[2]/a[2]"
    textbox_username_xpath = "//*[@id='root']/div[2]/section[1]/main/div/div/section[2]/section/form/div[1]/input"
    textbox_password_xpath = "//*[@id='root']/div[2]/section[1]/main/div/div/section[2]/section/form/div[2]/input"
    button_login_xpath = "//*[@id='root']/div[2]/section[1]/main/div/div/section[2]/section/form/div[4]/button"
    btn_profileicondropdown_xpath = "//p[text()='Me']"
    #oldproficondropdown_xpath=     "/html/body/div[1]/section[1]/nav/main/div[1]/aside[1]/div/span"
    btn_logout_xpath = "//span[text()='Logout']"
    #old_logout_xpath = "/html/body/div[1]/section[1]/nav/main/div[1]/aside[1]/div/div/div/div[2]/div[2]/ul/li[5]/div/label"
    btn_yes_xpath = "//button[text()='Yes']"
    #old_btn_yes_xpath = "/html/body/div[5]/div/div/div[2]/section/div/button[1]"


    def __init__(self, driver):
        self.driver = driver

    def clickSignin(self):
        self.driver.find_element(By.XPATH, self.btn_signin_xpath).click()

    def setUsername(self, username):
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).send_keys(username)

    def negativeusername(self):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys("")

    def invalidUsername(self, invalidusername):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(invalidusername)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def negativepassword(self):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys("")

    def invalidPassword(self, invalidpassword):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(invalidpassword)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def clickProfiledropdown(self):
        self.driver.find_element(By.XPATH, self.btn_profileicondropdown_xpath).click()
        # # Find the element to hover over
        # element_to_hover_over = self.driver.find_element(By.XPATH, self.btn_profileicondropdown_xpath)
        #
        # # Create an ActionChains object
        # action_chains = ActionChains(self.driver)
        #
        # # Perform the mouse hover action
        # action_chains.move_to_element(element_to_hover_over).perform()
        #
        # # After performing the hover action, you can interact with the elements that appear after the hover
        # # For example, you can click on an element that appears after the hover
        # element_to_click = self.driver.find_element(By.XPATH, self.btn_logout_xpath)
        # element_to_click.click()


    def scrollLogout(self):
        icon = self.driver.find_element(By.XPATH, self.btn_logout_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", icon)

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.btn_logout_xpath).click()

    def clickLogoutYes(self):
        self.driver.find_element(By.XPATH, self.btn_yes_xpath).click()
