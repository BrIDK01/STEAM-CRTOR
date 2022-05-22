
from pydoc import doc
import time
import os
from tkinter import BROWSE
from selenium import webdriver
import requests
from pynput. keyboard import Key, Controller
import pyautogui 
from selenium.webdriver.common.by import By








##öffnet Tabs und kopiert Mail



driver = webdriver.Firefox(executable_path=r'C:\Users\Rayan\OneDrive\Desktop\yk\geckodriver.exe')

driver.get ('https://10minutemail.net/?lang=de')

time.sleep (5)

email = driver.find_element(By.CLASS_NAME, "mailtext").get_attribute("value")

driver.execute_script("window.open('about:blank','secondtab');")

driver.switch_to.window("secondtab")

driver.get('https://store.steampowered.com/join')

##Daten eingeben
keyboard = Controller()

driver.find_element(By.ID, "email").send_keys(email)

driver.find_element(By.ID, "reenter_email").send_keys(email)

time.sleep (20)

driver.find_element_by_id("i_agree_check").click()

##time.sleep(1)

driver.find_element_by_id('createAccountButton').click()

time.sleep(2)

driver.find_element_by_id("overAgeButton").click()

##EMail

time.sleep(3)

driver.switch_to.window(driver.window_handles[0])


driver.find_element_by_class_name("inboxSenderName inboxSenderEllipsis").click()


