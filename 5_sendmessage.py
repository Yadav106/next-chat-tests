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

a_tag = driver.find_element(By.XPATH, "//a[contains(@class, 'group') and @href='/conversations']")
a_tag.click()

first_chat = driver.find_element(By.XPATH, "(//div[@class='w-full relative flex mb-[10px] items-center space-x-3 hover:bg-neutral-100 rounded-lg transition cursor-pointer bg-white'])[1]")
first_chat.click()

sleep(2)

message_box = driver.find_element(By.ID, "message")
message_box.send_keys("Hi Test")

send_button = driver.find_element(By.XPATH, "//button[@type='submit']")
send_button.click()

while 1:
    continue

driver.quit()


