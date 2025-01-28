import time
from telnetlib import EC

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.customLogger import LogGen

class Brands:

    logger = LogGen.loggen()

    #Click profile icon
    btn_profileicon_xpath = "/html/body/div[1]/section[1]/nav/main/div[1]/aside[1]/div/span"

    #Click profilename
    btn_profilename_xpath = "/html/body/div[1]/section[1]/nav/main/div[1]/aside[1]/div/div/div/div[1]/div[2]/p[1]"
    navbar_services_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[1]/main/div[2]/ul/a[2]/li"

    #Services and Solutions
    btn_services_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[4]/main/section[1]/div[1]"
    input_servicetitle_xpath = "/html/body/div[3]/div[3]/div/div/main/section/div[2]/form/div[2]/div/div[1]/input"
    input_servicecontent_xpath = "/html/body/div[3]/div[3]/div/div/main/section/div[2]/form/div[2]/div/div[2]/textarea"
    btn_addservices_xpath = "/html/body/div[3]/div[3]/div/div/main/section/div[2]/form/div/button[1]"
    #btn_addservices_xpath = "/html/body/div[3]/div[3]/div/div/main/section/div[2]/form/div[3]/button[1]"
    input_afteraddtitle_xpath = "/html/body/div[3]/div[3]/div/div/main/section/div[2]/form/div[3]/div/div[1]/input"
    input_afteraddcontent_xpath = "/html/body/div[3]/div[3]/div/div/main/section/div[2]/form/div[3]/div/div[2]/textarea"
    btn_saveservices_xpath = "/html/body/div[3]/div[3]/div/div/main/section/div[2]/form/div/button[2]"
    #btn_saveservices2_xpath = "/html/body/div[3]/div[3]/div/div/main/section/div[2]/form/div[4]/button[2]"

    btn_deleteservices_xpath = "/html/body/div[3]/div[3]/div/div/main/section/div[2]/form/div[1]/div/button"
    btn_mousehover_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[4]/main/section[1]/div[2]/main[1]"
    btn_hoverdeleteicon = "/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[4]/main/section[1]/div[2]/main[1]/button"

    #Solution
    icon_solutions_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[4]/main/section[2]/div[1]"
    input_solutiontitle_xpath = "/html/body/div[3]/div[3]/div/div/main/section/div[2]/form/div[2]/div/div[1]/input"
    input_solutioncontent_xpath = "/html/body/div[3]/div[3]/div/div/main/section/div[2]/form/div[2]/div/div[2]/textarea"
    btn_addsolution_xpath = "/html/body/div[3]/div[3]/div/div/main/section/div[2]/form/div/span"
    input_solutionaddtitle_xpath = "/html/body/div[3]/div[3]/div/div/main/section/div[2]/form/div[3]/div/div[1]/input"
    input_solutionaddcontent_xpath = "/html/body/div[3]/div[3]/div/div/main/section/div[2]/form/div[3]/div/div[2]/textarea"
    btn_savesolution_xpath = "/html/body/div[3]/div[3]/div/div/main/section/div[2]/form/div/button"
    btn_deletesolution_xpath = "/html/body/div[3]/div[3]/div/div/main/section/div[2]/form/div[1]/div/button"
    btn_mousehoversolution_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[4]/main/section[2]/div[2]/main[1]"
    btn_hoverdeleteiconsolution_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[4]/main/section[2]/div[2]/main[1]/button"


    def __init__(self, driver):
        self.driver = driver


    def clickProfileicon(self):
        self.driver.find_element(By.XPATH, self.btn_profileicon_xpath).click()

    def clickProfilename(self):
        self.driver.find_element(By.XPATH, self.btn_profilename_xpath).click()

    def scrollServicesicon(self):
        icon=self.driver.find_element(By.XPATH, self.btn_services_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", icon)

    def clickServicesicon(self):
        self.driver.find_element(By.XPATH, self.btn_services_xpath).click()

    def typeServicetitle(self, servicetitle):
        input1 = self.driver.find_element(By.XPATH, self.input_servicetitle_xpath).is_displayed()
        self.logger.info("Is Displayed: %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_servicetitle_xpath).is_enabled()
        self.logger.info("Is Enabled: %s", input2)
        self.driver.find_element(By.XPATH, self.input_servicetitle_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_servicetitle_xpath).send_keys(servicetitle)

    def invalidServiceTitle(self):
        self.driver.find_element(By.XPATH, self.input_servicetitle_xpath).click()
        self.driver.find_element(By.XPATH, self.input_servicetitle_xpath).send_keys("                     ")


    def typeServicecontent(self, servicecontent):
        input1 = self.driver.find_element(By.XPATH, self.input_servicecontent_xpath).is_displayed()
        self.logger.info("Is Displayed: %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_servicecontent_xpath).is_enabled()
        self.logger.info("Is Enabled: %s", input2)
        self.driver.find_element(By.XPATH, self.input_servicecontent_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_servicecontent_xpath).send_keys(servicecontent)

    def lengthServiceContent(self):
        self.driver.find_element(By.XPATH, self.input_servicecontent_xpath).click()
        self.driver.find_element(By.XPATH, self.input_servicecontent_xpath).send_keys("Krato enables you to spend each unit of money as effectively as possible best,products and services.Krato enables you to spend each unit of money as effectively as possible best,products and services.Krato enables you to spend each unit of money as effectively as possible best,products and services.")

    def shortServiceContent(self):
        self.driver.find_element(By.XPATH, self.input_servicecontent_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_servicecontent_xpath).send_keys("a")

    def scrollSaveservice(self):
        icon=self.driver.find_element(By.XPATH, self.btn_saveservices_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", icon)


    def clickSaveservice(self):
        self.driver.find_element(By.XPATH, self.btn_saveservices_xpath).click()


    def clickDeleteService(self):
        self.driver.find_element(By.XPATH, self.btn_deleteservices_xpath).click()

    def mouseHoverclick(self):
        # Find the element to hover over
        element_to_hover_over = self.driver.find_element(By.XPATH, self.btn_mousehover_xpath)

        # Create an ActionChains object
        action_chains = ActionChains(self.driver)

        # Perform the mouse hover action
        action_chains.move_to_element(element_to_hover_over).perform()

        # After performing the hover action, you can interact with the elements that appear after the hover
        # For example, you can click on an element that appears after the hover
        element_to_click = self.driver.find_element(By.XPATH, self.btn_hoverdeleteicon)
        element_to_click.click()

    def scrollAddservice(self):
        icon = self.driver.find_element(By.XPATH, self.btn_addservices_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", icon)

    def clickAddservice(self):
        self.driver.find_element(By.XPATH, self.btn_addservices_xpath).click()


    def typeAddedtitle(self):
        input1 = self.driver.find_element(By.XPATH, self.input_afteraddtitle_xpath).is_displayed()
        self.logger.info("Is Displayed: %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_afteraddtitle_xpath).is_enabled()
        self.logger.info("Is Enabled: %s", input2)
        self.driver.find_element(By.XPATH, self.input_afteraddtitle_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_afteraddtitle_xpath).send_keys("MARKETING ANALYTICS")

    def typeAddedcontent(self):
        input1 = self.driver.find_element(By.XPATH, self.input_afteraddcontent_xpath).is_displayed()
        self.logger.info("Is Displayed: %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_afteraddcontent_xpath).is_enabled()
        self.logger.info("Is Enabled: %s", input2)
        self.driver.find_element(By.XPATH, self.input_afteraddcontent_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_afteraddcontent_xpath).send_keys("Krato enables you to spend each unit of money as effectively as possible best,products and services.")

    def clickSolutionsIcon(self):
        self.driver.find_element(By.XPATH, self.icon_solutions_xpath).click()

    def typeSolutiontitle(self, solutiontitle):
        input1 = self.driver.find_element(By.XPATH, self.input_solutiontitle_xpath).is_displayed()
        self.logger.info("Is Displayed: %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_solutiontitle_xpath).is_enabled()
        self.logger.info("Is Enabled: %s", input2)
        self.driver.find_element(By.XPATH, self.input_solutiontitle_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_servicetitle_xpath).send_keys(solutiontitle)

    def invalidSolutionTitle(self):
        self.driver.find_element(By.XPATH, self.input_solutiontitle_xpath).click()
        self.driver.find_element(By.XPATH, self.input_solutiontitle_xpath).send_keys("                     ")

    def typeSolutioncontent(self, solutioncontent):
        input1 = self.driver.find_element(By.XPATH, self.input_solutioncontent_xpath).is_displayed()
        self.logger.info("Is Displayed: %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_solutioncontent_xpath).is_enabled()
        self.logger.info("Is Enabled: %s", input2)
        self.driver.find_element(By.XPATH, self.input_solutioncontent_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_solutioncontent_xpath).send_keys(solutioncontent)

    def lengthSolutionContent(self):
        self.driver.find_element(By.XPATH, self.input_solutioncontent_xpath).click()
        self.driver.find_element(By.XPATH, self.input_solutioncontent_xpath).send_keys("Krato enables you to spend each unit of money as effectively as possible best,products and services.Krato enables you to spend each unit of money as effectively as possible best,products and services.Krato enables you to spend each unit of money as effectively as possible best,products and services.")

    def shortSolutionContent(self):
        self.driver.find_element(By.XPATH, self.input_solutioncontent_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_solutioncontent_xpath).send_keys("a")

    def scrollSaveSolution(self):
        icon = self.driver.find_element(By.XPATH, self.btn_savesolution_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", icon)

    def clickSaveSolution(self):
        self.driver.find_element(By.XPATH, self.btn_savesolution_xpath).click()

    def clickDeleteSolution(self):
        self.driver.find_element(By.XPATH, self.btn_deletesolution_xpath).click()

    def mouseHoverclickSolution(self):
        # Find the element to hover over
        element_to_hover_over = self.driver.find_element(By.XPATH, self.btn_mousehoversolution_xpath)

        # Create an ActionChains object
        action_chains = ActionChains(self.driver)

        # Perform the mouse hover action
        action_chains.move_to_element(element_to_hover_over).perform()

        # After performing the hover action, you can interact with the elements that appear after the hover
        # For example, you can click on an element that appears after the hover
        element_to_click = self.driver.find_element(By.XPATH, self.btn_hoverdeleteiconsolution_xpath)
        element_to_click.click()

    def scrollAddSolution(self):
        icon = self.driver.find_element(By.XPATH, self.btn_addsolution_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", icon)

    def clickAddSolution(self):
        self.driver.find_element(By.XPATH, self.btn_addsolution_xpath).click()

    def typeAddedtitleSolution(self):
        input1 = self.driver.find_element(By.XPATH, self.input_solutionaddtitle_xpath).is_displayed()
        self.logger.info("Is Displayed: %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_solutionaddtitle_xpath).is_enabled()
        self.logger.info("Is Enabled: %s", input2)
        self.driver.find_element(By.XPATH, self.input_solutionaddtitle_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_solutionaddtitle_xpath).send_keys("MARKETING ANALYTICS")

    def typeAddedcontentSolution(self):
        input1 = self.driver.find_element(By.XPATH, self.input_solutionaddcontent_xpath).is_displayed()
        self.logger.info("Is Displayed: %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_solutionaddcontent_xpath).is_enabled()
        self.logger.info("Is Enabled: %s", input2)
        self.driver.find_element(By.XPATH, self.input_solutionaddcontent_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_solutionaddcontent_xpath).send_keys("Krato enables you to spend each unit of money as effectively as possible best,products and services.")

    def clickNavbarServices(self):
        self.driver.find_element(By.XPATH, self.navbar_services_xpath).click()