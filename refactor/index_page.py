from selenium.webdriver.common.by import By
from page_base import PageBase

class IndexPage(PageBase):

    update_cart_btn = (By.XPATH, "//button[text()='Update cart']")
    update_msg = (By.CLASS_NAME, "woocommerce-message")
    subtotal_value = (By.XPATH, "//td[@data-title='Subtotal']/descendant::bdi")

    def add_to_cart_btn(self, product_name):
        return (By.XPATH, f"//h2[text()='{product_name}']/ancestor::li/a[text()='Add to cart']")

    def view_cart_btn(self, product_name):
        return (By.XPATH, f"//h2[text()='{product_name}']/ancestor::li/a[@title='View cart']")
    
    def qty_text_field(self, product_name):
        return (By.XPATH, f"//a[text()='{product_name}']/ancestor::tr/descendant::input[@title='Qty']")
    
    def unit_price_value(self, product_name):
        return (By.XPATH, f"//a[text()='{product_name}']/ancestor::tr/descendant::span[contains(@class, 'amount')]/bdi")
   
    # Function
    def click_add_to_cart(self, product_name):
        add_to_cart_elem = self.find_element(self.add_to_cart_btn(product_name), clickable = True)
        add_to_cart_elem.click()

    def click_view_cart(self,product_name):
        go_to_cart_elem = self.find_element(self.view_cart_btn(product_name), clickable = True)
        go_to_cart_elem.click()

    def edit_quantity(self, product_name, qty):
        qty_text_field_elem = self.find_element(self.qty_text_field(product_name), clickable = True)
        self.input_text(qty_text_field_elem, qty)

    def click_update_cart(self):
        update_cart_btn_elem = self.find_element(self.update_cart_btn, clickable = True)
        update_cart_btn_elem.click()

    def get_update_msg(self):
        return self.find_element(self.update_msg)

    def get_unit_price_value(self, product_name):
        return self.find_element(self.unit_price_value(product_name), clickable = True)
    
    def get_subtotal_value(self):
        return self.find_element(self.subtotal_value)
