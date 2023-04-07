import time
from selenium.webdriver.common.by import By
def ProceedCheckout(driver,payment_option,shipping):
    driver.get("https://www.solebox.com/en_CZ/checkout?stage=shipping#shipping")
    
    #close_news_btn = driver.find_element(By.XPATH, f"//button[@aria-label='Close']")
    #close_news_btn.click()
    driver.implicitly_wait(3)

    checkbox_bill_address = driver.find_element(By.XPATH,f"(//input[contains(@class,'js-field f-form-control')]/following-sibling::label)[2]")
    
    if not checkbox_bill_address.is_selected():        
        checkbox_bill_address.click()
    
    if shipping == "EXPRESS":
        radio_express = driver.find_element(By.XPATH,f"(//input[@name='serviceShippingMethod']/following-sibling::span)[3]")
        radio_express.click()

    else:
        radio_standard = driver.find_element(By.XPATH,f"(//input[@name='serviceShippingMethod']/following-sibling::span)[1]")
        radio_standard.click()
    
    driver.implicitly_wait(2)
    to_payment = driver.find_element(By.XPATH,f"//button[@value='submit-shipping']")
    to_payment.click()


    open_pay_options = driver.find_element(By.XPATH,f"(//div[@class='b-checkout-step-edit-wrapper']//a)[2]")
    open_pay_options.click()

    if payment_option == "-c":
        PayByCard(driver)
    if payment_option == "-p":
        PayByPaypal(driver)

    # to check order
    driver.find_element(By.XPATH,f"(//button[@name='submit'])[2]").click()
    time.sleep(1)
    # confirm payment
    driver.find_element(By.XPATH,f"(//button[@name='submit'])[3]").click()


def PayByCard(driver):
    # select payment by card
    driver.find_element(By.XPATH,f"(//input[@class='js-payment f-native-radio-input']/following-sibling::span)[3]").click()

def PayByPaypal(driver):
    # select payment by paypal
    driver.find_element(By.XPATH,f"(//span[@class='f-custom-radio-button'])[5]").click()

    
