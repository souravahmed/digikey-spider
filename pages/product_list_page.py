from locators.product_list_page_locator import ProductListPageLocator
from pages.base_page import BasePage
from pages.product_details_page import ProductDetailsPage
from utils.file_util import FileUtil
from selenium.webdriver.common.by import By

class ProductListPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def scrap(self, url: str)->None:
        self.open(url)
        page_links = []
        category_name = self.find_element(*ProductListPageLocator.CATEGORY_NAME_SELECTOR).text
        row_counter = 1
        for product_row_element in self.find_elements(*ProductListPageLocator.PRODUCT_ROWS):
            row_selector = "//*[@id='data-table-0']/tbody/tr" + f"[{row_counter}]" + "/td[2]/div/div[3]/a[1]"
            page_link_element = product_row_element.find_element(By.XPATH, row_selector)
            page_links.append(page_link_element.get_attribute('href'))
            row_counter +=1
        
        self.driver.quit()
        
        rows = []
        print(f'{len(page_links)} products need to scrap')
        for count, page_link in enumerate(page_links, start=1):
           self.re_init()
           print(f'scrapping {count} of {len(page_links)} -> {page_link}')
           product_details_page = ProductDetailsPage(self.driver)
           data = product_details_page.scrap(page_link, category_name)
           rows.append(data)
           self.driver.quit()
        
        FileUtil.export_to_csv(f'{category_name}.csv', rows)
           
        
           
            