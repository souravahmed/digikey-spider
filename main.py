
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

from pages.product_list_page import ProductListPage
from utils.file_util import FileUtil


if __name__ == '__main__':
    selenium_driver_path = os.path.join(os.getcwd(), 'chromedriver_win32', 'chromedriver.exe')
    download_data_sheet_folder_path = os.path.join(os.getcwd(), 'data_sheets')
    FileUtil.create_folder(download_data_sheet_folder_path)
    ua = UserAgent()
    user_agent = ua.random
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument(f'user-agent={user_agent}')
    prefs = {"download.default_directory" : download_data_sheet_folder_path}
    options.add_experimental_option("prefs",prefs)
    url = input('Please enter url: ')
    driver = webdriver.Chrome(options=options, executable_path=selenium_driver_path)
    product_list_page = ProductListPage(driver)
    product_list_page.scrap(url)
    print('scrapping done. closing the driver...')
    driver.quit()
    