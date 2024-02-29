from config import start, find, url, focus, find_and_scroll, find_images

def equal_images():
    start(url=url)
    find(element='//*[@id="wasaby-content"]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]')
    find(element='//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a')
    focus()
    find_and_scroll(element='/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a')
    find_images()
