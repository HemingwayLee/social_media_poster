from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
import time
import random

def human_delay(min_ms=100, max_ms=300):
    time.sleep(random.uniform(min_ms / 1000.0, max_ms / 1000.0))

load_dotenv()
EMAIL = os.getenv("FB_EMAIL")
PASSWORD = os.getenv("FB_PASSWORD")

service = Service('./geckodriver')
driver = webdriver.Firefox(service=service)
driver.execute_script("""
Object.defineProperty(navigator, 'webdriver', {
  get: () => undefined,
});
""")
driver.execute_script("""
Object.defineProperty(navigator, 'platform', { get: () => 'MacIntel' });
Object.defineProperty(navigator, 'language', { get: () => 'en-US' });
""")

time.sleep(3)
driver.get("https://www.facebook.com")

# Simulate typing
email_box = driver.find_element(By.ID, "email")
for char in EMAIL:
    email_box.send_keys(char)
    human_delay(50, 150)

pass_box = driver.find_element(By.ID, "pass")
for char in PASSWORD:
    pass_box.send_keys(char)
    human_delay(50, 150)

driver.find_element(By.NAME, "login").click()

# Wait to see result
time.sleep(15)

# search_box.send_keys(Keys.RETURN)

driver.quit()

