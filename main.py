import time
# main branch
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://bestbet.bet/")
driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))

try:
    betslip = driver.find_element(By.XPATH, "//div[@class='load-betslip-wrapper  ng-isolate-scope']//form/input")
    betslip.send_keys("CC43496")
    print(betslip)
except NoSuchElementException as e:
    print("1. No such Elements")

try:
    button = driver.find_element(By.XPATH, "//div[@class='load-betslip-wrapper  ng-isolate-scope']//form/button")
    button.click()
except NoSuchElementException as e:
    print("button: No such Elements")


time.sleep(50)
driver.close()
driver.quit()
print('done')


# CC43496
# xpath:
# //div[contains(@class, 'load-betslip-content')]/form/input
 