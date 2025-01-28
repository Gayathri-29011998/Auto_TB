import time
from telnetlib import EC

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.customLogger import LogGen


class HomePage:

    logger = LogGen.loggen()

    profileicon_xpath = "/html/body/div[1]/div[2]/section[1]/main/nav/main/div[1]/aside[1]/div/span"
    profilename_xpath = "/html/body/div[1]/section[1]/nav/main/div[1]/aside[1]/div/div/div/div[1]/div[2]/p[1]"
    #profilename_xpath = "/html/body/div[1]/section[1]/nav/main/div[1]/aside[1]/div/div/div/div[1]/div[2]/p[1]"
    jobs_lock_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/div/section/div[2]/div[2]/aside[1]/div/label/span/span[1]/input"
    proj_lock_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/div/section/div[2]/div[2]/aside[2]/div/label/span/span[1]/input"
    fund_lock_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/div/section/div[2]/div[2]/aside[3]/div/label/span/span[1]/input"
    invs_lock_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/div/section/div[2]/div[2]/aside[4]/div/label/span/span[1]/input"
    logout_xpath = "/html/body/div[1]/div[2]/section[1]/main/nav/main/div[1]/aside[1]/div/div/div/div[2]/div[2]/ul/li[5]/div/label"
    logout_yes_xpath = "/html/body/div[4]/div/div/div[2]/section/div/button[1]"
    jpfi_homepageicon_xpath = "/html/body/div[1]/section[1]/nav/main/div[2]/aside/p/a"

    def __init__(self, driver):
        self.driver = driver

    def clickProfileIcon(self):
        self.driver.find_element(By.XPATH, self.profileicon_xpath).click()

    def clickProfileName(self):
        self.driver.find_element(By.XPATH, self.profilename_xpath).click()
    def clickJobsLock(self):
        self.driver.find_element(By.XPATH, self.jobs_lock_xpath).click()

    def clickProjectsLock(self):
        self.driver.find_element(By.XPATH, self.proj_lock_xpath).click()

    def clickFundingLock(self):
        self.driver.find_element(By.XPATH, self.fund_lock_xpath).click()

    def clickInvestingLock(self):
        self.driver.find_element(By.XPATH, self.invs_lock_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.logout_xpath).click()

    def clickLogoutYes(self):
        self.driver.find_element(By.XPATH, self.logout_yes_xpath).click()

    def clickJPFIHomepageIcon(self):
        self.driver.find_element(By.XPATH, self.jpfi_homepageicon_xpath).click()

