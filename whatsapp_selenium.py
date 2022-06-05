import time
import os

# selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.service import Service

# kill all chrome and chromedriver process
os.system("pkill chrome")
os.system("pkill chromedriver")

# web page elements path
NEW_CHAT_BTN = "/html/body/div[1]/div/div/div[3]/div/header/div[2]/div/span/div[2]/div/span"
INPUT_TXT_BOX = "/html/body/div[1]/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/div/div[2]/div/div[2]"
ONLINE_STATUS_LABEL = "/html/body/div[1]/div/div/div[4]/div/header/div[2]/div[2]/span"

# chat list of users
TARGETS = {'whatsapp user 1 name': 'phone number 1',
           'whatsapp user 2 name': 'phone number 2'}

options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=/home/bhagirath/.config/google-chrome/")
options.add_argument("--profile-directory=Default")
capabilities = DesiredCapabilities.CHROME.copy()

service = Service("./driver/chromedriver")

browser = webdriver.Chrome(service=service, options=options, desired_capabilities=capabilities)

browser.get("https://web.whatsapp.com/")
wait = WebDriverWait(browser, 60)

while True:
    for target in TARGETS:
        tryAgain = True
        new_chat_title = wait.until(
            EC.presence_of_element_located((By.XPATH, NEW_CHAT_BTN)))
        while (tryAgain):
            try:
                new_chat_title.click()
                input_box = wait.until(
                    EC.presence_of_element_located((By.XPATH, INPUT_TXT_BOX)))
                time.sleep(0.5)
                input_box.send_keys(TARGETS[target])
                time.sleep(0.5)
                input_box.send_keys(Keys.ENTER)
                time.sleep(2)
                tryAgain = False
                try:
                    try:
                        browser.find_element(By.XPATH, ONLINE_STATUS_LABEL)
                        print(target + ' is online')
                    except:
                        print(target + ' is offline')
                    time.sleep(1)
                except:
                    print('Exception 1 : status is not exist.')
                    time.sleep(10)
            except:
                print('Exception 2 : chat is not exist.')
                time.sleep(4)
