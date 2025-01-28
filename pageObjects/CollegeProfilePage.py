import time
from telnetlib import EC

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.customLogger import LogGen


class College:

    logger = LogGen.loggen()

    #Click profile icon
    btn_profiledropdown_xpath = "//p[text()='Me']"
    
    #Click profilename
    btn_profilename_xpath = "/html/body/div[1]/section[1]/nav/main/div[1]/aside[1]/div/div/div/div[1]/div[2]/p[1]"
    navbar_about_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[1]/main/div[2]/ul/a[1]/li"
    navbar_certifiedcourse_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[1]/main/div[2]/ul/a[2]/li"
    navbar_specialprogram_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[1]/main/div[2]/ul/a[3]/li"
    navbar_placements_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[1]/main/div[2]/ul/a[4]/li"
    navbar_trustedcompanies_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[1]/main/div[2]/ul/a[5]/li"
    navbar_milestone_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[1]/main/div[2]/ul/a[6]/li"
    navbar_rating_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[1]/main/div[2]/ul/a[7]/li"
    navbar_testimonial_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[1]/main/div[2]/ul/a[8]/li"

    #Quotes
    btn_editquote_xpath ="//*[@id='root']/div[2]/section[1]/main/div/div/main/section[2]/section/div[2]/button"
    txt_quotes_xpath = "/html/body/div[3]/div[3]/div/div/main/section/form/div[1]/div/textarea"
    savequote_xpath = "/html/body/div[3]/div[3]/div/div/main/section/form/div[2]/button"

    #Profile page about icon
    btn_abouticon_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[3]/main/div[1]/div"
    tog_openconsult_xpath = "/html/body/div[3]/div[3]/main/section/div[2]/form/div[2]/div[1]/div/label/span/span[1]/input"
    tog_openhiring_xpath = "/html/body/div[3]/div[3]/main/section/div[2]/form/div[2]/div[3]/div/label/span/span[1]/input"
    tog_raisingfund_xpath = "/html/body/div[3]/div[3]/main/section/div[2]/form/div[2]/div[2]/div/label/span/span[1]/input"
    tog_openinvest_xpath = "/html/body/div[3]/div[3]/main/section/div[2]/form/div[2]/div[4]/div/label/span/span[1]/input"
    txt_aboutdescri_xpath = "/html/body/div[3]/div[3]/main/section/div[2]/form/div[3]/div/div/textarea[1]"
    btn_saveabout_xpath = "/html/body/div[3]/div[3]/main/section/div[2]/form/span/button"

    #Profile page certified courses + icon
    icon_certifiedcourse_xpath ="/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[4]/main/section[1]/div[2]/div"
    view_certifiedcourse_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[4]/main/section[1]/div[1]/div/div/div[1]"
    input_editcourse_xpath = "/html/body/div[3]/div[3]/div/div/main/section/div[2]/form/div[1]/div[1]/div/input"
    icon_deleteexistcourse_xpath = "/html/body/div[3]/div[3]/div/div/main/section/div[2]/form/div[4]/div[2]/button"
    icon_addcourse_xpath = "/html/body/div[3]/div[3]/div/div/main/section/div[2]/form/div/span"
    input_boxes_xpath = "did-floating-input "
    txt_typecourse_xpath = "/html/body/div[3]/div[3]/div/div/main/section/div[2]/form/div[3]/div[1]/div/input"
                           #"/html/body/div[3]/div[3]/div/div/main/section/div[2]/form/div[3]/div[1]/div"
    icon_deletecourse_xpath = "/html/body/div[3]/div[3]/div/div/main/section/div[2]/form/div/div[2]/button"
                              #"/html/body/div[3]/div[3]/div/div/main/section/div[2]/form/div[1]/div[2]/button"

    btn_savecourse_xpath = "/html/body/div[3]/div[3]/div/div/main/section/div[2]/form/div/button"
                           #"/html/body/div[3]/div[3]/div/div/main/section/div[2]/form/div[2]/button"
    icon_closecertifiedcourse_xpath = "/html/body/div[3]/div[3]/div/div/main/section/div[1]/div[2]/div"

    #Specialist program
    #Specialist program icon
    newicon_specialistprogram = "/html/body/div[1]/div[2]/section[1]/main/div/div/main/div/section/div/div[1]/button"
    icon_specialistprogram_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[4]/main/section[2]/div[2]/div"
    btn_addspecilistpgm_xpath = "/html/body/div[3]/div[3]/div/div/main/section/div[2]/form/div/span"
    txt_typespecilistpgm_xpath = "/html/body/div[3]/div[3]/div/div/main/section/div[2]/form/div[2]/div[1]/div/input"
    btn_savespecialpgm_xpath = "/html/body/div[3]/div[3]/div/div/main/section/div[2]/form/div/button"
    icon_deletesplprogram_xpath = "/html/body/div[3]/div[3]/div/div/main/section/div[2]/form/div[1]/div[2]/button"


    #Placements:
    #Add placements button
    icon_addplacements_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[5]/section/div[2]/div"
    num_addpercentage_xpath = "/html/body/div[3]/div[3]/div/div/main/section/div[2]/form/div[1]/div[1]/input"
    num_addtotalpersonsplaced_xpath = "/html/body/div[3]/div[3]/div/div/main/section/div[2]/form/div[1]/div[2]/input"
    btn_saveplacements_xpath = "/html/body/div[3]/div[3]/div/div/main/section/div[2]/form/div[2]/button"
    #alabamalion college placements icon


    # Milestone
    # Milestone button in profile page
    #btn_newmilestone_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/main/div/section/div/div[3]/button"
    btn_milestone_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[7]/section/div[2]"
    input_milestoneyear_xpath = "/html/body/div[3]/div[3]/div/div[2]/main/section/div[2]/form/div[2]/div/div[1]/input"
    input_milestonedescription_xpath = "/html/body/div[3]/div[3]/div/div[2]/main/section/div[2]/form/div[2]/div/div[2]/textarea"
    btn_addmilestone_xpath = "/html/body/div[3]/div[3]/div/div[2]/main/section/div[2]/form/div/span"
    input_milestoneyearadd_xpath = "/html/body/div[3]/div[3]/div/div[2]/main/section/div[2]/form/div[3]/div/div[1]/input"
    input_milestonedescadd_xpath = "/html/body/div[3]/div[3]/div/div[2]/main/section/div[2]/form/div[3]/div/div[2]/textarea"
    btn_savemilestone_xpath = "/html/body/div[3]/div[3]/div/div[2]/main/section/div[2]/form/div/button"
    btn_milestonedelete_xpath = "/html/body/div[3]/div[3]/div/div[2]/main/section/div[2]/form/div[1]/div/button"
    btn_mousehovermilestone_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[7]/section/main/div/div/div[1]/div"
    btn_hoverdeleteiconmilestone_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[7]/section/main/div/div/div/i"

    #Social Links
    icon_sociallink_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[9]/section/section/div[2]/div"
    input_facebook_xpath = "/html/body/div[3]/div[3]/div/div/main/section/form/div[1]/div[1]/div/div/input"
    input_twitter_xpath = "/html/body/div[3]/div[3]/div/div/main/section/form/div[1]/div[2]/div/div/input"
    input_linkedin_xpath = "/html/body/div[3]/div[3]/div/div/main/section/form/div[2]/div[1]/div/div/input"
    input_instagram_xpath = "/html/body/div[3]/div[3]/div/div/main/section/form/div[2]/div[2]/div/div/input"
    input_website_xpath = "/html/body/div[3]/div[3]/div/div/main/section/form/div[3]/div/div/div/input"
    btn_savesociallinks_xpath = "/html/body/div[3]/div[3]/div/div/main/section/form/div[4]/button"
    btn_FBlink_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[9]/section/section/div[1]/a[2]"
    btn_Twitterlink_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[9]/section/section/div[1]/a[1]"
    btn_LinkedInlink_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[9]/section/section/div[1]/a[3]"
    btn_Instalink_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[9]/section/section/div[1]/a[4]"
    btn_Websitelink_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[9]/section/section/div[1]/a[5]"

    #Businesscard
    btn_editbcard_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[2]/section/div[3]/div[1]/button[2]"
    input_institutename_xpath = "/html/body/div[3]/div[3]/div/div/form/div[1]/div/input"
    input_tagline_xpath = "/html/body/div[3]/div[3]/div/div/form/div[2]/div/input"
    input_foundedyear_xpath = "/html/body/div[3]/div[3]/div/div/form/div[3]/div/input"
    input_noofstudents_xpath = "/html/body/div[3]/div[3]/div/div/form/div[4]/div/input"
    input_noofcourses_xpath = "/html/body/div[3]/div[3]/div/div/form/div[5]/div/input"
    input_noofcompaniestrusting_xpath = "/html/body/div[3]/div[3]/div/div/form/div[6]/div/input"
    input_summary_xpath = "/html/body/div[3]/div[3]/div/div/form/div[7]/div/textarea[1]"
    input_address1_xpath = "/html/body/div[3]/div[3]/div/div/form/div[9]/div/textarea[1]"
    input_address2_xpath = "/html/body/div[3]/div[3]/div/div/form/div[10]/div/textarea[1]"
    input_city_xpath = "/html/body/div[3]/div[3]/div/div/form/div[11]/div[1]/div/div/input"
    input_state_xpath = "/html/body/div[3]/div[3]/div/div/form/div[11]/div[2]/div/div/input"
    input_country_xpath = "/html/body/div[3]/div[3]/div/div/form/div[11]/div[3]/div/div/input"
    input_pincode_xpath = "/html/body/div[3]/div[3]/div/div/form/div[11]/div[4]/div/div/input"
    input_mobile_xpath = "/html/body/div[3]/div[3]/div/div/form/div[12]/div/input"
    btn_savebusinesscard_xpath = "/html/body/div[3]/div[3]/div/div/form/button"

    #Trusted Companies
    icon_trustcompanies_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[6]/section/main/div[1]/div/div"
    input_clientname_xpath = "/html/body/div[3]/div[3]/div/div/main/section/div[2]/div/div/div/input"
    btn_addcompanyname_xpath = "/html/body/div[3]/div[3]/div/div/main/section/div[2]/div[2]/div[1]/div/div/div[1]"
    btn_saveclients_xpath = "/html/body/div[3]/div[3]/div/div/main/section/div[2]/button"
    icon_hoverdeleteclient_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[6]/section/main/div[3]/div/div/div/div/button"
    btn_mousehoverclientname_xpath = "/html/body/div[1]/div[2]/section[1]/main/div/div/main/section[6]/section/main/div[3]/div/div/div/div"


    def __init__(self, driver):
        self.driver = driver

    def clickProfileicon(self):
        self.driver.find_element(By.XPATH, self.btn_profiledropdown_xpath).click()

    def clickProfilename(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.btn_profilename_xpath))
            )
            # Once the element is clickable, perform actions on it
            element.click()

        except TimeoutException:
            print("Element not found within the specified time.")

    def clickEditquote(self):
        self.driver.find_element(By.XPATH,self.btn_editquote_xpath).click()

    def typeQuotes(self, quote):

        self.driver.find_element(By.XPATH,self.txt_quotes_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,self.txt_quotes_xpath).send_keys(quote)

    def shortQuote(self):
        self.driver.find_element(By.XPATH, self.txt_quotes_xpath).click()
        self.driver.find_element(By.XPATH, self.txt_quotes_xpath).send_keys("a")

    def lengthQuote(self):
        self.driver.find_element(By.XPATH, self.txt_quotes_xpath).click()
        self.driver.find_element(By.XPATH, self.txt_quotes_xpath).send_keys("agfdtdwetdfttftereyerynfbcctgggreiuegiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiuywfgetfgftewgdtwefetdgextgxtgctgftfgexegiwufwguwyerytryyrtycgnwxgyfgrfyxgryxfgyfry")

    def clickSave(self):
        #WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.savequote_xpath)))
        self.driver.find_element(By.XPATH, self.savequote_xpath).click()

    def clickNavbarAbout(self):
        self.driver.find_element(By.XPATH, self.navbar_about_xpath).click()

    def scrollAbouticon(self):
        #self.driver.find_element(By.XPATH, self.btn_abouticon_xpath).click()
        icon = self.driver.find_element(By.XPATH, self.btn_abouticon_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();",icon)

        # self.driver.execute_script("arguments[0].scrollIntoView();", element)
        # element.click()

    def clickAbouticon(self):
        self.driver.find_element(By.XPATH, self.btn_abouticon_xpath).click()
    def clickOpenconsult(self):
        status = self.driver.find_element(By.XPATH, self.tog_openconsult_xpath).is_selected()
        #print("Is Selected:",status)
        self.logger.info("Is Selected:" + str(status))
        self.driver.find_element(By.XPATH,self.tog_openconsult_xpath).click()
    def clickHiring(self):
        self.driver.find_element(By.XPATH, self.tog_openhiring_xpath).click()

    def clickRaisingfund(self):
        self.driver.find_element(By.XPATH, self.tog_raisingfund_xpath).click()

    def clickOpeninvest(self):
        self.driver.find_element(By.XPATH, self.tog_openinvest_xpath).click()

    def typeAboutdesc(self, aboutdescription):
        self.driver.find_element(By.XPATH, self.txt_aboutdescri_xpath).click()
        self.driver.find_element(By.XPATH, self.txt_aboutdescri_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_aboutdescri_xpath).send_keys(aboutdescription)

    def withoutaboutdescription(self):
        self.driver.find_element(By.XPATH, self.txt_aboutdescri_xpath).clear()

    def lengthaboutdescription(self):
        self.driver.find_element(By.XPATH, self.txt_aboutdescri_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_aboutdescri_xpath).send_keys("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. typesetting, remaining essentially unchanged. ")

    def clickSaveabout(self):
        self.driver.find_element(By.XPATH, self.btn_saveabout_xpath).click()


    def clickNavbarCertifiedCourse(self):
        self.driver.find_element(By.XPATH, self.navbar_certifiedcourse_xpath).click()

    def scrollCertifiedcourseicon(self):
        icon = self.driver.find_element(By.XPATH, self.icon_certifiedcourse_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", icon)

    def clickCertifiedcourseicon(self):
        self.driver.find_element(By.XPATH, self.icon_certifiedcourse_xpath).click()

    def scrollAddcourse(self):
        icon = self.driver.find_element(By.XPATH, self.icon_addcourse_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", icon)

    def clickAddcourse(self):
        self.driver.find_element(By.XPATH, self.icon_addcourse_xpath).click()


    def typeCourse(self, course):
        input1 = self.driver.find_element(By.XPATH, self.txt_typecourse_xpath).is_displayed()
        self.logger.info("Is Displayed %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.txt_typecourse_xpath).is_enabled()
        self.logger.info("Is Enabled %s", input2)
        self.driver.find_element(By.XPATH, self.txt_typecourse_xpath).click()
        #self.driver.find_element(By.XPATH, self.txt_typecourse_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_typecourse_xpath).send_keys(course)

    #Negative test
    def withoutTypecourse(self):
        self.driver.find_element(By.XPATH, self.txt_typecourse_xpath).send_keys("")

    def displayCourse(self):
        status = self.driver.find_element(By.XPATH, self.input_editcourse_xpath).is_displayed()
        # print("Is Selected:",status)
        self.logger.info("Is Displayed:" + str(status))
        self.logger.info("************* Fetched The Status************")

    def clickSavecourse(self):
        self.driver.find_element(By.XPATH, self.btn_savecourse_xpath).click()


    def scrollTypecourse(self):
        icon = self.driver.find_element(By.XPATH, self.txt_typecourse_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", icon)

    def clickDeletecourse(self):
        self.driver.find_element(By.XPATH, self.icon_deletecourse_xpath).click()

    def clickClosecertifiedcourse(self):
        self.driver.find_element(By.XPATH, self.icon_closecertifiedcourse_xpath).click()

    def editCourse(self):

        self.driver.find_element(By.XPATH, self.input_editcourse_xpath).click()
        self.driver.find_element(By.XPATH, self.input_editcourse_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_editcourse_xpath).send_keys("Selenium")

    def existCoursedelete(self):
        self.driver.find_element(By.XPATH, self.icon_deleteexistcourse_xpath).click()



    #specialized program functions

    def clickNavbarSpecialistProgram(self):
        self.driver.find_element(By.XPATH, self.navbar_specialprogram_xpath).click()

    def scrollSpecialistpgmicon(self):
        icon = self.driver.find_element(By.XPATH, self.newicon_specialistprogram)
        self.driver.execute_script("arguments[0].scrollIntoView();", icon)

    def speciallistprgmNewIcon(self):
        self.driver.find_element(By.XPATH, self.newicon_specialistprogram).click()
    def clickSpelialistpgmicon(self):
        self.driver.find_element(By.XPATH, self.icon_specialistprogram_xpath).click()

    def clickAddspecialistpgm(self):
        self.driver.find_element(By.XPATH, self.btn_addspecilistpgm_xpath).click()

    def typeSpecialistpgm(self, specialprogram):
        self.driver.find_element(By.XPATH, self.txt_typespecilistpgm_xpath).click()
        self.driver.find_element(By.XPATH, self.txt_typespecilistpgm_xpath).send_keys(specialprogram)

    def clickSavespecialistpgm(self):
        self.driver.find_element(By.XPATH, self.btn_savespecialpgm_xpath).click()

    def clickDeletespecialpgm(self):
        self.driver.find_element(By.XPATH, self.icon_deletesplprogram_xpath).click()

    def clickNavbarPlacements(self):
        self.driver.find_element(By.XPATH, self.navbar_placements_xpath).click()

    def scrollAddplacementsicon(self):
        icon = self.driver.find_element(By.XPATH, self.icon_addplacements_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", icon)

    def clickAddplacements(self):
        self.driver.find_element(By.XPATH, self.icon_addplacements_xpath).click()

    def typePercentage(self, percentage):
        input1=self.driver.find_element(By.XPATH, self.num_addpercentage_xpath).is_displayed()
        self.logger.info("Is Displayed: %s", input1)
        input2=self.driver.find_element(By.XPATH, self.num_addpercentage_xpath).is_enabled()
        self.logger.info("Is Enabled: %s", input2)
        self.driver.find_element(By.XPATH, self.num_addpercentage_xpath).click()
        self.driver.find_element(By.XPATH, self.num_addpercentage_xpath).send_keys(percentage)

    def invalidPercentage(self):
        self.driver.find_element(By.XPATH, self.num_addpercentage_xpath).clear()
        self.driver.find_element(By.XPATH, self.num_addpercentage_xpath).send_keys("ahagvddgw")
    def editPercentage(self, editpercentage):
        input1 = self.driver.find_element(By.XPATH, self.num_addpercentage_xpath).is_displayed()
        self.logger.info("Is Displayed: %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.num_addpercentage_xpath).is_enabled()
        self.logger.info("Is Enabled: %s", input2)
        self.driver.find_element(By.XPATH, self.num_addpercentage_xpath).clear()
        self.driver.find_element(By.XPATH, self.num_addpercentage_xpath).send_keys(editpercentage)

    def withoutPercentage(self):
        self.driver.find_element(By.XPATH, self.num_addpercentage_xpath).clear()


    def typeTotalpersonplaced(self, totalpersonplaced):
        input1 = self.driver.find_element(By.XPATH, self.num_addtotalpersonsplaced_xpath).is_displayed()
        self.logger.info("Is Displayed: %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.num_addtotalpersonsplaced_xpath).is_enabled()
        self.logger.info("Is Enabled: %s", input2)
        self.driver.find_element(By.XPATH, self.num_addtotalpersonsplaced_xpath).click()
        self.driver.find_element(By.XPATH, self.num_addtotalpersonsplaced_xpath).send_keys(totalpersonplaced)

    def invalidTotalPersonPlaced(self):
        self.driver.find_element(By.XPATH, self.num_addtotalpersonsplaced_xpath).clear()
        self.driver.find_element(By.XPATH, self.num_addtotalpersonsplaced_xpath).send_keys("ysvstsshsbygyyyyyf")
    def editTotalpersonplaced(self, edittotalpersonplaced):
        input1 = self.driver.find_element(By.XPATH, self.num_addtotalpersonsplaced_xpath).is_displayed()
        self.logger.info("Is Displayed: %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.num_addtotalpersonsplaced_xpath).is_enabled()
        self.logger.info("Is Enabled: %s", input2)
        self.driver.find_element(By.XPATH, self.num_addtotalpersonsplaced_xpath).clear()
        self.driver.find_element(By.XPATH, self.num_addtotalpersonsplaced_xpath).send_keys(edittotalpersonplaced)

    def withoutTotalpersonplaced(self):
        self.driver.find_element(By.XPATH, self.num_addtotalpersonsplaced_xpath).clear()

    def clickSaveplacements(self):
        self.driver.find_element(By.XPATH, self.btn_saveplacements_xpath).click()


    def scrollMilestoneicon(self):
        icon=self.driver.find_element(By.XPATH, self.btn_milestone_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", icon)

    def clickMilestoneIcon(self):
        self.driver.find_element(By.XPATH, self.btn_milestone_xpath).click()
    def typeMilestoneyear(self, milestoneyear):
        input1 = self.driver.find_element(By.XPATH, self.input_milestoneyear_xpath).is_displayed()
        self.logger.info("Is Displayed: %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_milestoneyear_xpath).is_enabled()
        self.logger.info("Is Enabled: %s", input2)
        self.driver.find_element(By.XPATH, self.input_milestoneyear_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_milestoneyear_xpath).send_keys(milestoneyear)

    def typeMilestonedesc(self, milestonedescription):
        input1 = self.driver.find_element(By.XPATH, self.input_milestonedescription_xpath).is_displayed()
        self.logger.info("Is Displayed: %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_milestonedescription_xpath).is_enabled()
        self.logger.info("Is Enabled: %s", input2)
        self.driver.find_element(By.XPATH, self.input_milestonedescription_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_milestonedescription_xpath).send_keys(milestonedescription)

    def typeaddMilestoneyear(self):
        input1 = self.driver.find_element(By.XPATH, self.input_milestoneyearadd_xpath).is_displayed()
        self.logger.info("Is Displayed: %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_milestoneyearadd_xpath).is_enabled()
        self.logger.info("Is Enabled: %s", input2)
        self.driver.find_element(By.XPATH, self.input_milestoneyearadd_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_milestoneyearadd_xpath).send_keys("2021")

    def invalidAddMilestoneyear(self):
        self.driver.find_element(By.XPATH, self.input_milestoneyear_xpath).clear()

        self.driver.find_element(By.XPATH, self.input_milestoneyear_xpath).send_keys("adddd21343435454335")

    def typeaddMilestonedesc(self):
        input1 = self.driver.find_element(By.XPATH, self.input_milestonedescadd_xpath).is_displayed()
        self.logger.info("Is Displayed: %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_milestonedescadd_xpath).is_enabled()
        self.logger.info("Is Enabled: %s", input2)
        self.driver.find_element(By.XPATH, self.input_milestonedescadd_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_milestonedescadd_xpath).send_keys("It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.")

    def lengthMilestoneContent(self):
        self.driver.find_element(By.XPATH, self.input_milestonedescription_xpath).click()
        self.driver.find_element(By.XPATH, self.input_milestonedescription_xpath).send_keys("Krato enables you to spend each unit of money as effectively as possible best,products and services.Krato enables you to spend each unit of money as effectively as possible best,products and services.Krato enables you to spend each unit of money as effectively as possible best,products and services.")

    def shortMilestoneContent(self):
        self.driver.find_element(By.XPATH, self.input_milestonedescription_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_milestonedescription_xpath).send_keys("a")

    def scrollAddMilestone(self):
        icon = self.driver.find_element(By.XPATH, self.btn_addmilestone_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", icon)

    def clickAddMilestone(self):
        self.driver.find_element(By.XPATH, self.btn_addmilestone_xpath).click()

    def scrollSaveMilestone(self):
        icon = self.driver.find_element(By.XPATH, self.btn_savemilestone_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", icon)
    def clickSaveMilestone(self):
        self.driver.find_element(By.XPATH, self.btn_savemilestone_xpath).click()

    def clickDeletemilestone(self):
        self.driver.find_element(By.XPATH, self.btn_milestonedelete_xpath).click()

    def mouseHoverclickMilestone(self):
        # Find the element to hover over
        element_to_hover_over = self.driver.find_element(By.XPATH, self.btn_mousehovermilestone_xpath)

        # Create an ActionChains object
        action_chains = ActionChains(self.driver)

        # Perform the mouse hover action
        action_chains.move_to_element(element_to_hover_over).perform()

        # After performing the hover action, you can interact with the elements that appear after the hover
        # For example, you can click on an element that appears after the hover
        element_to_click = self.driver.find_element(By.XPATH, self.btn_hoverdeleteiconmilestone_xpath)
        element_to_click.click()

    def scrollSociallinksicon(self):
        icon=self.driver.find_element(By.XPATH, self.icon_sociallink_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", icon)

    def clickSociallinksicon(self):
        self.driver.find_element(By.XPATH, self.icon_sociallink_xpath).click()

    def typeFacebooklink(self, facebook):
        input1 = self.driver.find_element(By.XPATH, self.input_facebook_xpath).is_displayed()
        self.logger.info("Is Displayed: %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_facebook_xpath).is_enabled()
        self.logger.info("Is Enabled: %s", input2)
        self.driver.find_element(By.XPATH, self.input_facebook_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_facebook_xpath).send_keys(facebook)

    def withoutFacebooklink(self):
        self.driver.find_element(By.XPATH, self.input_facebook_xpath).clear()
        #self.driver.find_element(By.XPATH, self.input_facebook_xpath).send_keys(" ")

    def typeTwitterlink(self, twitter):
        input1 = self.driver.find_element(By.XPATH, self.input_twitter_xpath).is_displayed()
        self.logger.info("Is Displayed: %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_twitter_xpath).is_enabled()
        self.logger.info("Is Enabled: %s", input2)
        self.driver.find_element(By.XPATH, self.input_twitter_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_twitter_xpath).send_keys(twitter)

    def withoutTwitterlink(self):
        self.driver.find_element(By.XPATH, self.input_twitter_xpath).clear()
        #self.driver.find_element(By.XPATH, self.input_twitter_xpath).send_keys(" ")

    def typeLinkedinlink(self, linkedin):
        input1 = self.driver.find_element(By.XPATH, self.input_linkedin_xpath).is_displayed()
        self.logger.info("Is Displayed: %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_linkedin_xpath).is_enabled()
        self.logger.info("Is Enabled: %s", input2)
        self.driver.find_element(By.XPATH, self.input_linkedin_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_linkedin_xpath).send_keys(linkedin)

    def withoutLinkedinlink(self):
        self.driver.find_element(By.XPATH, self.input_linkedin_xpath).clear()
        #self.driver.find_element(By.XPATH, self.input_linkedin_xpath).send_keys(" ")

    def typeInstagramlink(self, instagram):
        input1 = self.driver.find_element(By.XPATH, self.input_instagram_xpath).is_displayed()
        self.logger.info("Is Displayed: %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_instagram_xpath).is_enabled()
        self.logger.info("Is Enabled: %s", input2)
        self.driver.find_element(By.XPATH, self.input_instagram_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_instagram_xpath).send_keys(instagram)

    def withoutInstagramlink(self):
        self.driver.find_element(By.XPATH, self.input_instagram_xpath).clear()
        #self.driver.find_element(By.XPATH, self.input_instagram_xpath).send_keys(" ")

    def typeWebsitelink(self, websitelink):
        input1 = self.driver.find_element(By.XPATH, self.input_website_xpath).is_displayed()
        self.logger.info("Is Displayed: %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_website_xpath).is_enabled()
        self.logger.info("Is Enabled: %s", input2)
        self.driver.find_element(By.XPATH, self.input_website_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_website_xpath).send_keys(websitelink)

    def withoutWebsitelink(self):
        self.driver.find_element(By.XPATH, self.input_website_xpath).clear()
        #self.driver.find_element(By.XPATH, self.input_website_xpath).send_keys(" ")

    def clickSavesociallinks(self):
        self.driver.find_element(By.XPATH, self.btn_savesociallinks_xpath).click()

    def clickFBlink(self):
        self.driver.find_element(By.XPATH, self.btn_FBlink_xpath).click()

        new_window_handle = WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.logger.info("FaceBook URL is: %s", self.driver.current_url)
        self.driver.save_screenshot(".\\Screenshots\\" + "FB.png")
        self.driver.close()  # Close the new window
        self.driver.switch_to.window(self.driver.window_handles[0])  # Switch back to the original window

    def clickTwitterlink(self):
        self.driver.find_element(By.XPATH, self.btn_Twitterlink_xpath).click()
        # Wait for the new window to open
        new_window_handle = WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))

        # Switch to the new window
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.logger.info("Twitter URL is: %s", self.driver.current_url)
        self.driver.save_screenshot(".\\Screenshots\\" + "Twitter.png")
        # Close the new window
        self.driver.close()

        # Switch back to the original window
        self.driver.switch_to.window(self.driver.window_handles[0])

    def clickLinkedinlink(self):
        self.driver.find_element(By.XPATH, self.btn_LinkedInlink_xpath).click()

        new_window_handle = WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.logger.info("LinkedIn URL is: %s", self.driver.current_url)
        self.driver.save_screenshot(".\\Screenshots\\" + "LinkedIn.png")
        self.driver.close()  # Close the new window
        self.driver.switch_to.window(self.driver.window_handles[0])  # Switch back to the original window

    def clickInstalink(self):
        self.driver.find_element(By.XPATH, self.btn_Instalink_xpath).click()

        new_window_handle = WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.logger.info("Instagram URL is: %s", self.driver.current_url)
        self.driver.save_screenshot(".\\Screenshots\\" + "Insta.png")
        self.driver.close()  # Close the new window
        self.driver.switch_to.window(self.driver.window_handles[0])  # Switch back to the original window

    def clickWebsitelink(self):
        self.driver.find_element(By.XPATH, self.btn_Websitelink_xpath).click()

        new_window_handle = WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.logger.info("Website URL is: %s", self.driver.current_url)
        self.driver.save_screenshot(".\\Screenshots\\" + "Website.png")
        self.driver.close()  # Close the new window
        self.driver.switch_to.window(self.driver.window_handles[0])  # Switch back to the original window

    def clickEditbusinesscard(self):
        self.driver.find_element(By.XPATH, self.btn_editbcard_xpath).click()


    def scrollInstitutename(self):
        icon = self.driver.find_element(By.XPATH, self.input_institutename_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", icon)

    def typeInstitutename(self):
        input1 = self.driver.find_element(By.XPATH, self.input_institutename_xpath).is_displayed()
        self.logger.info("Is Displayed: %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_institutename_xpath).is_enabled()
        self.logger.info("Is Enabled: %s", input2)

    def typeTagline(self, tagline):
        input1 = self.driver.find_element(By.XPATH, self.input_tagline_xpath).is_displayed()
        self.logger.info("Is Displayed: %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_tagline_xpath).is_enabled()
        self.logger.info("Is Enabled: %s", input2)
        self.driver.find_element(By.XPATH, self.input_tagline_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_tagline_xpath).send_keys(tagline)

    def withoutTagline(self):
        self.driver.find_element(By.XPATH, self.input_tagline_xpath).clear()

    def invalidTagline(self):
        self.driver.find_element(By.XPATH, self.input_tagline_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_tagline_xpath).send_keys("      ")
    def typeFoundedyear(self, foundedyear):
        input1 = self.driver.find_element(By.XPATH, self.input_foundedyear_xpath).is_displayed()
        self.logger.info("Is Displayed: %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_foundedyear_xpath).is_enabled()
        self.logger.info("Is Enabled: %s", input2)
        self.driver.find_element(By.XPATH, self.input_foundedyear_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_foundedyear_xpath).send_keys(foundedyear)

    def withoutFoundedyear(self):
        self.driver.find_element(By.XPATH, self.input_foundedyear_xpath).clear()

    def invalidFoundedyear(self):
        self.driver.find_element(By.XPATH, self.input_foundedyear_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_foundedyear_xpath).send_keys("         ")
    def typeNoofstudents(self, noofstudents):
        input1 = self.driver.find_element(By.XPATH, self.input_noofstudents_xpath).is_displayed()
        self.logger.info("Is Displayed: %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_noofstudents_xpath).is_enabled()
        self.logger.info("Is Enabled: %s", input2)
        self.driver.find_element(By.XPATH, self.input_noofstudents_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_noofstudents_xpath).send_keys(noofstudents)

    def withoutNoofstudents(self):
        self.driver.find_element(By.XPATH, self.input_noofstudents_xpath).clear()

    def invalidNoofstudents(self):
        self.driver.find_element(By.XPATH, self.input_noofstudents_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_noofstudents_xpath).send_keys("        ")

    def typeNoofcourses(self, noofcourses):
        input1 = self.driver.find_element(By.XPATH, self.input_noofcourses_xpath).is_displayed()
        self.logger.info("Is Displayed: %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_noofcourses_xpath).is_enabled()
        self.logger.info("Is Enabled: %s", input2)
        self.driver.find_element(By.XPATH, self.input_noofcourses_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_noofcourses_xpath).send_keys(noofcourses)

    def withoutNoofcourses(self):
        self.driver.find_element(By.XPATH, self.input_noofcourses_xpath).clear()

    def invalidNoofcourses(self):
        self.driver.find_element(By.XPATH, self.input_noofcourses_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_noofcourses_xpath).send_keys("        ")
    def typeNoofcompaniestrusting(self, noofcompaniestrusting):
        input1 = self.driver.find_element(By.XPATH, self.input_noofcompaniestrusting_xpath).is_displayed()
        self.logger.info("Is Displayed: %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_noofcompaniestrusting_xpath).is_enabled()
        self.logger.info("Is Enabled: %s", input2)
        self.driver.find_element(By.XPATH, self.input_noofcompaniestrusting_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_noofcompaniestrusting_xpath).send_keys(noofcompaniestrusting)

    def withoutNoofcompaniestrusting(self):
        self.driver.find_element(By.XPATH, self.input_noofcompaniestrusting_xpath).clear()

    def invalidNoofcompaniestrusting(self):
        self.driver.find_element(By.XPATH, self.input_noofcompaniestrusting_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_noofcompaniestrusting_xpath).send_keys("      ")


    def typeSummary(self, summary):
        input1 = self.driver.find_element(By.XPATH, self.input_summary_xpath).is_displayed()
        self.logger.info("Is Displayed: %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_summary_xpath).is_enabled()
        self.logger.info("Is Enabled: %s", input2)
        self.driver.find_element(By.XPATH, self.input_summary_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_summary_xpath).send_keys(summary)

    def withoutSummary(self):
        self.driver.find_element(By.XPATH, self.input_summary_xpath).clear()

    def invalidSummary(self):
        self.driver.find_element(By.XPATH, self.input_summary_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_summary_xpath).send_keys("       ")

    def typeAddress1(self, address1):
        input1 = self.driver.find_element(By.XPATH, self.input_address1_xpath).is_displayed()
        self.logger.info("Is Displayed: %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_address1_xpath).is_enabled()
        self.logger.info("Is Enabled: %s", input2)
        self.driver.find_element(By.XPATH, self.input_address1_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_address1_xpath).send_keys(address1)

    def withoutAddress1(self):
        self.driver.find_element(By.XPATH, self.input_address1_xpath).clear()

    def invalidAddress1(self):
        self.driver.find_element(By.XPATH, self.input_address1_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_address1_xpath).send_keys("        ")

    def typeAddress2(self, address2):
        input1 = self.driver.find_element(By.XPATH, self.input_address2_xpath).is_displayed()
        self.logger.info("Is Displayed: %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_address2_xpath).is_enabled()
        self.logger.info("Is Enabled: %s", input2)
        self.driver.find_element(By.XPATH, self.input_address2_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_address2_xpath).send_keys(address2)

    def withoutAddress2(self):
        self.driver.find_element(By.XPATH, self.input_address2_xpath).clear()

    def invalidAddress2(self):
        self.driver.find_element(By.XPATH, self.input_address2_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_address2_xpath).send_keys("        ")

    def typeCity(self, city):
        input1 = self.driver.find_element(By.XPATH, self.input_city_xpath).is_displayed()
        self.logger.info("Is Displayed: %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_city_xpath).is_enabled()
        self.logger.info("Is Enabled: %s", input2)
        self.driver.find_element(By.XPATH, self.input_city_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_city_xpath).send_keys(city)

    def withoutCity(self):
        self.driver.find_element(By.XPATH, self.input_city_xpath).clear()

    def invalidCity(self):
        self.driver.find_element(By.XPATH, self.input_city_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_city_xpath).send_keys("             ")

    def typeState(self, state):
        input1 = self.driver.find_element(By.XPATH, self.input_state_xpath).is_displayed()
        self.logger.info("Is Displayed: %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_state_xpath).is_enabled()
        self.logger.info("Is Enabled: %s", input2)
        self.driver.find_element(By.XPATH, self.input_state_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_state_xpath).send_keys(state)

    def withoutState(self):
        self.driver.find_element(By.XPATH, self.input_state_xpath).clear()

    def invalidState(self):
        self.driver.find_element(By.XPATH, self.input_state_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_state_xpath).send_keys("        ")

    def numberState(self):
        self.driver.find_element(By.XPATH, self.input_state_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_state_xpath).send_keys("12345678")


    def typeCountry(self, country):
        input1 = self.driver.find_element(By.XPATH, self.input_country_xpath).is_displayed()
        self.logger.info("Is Displayed: %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_country_xpath).is_enabled()
        self.logger.info("Is Enabled: %s", input2)
        self.driver.find_element(By.XPATH, self.input_country_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_country_xpath).send_keys(country)


    def withoutCountry(self):
        self.driver.find_element(By.XPATH, self.input_country_xpath).clear()

    def invalidCountry(self):
        self.driver.find_element(By.XPATH, self.input_country_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_country_xpath).send_keys("       ")

    def numberCountry(self):
        self.driver.find_element(By.XPATH, self.input_country_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_country_xpath).send_keys("123456789")

    def typePincode(self, pincode):
        input1 = self.driver.find_element(By.XPATH, self.input_pincode_xpath).is_displayed()
        self.logger.info("Is Displayed: %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_pincode_xpath).is_enabled()
        self.logger.info("Is Enabled: %s", input2)
        self.driver.find_element(By.XPATH, self.input_pincode_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_pincode_xpath).send_keys(pincode)


    def withoutPincode(self):
        self.driver.find_element(By.XPATH, self.input_pincode_xpath).clear()

    def invalidPincode(self):
        self.driver.find_element(By.XPATH, self.input_pincode_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_pincode_xpath).send_keys("          ")

    def scrollMobile(self):
        icon = self.driver.find_element(By.XPATH, self.input_mobile_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", icon)

    def typeMobile(self):
        input1 = self.driver.find_element(By.XPATH, self.input_mobile_xpath).is_displayed()
        self.logger.info("Is Displayed: %s", input1)
        input2 = self.driver.find_element(By.XPATH, self.input_mobile_xpath).is_enabled()
        self.logger.info("Is Enabled: %s", input2)

    def clickSavebusinesscard(self):
        self.driver.find_element(By.XPATH, self.btn_savebusinesscard_xpath).click()

    def clickNavbarTrustedCompanies(self):
        self.driver.find_element(By.XPATH, self.navbar_trustedcompanies_xpath).click()
    def scrollTrustedcompanyicon(self):
        icon=self.driver.find_element(By.XPATH, self.icon_trustcompanies_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", icon)

    def clickTrustedcompanyicon(self):
        self.driver.find_element(By.XPATH, self.icon_trustcompanies_xpath).click()

    def typeClientname(self, client):
        self.driver.find_element(By.XPATH, self.input_clientname_xpath).click()
        self.driver.find_element(By.XPATH, self.input_clientname_xpath).send_keys(client)

    def typeClientname1(self):
        self.driver.find_element(By.XPATH, self.input_clientname_xpath).click()
        self.driver.find_element(By.XPATH, self.input_clientname_xpath).send_keys("Cognizant")

    def clickAddcompany(self):
        self.driver.find_element(By.XPATH, self.btn_addcompanyname_xpath).click()

    def clickSaveclients(self):
        self.driver.find_element(By.XPATH, self.btn_saveclients_xpath).click()

    def mouseHoverclick(self):
        # Find the element to hover over
        element_to_hover_over = self.driver.find_element(By.XPATH, self.btn_mousehoverclientname_xpath)

        # Create an ActionChains object
        action_chains = ActionChains(self.driver)

        # Perform the mouse hover action
        action_chains.move_to_element(element_to_hover_over).perform()

        # After performing the hover action, you can interact with the elements that appear after the hover
        # For example, you can click on an element that appears after the hover
        element_to_click = self.driver.find_element(By.XPATH, self.icon_hoverdeleteclient_xpath)
        element_to_click.click()

    def viewCertifiedCourse(self):
        self.driver.find_element(By.XPATH, self.view_certifiedcourse_xpath).click()