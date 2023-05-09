from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from index_page import IndexPage

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.maximize_window()
    driver.get("http://demostore.supersqa.com/")

    # Click Add To Cart - Album
    index_page = IndexPage(driver)
    product_name = "Album"
    index_page.click_add_to_cart(product_name)

    # Click view cart element
    index_page.click_view_cart(product_name)

    # Change quantity to 2
    qty = 2
    index_page.edit_quantity(product_name, qty)

    # Click Update Cart Button
    index_page.click_update_cart()

    # Wait for Update Success Message
    index_page.get_update_msg()

    # Get Unit Price Value
    unit_price_elem = index_page.get_unit_price_value(product_name)

    # Get Subtotal Value
    subtotal_text_elem = index_page.get_subtotal_value()

    expect_subtotal = float(unit_price_elem.text[1:]) * qty

    assert float(subtotal_text_elem.text[1:]) == float(unit_price_elem.text[1:]) * qty, \
        f"Expected: {expect_subtotal}, Actual: {float(subtotal_text_elem.text[1:])}"

finally:
    driver.quit()