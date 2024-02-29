from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://sbis.ru/')
action = ActionChains(browser)
button = browser.find_element(by=By.XPATH, value='//*[@id="wasaby-content"]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]')
button.click()
tensor_banner = browser.find_element(by=By.XPATH, value='//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a')
tensor_banner.click()
for handle in browser.window_handles:
    browser.switch_to.window(handle)
people_power = browser.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a')
browser.execute_script("arguments[0].scrollIntoView();", people_power)
people_power.click()
width_photo_1 = browser.find_element(by=By.XPATH, value='//*[@id="container"]/div[1]/div/div[4]/div[2]/div[1]/a/div[1]/img').get_attribute('width')
height_photo_1 = browser.find_element(by=By.XPATH, value='//*[@id="container"]/div[1]/div/div[4]/div[2]/div[1]/a/div[1]/img').get_attribute('height')
width_photo_2 = browser.find_element(by=By.XPATH, value='//*[@id="container"]/div[1]/div/div[4]/div[2]/div[2]/a/div[1]/img').get_attribute('width')
height_photo_2 = browser.find_element(by=By.XPATH, value='//*[@id="container"]/div[1]/div/div[4]/div[2]/div[2]/a/div[1]/img').get_attribute('height')
width_photo_3 = browser.find_element(by=By.XPATH, value='//*[@id="container"]/div[1]/div/div[4]/div[2]/div[3]/a/div[1]/img').get_attribute('width')
height_photo_3 = browser.find_element(by=By.XPATH, value='//*[@id="container"]/div[1]/div/div[4]/div[2]/div[3]/a/div[1]/img').get_attribute('height')
width_photo_4 = browser.find_element(by=By.XPATH, value='//*[@id="container"]/div[1]/div/div[4]/div[2]/div[4]/a/div[1]/img').get_attribute('width')
height_photo_4 = browser.find_element(by=By.XPATH, value='//*[@id="container"]/div[1]/div/div[4]/div[2]/div[4]/a/div[1]/img').get_attribute('height')
print(width_photo_1, width_photo_2, width_photo_3, width_photo_4)
print(height_photo_1, height_photo_2, height_photo_3, height_photo_4)