from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from time import sleep

user1_id = "603102758f73645a9cbc7a27"
user2_id = "603102758f73645a9cbc7a28"
user3_id = "603102758f73645a9cbc7a29"

# ignore errors for testing
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument("--start-maximized")

PATH = r"C:\Program Files\chromedriver"

driver = webdriver.Chrome(PATH, options=options)

driver.get("http://localhost:3000")

sleep(3)
# trigger temporary points
driver.find_element_by_id("button1").click()
sleep(.5)
driver.find_element_by_id("button2").click()
sleep(.5)
driver.find_element_by_id("button3").click()
sleep(.5)


driver.find_element_by_id("titleField").send_keys("Mr.")
sleep(.5)
driver.find_element_by_id("firstnameField").send_keys("Jamir")
sleep(.5)
driver.find_element_by_id("lastnameField").send_keys("Gupta")
sleep(.5)
driver.find_element_by_id("emailField").send_keys("jamir.gupta@mail.com")
sleep(.5)

driver.find_element_by_id("submitButton").click()
sleep(.5)
driver.find_element_by_id("loginField").send_keys("jamir.gupta@mail.com")
sleep(.5)
driver.find_element_by_id("loginButton").click()
sleep(.5)
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "profileNav"))
    )
    element.click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "userPhone"))
    )
    element.send_keys("0123456789")
    sleep(.5)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "userImage"))
    )
    element.send_keys("some_picture_id")
    sleep(.5)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "confirmProfile"))
    )
    element.click()
    sleep(.5)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "avatarAndShopNav"))
    )
    element.click()
    sleep(.5)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//select[@id='avatarFace']/option[text()='MASKULIN']"))
    )
    element.click()
    sleep(.5)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//select[@id='avatarHair']/option[text()='BLACK']"))
    )
    element.click()
    sleep(.5)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@title='#f44336']"))
    )
    element.click()
    sleep(.5)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//select[@id='avatarExpression']/option[text()='COOL']"))
    )
    element.click()
    sleep(.5)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "changeAvatarButton"))
    )
    element.click()
    sleep(.5)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "button Nice trousers"))
    )
    element.click()
    sleep(.5)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "equip Nice trousers"))
    )
    element.click()    
    sleep(.5)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "changeAvatarButton"))
    )
    element.click()
    sleep(.5)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ProjectNav"))
    )
    element.click()
    sleep(.5)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "join Keep Planting"))
    )
    element.click()
    sleep(.5)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "like wheatear"))
    )
    element.click()
    sleep(.5)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "taskName"))
    )
    element.send_keys("Jamir's task")
    sleep(.5)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "taskDescription"))
    )    
    element.send_keys("My first task")
    sleep(.5)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "taskDeadline"))
    )    
    element.send_keys("02/22/2021")
    sleep(.5)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "addTaskButton"))
    )
    element.click()
    sleep(.5)
    
except:
    driver.quit()

sleep(100)

driver.quit()