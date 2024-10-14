from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://baat-cheet-two.vercel.app/")

expected_title = "Next Chat App"
actual_title = driver.title

if expected_title == actual_title:
    print("Expected Title and Actual Title match, test case passed")
else:
    print(f"Expected {expected_title}, Received {actual_title}")

driver.quit()

