from config import start, find, download_file, url
import os


def test_file_result():
    start(url=url)
    find(element='//*[@id="container"]/div[2]/div[1]/div[3]/div[3]/ul/li[8]/a')
    find(element='/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[1]/div/div/div/div[3]/div[2]')
    size_on_site = download_file('/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/a')
    size_of_file = os.path.getsize(
        '/Users/artemzarankov/PycharmProjects/autotest_tensor/downloadFiles/sbisplugin-setup-web.exe')
    size_of_file_mb = float(size_of_file / 1048576)
    print(size_on_site, size_of_file_mb)