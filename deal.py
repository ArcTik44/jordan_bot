from selenium.webdriver.common.by import By
import time

def FindShoesById(driver,shoe_id,shoe_size): 
    search_bar = driver.find_element(By.XPATH, "/html/body/div[2]/header/div/div[2]/div/div/div[1]/div[4]/div/div/div/div/div/form/div[1]/div/input[1]")
    search_bar.send_keys(shoe_id)
    search_bar.submit()
    time.sleep(4)

# klikni 1. nalezenou botu
    select_shoe = driver.find_element(By.XPATH,f"//div[@data-pid='{shoe_id}']")
    select_shoe.click()
 
# najdeme velikost produktu a klikneme na ni
    driver.implicitly_wait(2)
    size = driver.find_element(By.XPATH, f"//span[@data-attr-value='{shoe_size}']")
    size.click()

# počkáme na načtení velikostí
    time.sleep(2)

# najdeme tlačítko "Přidat do košíku" a klikneme na něj
    add_to_cart = driver.find_element(By.XPATH, f"//button[@aria-label='Add to Cart']")
    add_to_cart.click()
    time.sleep(3)