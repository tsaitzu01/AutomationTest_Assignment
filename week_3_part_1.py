# Assignment 1
print('---------- Assignment 1 ----------')
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
try:
    driver.maximize_window()
    driver.get('https://school.appworks.tw/')

    title_of_page = driver.find_element(By.CSS_SELECTOR, '#page > div.header-wrapper > div > div.header-description.content-on-center.gridContainer > div > div > div > h1 > span').text
    if title_of_page == 'Code Your Future':
        print('PASS')
    else:
        print('FAIL')

    driver.find_element(By.XPATH, "//a[text()='AppWorks']").click()
    wins = driver.window_handles
    driver.switch_to.window(wins[-1])
    appworks_subtitle = driver.find_element(By.CSS_SELECTOR, '#main > div:nth-child(1) > div.wpb_column.vc_column_container.vc_col-sm-12 > div > div > div.wpb_text_column.wpb_content_element.vc_custom_1503949130309.en.bold > div > h3 > span > em').text
    if appworks_subtitle == 'By Founders, For Founders':
        print('PASS')
    else:
        print('FAIL')

    driver.get('https://appworks.tw/investments/')
    investments_subtitle = driver.find_element(By.CSS_SELECTOR, '#main > div:nth-child(1) > div.wpb_column.vc_column_container.vc_col-sm-12 > div > div > div.wpb_text_column.wpb_content_element.vc_custom_1508692402796.en > div > h3 > span > em').text
    if investments_subtitle == 'We know you have a choice. We want you to choose us.':
        print('PASS')
    else:
        print('FAIL')

    driver.back()
    print(driver.current_url)

    driver.forward()
    driver.close()

    driver.switch_to.window(wins[0])
    driver.refresh()    
finally:                    # ensuring sessions end cleanly
    driver.quit()


# Assignment 2
print('---------- Assignment 2 ----------')
def plus_one(nums):
    nums[-1] += 1                           # 個位數加一
    if nums[0] > 9:                         # 如果只有個位數不能用遞迴，直接透過 insert 進位
        nums[0] = 0                         # 本身變成 0
        nums.insert(0, 1)                   # insert 1 在 index 0 的位置
        return nums
    if nums[-1] > 9:                        # 如果最後一位數是 0 要進位
        nums[-1] = 0                        # 本身變成 0
        nums[:-1] = plus_one(nums[:-1])     # 前面位數的數字做遞迴
    return nums


print(plus_one([1, 2, 3])) # Should be [1, 2, 4] because 123 + 1 = 124 ==> [1, 2, 4]
print(plus_one([4, 3, 2, 1])) # Should be [4, 3, 2, 2]
print(plus_one([9])) # Should be [1, 0]
print(plus_one([9, 9])) # Should be [1, 0, 0]
print(plus_one([1, 9, 9])) # Should be [2, 0, 0]
print(plus_one([9, 9, 0])) # Should be [9, 9, 1]