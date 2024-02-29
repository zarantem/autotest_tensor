import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import ChromiumOptions
import os


preferences = {"download.default_directory":r"/Users/artemzarankov/PycharmProjects/autotest_tensor/downloadFiles"}
chrome_options = ChromiumOptions()
chrome_options.add_experimental_option("prefs", preferences)
chrome_options.enable_downloads = True
browser = webdriver.Chrome(options=chrome_options)
browser.maximize_window()
browser.get('https://sbis.ru/')
action = ActionChains(browser)
download = browser.find_element(by=By.XPATH, value='//*[@id="container"]/div[2]/div[1]/div[3]/div[3]/ul/li[8]/a')
browser.execute_script("arguments[0].scrollIntoView();", download)
download.click()
time.sleep(5)
download_plugin = browser.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[1]/div/div/div/div[3]/div[2]')
download_plugin.click()
time.sleep(5)
download_button = browser.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/a')
size_on_site = download_button.text
download_button.click()
size_of_file = os.path.getsize('/Users/artemzarankov/PycharmProjects/autotest_tensor/downloadFiles/sbisplugin-setup-web.exe')
size_of_file_mb = float(size_of_file / 1048576)
print(size_on_site, size_of_file_mb)