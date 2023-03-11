from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

import time

# inicializace driveru
driver = webdriver.Firefox()

# načtení stránky
driver.get("https://www.solebox.com/en_CZ/login")

reject_btn = driver.find_element(By.ID,"onetrust-reject-all-handler")
reject_btn.click()

#newsletter_btn = driver.find_element(By.CLASS_NAME,"js-close-btn a-modal-close-button close")
#newsletter_btn.click()

# najdeme pole pro email a heslo a vyplníme je
email_field = driver.find_element(By.ID,"dwfrm_profile_customer_email")
email_field.send_keys("dvangard@seznam.cz")

password_field = driver.find_element(By.ID,"dwfrm_profile_login_password")
password_field.send_keys("Starakrabice404")
time.sleep(3)

# klikneme na tlačítko "Login"
login_button = driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div[2]/div[2]/div/div[1]/form/div[2]/div[6]/button")
login_button.click()

# necháme driver počkat pár sekund na načtení stránky
time.sleep(3)

# získáme html kód načtené stránky a vypíšeme ho
html = driver.get("https://www.solebox.com/en_CZ")
print(html)

# ukončíme driver
driver.quit()