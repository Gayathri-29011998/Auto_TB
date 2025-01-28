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



class Jobs:

    logger = LogGen.loggen()

    #old_jobs_button_xpath="/html/body/div[1]/section[1]/main/div/div[1]/main/section[1]/main/div[2]/ul/li[1]/a"
    jobs_button_xpath = "//a[text()= 'Jobs']"
    postjob_button_xpath="/html/body/div[1]/section[1]/main/div/div[1]/main/section[1]/main/div[4]/a/div/p"
    postjobfinal_button_xpath="/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[12]/button[2]/span[1]"
    input_designation_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[1]/div/input"
    input_experience_min_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[2]/div/div/input[1]"
    input_experience_max_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[2]/div/div/input[2]"

    dropdown_joining_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[3]/div/div/div/div[1]/div[2]"
    joinint_type1_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[3]/div/div/div[2]/div/div[1]"

    dropdown_employmenttype_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[4]/div/div/div/div[1]/div[2]"
    employment_type1_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[4]/div/div/div[2]/div/div[1]"

    input_location_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[5]/div/input"

    dropdown_salarytype_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[6]/div/div/div[1]/div/div/div[1]/div[2]"
    salary_type1_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[6]/div/div/div[1]/div/div[2]/div/div[1]"
    input_salary_min_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[6]/div/div/div[2]/input[1]"
    input_salary_max_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[6]/div/div/div[2]/input[2]"

    input_jobdescription_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[7]/div[1]/div/div/div/textarea[1]"

    input_jobresponsiblities_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[7]/div[2]/div/div[2]/div[1]"

    input_skill_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[9]/div/input"
    icon_addskill_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[9]/div/img"

    dropdown_whocanapply_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[10]/div/div/div[1]/div[1]/div[2]"
    whocanapply_account1_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[10]/div/div/div[2]/div/div[1]"
    whocanapply_account2_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[10]/div/div/div[2]/div/div[1]"
    whocanapply_account3_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[10]/div/div/div[2]/div/div[1]"
    whocanapply_account4_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[10]/div/div/div[2]/div/div[1]"
    whocanapply_account5_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[10]/div/div/div[2]/div/div[1]"

    onbehalfofpostjob_toggle_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[11]/div/label/span[1]/span[1]/input"
    onbehalfofpostjob_choose_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[11]/div[2]"
    onbehalfof_chooseaccount_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[11]/div[2]/div[2]/div"
                                     #"/html/body/div[1]/div[2]/section[1]/main/div/div/section/div/div[2]/div/form/div/div[2]/div[11]/div[2]/div[2]/div"


    def __init__(self, driver):
        self.driver = driver

    def clickJobButton(self):
        self.driver.find_element(By.XPATH, self.jobs_button_xpath).click()

    def clickPostJobButton(self):
        self.driver.find_element(By.XPATH, self.postjob_button_xpath).click()

    def typeDesignation(self, designation):
        input1 = self.driver.find_element(By.XPATH, self.input_designation_xpath).is_displayed()
        self.logger.info("Is Displayed %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_designation_xpath).is_enabled()
        self.logger.info("Is Enabled %s", input2)
        self.driver.find_element(By.XPATH, self.input_designation_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_designation_xpath).send_keys(designation)

    def scrollDesignation(self):
        Button = self.driver.find_element(By.XPATH, self.input_designation_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Button)

    def shortDesignation(self):
        self.driver.find_element(By.XPATH, self.input_designation_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_designation_xpath).send_keys("d")

    def lengthDesignation(self):
        self.driver.find_element(By.XPATH, self.input_designation_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_designation_xpath).send_keys("Ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg")

    def invalidDesignation(self):
        self.driver.find_element(By.XPATH, self.input_designation_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_designation_xpath).send_keys("@#$%^&^%$")

    def scrollExperience(self):
        Button = self.driver.find_element(By.XPATH, self.input_experience_min_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Button)

    def typeExperienceMin(self, experiencemin):
        input1 = self.driver.find_element(By.XPATH, self.input_experience_min_xpath).is_displayed()
        self.logger.info("Is Displayed %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_experience_min_xpath).is_enabled()
        self.logger.info("Is Enabled %s", input2)
        self.driver.find_element(By.XPATH, self.input_experience_min_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_experience_min_xpath).send_keys(experiencemin)

    def typeInvalidExperienceMin(self):
        self.driver.find_element(By.XPATH, self.input_experience_min_xpath).click()
        self.driver.find_element(By.XPATH, self.input_experience_min_xpath).send_keys("sd")
        self.driver.find_element(By.XPATH, self.input_experience_min_xpath).clear()


    def typeExperienceMax(self, experiencemax):
        input1 = self.driver.find_element(By.XPATH, self.input_experience_max_xpath).is_displayed()
        self.logger.info("Is Displayed %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_experience_max_xpath).is_enabled()
        self.logger.info("Is Enabled %s", input2)
        self.driver.find_element(By.XPATH, self.input_experience_max_xpath).click()
        self.driver.find_element(By.XPATH, self.input_experience_max_xpath).send_keys(experiencemax)

    def typeInvalidExperienceMax(self):
        self.driver.find_element(By.XPATH, self.input_experience_max_xpath).click()
        self.driver.find_element(By.XPATH, self.input_experience_max_xpath).send_keys("@#$")
        self.driver.find_element(By.XPATH, self.input_experience_max_xpath).clear()

    def lessExperiencemax(self):
        self.driver.find_element(By.XPATH, self.input_experience_max_xpath).click()
        self.driver.find_element(By.XPATH, self.input_experience_max_xpath).send_keys("1")

    def clickJoiningSelect(self):
        input1 = self.driver.find_element(By.XPATH, self.dropdown_joining_xpath).is_displayed()
        self.logger.info("Is Displayed %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.dropdown_joining_xpath).is_enabled()
        self.logger.info("Is Enabled %s", input2)
        self.driver.find_element(By.XPATH, self.dropdown_joining_xpath).click()
        #self.driver.find_element(By.XPATH, self.dropdown_joining_xpath).send_keys()

    def clickJoiningType1(self):
        self.driver.find_element(By.XPATH, self.joinint_type1_xpath).click()

    def scrollEmploymenttype(self):
        Button = self.driver.find_element(By.XPATH, self.dropdown_employmenttype_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Button)

    def clickEmploymentSelect(self):
        input1 = self.driver.find_element(By.XPATH, self.dropdown_employmenttype_xpath).is_displayed()
        self.logger.info("Is Displayed %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.dropdown_employmenttype_xpath).is_enabled()
        self.logger.info("Is Enabled %s", input2)
        self.driver.find_element(By.XPATH, self.dropdown_employmenttype_xpath).click()
        #self.driver.find_element(By.XPATH, self.dropdown_employmenttype_xpath).send_keys()

    def clickEmploymentType1(self):
        self.driver.find_element(By.XPATH, self.employment_type1_xpath).click()

    def typeLocation(self, location):
        input1 = self.driver.find_element(By.XPATH, self.input_location_xpath).is_displayed()
        self.logger.info("Is Displayed %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_location_xpath).is_enabled()
        self.logger.info("Is Enabled %s", input2)
        self.driver.find_element(By.XPATH, self.input_location_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_location_xpath).send_keys(location)

    def scrollLocation(self):
        Button = self.driver.find_element(By.XPATH, self.input_location_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Button)

    def invalidLocation(self):
        self.driver.find_element(By.XPATH, self.input_location_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_location_xpath).send_keys("1234567")

    def scrollSalaryType(self):
        Button = self.driver.find_element(By.XPATH, self.dropdown_salarytype_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Button)

    def clickSalarytypeSelect(self):
        input1 = self.driver.find_element(By.XPATH, self.dropdown_salarytype_xpath).is_displayed()
        self.logger.info("Is Displayed %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.dropdown_salarytype_xpath).is_enabled()
        self.logger.info("Is Enabled %s", input2)
        self.driver.find_element(By.XPATH, self.dropdown_salarytype_xpath).click()
        #self.driver.find_element(By.XPATH, self.input_location_xpath).send_keys()

    def clickSalaryType1(self):
        self.driver.find_element(By.XPATH, self.salary_type1_xpath).click()

    def typeSalaryMin(self, salarymin):
        input1 = self.driver.find_element(By.XPATH, self.input_salary_min_xpath).is_displayed()
        self.logger.info("Is Displayed %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_salary_min_xpath).is_enabled()
        self.logger.info("Is Enabled %s", input2)
        self.driver.find_element(By.XPATH, self.input_salary_min_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_salary_min_xpath).send_keys(salarymin)

    def scrollSalaryMin(self):
        Button = self.driver.find_element(By.XPATH, self.input_salary_min_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Button)

    def invalidSalaryMin(self):
        self.driver.find_element(By.XPATH, self.input_salary_min_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_salary_min_xpath).send_keys("fxgchvj")
        self.driver.find_element(By.XPATH, self.input_salary_min_xpath).clear()

    def typeSalaryMax(self, salarymax):
        input1 = self.driver.find_element(By.XPATH, self.input_salary_max_xpath).is_displayed()
        self.logger.info("Is Displayed %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_salary_max_xpath).is_enabled()
        self.logger.info("Is Enabled %s", input2)
        self.driver.find_element(By.XPATH, self.input_salary_max_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_salary_max_xpath).send_keys(salarymax)

    def invalidSalaryMax(self):
        self.driver.find_element(By.XPATH, self.input_salary_max_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_salary_max_xpath).send_keys("@#$%^&*")
        self.driver.find_element(By.XPATH, self.input_salary_max_xpath).clear()

    def lessSalaryMax(self):
        self.driver.find_element(By.XPATH, self.input_salary_max_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_salary_max_xpath).send_keys("1000")

    def typeJobDescription(self, jobdescription):
        Button = self.driver.find_element(By.XPATH, self.input_jobdescription_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Button)
        input1 = self.driver.find_element(By.XPATH, self.input_jobdescription_xpath).is_displayed()
        self.logger.info("Is Displayed %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_jobdescription_xpath).is_enabled()
        self.logger.info("Is Enabled %s", input2)
        self.driver.find_element(By.XPATH, self.input_jobdescription_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_jobdescription_xpath).send_keys(jobdescription)

    def scrollJobDescription(self):
        Button = self.driver.find_element(By.XPATH, self.input_jobdescription_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Button)

    def invalidJobDescription(self):
        self.driver.find_element(By.XPATH, self.input_jobdescription_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_jobdescription_xpath).send_keys("RKSSDGv4")

    def emptyJobDescription(self):
        self.driver.find_element(By.XPATH, self.input_jobdescription_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_jobdescription_xpath).send_keys("                                                                                                                           ")

    def scrollJobResponsiblities(self):
        Button = self.driver.find_element(By.XPATH, self.input_jobresponsiblities_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Button)
    def typeJobResponsiblities(self, jobresponsiblities):
        input1 = self.driver.find_element(By.XPATH, self.input_jobresponsiblities_xpath).is_displayed()
        self.logger.info("Is Displayed %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_jobresponsiblities_xpath).is_enabled()
        self.logger.info("Is Enabled %s", input2)
        self.driver.find_element(By.XPATH, self.input_jobresponsiblities_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_jobresponsiblities_xpath).send_keys(jobresponsiblities)

    def scrollJobResponsiblities(self):
        Button = self.driver.find_element(By.XPATH, self.input_jobresponsiblities_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Button)

    def invalidJobResponsiblities(self):
        self.driver.find_element(By.XPATH, self.input_jobresponsiblities_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_jobresponsiblities_xpath).send_keys("ddewfewfffefefffffrff")

    def typeSkill(self, skill):
        Button = self.driver.find_element(By.XPATH, self.input_skill_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Button)
        input1 = self.driver.find_element(By.XPATH, self.input_skill_xpath).is_displayed()
        self.logger.info("Is Displayed %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_skill_xpath).is_enabled()
        self.logger.info("Is Enabled %s", input2)
        self.driver.find_element(By.XPATH, self.input_skill_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_skill_xpath).send_keys(skill)

    def clickAddSkillIcon(self):
        self.driver.find_element(By.XPATH, self.icon_addskill_xpath).click()

    def clickWhocanapplySelect(self):
        Button = self.driver.find_element(By.XPATH, self.dropdown_whocanapply_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Button)
        input1 = self.driver.find_element(By.XPATH, self.dropdown_whocanapply_xpath).is_displayed()
        self.logger.info("Is Displayed %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.dropdown_whocanapply_xpath).is_enabled()
        self.logger.info("Is Enabled %s", input2)
        self.driver.find_element(By.XPATH, self.dropdown_whocanapply_xpath).click()

    def selectWhocanapplyAccount1(self):  # Student
        self.driver.find_element(By.XPATH, self.whocanapply_account1_xpath).click()

    def selectWhocanapplyAccount2(self):  # Professional
        self.driver.find_element(By.XPATH, self.whocanapply_account2_xpath).click()

    def selectWhocanapplyAccount3(self):  # Freelancer
        self.driver.find_element(By.XPATH, self.whocanapply_account3_xpath).click()

    def selectWhocanapplyAccount4(self):  # Homegrown
        self.driver.find_element(By.XPATH, self.whocanapply_account4_xpath).click()

    def selectWhocanapplyAccount5(self):  # Registered
        self.driver.find_element(By.XPATH, self.whocanapply_account5_xpath).click()

    def clickOnbehalfofToggle(self):
        self.driver.find_element(By.XPATH, self.onbehalfofpostjob_toggle_xpath).click()

    def clickOnbehalfofChoose(self):
        self.driver.find_element(By.XPATH, self.onbehalfofpostjob_choose_xpath).click()

    def clickOnbehalfofChooseAccount(self):
        self.driver.find_element(By.XPATH, self.onbehalfof_chooseaccount_xpath).click()


    def scrollPostJobFinalButton(self):
        Button = self.driver.find_element(By.XPATH, self.postjobfinal_button_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Button)

    def clickPostJobFinalButton(self):
        self.driver.find_element(By.XPATH, self.postjobfinal_button_xpath).click()

    def selectionElement(self):
        # List of XPaths or CSS selectors for the elements you want to find
        element_selectors = [
            (By.XPATH, '/html/body/div[1]/div[2]/section[1]/main/div/div/div/section/div[2]/div[2]/aside[1]/a/p'),
            # home page job xpath
            #(By.XPATH, '/html/body/div[1]/div[2]/section[1]/main/div/div/div/section/div[2]/div[2]/aside[3]/a/p'),
            # home page funding xpath
            #(By.XPATH, '/html/body/div[1]/div[2]/section[1]/main/div/div/div/section/div[2]/div[2]/aside[2]/a/p')
            # home page pjt xpath
        ]
        # Define a wait time
        wait = WebDriverWait(self.driver, 10)

        for by, selector in element_selectors:
            try:
                # # Attempt to find the element
                # element = self.driver.find_element(by, selector)
                # Wait for the element to be present
                element = wait.until(EC.presence_of_element_located((by, selector)))
                # Perform actions with the element (e.g., click, extract text, etc.)
                element.click()
                # print(element.text)
            except (NoSuchElementException, TimeoutException):
                # Skip to the next element if not found
                print(f'Element not found: {selector}')
                continue




