import pytest
from selenium.webdriver import Chrome  # Import the WebDriver class from the correct location
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import random
import requests
from selenium.webdriver.common.keys import Keys
from datetime import datetime

@pytest.fixture()
def driver():
    driver = Chrome()  # Use Chrome() instead of WebDriver.Chrome()
    driver.maximize_window()
    yield driver

def test_login(driver):
    driver.get("https://www.docsmart.in/")
    button_login = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.ID, "loginRegister")))
    button_login.click()

    role = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, ".//div[@class='v-select__selections']")))
    role.click()

    select_role = WebDriverWait(driver,15).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='v-list-item v-list-item--link theme--light'][2]")))
    select_role.click()

    username = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, "//label[text()='Enter your mobile number here.']/following-sibling::input")))
    username.send_keys("1111111111")

    password = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, "//label[text()='Password']/following-sibling::div//input[@type='password']"))
    )
    password.send_keys("Docsmart@20")

    login = driver.find_element(By.XPATH, "//span[normalize-space()='Login']")
    login.click()
    time.sleep(5)

    profile_name = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, "//h6[@class='font-weight-bold line-clamp text-capitalize']"))
    )
    profile_name.click()

    edit_profile = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, "//li[normalize-space()='Edit Profile']"))
    )
    edit_profile.click()

    clinic_details = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Clinic Details']"))
    )
    clinic_details.click()

    Add_clinic = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='v-btn__content'][normalize-space()='Add Clinic']"))

)
    Add_clinic.click()

    time.sleep(5)
    element = driver.find_element(By.XPATH, "//div[@class='v-card__text  v-card-min-height']")

    # Scroll to the element
    scroll_script = "arguments[0].scrollTop += 400;"
    driver.execute_script(scroll_script, element)

    from_time =driver.find_element(By.XPATH, "//div[@class='v-input active d-block v-text-field v-text-field--single-line v-text-field--solo v-text-field--enclosed v-select v-input--hide-details theme--light']//i[@class='v-icon material-icons theme--light'][normalize-space()='arrow_drop_down']")

    from_time.click()
    time.sleep(5)
    list1 = driver.find_element(By.XPATH,"//body/div[@id='app']/div[contains(@class,'v-menu__content theme--light v-menu__content--fixed menuable__content__active')]/div[contains(@class,'v-select-list v-card theme--light')]/div[contains(@role,'list')]/div[1]")
    list1.click()
    time.sleep(5)

    print("list is",from_time.text)



    time.sleep(10)

    to_time = driver.find_element(By.XPATH,"//div[contains(@class,'col-sm-12 nopad')]//div[contains(@class,'col-sm-12')]//div//div[2]//div[1]//div[1]//div[1]//div[1]//div[2]//div[1]//i[1]")
    to_time.click()
    time.sleep(5)
    list2 = driver.find_element(By.XPATH,"//body/div[@id='app']/div[contains(@class,'v-menu__content theme--light v-menu__content--fixed menuable__content__active')]/div[contains(@class,'v-select-list v-card theme--light')]/div[contains(@role,'list')]/div[2]")
    list2.click()


    time.sleep(10)