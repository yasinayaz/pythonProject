import pytest

import pages.qlub_page
from pages.create_drive import driver


class TestPayTheBill:


    def test_click_on_pay_the_bill(self):
        pages.qlub_page.page_click_on_pay_the_bill(driver)

    def test_click_on_let_split_the_bill(self):
        pages.qlub_page.page_click_on_let_split_the_bill(driver)

    def test_custom_amount(self):
        pages.qlub_page.page_custom_amount(driver)

    def test_set_amaount(self):
        pages.qlub_page.page_set_amaount(driver)

    def test_confirm_button(self):
        pages.qlub_page.page_confirm_button(driver)

    def test_cardNumber(self):
        pages.qlub_page.page_cardNumber(driver)

    def test_card_time(self):
        pages.qlub_page.page_card_time(driver)

    def test_cardCvv(self):
        pages.qlub_page.page_cardCvv(driver)


    def test_payNow(self):
        pages.qlub_page.page_payNow(driver)



   # driver.find_element(By.XPATH, "//iframe[@name='checkout-frames-expiryDate']")






