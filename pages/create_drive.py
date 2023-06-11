import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(".\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://newapp-staging.qlub.cloud/qr/ae/dummy-checkout/90/_/_/1827c10c80")
driver.maximize_window()
