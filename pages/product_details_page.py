from locators.product_details_page_locator import ProductDetailsPageLocator
from pages.base_page import BasePage
from utils.data_format_util import DataFormatUtil
from utils.file_util import FileUtil
from slugify import slugify
import uuid
import time

class ProductDetailsPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def scrap(self, url: str, category_name: str)->list:
        self.open(url)
        product_name = self.find_element(*ProductDetailsPageLocator.PRODUCT_NAME_SELECTOR).text
        slug = slugify(str(product_name))
        digi_key = self.find_element(*ProductDetailsPageLocator.DIGI_KEY_PART_NUMBER_SELECTOR).text
        sku = digi_key
        product_quantity = self.find_element(*ProductDetailsPageLocator.PRODUCT_QUANTITY_SELECTOR).text
        formatted_quantity = DataFormatUtil.format_quantity(product_quantity)
        manufacturer = self.find_element(*ProductDetailsPageLocator.MANUFACTURER_SELECTOR)
        
        if not isinstance(manufacturer, str):
            manufacturer = manufacturer.text
            
        manufacturer_product_number = self.find_element(*ProductDetailsPageLocator.MANUFACTURER_PRODUCT_NUMBER_SELECTOR)
        
        if not isinstance(manufacturer_product_number, str):
            manufacturer_product_number = manufacturer_product_number.text
            
        description = self.find_element(*ProductDetailsPageLocator.DESCRIPTION)
        
        if not isinstance(description, str):
            description = description.text
        
        manufacturer_lead_time = self.find_element(*ProductDetailsPageLocator.MANUFACTURER_STD_LEAD_TIME)
       
        if not isinstance(manufacturer_lead_time, str):
            manufacturer_lead_time = manufacturer_lead_time.text
        
        detailed_description = self.find_element(*ProductDetailsPageLocator.DETAILED_DESCRIPTION)
        
        if not isinstance(detailed_description, str):
            detailed_description = detailed_description.text
        
        bulk_price = self.find_element(*ProductDetailsPageLocator.BULK_PRICE)
        formatted_bulk_price = ''
        price = ''
        
        if not isinstance(bulk_price, str):
            bulk_price = bulk_price.text
            price = DataFormatUtil.format_price(bulk_price)
            formatted_bulk_price = DataFormatUtil.format_bulk_price(bulk_price)
       
        product_attrs = self.find_element(*ProductDetailsPageLocator.PRODUCT_ATTRS).text
        formatted_product_attrs = DataFormatUtil.format_product_attrs(product_attrs)
        
        product_image_name = f'Products-{uuid.uuid4()}.png'
        others = DataFormatUtil.format_others([description, digi_key, manufacturer, manufacturer_product_number, manufacturer_lead_time])
        
        product_image = self.find_element(*ProductDetailsPageLocator.PRODUCT_IMAGE_SELECTOR)
        
        data_sheet = self.find_element(*ProductDetailsPageLocator.DATA_SHEET_SELECTOR)
        data_sheet_file_name = ''
        if not isinstance(data_sheet, str):
            data_sheet.click()
            data_sheet_file_link = data_sheet.get_attribute('href')
            data_sheet_file_name = data_sheet_file_link.split('/').pop()
            print(f'downloading data sheet {data_sheet_file_name}, sleeping for 5s...')
            time.sleep(5)
        
        if not isinstance(product_image, str):
            FileUtil.save_image(product_image_name, product_image.screenshot_as_png)
              
        data = [product_name, slug, sku, detailed_description, price, formatted_quantity, manufacturer_product_number, formatted_product_attrs, formatted_bulk_price, others, product_image_name, data_sheet_file_name, category_name]
        
        return data