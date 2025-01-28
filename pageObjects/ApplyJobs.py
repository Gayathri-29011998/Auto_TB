import time
from telnetlib import EC
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from utilities.customLogger import LogGen



class Applyjob:

    logger = LogGen.loggen()
#Jobs:

    savejob_button_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div[1]/main/section[2]/div/div/main/main[1]/div[4]/div/button[2]"
    jobthreedots_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div[1]/main/section[2]/div/div/main/main[1]/div[1]/div[3]/div/button"
    jobnotinterest_xpath="//button[text()= 'Not interested']"
    jobnotinterestYes_xpath = "//button[text()= 'Yes']"
    jobcopylink_xpath="//p[text()= 'CopyLink']"

    jobreview_xpath = "//p[text()= 'Write a review']"
    jobrating_xpath="/html/body/div[4]/div[3]/span/label[5]"
    jobreviewtxt_xpath="/html/body/div[4]/div[3]/textarea"
    jobreviewsubmit_xpath="//button[text()= 'Submit']"

    jobreport_xpath = "//p[text()= 'Report']"
    jobreporttxt_xpath="/html/body/div[4]/div[3]/textarea"
    jobreportsubmit_xpath="//button[text()= 'Report']"

    # Job apply
    #old_jobapply_button_xpath = "/html/body/div[1]/section[1]/main/div/div[1]/main/section[2]/div/div/main/main[1]/div[4]/div/button[1]"
    jobapply_button_xpath = "//button[text()= 'Apply']"
    nextjobapply_button_xpath = "//span[text()= 'Apply']"
    onbehalfofjobapply_toggle_xpath = "/html/body/div[4]/div[3]/div[2]/label/span[1]/span[1]/input"
    jobinput_pdfupload_xpath = "/html/body/div[4]/div[3]/div[2]/div[1]/input"
    jobinput_zipfileupload_xpath = "/html/body/div[4]/div[3]/div[2]/div[2]/input"
    jobinput_description_xpath = "/html/body/div[4]/div[3]/div[2]/textarea"
    jobapply_onbehalfchooseone_xpath="/html/body/div[4]/div[3]/div[3]/div/div"

    jobapply_onbehalfofaccount_xpath = "/html/body/div[4]/div[3]/div[3]/div/div[2]/div"
                                       #"/html/body/div[4]/div[3]/div[3]/div/div[2]/div"
    jobsubmit_xpath = "//span[text()= 'Submit']"

    alljobs_xpath = "/html/body/div[1]/div[2]/section[1]/main/nav/main/div[1]/aside[1]/div/div/div/div[2]/div[1]/div[1]/div/p[1]"



    def __init__(self, driver):
        self.driver = driver

    def clickJobApplyButton(self):
        self.driver.find_element(By.XPATH, self.jobapply_button_xpath).click()

    def clickNextJobApplyButton(self):
        self.driver.find_element(By.XPATH, self.nextjobapply_button_xpath).click()
    def clickOnbehalfofJobapplytoggle(self):
        self.driver.find_element(By.XPATH, self.onbehalfofjobapply_toggle_xpath).click()

    def clickJobapplyPdfupload(self):
        self.driver.find_element(By.XPATH, self.jobinput_pdfupload_xpath).send_keys("C://Users/user/Downloads/Automation.pdf")

    def clickJobapplyZipfileupload(self):
        self.driver.find_element(By.XPATH, self.jobinput_zipfileupload_xpath).send_keys("C://Users/user/Downloads/sample-zip-file.zip")

    def typeDescriptionjobapply(self):
        self.driver.find_element(By.XPATH, self.jobinput_description_xpath).clear()
        self.driver.find_element(By.XPATH, self.jobinput_description_xpath).send_keys("job apply desicription,job apply desicription,job apply desicription")

    def clickOnbehalfchooseone_JobApply(self):
        self.driver.find_element(By.XPATH, self.jobapply_onbehalfchooseone_xpath).click()

    def selectOnbehalfofAccount(self):
        self.driver.find_element(By.XPATH, self.jobapply_onbehalfofaccount_xpath).click()

    def clickSubmitjobapply(self):
        self.driver.find_element(By.XPATH, self.jobsubmit_xpath).click()


    def clickJobSave(self):
        self.driver.find_element(By.XPATH,self.savejob_button_xpath).click()

    def clickJobThreedots(self):
        self.driver.find_element(By.XPATH, self.jobthreedots_xpath).click()

    def clickJobCopylink(self):
        self.driver.find_element(By.XPATH, self.jobcopylink_xpath).click()


        # # Open a new tab using JavaScript
        # self.driver.execute_script("window.open('');")
        # # Switch to the new tab
        # self.driver.switch_to.window(driver.window_handles[-1])
        # # Open a different webpage in the new tab
        # self.driver.get('http://another-example.com')  # Replace with the actual URL you want to open in the new tab
        # # Optionally, perform actions on the new tab
        # time.sleep(3)  # Wait for a few seconds to see the new tab (for demonstration purposes)
        # # Close the new tab
        # self.driver.close()
        # # Switch back to the original tab
        # self.driver.switch_to.window(driver.window_handles[0])
        # # Optionally, perform actions on the original tab
        # time.sleep(3)  # Wait for a few seconds to see the original tab (for demonstration purposes)
    def clickJobReview(self):
        self.driver.find_element(By.XPATH, self.jobreview_xpath).click()


    def clickJobRating(self):
        self.driver.find_element(By.XPATH, self.jobrating_xpath).click()

    def clickJobReviewtxt(self):
        self.driver.find_element(By.XPATH, self.jobreviewtxt_xpath).click()
        self.driver.find_element(By.XPATH, self.jobreviewtxt_xpath).send_keys("Good Job Review")

    def clickJobReviewSubmit(self):
        self.driver.find_element(By.XPATH, self.jobreviewsubmit_xpath).click()

    def clickJobNotInterest(self):
        self.driver.find_element(By.XPATH, self.jobnotinterest_xpath).click()

    def clickjobNotInterestYesButton(self):
        self.driver.find_element(By.XPATH, self.jobnotinterestYes_xpath).click()


    def clickJobReport(self):
        self.driver.find_element(By.XPATH, self.jobreport_xpath).click()

    def typeJobReportTxt(self):
        self.driver.find_element(By.XPATH, self.jobreporttxt_xpath).click()
        self.driver.find_element(By.XPATH, self.jobreporttxt_xpath).send_keys("automation testing report")
    def clickJobReportSubmit(self):
        self.driver.find_element(By.XPATH, self.jobreportsubmit_xpath).click()

    def clickAllJobs(self):
        self.driver.find_element(By.XPATH, self.alljobs_xpath).click()


