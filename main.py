from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# do loop
x = 1
while True:
    # Open Chrome
    browser = webdriver.Chrome()

    # Open google with keyword
    browser.get('https://www.google.com/search?q=kerajinan+bambu+gunung+kidul')

    # give break before find link
    time.sleep(10)

    # find partial link text with that value
    button = browser.find_element(by=By.PARTIAL_LINK_TEXT, value="Kerajinan Bambu Gunung Kidul Yogyakarta")

    # click partial link
    button.click()

    # give break
    time.sleep(10)

    # Closing browser
    browser.close()
    x+=1