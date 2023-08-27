from selenium.webdriver.common.by import By

class LoginPage():

    def __init__(self,driver):
        self.driver = driver




    username = (By.ID,"login-username")
    password = (By.NAME,"password")
    submit_button = (By.XPATH,"//button[@id='js-login-btn']")
    error_msg = (By.CSS_SELECTOR,"#js-notification-box-msg")

    def get_usernmae(self):
        return self.driver.find_element(*LoginPage.username)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_submit(self):
        return self.driver.find_element(*LoginPage.submit_button)

    def get_errormessage(self):
        return self.driver.find_element(*LoginPage.error_msg)

    def login_to_vwo(self,user,pwd):
        self.get_usernmae().send_keys(user)
        self.get_password().send_keys(pwd)
        self.get_submit().click()
