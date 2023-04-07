from selenium.webdriver.common.by import By
import time

def Login(driver,email,password):
    driver.get("https://www.solebox.com/en_CZ/login")

    driver.implicitly_wait(5)

    reject_btn = driver.find_element(By.ID,"onetrust-reject-all-handler")
    reject_btn.click()

    # find the login credentials
    email_field = driver.find_element(By.ID,"dwfrm_profile_customer_email")
    email_field.send_keys(email)

    password_field = driver.find_element(By.ID,"dwfrm_profile_login_password")
    password_field.send_keys(password)
    
    time.sleep(2)
    login_button = driver.find_element(By.XPATH,f"//button[contains(@class,'f-button f-button--medium')]")
    login_button.click()

   # go to home screen
    time.sleep(5)

    driver.get("https://www.solebox.com/en_CZ")
