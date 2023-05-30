import unittest
from selenium import webdriver
from main import AdidasPage

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.adidas_page = AdidasPage(self.driver)
        self.adidas_page.open_page()
        self.adidas_page.close_cookies()
        self.adidas_page.search("balon")
        self.driver.implicitly_wait(5)
        self.adidas_page.close_modal()
        
    def test_find_title(self):
        self.assertIn("adidas Online Shop | adidas.es", self.adidas_page.get_title())

    def test_product_listing(self):    
        count_products = self.adidas_page.get_product_listing()
        expected_min_products = 35
        expected_max_products = 55
        self.assertTrue(count_products >= expected_min_products)
        self.assertTrue(count_products <= expected_max_products)

    def test_add_product_to_cart(self):
        self.adidas_page.add_product_to_cart()
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
