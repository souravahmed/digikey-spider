import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from selenium.common.exceptions import NoSuchElementException




class BasePage(object):
    """
    this Base class is serving basic attributes for every single page inherited from Page class
    
    """
    def __init__(self, driver):
        self.driver = driver
        
    def open(self, url: str)->None:
        self.driver.get(url)
     
         
    def find_element(self, *locator):
      try:
        return  self.driver.find_element(*locator)
      except NoSuchElementException:
          return '' 
    
    def find_elements(self, *locator):
        try:
            return self.driver.find_elements(*locator)
        except NoSuchElementException:
            return []
        
        
    def re_init(self)->None:
        selenium_driver_path = os.path.join(os.getcwd(), 'chromedriver_win32', 'chromedriver.exe')
        download_data_sheet_folder_path = os.path.join(os.getcwd(), 'data_sheets')
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
        self.driver = webdriver.Chrome(options=options, executable_path=selenium_driver_path)    