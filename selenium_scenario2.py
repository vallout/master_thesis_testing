from selenium import webdriver
import selenium
from datetime import date, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from time import sleep

# ignore errors for testing
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument("--start-maximized")

PATH = r"C:\Program Files\chromedriver"

driver = webdriver.Chrome(PATH, options=options)

driver.get("http://localhost:3000")

sleep(3)
driver.find_element_by_id("loginField").send_keys("jamal.abara@mail.com")
sleep(.5)
driver.find_element_by_id("loginButton").click()
sleep(.5)

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "administrationNav"))
    )
    element.click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "usageStatsNav"))
    )
    element.click()
    sleep(2)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "gameStatsNav"))
    )
    element.click()
    sleep(100)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "createItemNav"))
    )
    element.click()
    sleep(.5)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//select[@id='itemType']/option[text()='SHOES']"))
    )
    element.click()
    sleep(.5)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "itemName"))
    )
    element.send_keys("Mysterious boots")
    sleep(.5)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "itemDescription"))
    )
    element.send_keys("A mystery")
    sleep(.5)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "itemModelId"))
    )
    element.send_keys("some_item_model")
    sleep(.5)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "createItemButton"))
    )
    element.click()
    sleep(.5)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "id Mysterious boots"))
    )
    id_text = element.text
    item_id = id_text[-24:]
    sleep(.5)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "createChallengeNav"))
    )
    element.click()
    sleep(.5)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//select[@id='groupChallengeEventName']/option[text()='task finished']"))
    )
    element.click()
    sleep(.5)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "groupChallengeDescription"))
    )
    element.send_keys("Finish'em")
    sleep(.5)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "groupChallengeEnd"))
    )
    date = date.today() + timedelta(7)
    date_formatted = date.strftime("%m/%d/%y")
    element.send_keys(Keys.BACKSPACE*10)
    element.send_keys(date_formatted)
    sleep(.5)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "groupChallengeCondition"))
    )
    element.send_keys("100")
    sleep(.5)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "groupChallengeRewardType"))
    )
    element.click()
    sleep(.5)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "groupChallengeItemReward"))
    )
    element.send_keys(item_id)
    sleep(.5)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "createGroupChallengeButton"))
    )
    element.click()
    sleep(.5)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "showChallengesNav"))
    )
    element.click()
    sleep(.5)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "showChallengesNav"))
    )
    element.click()
    sleep(.5)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "activateFinish'em"))
    )
    element.click()
except:
    driver.close()

sleep(10)

driver.close()