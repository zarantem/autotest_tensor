import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://sbis.ru/')
action = ActionChains(browser)
button = browser.find_element(by=By.XPATH, value='//*[@id="wasaby-content"]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]')
button.click()
state = browser.find_element(by=By.XPATH, value='//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')
state.click()
time.sleep(5)
new_state = browser.find_element(by=By.XPATH, value='//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span')
new_state.click()
time.sleep(5)
proof_new_state = browser.find_element(by=By.XPATH, value='//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')
proof_new_state2 = browser.find_element(by=By.XPATH, value='//*[@id="contacts_list"]/div/div[2]/div[1]/div/div[1]')
proof_new_state3 = browser.current_url
print(proof_new_state.text, proof_new_state2.text, proof_new_state3)