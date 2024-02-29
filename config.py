from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import ChromiumOptions
import time


preferences = {"download.default_directory":r"/Users/artemzarankov/PycharmProjects/autotest_tensor/downloadFiles"}
chrome_options = ChromiumOptions()
chrome_options.add_experimental_option("prefs", preferences)
chrome_options.enable_downloads = True
browser = webdriver.Chrome(options=chrome_options)
browser.maximize_window()
action = ActionChains(browser)


url = 'https://sbis.ru/'


def start(url):
    browser.get(url)


def find(element):
    searching_element = browser.find_element(by=By.XPATH, value=element)
    time.sleep(2)
    searching_element.click()
    time.sleep(5)


def find_and_scroll(element):
    searching_element = browser.find_element(by=By.XPATH, value=element)
    browser.execute_script("arguments[0].scrollIntoView();", searching_element)
    time.sleep(2)
    searching_element.click()
    time.sleep(5)


def download_file(element):
    download_button = browser.find_element(by=By.XPATH, value=element)
    size = download_button.text
    download_button.click()
    time.sleep(5)
    return size


def focus():
    for handle in browser.window_handles:
        browser.switch_to.window(handle)


def get_url():
    curl = browser.current_url
    return curl


def find_images():
    width_photo_1 = browser.find_element(by=By.XPATH,
                                         value='//*[@id="container"]/div[1]/div/div[4]/div[2]/div[1]/a/div[1]/img').get_attribute(
        'width')
    height_photo_1 = browser.find_element(by=By.XPATH,
                                          value='//*[@id="container"]/div[1]/div/div[4]/div[2]/div[1]/a/div[1]/img').get_attribute(
        'height')
    width_photo_2 = browser.find_element(by=By.XPATH,
                                         value='//*[@id="container"]/div[1]/div/div[4]/div[2]/div[2]/a/div[1]/img').get_attribute(
        'width')
    height_photo_2 = browser.find_element(by=By.XPATH,
                                          value='//*[@id="container"]/div[1]/div/div[4]/div[2]/div[2]/a/div[1]/img').get_attribute(
        'height')
    width_photo_3 = browser.find_element(by=By.XPATH,
                                         value='//*[@id="container"]/div[1]/div/div[4]/div[2]/div[3]/a/div[1]/img').get_attribute(
        'width')
    height_photo_3 = browser.find_element(by=By.XPATH,
                                          value='//*[@id="container"]/div[1]/div/div[4]/div[2]/div[3]/a/div[1]/img').get_attribute(
        'height')
    width_photo_4 = browser.find_element(by=By.XPATH,
                                         value='//*[@id="container"]/div[1]/div/div[4]/div[2]/div[4]/a/div[1]/img').get_attribute(
        'width')
    height_photo_4 = browser.find_element(by=By.XPATH,
                                          value='//*[@id="container"]/div[1]/div/div[4]/div[2]/div[4]/a/div[1]/img').get_attribute(
        'height')
    if width_photo_1 == width_photo_2 == width_photo_3 == width_photo_4 and height_photo_1 == height_photo_2 == height_photo_3 == height_photo_4:
        print(f'Всё хорошо, фото одного размера: {width_photo_1} x {height_photo_1}')
    else:
        print('у фото разный размер')


def close_driver():
    browser.close()