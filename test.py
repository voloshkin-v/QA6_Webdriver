import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

USERNAME = 'test'
PASSWORD = 'password'

browser = webdriver.Chrome()
browser.get("https://www.instagram.com/")
browser.implicitly_wait(30)

browser.find_element_by_css_selector('[name="username"]').send_keys(USERNAME)
browser.find_element_by_css_selector('[name="password"]').send_keys(PASSWORD)
browser.find_element_by_css_selector('[name="password"]').send_keys(Keys.RETURN)

expected_text = 'К сожалению, вы ввели неправильный пароль. Проверьте свой пароль еще раз.'
actual_text = browser.find_element_by_id('slfErrorAlert').text

assert actual_text == expected_text 

print('test worked successfully')