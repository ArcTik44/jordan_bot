import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import time


# inicializace driveru
driver = webdriver.Firefox(executable_path=r'C:\DRIVERS\geckodriver.exe')
load_dotenv()
acc_email = os.getenv('EMAIL')
acc_pass = os.getenv('PASSWORD')



# načtení stránky
driver.get("https://www.solebox.com/en_CZ/login")

reject_btn = driver.find_element(By.ID,"onetrust-reject-all-handler")
reject_btn.click()

#newsletter_btn = driver.find_element(By.CLASS_NAME,"js-close-btn a-modal-close-button close")
#newsletter_btn.click()

# najdeme pole pro email a heslo a vyplníme je
email_field = driver.find_element(By.ID,"dwfrm_profile_customer_email")
email_field.send_keys(acc_email)

password_field = driver.find_element(By.ID,"dwfrm_profile_login_password")
password_field.send_keys(acc_pass)
time.sleep(3)

# klikneme na tlačítko "Login"
login_button = driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div[2]/div[2]/div/div[1]/form/div[2]/div[6]/button")
login_button.click()

# necháme driver počkat pár sekund na načtení stránky
time.sleep(3)

# získáme html kód načtené stránky a vypíšeme ho

driver.get("https://www.solebox.com/en_CZ")

searcher = driver.find_element(By.XPATH,"/html/body/div[2]/header/div/div[2]/div/div/div[1]/div[4]/div/div/div/div/div/form/div[1]/div/input[1]")
html = searcher.send_keys("02170971")

link_to_shoes = driver.find_element()

print(html)

# ukončíme driver
driver.quit()