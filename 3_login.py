from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get("https://baat-cheet-two.vercel.app/")

email = "yadavtest@gmail.com"
password = "12345"

email_textbox = driver.find_element(By.ID, "email")
password_textbox = driver.find_element(By.ID, "password")

email_textbox.send_keys(email)
password_textbox.send_keys(password)

submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
submit_button.click()

sleep(5)

elements = driver.find_elements(By.XPATH, "//h3[@class='mt-2 text-2xl font-semibold text-gray-900']")

if elements:
    print("Logged in")
else:
    print("Error while logging in")

a_tag = driver.find_element(By.XPATH, "//a[contains(@class, 'group') and @href='/conversations']")
a_tag.click()

while 1:
    continue

driver.quit()

