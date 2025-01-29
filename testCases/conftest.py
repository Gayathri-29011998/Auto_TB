
import pytest
# import pytest-html
from selenium import webdriver





@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser")
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox Browser")
    else:
        driver = webdriver.Edge()
        print("Launching Edge Browser")
    return driver

def pytest_addoption(parser):  #This will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #This will return the browser value to setup method
    return request.config.getoption("--browser")



##### Pytest HTML Report #####

#It is hook for adding environment info to HTML report

# def pytest_configure(config):
#     config.metadata['Project Name'] = 'Tick Big'
#     config.metadata['Module Name'] = 'Login'
#     config.metadata['Tester'] = 'Gayathri'
#
# #It is hook for delete/modify environment info to HTML report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)
