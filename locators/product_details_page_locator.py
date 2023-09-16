from selenium.webdriver.common.by import By

class ProductDetailsPageLocator:
    PRODUCT_NAME_SELECTOR = (By.XPATH, '//*[@id="__next"]/main/div/div/div[1]/div[2]/div/table/thead/tr/th/h1')
    DIGI_KEY_PART_NUMBER_SELECTOR = (By.XPATH, '//*[@id="__next"]/main/div/div/div[1]/div[2]/div/table/tbody/tr[1]/td[2]/div')
    PRODUCT_QUANTITY_SELECTOR = (By.XPATH, '//*[@id="__next"]/main/div/div/div[2]/div/div/div[1]/div/div/span')
    MANUFACTURER_SELECTOR = (By.XPATH, '//*[@id="__next"]/main/div/div/div[1]/div[2]/div/table/tbody/tr[2]/td[2]/div/a')
    MANUFACTURER_PRODUCT_NUMBER_SELECTOR = (By.XPATH, '//*[@id="__next"]/main/div/div/div[1]/div[2]/div/table/tbody/tr[3]/td[2]/div')
    DESCRIPTION = (By.XPATH, '//*[@id="__next"]/main/div/div/div[1]/div[2]/div/table/tbody/tr[4]/td[2]/div')
    MANUFACTURER_STD_LEAD_TIME = (By.XPATH, '//*[@id="stdLeadTime"]')
    DETAILED_DESCRIPTION = (By.XPATH, '//*[@id="__next"]/main/div/div/div[1]/div[2]/div/table/tbody/tr[6]/td[2]/div')
    BULK_PRICE = (By.XPATH, '//*[@id="__next"]/main/div/div/div[2]/div/div/div[4]/span/table')
    PRODUCT_ATTRS = (By.XPATH, '//*[@id="product-attributes"]')
    PRODUCT_IMAGE_SELECTOR = (By.XPATH, '//*[@id="__next"]/main/div/div/div[1]/div[1]/div/div[1]/div/img')
    DATA_SHEET_SELECTOR = (By.XPATH, '//*[@id="__next"]/main/div/div/div[1]/div[2]/div/table/tbody/tr/td/a')