import time
import os

# selenium
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# kill all chrome and chromedriver process
os.system("pkill chrome")
os.system("pkill chromedriver")

options = webdriver.ChromeOptions()
options.add_argument(
    "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36")
options.add_argument("--user-data-dir=/home/bhagirath/.config/google-chrome/")
options.add_argument("--profile-directory=Default")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(options=options, executable_path="./driver/chromedriver")
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Ubuntu 20.04.3 LTS",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )


driver.get("https://contacts.google.com/")
time.sleep(30)
driver.get("https://contacts.google.com/new")
driver.find_element(By.XPATH, '//input[@aria-label="First name"]').send_keys("testing contact")
driver.find_element(By.XPATH, '//input[@aria-label="Phone"]').send_keys("+911234567890")
driver.find_element(By.XPATH, '//button[@aria-label="Save"]').click()
