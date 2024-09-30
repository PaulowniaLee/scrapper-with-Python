from email import message
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.safari.service import Service as SafariService
# The safaridriver is installed with the Operating System

def test_eight_components():
    driver = webdriver.Safari(service=SafariService)

    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    