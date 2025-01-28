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



class ApplyInvest:

    logger = LogGen.loggen()
#Investings:
# review,save,report,copy link, not interest
    investthreedots_xpath = "/html/body/div[1]/section[1]/main/div/div[1]/main/section[2]/div/div/main/main[1]/div[1]/div[3]/div/button/img"
    saveinvest_button_xpath = "/html/body/div[4]/div[3]/ul/div/li[1]/p"
    unsaveinvest_button_xpath="/html/body/div[4]/div[3]/ul/div/li[1]/p"
    investcopylink_xpath = "/html/body/div[4]/div[3]/ul/div/li[2]/p"
    investnotinterest_xpath = "/html/body/div[4]/div[3]/ul/div/li[4]/button"
    investnotinterestYes_xpath = "/html/body/div[5]/div/div/div[2]/section/div/button[1]"

    investreview_xpath = "/html/body/div[4]/div[3]/ul/div/li[3]/p"
    investrating_xpath = "/html/body/div[4]/div[3]/span/label[3]"
    investreviewtxt_xpath = "/html/body/div[4]/div[3]/textarea"
    investreviewsubmit_xpath = "/html/body/div[4]/div[3]/div/button[2]"

    investreport_xpath = "/html/body/div[4]/div[3]/ul/div/li[5]/p"
    investreporttxt_xpath = "/html/body/div[4]/div[3]/textarea"
    investreportsubmit_xpath = "/html/body/div[4]/div[3]/div/button[2]"

    pitch_button_xpath = "/html/body/div[1]/section[1]/main/div/div[1]/main/section[2]/div/div/main/main[1]/div[7]/div/button[1]/span"
    input_fundrequired_xpath = "/html/body/div[4]/div[3]/form/div[1]/input"
    stage_xpath = "/html/body/div[4]/div[3]/form/div[2]/div[1]/div/div/div[1]/div[2]"
    stage1_xpath = "/html/body/div[4]/div[3]/form/div[2]/div[1]/div/div[2]/div/div[3]" #seriesA
    stage2_xpath = "/html/body/div[4]/div[3]/form/div[2]/div[1]/div/div[2]/div/div[6]" #seriesD
    sector_xpath = "/html/body/div[4]/div[3]/form/div[2]/div[2]/div/div/div[1]/div[2]"
    sector1_xpath = "/html/body/div[4]/div[3]/form/div[2]/div[2]/div/div[2]/div/div[2]" #Airlines/Aviation
    sector2_xpath = "/html/body/div[4]/div[3]/form/div[2]/div[2]/div/div[2]/div/div[5]" #Animation
    applyinvest_description_xpath = "/html/body/div[4]/div[3]/form/textarea"
    applyinvest_pdfupload_xpath = "/html/body/div[4]/div[3]/form/div[3]/input"
    onbehalfofinvestapply_toggle_xpath = "/html/body/div[4]/div[3]/form/div[4]/label/span[1]/span[1]/input"
    applyinvest_onbehalfchooseone_xpath = "/html/body/div[4]/div[3]/form/div[4]/div/div"

    investapply_onbehalfofaccount_xpath = "/html/body/div[4]/div[3]/form/div[4]/div/div[2]/div"

    applyinvest_submit_xpath = "/html/body/div[4]/div[3]/form/div[5]/button[2]"

    # review,save,report,copy link, not interest
    def __init__(self, driver):
        self.driver = driver

    def clickPitchButton(self):
        self.driver.find_element(By.XPATH, self.pitch_button_xpath).click()

    def typeInvestFundRequired(self):
        self.driver.find_element(By.XPATH, self.input_fundrequired_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_fundrequired_xpath).send_keys("200000")

    def clickStage(self):
        self.driver.find_element(By.XPATH, self.stage_xpath).click()

    def selectStage1(self):
        self.driver.find_element(By.XPATH, self.stage1_xpath).click()

    def selectStage2(self):
        self.driver.find_element(By.XPATH, self.stage2_xpath).click()

    def clickSector(self):
        self.driver.find_element(By.XPATH, self.sector_xpath).click()

    def selectSector1(self):
        self.driver.find_element(By.XPATH, self.sector1_xpath).click()

    def selectSector2(self):
        self.driver.find_element(By.XPATH, self.sector2_xpath).click()

    def typeDescription(self):
        self.driver.find_element(By.XPATH, self.applyinvest_description_xpath).clear()
        self.driver.find_element(By.XPATH, self.applyinvest_description_xpath).send_keys("fadfsgfvafdvtfdtdffgyrerwetuuadffgvvctafbajghvagaddgfcagafafagfggagxcfgvbjajjdhaftftft")

    def clickPDFUpload(self):
        self.driver.find_element(By.XPATH, self.applyinvest_pdfupload_xpath).clear()
        self.driver.find_element(By.XPATH, self.applyinvest_pdfupload_xpath).send_keys("C://Users/user/Downloads/Automation.pdf")

    def clickOnbehalfofToggle(self):
        self.driver.find_element(By.XPATH, self.onbehalfofinvestapply_toggle_xpath).click()

    def clickOnbehalfofChoose(self):
        self.driver.find_element(By.XPATH, self.applyinvest_onbehalfchooseone_xpath).click()

    def clickOnbehalfofAccount(self):
        self.driver.find_element(By.XPATH, self.investapply_onbehalfofaccount_xpath).click()

    def clickApplyInvestSubmitButton(self):
        self.driver.find_element(By.XPATH, self.applyinvest_submit_xpath).click()

    def clickInvestThreedots(self):
        self.driver.find_element(By.XPATH, self.investthreedots_xpath).click()

    def clickInvestcopylink(self):
        self.driver.find_element(By.XPATH, self.investcopylink_xpath).click()

    def clickInvestreview(self):
        self.driver.find_element(By.XPATH, self.investreview_xpath).click()

    def clickInvestreviewsubmit(self):
        self.driver.find_element(By.XPATH, self.investreviewsubmit_xpath).click()

    def clickInvestrating(self):
        self.driver.find_element(By.XPATH, self.investrating_xpath).click()

    def clickInvestreviewtext(self):
        self.driver.find_element(By.XPATH, self.investreviewtxt_xpath).click()
        self.driver.find_element(By.XPATH, self.investreviewtxt_xpath).send_keys("automation testing review")

    def clickInvestnotinterest(self):
        self.driver.find_element(By.XPATH,self.investnotinterest_xpath).click()

    def clickInvestnotinterestyes(self):
        self.driver.find_element(By.XPATH, self.investnotinterestYes_xpath).click()

    def clickInvestreport(self):
        self.driver.find_element(By.XPATH,self.investreport_xpath).click()

    def clickInvestreportsubmit(self):
        self.driver.find_element(By.XPATH, self.investreportsubmit_xpath).click()

    def clickInvestreporttext(self):
        self.driver.find_element(By.XPATH, self.investreporttxt_xpath).send_keys("automation testing report")

    def clickInvestsave(self):
        self.driver.find_element(By.XPATH, self.saveinvest_button_xpath).click()