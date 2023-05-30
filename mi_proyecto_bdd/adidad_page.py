from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class AdidasPage:
    def __init__(self, driver):
        self.driver = driver        

    def open_page(self):
        self.driver.get("https://www.adidas.es/")

    def close_kookies(self):
        search_bar = self.driver.find_element(By.ID,"glass-gdpr-default-consent-accept-button")
        search_bar.click()

    def search(self, product_name):
        search_bar = self.driver.find_element(By.NAME,"q")
        search_bar.send_keys(product_name)
        search_bar.send_keys(Keys.RETURN)

    def close_m(self):
        scap_bar = self.driver.find_element(By.XPATH,"//button[@class='gl-modal__close']")
        scap_bar.click()

    def get_title(self):
        return self.driver.title

    def get_product_listing(self):
        title_products= self.driver.find_elements(By.XPATH,"//p[@class='glass-product-card__title']")
        return len(title_products)

    def add_product_to_cart(self):
        product =self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div/div/div/div/div/div/a/div/p[1]")  
        product.click() 
        add_to_cart_button = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/section/div[3]/button/span[1]")
        add_to_cart_button.click()
