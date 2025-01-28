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



class Investings:

    logger = LogGen.loggen()

    investing_button_xpath = "/html/body/div[1]/section[1]/main/div/div[1]/main/section[1]/main/div[2]/ul/li[4]/a"
    postinvesting_button_xpath = "/html/body/div[1]/section[1]/main/div/div[1]/main/section[1]/main/div[4]/a/div"
    postinvestingfinal_button_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[13]/button[2]"
    investorname_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[2]/div/input"
    invesmentexperience_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[3]/div/input"
    investortype_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[4]/div/div/div/div[1]/div[2]"
    investortype1_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[4]/div/div/div[2]/div/div[1]" #bank
    investortype2_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[4]/div/div/div[2]/div/div[2]" #angel
    investortype3_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[4]/div/div/div[2]/div/div[3]"  #peer-to-peer
    investortype4_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[4]/div/div/div[2]/div/div[4]"    #venture
    total_amount_invested_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[5]/div/input"
    no_of_previousinvest_companies_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[6]/div/input"
    sector_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[7]/div/div/div[1]/div[1]/div[2]"
    sector_type1_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[7]/div/div/div[2]/div/div[1]"  #Accounting
    invesment_stages_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[8]/div/div/div[1]/div[1]/div[2]"
    invesment_stage1_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[8]/div/div/div[2]/div/div[2]"    #Pre Seed
    invesment_stage2_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[8]/div/div/div[2]/div/div[5]"    #Series c
    evaluation_duration_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[9]/div/input"
    invesment_range_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[10]/div/div[1]/div/div/div[1]/div[2]"
    invest_rangetype_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[10]/div/div[1]/div/div[2]/div/div[1]"   #INR
    invesmentrange_min_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[10]/div/div[2]/input[1]"
    invesmentrange_max_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[10]/div/div[2]/input[2]"
    whocanapply_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[11]/div/div/div[1]/div[1]"
    whocanapply_account1_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[11]/div/div/div[2]/div/div[1]"
    whocanapply_account2_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[11]/div/div/div[2]/div/div[1]"
    whocanapply_account3_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[11]/div/div/div[2]/div/div[1]"
    whocanapply_account4_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[11]/div/div/div[2]/div/div[1]"
    whocanapply_account5_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[11]/div/div/div[2]/div/div[1]"
    whocanapply_account6_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[11]/div/div/div[2]/div/div[1]"
    whocanapply_account7_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[11]/div/div/div[2]/div/div[1]"

    onbehalfofpost_toggle_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[12]/div/label/span[1]/span[1]/input"
    onbehalfof_choose_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[12]/div[2]"
    onbehalfof_account_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[12]/div[2]/div[2]/div"


    def __init__(self, driver):
        self.driver = driver

    def clickInvestings(self):
        self.driver.find_element(By.XPATH, self.investing_button_xpath).click()

    def clickPostInvestingButton(self):
        self.driver.find_element(By.XPATH, self.postinvesting_button_xpath).click()

    def typeInvestorname(self, investorname):
        input1 = self.driver.find_element(By.XPATH, self.investorname_xpath).is_displayed()
        self.logger.info("Is Displayed %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.investorname_xpath).is_enabled()
        self.logger.info("Is Enabled %s", input2)
        self.driver.find_element(By.XPATH, self.investorname_xpath).clear()
        self.driver.find_element(By.XPATH, self.investorname_xpath).send_keys(investorname)

    def invalidInvestorname(self):
        self.driver.find_element(By.XPATH, self.investorname_xpath).clear()
        self.driver.find_element(By.XPATH, self.investorname_xpath).send_keys("1234567")

    def typeInvestExperience(self, invesmentexperience):
        input1 = self.driver.find_element(By.XPATH, self.invesmentexperience_xpath).is_displayed()
        self.logger.info("Is Displayed %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.invesmentexperience_xpath).is_enabled()
        self.logger.info("Is Enabled %s", input2)
        self.driver.find_element(By.XPATH, self.invesmentexperience_xpath).clear()
        self.driver.find_element(By.XPATH, self.invesmentexperience_xpath).send_keys(invesmentexperience)

    def invalidInvestExperience(self):
        self.driver.find_element(By.XPATH, self.invesmentexperience_xpath).clear()
        self.driver.find_element(By.XPATH, self.invesmentexperience_xpath).send_keys("asdfghjk")

    def clickInvestorType(self):
        self.driver.find_element(By.XPATH, self.investortype_xpath).click()

    def selectInvestorType1(self):   # Banks
        self.driver.find_element(By.XPATH, self.investortype1_xpath).click()

    def selectInvestorType2(self):   #Anjel Investors
        self.driver.find_element(By.XPATH, self.investortype2_xpath).click()

    def selectInvestorType3(self):   #Peer-to-Peer Investors
        self.driver.find_element(By.XPATH, self.investortype3_xpath).click()

    def selectInvestorType4(self):   #Venture Capitals
        self.driver.find_element(By.XPATH, self.investortype4_xpath).click()

    def typeTotalAmountInvest(self, totalamountinvest):
        input1 = self.driver.find_element(By.XPATH, self.total_amount_invested_xpath).is_displayed()
        self.logger.info("Is Displayed %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.total_amount_invested_xpath).is_enabled()
        self.logger.info("Is Enabled %s", input2)
        self.driver.find_element(By.XPATH, self.total_amount_invested_xpath).clear()
        self.driver.find_element(By.XPATH, self.total_amount_invested_xpath).send_keys(totalamountinvest)

    def invalidTotalAmountInvest(self):
        self.driver.find_element(By.XPATH, self.total_amount_invested_xpath).clear()
        self.driver.find_element(By.XPATH, self.total_amount_invested_xpath).send_keys("@#$%^$%^")


    def typeNoofpreviousInvCompany(self, noofpreviousinvestcompany):
        input1 = self.driver.find_element(By.XPATH, self.no_of_previousinvest_companies_xpath).is_displayed()
        self.logger.info("Is Displayed %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.no_of_previousinvest_companies_xpath).is_enabled()
        self.logger.info("Is Enabled %s", input2)
        self.driver.find_element(By.XPATH, self.no_of_previousinvest_companies_xpath).clear()
        self.driver.find_element(By.XPATH, self.no_of_previousinvest_companies_xpath).send_keys(noofpreviousinvestcompany)

    def scrollNoofpreviousInvCompany(self):
        Button = self.driver.find_element(By.XPATH, self.no_of_previousinvest_companies_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Button)

    def invalidNoofpreviousInvCompany(self):
        self.driver.find_element(By.XPATH, self.no_of_previousinvest_companies_xpath).clear()
        self.driver.find_element(By.XPATH, self.no_of_previousinvest_companies_xpath).send_keys("adfgdfg")

    def scrollSector(self):
        Button = self.driver.find_element(By.XPATH, self.sector_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Button)

    def clickSector(self):
        self.driver.find_element(By.XPATH, self.sector_xpath).click()

    def selectSectortype1(self):  #Accounting
        self.driver.find_element(By.XPATH, self.sector_type1_xpath).click()

    def clickInvestmentStage(self):
        self.driver.find_element(By.XPATH, self.invesment_stages_xpath).click()

    def selectStage1(self):  #Pre Seed
        self.driver.find_element(By.XPATH, self.invesment_stage1_xpath).click()

    def selectStage2(self):  # Series C
        self.driver.find_element(By.XPATH, self.invesment_stage2_xpath).click()

    def typeEvaluationDuration(self, evaluationduration):
        input1 = self.driver.find_element(By.XPATH, self.evaluation_duration_xpath).is_displayed()
        self.logger.info("Is Displayed %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.evaluation_duration_xpath).is_enabled()
        self.logger.info("Is Enabled %s", input2)
        self.driver.find_element(By.XPATH, self.evaluation_duration_xpath).clear()
        self.driver.find_element(By.XPATH, self.evaluation_duration_xpath).send_keys(evaluationduration)

    def invalidEvaluationDuration(self):
        self.driver.find_element(By.XPATH, self.evaluation_duration_xpath).clear()
        self.driver.find_element(By.XPATH, self.evaluation_duration_xpath).send_keys("ff@#$#")

    def clickInvestRange(self):
        self.driver.find_element(By.XPATH, self.invesment_range_xpath).click()

    def selectInvestRangeINR(self):  #INR
        self.driver.find_element(By.XPATH, self.invest_rangetype_xpath).click()

    def typeRangeMin(self, investrangemin):
        input1 = self.driver.find_element(By.XPATH, self.invesmentrange_min_xpath).is_displayed()
        self.logger.info("Is Displayed %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.invesmentrange_min_xpath).is_enabled()
        self.logger.info("Is Enabled %s", input2)
        self.driver.find_element(By.XPATH, self.invesmentrange_min_xpath).clear()
        self.driver.find_element(By.XPATH, self.invesmentrange_min_xpath).send_keys(investrangemin)

    def invalidRangeMin(self):
        self.driver.find_element(By.XPATH, self.invesmentrange_min_xpath).clear()
        self.driver.find_element(By.XPATH, self.invesmentrange_min_xpath).send_keys("Assdfg")

    def lessRangeMin(self):
        self.driver.find_element(By.XPATH, self.invesmentrange_min_xpath).clear()
        self.driver.find_element(By.XPATH, self.invesmentrange_min_xpath).send_keys("421")


    def typeRangeMax(self, investrangemax):
        input1 = self.driver.find_element(By.XPATH, self.invesmentrange_max_xpath).is_displayed()
        self.logger.info("Is Displayed %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.invesmentrange_max_xpath).is_enabled()
        self.logger.info("Is Enabled %s", input2)
        self.driver.find_element(By.XPATH, self.invesmentrange_max_xpath).clear()
        self.driver.find_element(By.XPATH, self.invesmentrange_max_xpath).send_keys(investrangemax)

    def invalidRangeMax(self):
        self.driver.find_element(By.XPATH, self.invesmentrange_max_xpath).clear()
        self.driver.find_element(By.XPATH, self.invesmentrange_max_xpath).send_keys("@#$%^&")

    def lessRangeMax(self):
        self.driver.find_element(By.XPATH, self.invesmentrange_max_xpath).clear()
        self.driver.find_element(By.XPATH, self.invesmentrange_max_xpath).send_keys("124")

    def scrollWhoCanApply(self):
        Button = self.driver.find_element(By.XPATH, self.whocanapply_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Button)

    def clickWhoCanApply(self):
        self.driver.find_element(By.XPATH, self.whocanapply_xpath).click()

    def selectWhocanapplyAccount1(self):  # Student
        self.driver.find_element(By.XPATH, self.whocanapply_account1_xpath).click()

    def selectWhocanapplyAccount2(self):  # Professional
        self.driver.find_element(By.XPATH, self.whocanapply_account2_xpath).click()

    def selectWhocanapplyAccount3(self):   # Freelancer
        self.driver.find_element(By.XPATH, self.whocanapply_account3_xpath).click()

    def selectWhocanapplyAccount4(self):   # Homegrown
        self.driver.find_element(By.XPATH, self.whocanapply_account4_xpath).click()

    def selectWhocanapplyAccount5(self):   # Registered
        self.driver.find_element(By.XPATH, self.whocanapply_account5_xpath).click()

    def selectWhocanapplyAccount6(self):   # College
        self.driver.find_element(By.XPATH, self.whocanapply_account6_xpath).click()

    def selectWhocanapplyAccount7(self):   # Training Institute
        self.driver.find_element(By.XPATH, self.whocanapply_account7_xpath).click()

    def scrollPostInvestingFinalButton(self):
        Button = self.driver.find_element(By.XPATH, self.postinvestingfinal_button_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Button)
    def clickPostInvestingFinalButton(self):
        self.driver.find_element(By.XPATH, self.postinvestingfinal_button_xpath).click()

    def clickOnbehalfofToggle(self):
        self.driver.find_element(By.XPATH, self.onbehalfofpost_toggle_xpath).click()

    def clickOnbehalfofChoose(self):
        self.driver.find_element(By.XPATH, self.onbehalfof_choose_xpath).click()

    def clickOnbehalfofAccount(self):
        self.driver.find_element(By.XPATH, self.onbehalfof_account_xpath).click()








