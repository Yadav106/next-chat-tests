from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://baat-cheet-two.vercel.app/")

register_text = driver.find_element(By.CLASS_NAME, "cursor-pointer")
register_text.click()

name = input("Enter name : ")
email = input("Enter email : ")
password = input("Enter password : ")

name_textbox = driver.find_element(By.ID, "name")
email_textbox = driver.find_element(By.ID, "email")
password_textbox = driver.find_element(By.ID, "password")

name_textbox.send_keys(name)
email_textbox.send_keys(email)
password_textbox.send_keys(password)

submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
submit_button.click()

while 1:
    continue

driver.quit()

