import configparser

config = configparser.ConfigParser()
config.read('C:\\Users\\user\\PycharmProjects\\python framework\\configurations\\config.ini')

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('settings','baseurl')
        return url

    @staticmethod
    def getUseremail():
        username = config.get('settings', 'useremail')
        return username

    @staticmethod
    def getinvalidusername():
        invalidusername = config.get('settings', 'invalidusername')
        return invalidusername

    @staticmethod
    def getPassword():
        password = config.get('settings', 'password')
        return password

    @staticmethod
    def getinvalidpassword():
        invalidpassword = config.get('settings', 'invalidpassword')
        return invalidpassword
    @staticmethod
    def getquote():
        quote = config.get('settings','quote')
        return quote
    @staticmethod
    def getabout():
        aboutdescription = config.get('settings','aboutdescription')
        return aboutdescription
    @staticmethod
    def getcourse():
        course = config.get('settings','course')
        return course
    @staticmethod
    def geteditcourse():
        editcourse = config.get('settings','editcourse')
        return editcourse
    @staticmethod
    def getspecialprogram():
        specialprogram = config.get('settings','specialprogram')
        return specialprogram

    @staticmethod
    def getpercentage():
        percentage = config.get('settings','percentage')
        return percentage

    @staticmethod
    def gettotalpersonplaced():
        totalpersonplaced = config.get('settings','totalpersonplaced')
        return totalpersonplaced

    @staticmethod
    def geteditpercentage():
        editpercentage = config.get('settings','editpercentage')
        return editpercentage

    @staticmethod
    def getedittotalpersonplaced():
        edittotalpersonplaced = config.get('settings','edittotalpersonplaced')
        return edittotalpersonplaced

    @staticmethod
    def getmilestoneyear():
        milestoneyear = config.get('settings','milestoneyear')
        return milestoneyear

    @staticmethod
    def getmilestonedescri():
        milestonedescription = config.get('settings','milestonedescription')
        return milestonedescription

    @staticmethod
    def getaddmilestoneyear():
        addmilestoneyear = config.get('settings','addmilestoneyear')
        return addmilestoneyear

    @staticmethod
    def getaddmilestonedesc():
        addmilestonedesc = config.get('settings','addmilestonedesc')
        return addmilestonedesc

    @staticmethod
    def getfacebooklink():
        facebook = config.get('settings','facebook')
        return facebook

    @staticmethod
    def gettwitterlink():
        twitter = config.get('settings','twitter')
        return twitter

    @staticmethod
    def getlinkedinlink():
        linkedin = config.get('settings','linkedin')
        return linkedin

    @staticmethod
    def getinstagramlink():
        instagram = config.get('settings','instagram')
        return instagram

    @staticmethod
    def getwebsitelink():
        websitelink = config.get('settings','websitelink')
        return websitelink

    @staticmethod
    def gettagline():
        tagline = config.get('settings', 'tagline')
        return tagline

    @staticmethod
    def getfoundedyear():
        foundedyear = config.get('settings', 'foundedyear')
        return foundedyear

    @staticmethod
    def getnoofstudents():
        noofstudents = config.get('settings', 'noofstudents')
        return noofstudents

    @staticmethod
    def getnoofcourses():
        noofcourses = config.get('settings', 'noofcourses')
        return noofcourses

    @staticmethod
    def getnoofcompaniestrusting():
        noofcompaniestrusting = config.get('settings', 'noofcompaniestrusting')
        return noofcompaniestrusting

    @staticmethod
    def getsummary():
        summary = config.get('settings', 'summary')
        return summary

    @staticmethod
    def getaddress1():
        address1 = config.get('settings', 'address1')
        return address1

    @staticmethod
    def getaddress2():
        address2 = config.get('settings', 'address2')
        return address2

    @staticmethod
    def getcity():
        city = config.get('settings', 'city')
        return city

    @staticmethod
    def getstate():
        state = config.get('settings', 'state')
        return state

    @staticmethod
    def getcountry():
        country = config.get('settings', 'country')
        return country

    @staticmethod
    def getpincode():
        pincode = config.get('settings', 'pincode')
        return pincode

    @staticmethod
    def getclient():
        client = config.get('settings', 'client')
        return client

    @staticmethod
    def getservicetitle():
        servicetitle = config.get('settings', 'servicetitle')
        return servicetitle

    @staticmethod
    def getservicecontent():
        servicecontent = config.get('settings', 'servicecontent')
        return servicecontent

    @staticmethod
    def getsolutiontitle():
        solutiontitle = config.get('settings', 'solutiontitle')
        return solutiontitle

    @staticmethod
    def getsolutioncontent():
        solutioncontent = config.get('settings', 'solutioncontent')
        return solutioncontent

    @staticmethod
    def getemail():
        signupemail = config.get('settings', 'signupemail')
        return signupemail

    @staticmethod
    def getpassword():
        signuppassword = config.get('settings', 'signuppassword')
        return signuppassword

    @staticmethod
    def getconfirmpassword():
        signupconfirmpassword = config.get('settings', 'signupconfirmpassword')
        return signupconfirmpassword

    @staticmethod
    def getfirstname():
        firstname = config.get('settings', 'firstname')
        return firstname

    @staticmethod
    def getlastname():
        lastname = config.get('settings', 'lastname')
        return lastname

    @staticmethod
    def getcollegename():
        collegename = config.get('settings', 'collegename')
        return collegename

    @staticmethod
    def getregistername():
        registername = config.get('settings', 'registername')
        return registername

    @staticmethod
    def getwebsite():
        website = config.get('settings', 'website')
        return website

    @staticmethod
    def getmobile():
        mobile = config.get('settings', 'mobile')
        return mobile

    @staticmethod
    def getlenemail():
        lengthemail = config.get('settings', 'lengthemail')
        return lengthemail

    @staticmethod
    def getlenpassword():
        lengthpassword = config.get('settings', 'lengthpassword')
        return lengthpassword

    @staticmethod
    def getshortemail():
        shortemail = config.get('settings', 'shortemail')
        return shortemail

    @staticmethod
    def getshortpassword():
        shortpasssword = config.get('settings', 'shortpasssword')
        return shortpasssword

    @staticmethod
    def getinvalidemail():
        invalidemail = config.get('settings', 'invalidemail')
        return invalidemail

    @staticmethod
    def getinvalidpass():
        invalidpassword = config.get('settings', 'invalidpassword')
        return invalidpassword

    @staticmethod
    def getfnnegative1():
        fnnegative1 = config.get('settings', 'fnnegative1')
        return fnnegative1

    @staticmethod
    def getlnnegative1():
        lnnegative1 = config.get('settings', 'lnnegative1')
        return lnnegative1

    @staticmethod
    def getfnnegative2():
        fnnegative2 = config.get('settings', 'fnnegative2')
        return fnnegative2

    @staticmethod
    def getlnnegative2():
        lnnegative2 = config.get('settings', 'lnnegative2')
        return lnnegative2

    @staticmethod
    def getfnnegative3():
        fnnegative3 = config.get('settings', 'fnnegative3')
        return fnnegative3


    @staticmethod
    def getlnnegative3():
        lnnegative3 = config.get('settings', 'lnnegative3')
        return lnnegative3

    #Post Job Positive
    @staticmethod
    def getdesignation():
        designation = config.get('settings', 'designation')
        return designation

    @staticmethod
    def getexperiencemin():
        experiencemin = config.get('settings', 'experiencemin')
        return experiencemin

    @staticmethod
    def getexperiencemax():
        experiencemax = config.get('settings', 'experiencemax')
        return experiencemax

    @staticmethod
    def getlocation():
        location = config.get('settings', 'location')
        return location

    @staticmethod
    def getsalarymin():
        salarymin = config.get('settings', 'salarymin')
        return salarymin

    @staticmethod
    def getsalarymax():
        salarymax = config.get('settings', 'salarymax')
        return salarymax

    @staticmethod
    def getjobdescription():
        jobdescription = config.get('settings', 'jobdescription')
        return jobdescription

    @staticmethod
    def getjobresponsiblities():
        jobresponsiblities = config.get('settings', 'jobresponsiblities')
        return jobresponsiblities

    @staticmethod
    def getskill():
        skill = config.get('settings', 'skill')
        return skill

    @staticmethod
    def getinvestorname():
        investorname = config.get('settings', 'investorname')
        return investorname

    @staticmethod
    def getinvesmentexperience():
        invesmentexperience = config.get('settings', 'invesmentexperience')
        return invesmentexperience

    @staticmethod
    def gettotalamountinvest():
        totalamountinvest = config.get('settings', 'totalamountinvest')
        return totalamountinvest

    @staticmethod
    def getnoofpreviousinvestcompany():
        noofpreviousinvestcompany = config.get('settings', 'noofpreviousinvestcompany')
        return noofpreviousinvestcompany

    @staticmethod
    def getevaluationduration():
        evaluationduration = config.get('settings', 'evaluationduration')
        return evaluationduration

    @staticmethod
    def getinvestrangemin():
        investrangemin = config.get('settings', 'investrangemin')
        return investrangemin

    @staticmethod
    def getinvestrangemax():
        investrangemax = config.get('settings', 'investrangemax')
        return investrangemax
