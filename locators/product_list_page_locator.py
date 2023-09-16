from selenium.webdriver.common.by import By

class ProductListPageLocator:
    CATEGORY_NAME_SELECTOR = (By.XPATH, '//*[@id="__next"]/main/section/div[1]/h1')
    PRODUCT_ROWS = (By.XPATH, "//*[@id='data-table-0']/tbody/tr")