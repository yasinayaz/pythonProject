from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pages.qlub_utils


def page_click_on_pay_the_bill(driver):
    buttonPayNow = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pages.qlub_utils.BUTTON_PAY_NOW)))
    buttonPayNow.click()
    time.sleep(3)

def page_click_on_let_split_the_bill(driver):
    buttonSplitBill = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pages.qlub_utils.BUTTON_SPLIT_BILL)))
    buttonSplitBill.click()
    time.sleep(1)

def page_custom_amount(driver):
    selectButtonCustomAmount = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pages.qlub_utils.BUTTON_CUSTOM_AMOUNT)))
    selectButtonCustomAmount.click()
    time.sleep(1)

def page_set_amaount(driver):
    setAmount = driver.find_element(By.XPATH, pages.qlub_utils.SET_AMOUNT)
    time.sleep(3)
    setAmount.send_keys(20)
    time.sleep(1)

def page_confirm_button(driver):
    buttonConfirm = driver.find_element(By.ID, pages.qlub_utils.BUTTON_CONFIRM)
    buttonConfirm.click()
    time.sleep(3)

def page_cardNumber(driver):
    iframe = driver.find_element(By.XPATH, pages.qlub_utils.IFRAME_CARD_NUMBER )
    driver.switch_to.frame(iframe)
    cardNumber = driver.find_element(By.ID, pages.qlub_utils.CARD_NUMBER)
    cardNumber.click()
    cardNumber.send_keys(pages.qlub_utils.CARD_NUMBER_VALUE)
    driver.switch_to.default_content()
    time.sleep(3)

def page_card_time(driver):
    iframe = driver.find_element(By.XPATH, pages.qlub_utils.IFRAME_CARD_DATE)
    driver.switch_to.frame(iframe)
    cardTime = driver.find_element(By.ID, pages.qlub_utils.CARD_TIME)
    cardTime.click()
    cardTime.send_keys(pages.qlub_utils.CARD_TIME_VALUE)
    driver.switch_to.default_content()
    time.sleep(2)

def page_cardCvv(driver):
    iframe = driver.find_element(By.XPATH, pages.qlub_utils.IFRAME_CARD_CVV)
    driver.switch_to.frame(iframe)
    cardCvv = driver.find_element(By.ID, pages.qlub_utils.CARD_CVV)
    cardCvv.click()
    cardCvv.send_keys(pages.qlub_utils.CARD_CVV_VALUE)
    driver.switch_to.default_content()
    time.sleep(2)

def page_payNow(driver):
    buttonPay = driver.find_element(By.ID, pages.qlub_utils.BUTTON_PAY)
    buttonPay.click()
    time.sleep(2)

