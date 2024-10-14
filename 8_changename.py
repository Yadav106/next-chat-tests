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

div_element = driver.find_element(By.XPATH, "//div[@class='relative inline-block rounded-full overflow-hidden h-9 w-9 md:h-11 md:w-11']")
div_element.click()

name_box = driver.find_element(By.ID, "name")
name_box.send_keys("test_name")

submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
submit_button.click()

while 1:
    continue

driver.quit()


