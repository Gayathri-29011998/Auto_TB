import time
from telnetlib import EC

from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.customLogger import LogGen

class Opencloseapplysave:
# open,close,applied,save pjt

    logger = LogGen.loggen()

    profile_navbar_droparrow_xpath = "/html/body/div[1]/section[1]/nav/main/div[1]/aside[1]/div/span"
    jobs_downarrow_xpath = "/html/body/div[1]/section[1]/nav/main/div[1]/aside[1]/div/div/div/div[2]/div[1]/div[2]/h2/button"
    openjob_xpath = "/html/body/div[1]/section[1]/nav/main/div[1]/aside[1]/div/div/div/div[2]/div[1]/div[2]/div/p[2]"
    openjob_3dots_xpath = "/html/body/div[1]/section[1]/main/div/div[1]/main/section[2]/div/div/main/main[1]/div[1]/div[3]/div/button/img"
    openjob_close_xpath = "/html/body/div[3]/div[3]/ul/div/li[2]/p"
    openjob_applications_xpath = ""
    closedjob_button_xpath = "/html/body/div[1]/section[1]/main/div/div[1]/main/section[1]/div[2]/a[2]"
    closedjob_repost_xpath = "/html/body/div[1]/section[1]/main/div/div[1]/main/section[2]/div/div/main/main[1]/div[4]/div/button[2]"
    jobrepost_button_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[7]/div[7]/button[2]"
    appliedjob_button_xpath = "/html/body/div[1]/section[1]/nav/main/div[1]/aside[1]/div/div/div/div[2]/div[1]/div[2]/div/p[4]"
    savedjob_button_xpath = "/html/body/div[1]/section[1]/main/div/div[1]/main/section[1]/div[2]/a[2]"

# Open,Close,Applied,Save Job

    def __init__(self, driver):
       self.driver = driver

    def clickProfileNavbardropArrow(self):
        self.driver.find_element(By.XPATH, self.profile_navbar_droparrow_xpath).click()

        # try:
        #    # Wait for the profile navbar drop arrow to be clickable
        #    profilnavbardrop = WebDriverWait(self.driver, 10).until(
        #         EC.element_to_be_clickable((By.XPATH, self.profile_navbar_droparrow_xpath))
        # )
        #
        # except NoSuchElementException as e:
        #  self.logger.error("Profile Navbar Drop Arrow Element Not Found: %s", str(e))
        #  self.logger.debug("Page Source at Failure: %s", self.driver.page_source)
        #  self.driver.save_screenshot('screenshot.png')
        #  assert False, "Profile Navbar Drop Arrow element not found"
        # except Exception as e:
        #  self.logger.error("An error occurred: %s", str(e))
        #  self.driver.save_screenshot('screenshot.png')
        #  assert False, "An unexpected error occurred"

    # self.driver.find_element(By.XPATH, self.profilenavbardroparrow_xpath).click()

    # # Locate the element to hover over
    # element_to_hover_over = self.driver.find_element(By.XPATH, self.profilenavbardroparrow_xpath)
    # # Create an ActionChains object
    # actions = ActionChains(self.driver)
    # # Perform the mouse hover action
    # actions.move_to_element(element_to_hover_over).perform()
    # time.sleep(1)


    def clickJobDownArrow(self):
        self.driver.find_element(By.XPATH, self.jobs_downarrow_xpath).click()

    def clickOpenJob(self):
        self.driver.find_element(By.XPATH, self.openjob_xpath).click()

    def clickOpenJob3dots(self):
        self.driver.find_element(By.XPATH, self.openjob_3dots_xpath).click()

    def clickOpenJobClose(self):
        self.driver.find_element(By.XPATH, self.openjob_close_xpath).click()

    def clickClosedJobButton(self):
        self.driver.find_element(By.XPATH, self.closedjob_button_xpath).click()

    def clickClosedJobRepost(self):
        self.driver.find_element(By.XPATH, self.closedjob_repost_xpath).click()

    def scrollJobRepostButton(self):
        Button = self.driver.find_element(By.XPATH, self.jobrepost_button_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Button)

    def clickJobRepostButton(self):
        self.driver.find_element(By.XPATH, self.jobrepost_button_xpath).click()

    def clickAppliedJob(self):
        self.driver.find_element(By.XPATH, self.appliedjob_button_xpath).click()

    def clickSavedJob(self):
        self.driver.find_element(By.XPATH, self.savedjob_button_xpath).click()