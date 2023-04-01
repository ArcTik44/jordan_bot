from selenium.webdriver.common.by import By
import time

def FindShoesById(driver,shoe_id,shoe_size): 
    search_bar = driver.find_element(By.XPATH, "/html/body/div[2]/header/div/div[2]/div/div/div[1]/div[4]/div/div/div/div/div/form/div[1]/div/input[1]")
    search_bar.send_keys(shoe_id)
    search_bar.submit()


# klikni 1. nalezenou botu
    select_shoe = driver.find_element()
    select_shoe.submit()

    print("==>")
# najdeme produkt podle ID a klikneme na něj
    product = driver.find_element(By.XPATH, f"//a[@data-id='{shoe_id}']")
    product.click()

# najdeme velikost produktu a klikneme na ni
    size = driver.find_element(By.XPATH, f"//span[text()='{shoe_size}']")
    size.click()

# počkáme na načtení velikostí
    time.sleep(1)

# vybereme konkrétní velikost a klikneme na ni
    size_option = driver.find_element(By.XPATH, f"//span[text()='{shoe_size}']")
    size_option.click()

# najdeme tlačítko "Přidat do košíku" a klikneme na něj
    add_to_cart = driver.find_element(By.XPATH, "//button[text()='Přidat do košíku']")
    add_to_cart.click()

# počkáme na načtení košíku
    time.sleep(1)