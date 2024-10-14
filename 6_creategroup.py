from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.common.keys import Keys

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

a_tag = driver.find_element(By.XPATH, "//a[contains(@class, 'group') and @href='/conversations']")
a_tag.click()

sleep(1)

create_group_element = driver.find_element(By.XPATH, "//div[contains(@class, 'rounded-full') and contains(@class, 'p-2') and contains(@class, 'bg-gray-100') and contains(@class, 'text-gray-600') and contains(@class, 'cursor-pointer') and contains(@class, 'hover:opacity-75') and contains(@class, 'transition')]")

create_group_element.click()

sleep(1)

group_name = driver.find_element(By.ID, "name")
group_name.send_keys("Test Group")

input_field = driver.find_element(By.ID, "react-select-2-input")
input_value = "Sahil Yadav"
input_field.send_keys(input_value)
input_field.send_keys(Keys.RETURN)
input_value = "Simran Yadav"
input_field.send_keys(input_value)
input_field.send_keys(Keys.RETURN)

submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
submit_button.click()

sleep(1)
driver.refresh()

while 1:
    continue

driver.quit()


