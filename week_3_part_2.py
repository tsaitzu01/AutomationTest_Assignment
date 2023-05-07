# Assignment 1
print('---------- Assignment 1 ----------')
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Open the Chrome browser
driver = webdriver.Chrome()
try:
    wait = WebDriverWait(driver, 10)
    # Go to Demo Store
    driver.get('http://demostore.supersqa.com')
    # Add “Album” to cart
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//a[@aria-label="Add “Album” to your cart"]')
    )).click()
    # Click View cart button
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//a[@class="added_to_cart wc-forward"]')
    )).click()
    # Change the quantity to 2
    quantity_input_element = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//input[@class="input-text qty text"]')
    ))
    quantity_input_element.click()
    quantity_input_element.clear()
    quantity_input_element.send_keys('2')
    # Update cart in Cart Page
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[@value="Update cart"]')
    )).click()
    # Wait for updating   
    wait.until(EC.invisibility_of_element_located(
        (By.XPATH, '//div[@class="blockUI blockOverlay"]')
    ))

    # Verify that Subtotal is $30.00
    subtotal_list = wait.until(EC.presence_of_all_elements_located(
        (By.XPATH, '//td[@data-title="Subtotal"]/span[@class="woocommerce-Price-amount amount"]')
    ))
    for subtotal in subtotal_list:
        assert subtotal.text == '$30.00'
    # Click “Checkout”
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//a[@class="checkout-button button alt wc-forward"]')
    )).click()
    # Fill in the form
    first_name = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//input[@id="billing_first_name"]')
    ))
    first_name.click()
    first_name.send_keys('First')

    last_name = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//input[@id="billing_last_name"]')
    ))
    last_name.click()
    last_name.send_keys('Last')

    company = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//input[@id="billing_company"]')
    ))
    company.click()
    company.send_keys('ABC Company')

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//span[@aria-label="Country / Region"]/span[@class="select2-selection__arrow"]')
    )).click()
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//li[text()='Taiwan']")
    )).click()

    address_1 = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//input[@id="billing_address_1"]')
    ))
    address_1.click()
    address_1.send_keys('Address Line 1')
    address_2 = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//input[@id="billing_address_2"]')
    ))
    address_2.click()
    address_2.send_keys('Address Line 2')

    town_or_city = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//input[@id="billing_city"]')
    ))
    town_or_city.click()
    town_or_city.send_keys('Taipei')

    state_or_country = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//input[@id="billing_state"]')
    ))
    state_or_country.click()
    state_or_country.send_keys('Taipei')

    postcode_or_zip = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//input[@id="billing_postcode"]')
    ))
    postcode_or_zip.click()
    postcode_or_zip.send_keys('101')

    phone = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//input[@id="billing_phone"]')
    ))
    phone.click()
    phone.send_keys('0123456789')

    email = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//input[@id="billing_email"]')
    ))
    email.click()
    email.send_keys('abc@abc.com')
    # Create an account in Checkout Page
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//input[@id="createaccount"]')
    )).click()
    password = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//input[@id="account_password"]')
    ))
    password.click()
    password.send_keys('1234QWERasdf!@#$')
    # Fill in Additional Information in Checkout Page
    additional_info = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//textarea[@id="order_comments"]')
    ))
    additional_info.click()
    additional_info.send_keys('Thank you!')
    # Click Place Order
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[@id="place_order"]')
    )).click()
    # Verify that “Invalid payment method” is displayed
    error_msg = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//ul[@class="woocommerce-error"]')
    )).text
    assert error_msg == "Invalid payment method."
# Finally, close the browser
finally:
    driver.quit()

# Assignment 2
print('---------- Assignment 2 ----------')
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if target - nums[i] == nums[j]:
                return [i, j]
            

print(two_sum([2, 7, 11, 15], 9)) # Should be [0, 1], because nums[0] + nums[1] = 9
print(two_sum([3, 6, 11, 15], 17)) # Should be [1, 2], because nums[1] + nums[2] = 17
print(two_sum([3, 2, 4], 6))    # Should be [1, 2], because nums[1] + nums[2] = 6
print(two_sum([3, 3, 4], 6))    # Should be [0, 1], because nums[0] + nums[1] = 6