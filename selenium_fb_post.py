from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
import time

# Load environment variables
load_dotenv()
EMAIL = os.getenv("FB_EMAIL")
PASSWORD = os.getenv("FB_PASSWORD")

# Set up Selenium WebDriver
options = Options()
service = Service()  # Assumes chromedriver is in PATH

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.facebook.com")

# Fill in credentials
time.sleep(3)
driver.find_element(By.ID, "email").send_keys(EMAIL)
driver.find_element(By.ID, "pass").send_keys(PASSWORD)
driver.find_element(By.NAME, "login").click()

# Wait to see result
time.sleep(15)

# search_box.send_keys(Keys.RETURN)

driver.quit()

