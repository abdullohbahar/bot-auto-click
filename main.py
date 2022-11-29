from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from fake_useragent import UserAgent
import subprocess
import os

# do loop
x = 1
while True:

    # open vpn
    # os.startfile("E:\Project Coding\Python\Bot visitor\psiphon3.exe")
    # time.sleep(5)

    # os.system("TASKKILL /F /IM brave.exe")

    options = Options()

    # ua = UserAgent()

    # userAgent = ua.random

    # options.add_argument(f'user-agent={userAgent}')
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--incognito")

    # Open Chrome
    browser = webdriver.Chrome(chrome_options=options)

    # browser.set_window_position(2000, 0)


    # Open google with keyword
    browser.get('https://www.google.com/search?q=kerajinan+bambu+gunungkidul+yogyakarta')
    time.sleep(5)

    # find partial link text with that value
    button = browser.find_element(by=By.PARTIAL_LINK_TEXT, value="Kerajinan Bambu Gunungkidul Yogyakarta")
    button.click()
    time.sleep(5)

    # open hamburger menu
    button = browser.find_element(by=By.CLASS_NAME, value="navbar-toggler")
    button.click()
    time.sleep(5)

    # click Product menu
    button = browser.find_element(by=By.PARTIAL_LINK_TEXT, value="Produk")
    button.click()
    time.sleep(5)

    # click product item
    button = browser.find_element(by=By.XPATH, value="/html/body/section/div/div/div[2]/div[1]/div/div[2]/div/div[1]/a")
    button.click()
    time.sleep(5)

    # click hamburger menu 2
    button = browser.find_element(by=By.XPATH, value="/html/body/nav/div/button")
    button.click()
    time.sleep(5)

    # click Product menu 2
    button = browser.find_element(by=By.PARTIAL_LINK_TEXT, value="Produk")
    button.click()
    time.sleep(5)

    # click product item 2
    button = browser.find_element(by=By.XPATH, value="/html/body/section/div/div/div[2]/div[2]/div/div[2]/div/div[1]/a")
    button.click()
    time.sleep(5)

    # click hamburger menu 3
    button = browser.find_element(by=By.XPATH, value="/html/body/nav/div/button")
    button.click()
    time.sleep(5)

    # click Product menu 3
    button = browser.find_element(by=By.PARTIAL_LINK_TEXT, value="Produk")
    button.click()
    time.sleep(5)

    # click product item 3
    button = browser.find_element(by=By.XPATH, value="/html/body/section/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a")
    button.click()
    time.sleep(5)

    # click hamburger menu 4
    button = browser.find_element(by=By.XPATH, value="/html/body/nav/div/button")
    button.click()
    time.sleep(5)

    # click Product menu 4
    button = browser.find_element(by=By.PARTIAL_LINK_TEXT, value="Produk")
    button.click()
    time.sleep(5)

    # click product item 4
    button = browser.find_element(by=By.XPATH, value="/html/body/section/div/div/div[2]/div[4]/div/div[2]/div/div[1]/a")
    button.click()
    time.sleep(5)

    # click hamburger menu
    button = browser.find_element(by=By.XPATH, value="/html/body/nav/div/button")
    button.click()
    time.sleep(5)
    
    # click Home
    button = browser.find_element(by=By.XPATH, value="/html/body/nav/div/div/ul/li[1]/a")
    button.click()
    time.sleep(5)
    
    # click hamburger menu
    button = browser.find_element(by=By.XPATH, value="/html/body/nav/div/button")
    button.click()
    time.sleep(5)

    # click struktur organisasi
    button = browser.find_element(by=By.XPATH, value="/html/body/nav/div/div/ul/li[4]/a")
    button.click()
    time.sleep(5)

    # Closing browser
    browser.close()

    # os.system("TASKKILL /F /IM psiphon3.exe")

    # time.sleep(5)

    x+=1