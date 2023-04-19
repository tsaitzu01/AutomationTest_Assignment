# Assignment 1
print('---------- Assignment 1 ----------')

def check_bmi(height, weight):
    bmi = weight / (height ** 2)    # formula for BMI

    if bmi >= 18.5 and bmi <= 24:   # BMI between 18.5 and 24, return True
        return True
    else:                           # BMI doesn't between 18.5 and 24, return False
        return False
        
print(check_bmi(1.6, 60))   # print True
print(check_bmi(1.6, 40))   # print False
print(check_bmi(1.6, 100))  # print False


# Assignment 2
print('---------- Assignment 2 ----------')

def calculate_salary(salary = 25000):
    year = 0                # work year
    
    while salary < 50000:
        salary *= 1.03      # adjust 3% every year
        year += 1

    return (f'When you work for {year} years, your salary will be doubled to {salary:.2f}')

print(calculate_salary())


# Assignment 3
print('---------- Assignment 3 ----------')

def binary_search_position(numbers, target): 
    start = 0                  # 初始位置：numbers 中的第一個位置
    end = len(numbers) - 1     # 初始位置：numbers 中的最後一個位置

    while numbers[(end + start) // 2] != target:    # 如果中間位置的數字 = target，則直接回傳中間位置
        if numbers[(end + start) // 2] > target:    # 如果中間位置的數字 > target，代表 target 在左邊，則把 end 變成中間位置
            end = (end + start) // 2
        else:                                       # 如果中間位置的數字 < target，代表 target 在右邊，則把 start 變成中間位置
            start = (end + start) // 2

    return (end + start) // 2
    
print(binary_search_position([1, 2, 5, 6, 7], 1)) # should print 0 
print(binary_search_position([1, 2, 5, 6, 7], 6)) # should print 3


# Assignment 4
print('---------- Assignment 4 ----------')

def draw_pyramid(number): 

    ## Method 1
    for i in range(number):                                 # 行（逐行顯示）
        print(' ' * (number - i - 1) + '*' * (2 * i + 1))   # 顯示規則：
                                                            # 1. 空格數量為 number（總行數） - 目前行數
                                                            # 2. * 數量為目前行數的兩倍 + 
    ## Method 2
    #for i in range(number):
    #    for j in range(i + number):
    #        if i + j >= number - 1:
    #            print('*', end = '')
    #        else:
    #            print(' ', end = '')
    #    print('\n')  

draw_pyramid(3)
# output:
#   *
#  *** 
# *****
'''
0,0 0,1 0,2 0,3 0,4
1,0 1,1 1,2 1,3 1,4
2,0 2,1 2,2 2,3 2,4
'''

draw_pyramid(5)
# output:
#     *
#    *** 
#   *****
#  *******
# *********
