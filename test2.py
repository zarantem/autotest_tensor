from config import start, find, url, browser, By, get_url

def test_change_state():
    start(url=url)
    find(element='//*[@id="wasaby-content"]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]')
    find(element='//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')
    find(element='//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span')
    proof_new_state = browser.find_element(by=By.XPATH,
                                           value='//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')
    proof_new_state2 = browser.find_element(by=By.XPATH, value='//*[@id="contacts_list"]/div/div[2]/div[1]/div/div[1]')
    proof_new_state3 = get_url()
    print(proof_new_state.text, proof_new_state2.text, proof_new_state3)