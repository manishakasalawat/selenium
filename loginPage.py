from selenium.webdriver.common.by import By
class loginPage():
    #Locators of all the elements
    textbox_username_name = "user-name"
    textbox_password_name = "password"
    login_name = "login-button"
    button_add_to_cart_sauce_labs_backpack_name = "add-to-cart-sauce-labs-backpack"
    button_cart_xpath = "//*[@id='shopping_cart_container']"
    button_remove_from_cart_sauce_labs_backpack_name = "remove-sauce-labs-backpack"
    button_continue_shopping_id = "continue-shopping"
    button_add_to_cart_t_shirt_id = "add-to-cart-test.allthethings()-t-shirt-(red)"
    button_checkout_name = "checkout"
    button_continue_id= "continue"
    textbox_firstname_name = "firstName"
    textbox_lastname_name = "lastName"
    textbox_postalcode_name = "postalCode"
    button_finish_name = "finish"
    button_back_to_home_name = "back-to-products"
    button_menu_id = "react-burger-menu-btn"
    button_logout_id = "logout_sidebar_link"

    def __init__(self,driver): #constructor
        self.driver = driver

    def setUsername(self,username):
        self.driver.find_element(By.NAME,self.textbox_username_name).send_keys(username)  # search and send username

    def setPassword(self,password):
        self.driver.find_element(By.NAME,self.textbox_password_name).send_keys(password)  # search and send password

    def clickLogin(self):
        self.driver.find_element(By.NAME,self.login_name).click()  # click login

    def clickSetsauce_backpack(self):
        self.driver.find_element(By.NAME,self.button_add_to_cart_sauce_labs_backpack_name).click()  # click add_to_cart_sauce_backpack

    def clickAdd_to_cart(self):
        self.driver.find_element(By.XPATH,self.button_cart_xpath).click()  # click add_to_cart_button

    def clickRemove_backpack(self):
        self.driver.find_element(By.NAME,self.button_remove_from_cart_sauce_labs_backpack_name).click()  # click on remove_from_cart

    def clickContinue_shopping(self):
        self.driver.find_element(By.ID,self.button_continue_shopping_id).click() # click on continue shopping

    def clickAdd_tshirt(self):
        self.driver.find_element(By.ID,self.button_add_to_cart_t_shirt_id).click()  # click onadd_to_acrt tshirt
    #repeat def clickAdd_to_cart(self):

    def clickCheckout(self):
        self.driver.find_element(By.NAME,self.button_checkout_name).click() #click on checkout

    def setFirstname(self,firstname):
        self.driver.find_element(By.NAME,self.textbox_firstname_name).send_keys(firstname)  # search and send firstname

    def setLastname(self,lastname):
        self.driver.find_element(By.NAME,self.textbox_lastname_name).send_keys(lastname)  # search and send lastname

    def setPostalcode(self,postalcode):
        self.driver.find_element(By.NAME,self.textbox_postalcode_name).send_keys(postalcode)  # search and send postalcode
    #add continue
    def clickContinue(self):
        self.driver.find_element(By.ID,self.button_continue_id).click()
    def clickFinish(self):
        self.driver.find_element(By.NAME,self.button_finish_name).click() #click on Finish

    def clickBackhome(self):
        self.driver.find_element(By.NAME,self.button_back_to_home_name).click() #click on back home

    def clickMenu(self):
        self.driver.find_element(By.ID,self.button_menu_id).click() #click on menu

    def clickLogout(self):
        self.driver.find_element(By.ID,self.button_logout_id).click()  # click on logout

    def checkLogout(self):
        if(self.driver.find_element(By.NAME,self.login_name).is_enabled() == True) :
            print("login page verified")









