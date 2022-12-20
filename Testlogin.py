from selenium import webdriver
import time
#from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import unittest
import HtmlTestRunner
#import sys

#sys.path.append("C://Users//Admin//PycharmProjects//seleniumpython//venv")

from Pages.loginPage import loginPage

class Testlogin(unittest.TestCase):
    baseUrl = "https://www.saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"
    firstname = "abc"
    lastname = "test"
    postalcode = "1234"
    driver_service = Service(executable_path="C:\\Users\\Admin\\PycharmProjects\\seleniumpython\\venv\\driver\\chromedriver.exe")
    driver = webdriver.Chrome(service=driver_service)
    #driver = webdriver.Chrome(executable_path="C:\\Users\\Admin\\PycharmProjects\\seleniumpython\\venv\\driver\\chromedriver.exe")
    print("test1")

    @classmethod
    def setUpClass(cls):
        print("test2")
        cls.driver.get(cls.baseUrl)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_login(self):
        lp = loginPage(self.driver) #calls the constructor from login page
        lp.setUsername(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(2)
        lp.clickSetsauce_backpack()
        time.sleep(2)
        lp.clickAdd_to_cart()
        time.sleep(2)
        lp.clickRemove_backpack()
        time.sleep(2)
        lp.clickContinue_shopping()
        time.sleep(2)
        lp.clickAdd_tshirt()
        time.sleep(2)
        lp.clickAdd_to_cart()
        time.sleep(2)
        lp.clickCheckout()
        time.sleep(2)
        lp.setFirstname(self.firstname)
        lp.setLastname(self.lastname)
        lp.setPostalcode(self.postalcode)
        time.sleep(2)
        lp.clickContinue()
        time.sleep(2)
        lp.clickFinish()
        time.sleep(2)
        lp.clickBackhome()
        time.sleep(2)
        lp.clickMenu()
        time.sleep(2)
        lp.clickLogout()
        time.sleep(2)
        # check login
        lp.checkLogout()


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__=='__main__':
    unittest.main()


"""class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\Program Files\chromedriver\chromedriver.exe")
        # wait for sometimes
        cls.driver.implicitly_wait(5) # seconds(only one time at the beginning of the code) and applicable to all the elemeents
        cls.driver.maximize_window()

    def test_login_valid(self):
        self.driver.get("https://www.saucedemo.com/")  # get the website link
        #print(driver.title)  # returns the title of the page
        #user_ele = self.driver.find_element("name", 'user-name')  # search the element on the basis of username
        #print(user_ele.is_displayed())  # returns true or false based on the status of the element
        #print(user_ele.is_enabled())  # returns T/F if th element is enabled.
        # print.find_element_by_xpath("//*[@id='user-name']")
        #pwd_ele = self.driver.find_element("name", 'password')  # search the element on the basis of password
        #print(pwd_ele.is_displayed())  # returns true or false based on the status of the element
        #print(pwd_ele.is_enabled())  # returns T/F if th eelement is enabled.
        self.driver.find_element("name", 'user-name').send_keys('standard_user') #search and send username
        self.driver.find_element("name", 'password').send_keys('secret_sauce') #search and send password
        self.driver.find_element("name", 'login-button').click()  # login
        time.sleep(2)  # from python
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__=='__main__':
    unittest.main() """
