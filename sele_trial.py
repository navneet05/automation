from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
import time
driver =webdriver.Firefox(executable_path="D:\\Navneet_files\\geckodriver\\geckodriver.exe")
print('done')
# to maximize the browser window
driver.maximize_window()
#get method to launch the URL
#driver.get("https://www.pyimagesearch.com/start-here/")
#to refresh the browser
#driver.refresh()
#to close the browser

#form element
signup_1="/html/body/div[2]/div[1]/header/div/div[2]/div[1]/div[2]/a"
passward_2="/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input"
login_button_3="/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]"

#flow
driver.get("https://www.ondoor.com/")
driver.find_element(By.XPATH,signup_1).click() # by name,id,path
"""
driver.find_element_by_xpath(user_name_1).send_keys("username")
driver.find_element_by_xpath(passward_2).send_keys("password")
time.sleep(10)
driver.find_element_by_xpath(login_button_3).click()
time.sleep(5)
"""
driver.close()