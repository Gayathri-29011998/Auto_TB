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



class Adminpage:

    logger = LogGen.loggen()

    email_xpath = "//*[@id='root']/div[2]/section[1]/main/div/div/section[2]/section/form/div[1]/input"
    password_xpath = "//*[@id='root']/div[2]/section[1]/main/div/div/section[2]/section/form/div[2]/input"

    homepage_icon_xpath = "/html/body/div[1]/div[2]/section[1]/main/nav/main/div[2]/aside/p"
    settings_xpath = "/html/body/div[1]/section[1]/nav/main/div[1]/aside[1]/div/div/div/div[6]/ul/div/div/div/span"
    ind_settings_xpath = "/html/body/div[1]/section[1]/nav/main/div[1]/aside[1]/div/div/div/div[7]/ul/div/div/div/span"
    admin_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/div/div[1]/div/div[5]/a"
    admin_search_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/div/div[2]/section[2]/div/div/div[1]/section/input"
    adminsearch_add_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/div/div[2]/section[2]/div/div/div[2]/div[1]"
    adminaccountdelete_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/div/div[2]/section[2]/div/div/div[4]/div[1]/div[1]/div/div[2]"
    admindelete_yes_xpath = "/html/body/div[4]/div/div/div[2]/section/div/button[1]"
    individual_viewadminaccesspage_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/div/div[2]/section[2]/div/div/div[4]/div[1]"
    associated_account_xpath = "/html/body/div[1]/section[1]/nav/main/div[1]/aside[1]/div/div/div/div[2]/div[1]/div[1]/p"
    onbehalfofpostjob_toggle_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[11]/div/label/span[1]/span[1]/input"
    onbehalfofpostpjt_toggle_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[9]/div/label/span[1]/span[1]/input"
    onbehalfofpostfund_toggle_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[12]/div/label/span[1]/span[1]/input"
    onbehalfofpostinvest_toggle_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[12]/div/label/span[1]/span[1]/input"
    onbehalfofpostjob_choose_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[11]/div[2]"
    onbehalfofpostpjt_choose_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[10]/div"
    onbehalfofpostfund_choose_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[12]/div[2]/div"
    onbehalfofpostinvest_choose_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[12]/div[2]"
    projects_button_xpath = "/html/body/div[1]/section[1]/main/div/div[1]/main/section[1]/main/div[2]/ul/li[2]/a"
    postpjt_button_xpath = "/html/body/div[1]/section[1]/main/div/div[1]/main/section[1]/main/div[4]/a/div/p"
    fundraise_button_xpath = "/html/body/div[1]/section[1]/main/div/div[1]/main/section[1]/main/div[2]/ul/li[3]/a"
    postfund_button_xpath = "/html/body/div[1]/section[1]/main/div/div[1]/main/section[1]/main/div[4]/a/div/p"
    applypjt_xpath = "/html/body/div[1]/section[1]/main/div/div[1]/main/section[2]/div/div/main/main[1]/div[6]/div/button[1]"
    applypjt_onbehalf_toggle_xpath = "/html/body/div[4]/div[3]/form/div[7]/label/span[1]/span[1]/input"
    applypjt_onbehalfof_choose_xpath = "/html/body/div[4]/div[3]/form/div[7]/div"

    update_adminaccess_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/div/div[2]/section[2]/div/div/div[4]/div[1]"
    applyjob_toggle_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/div/div[2]/section[2]/div/div/div[4]/div[2]/div/div/div/div/div[1]/div/table/tbody/tr[1]/td[2]/div/label/span/span[1]/input"
    createjob_toggle_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/div/div[2]/section[2]/div/div/div[4]/div[2]/div/div/div/div/div[1]/div/table/tbody/tr[1]/td[3]/div/label/span/span[1]/input"
    applypjt_toggle_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/div/div[2]/section[2]/div/div/div[4]/div[2]/div/div/div/div/div[1]/div/table/tbody/tr[2]/td[2]/div/label/span/span[1]/input"
    createpjt_toggle_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/div/div[2]/section[2]/div/div/div[4]/div[2]/div/div/div/div/div[1]/div/table/tbody/tr[2]/td[3]/div/label/span/span[1]/input"
    applyfund_toggle_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/div/div[2]/section[2]/div/div/div[4]/div[2]/div/div/div/div/div[1]/div/table/tbody/tr[3]/td[2]/div/label/span/span[1]/input"
    createfund_toggle_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/div/div[2]/section[2]/div/div/div[4]/div[2]/div/div/div/div/div[1]/div/table/tbody/tr[3]/td[3]/div/label/span/span[1]/input"
    applyinvest_toggle_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/div/div[2]/section[2]/div/div/div[4]/div[2]/div/div/div/div/div[1]/div/table/tbody/tr[4]/td[2]/div/label/span/span[1]/input"
    createinvest_toggle_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/div/div[2]/section[2]/div/div/div[4]/div[2]/div/div/div/div/div[1]/div/table/tbody/tr[4]/td[3]/div/label/span/span[1]/input"

    adminaccess_resetbutton_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/div/div[2]/section[2]/div/div/div[4]/div[2]/div/div/div/div/div[2]/button[1]"
    adminaccess_savebutton_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/div/div[2]/section[2]/div/div/div[4]/div[2]/div/div/div/div/div[2]/button[2]"








    def __init__(self, driver):
        self.driver = driver

    def typeEmail(self):
        self.driver.find_element(By.XPATH, self.email_xpath).clear()
        self.driver.find_element(By.XPATH, self.email_xpath).send_keys("senthil@kratosolutions.com")

    def typepPassword(self):
        self.driver.find_element(By.XPATH, self.password_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys("P@ssw0rd 2024")

    def clickHomePageIcon(self):
        self.driver.find_element(By.XPATH, self.homepage_icon_xpath).click()

    def clickSettings(self):
        self.driver.find_element(By.XPATH, self.settings_xpath).click()

    def clickAdminPage(self):
        self.driver.find_element(By.XPATH, self.admin_xpath).click()

    def clickAdminSearch(self):
        self.driver.find_element(By.XPATH, self.admin_search_xpath).clear()
        self.driver.find_element(By.XPATH, self.admin_search_xpath).send_keys("Gaya")

    def clickAdminSearchAdd(self):
        self.driver.find_element(By.XPATH, self.adminsearch_add_xpath).click()

    def clickDeleteAdminAccount(self):
        self.driver.find_element(By.XPATH, self.adminaccountdelete_xpath).click()

    def clickDeleteAdminYes(self):
        self.driver.find_element(By.XPATH, self.admindelete_yes_xpath).click()

    def clickAssociatedAccount(self):
        self.driver.find_element(By.XPATH, self.associated_account_xpath).click()

    def clickIndAdminAccessView(self):
        self.driver.find_element(By.XPATH, self.individual_viewadminaccesspage_xpath).click()

    def scrollOnbehalftogglepostjob(self):
        Button = self.driver.find_element(By.XPATH, self.onbehalfofpostjob_toggle_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Button)

    def clickOnbehalftogglepostjob(self):
        self.driver.find_element(By.XPATH, self.onbehalfofpostjob_toggle_xpath).click()

    def clickOnbehalfofchoosepostjob(self):
        self.driver.find_element(By.XPATH, self.onbehalfofpostjob_choose_xpath).click()

    def scrollOnbehalftogglepostpjt(self):
        Button = self.driver.find_element(By.XPATH, self.onbehalfofpostpjt_toggle_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Button)

    def clickOnbehalftogglepostpjt(self):
        self.driver.find_element(By.XPATH, self.onbehalfofpostpjt_toggle_xpath).click()

    def clickOnbehalfofchoosepostpjt(self):
        self.driver.find_element(By.XPATH, self.onbehalfofpostpjt_choose_xpath).click()

    def scrollOnbehalftogglepostfund(self):
        Button = self.driver.find_element(By.XPATH, self.onbehalfofpostfund_toggle_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Button)

    def clickOnbehalftogglepostfund(self):
        self.driver.find_element(By.XPATH, self.onbehalfofpostfund_toggle_xpath).click()

    def clickOnbehalfofchoosepostfund(self):
        self.driver.find_element(By.XPATH, self.onbehalfofpostfund_choose_xpath).click()

    def scrollOnbehalftogglepostinvest(self):
        Button = self.driver.find_element(By.XPATH, self.onbehalfofpostinvest_toggle_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Button)

    def clickOnbehalftogglepostinvest(self):
        self.driver.find_element(By.XPATH, self.onbehalfofpostinvest_toggle_xpath).click()

    def clickOnbehalfofchoosepostinvest(self):
        self.driver.find_element(By.XPATH, self.onbehalfofpostinvest_choose_xpath).click()

    def clickProjects(self):
        self.driver.find_element(By.XPATH, self.projects_button_xpath).click()

    def clickPostProjects(self):
        self.driver.find_element(By.XPATH, self.postpjt_button_xpath).click()

    def clickFundraising(self):
        self.driver.find_element(By.XPATH, self.fundraise_button_xpath).click()

    def clickPostFundraising(self):
        self.driver.find_element(By.XPATH, self.postfund_button_xpath).click()

    def clickApplypjt(self):
        self.driver.find_element(By.XPATH, self.applypjt_xpath).click()

    def clickOnbehalfoftoggleApplypjt(self):
        self.driver.find_element(By.XPATH, self.applypjt_onbehalf_toggle_xpath).click()

    def clickonbehalfofchooseApplypjt(self):
        self.driver.find_element(By.XPATH, self.applypjt_onbehalfof_choose_xpath).click()

    def clickUpdateAdminAccessAccount(self):
        self.driver.find_element(By.XPATH, self.update_adminaccess_xpath).click()

    def clickApplyJobAccess(self):
        self.driver.find_element(By.XPATH, self.applyjob_toggle_xpath).click()

    def clickCreateJobAccess(self):
        self.driver.find_element(By.XPATH, self.createjob_toggle_xpath).click()

    def clickApplyPjtAccess(self):
        self.driver.find_element(By.XPATH, self.applypjt_toggle_xpath).click()

    def clickCreatePjtAccess(self):
        self.driver.find_element(By.XPATH, self.createpjt_toggle_xpath).click()

    def clickApplyFundAccess(self):
        self.driver.find_element(By.XPATH, self.applyfund_toggle_xpath).click()

    def clickCreateFundAccess(self):
        self.driver.find_element(By.XPATH, self.createfund_toggle_xpath).click()

    def clickApplyInvestAccess(self):
        self.driver.find_element(By.XPATH, self.applyinvest_toggle_xpath).click()

    def clickCreateInvestAccess(self):
        self.driver.find_element(By.XPATH, self.createinvest_toggle_xpath).click()

    def clickSaveAccess(self):
        self.driver.find_element(By.XPATH, self.adminaccess_savebutton_xpath).click()

    def clickResetAccess(self):
        self.driver.find_element(By.XPATH, self.adminaccess_resetbutton_xpath).click()

    def clickIndvidualSettings(self):
        self.driver.find_element(By.XPATH, self.ind_settings_xpath).click()