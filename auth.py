from selenium.webdriver.common.by import By
import time

def Login(driver,email,password):
    driver.get("https://www.solebox.com/en_CZ/login")

    time.sleep(2) 
    reject_btn = driver.find_element(By.ID,"onetrust-reject-all-handler")
    reject_btn.click()

    # najdeme pole pro email a heslo a vyplníme je
    email_field = driver.find_element(By.ID,"dwfrm_profile_customer_email")
    email_field.send_keys(email)

    password_field = driver.find_element(By.ID,"dwfrm_profile_login_password")
    password_field.send_keys(password)
    time.sleep(3)

    login_button = driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div[2]/div[2]/div/div[1]/form/div[2]/div[6]/button")
    login_button.click()

    # necháme driver počkat pár sekund na načtení stránky
    time.sleep(3)

    # získáme html kód načtené stránky a vypíšeme ho

    driver.get("https://www.solebox.com/en_CZ")
