# Assignment 1
print('---------- Assignment 1 ----------')

## Part 1: Write Excel
import pandas as pd

student_score = pd.DataFrame({                      # Define the value and colume name in the DataFrame
    'Student': ['Student A', 'Student B', 'Student C', 'Student D', 'Student E'],
    'Reading': [80, 88, 92, 81, 75],
    'Listening': [75, 86, 85, 88, 80],
    'Speaking': [88, 90, 92, 80, 78],
    'Writing': [80, 95, 98, 82, 80]    
})

file_name = 'StudentScore_sheet.xlsx'               # Define the file name of Excel

student_score.to_excel(file_name, index = False)    # Write DataFrame to Excel file

## Part 2: Read Excel
df = pd.read_excel('StudentScore_sheet.xlsx')               # Read Excel
section = ['Reading', 'Listening', 'Speaking', 'Writing']   # Column names
weight = [0.2, 0.25, 0.3, 0.25]                             # The weights of different section of the score

for i in range(len(df)):                                    # 計算每一位學生的分數
    score = 0                                               # 初始化 score 的值
    for j in range(len(section)):                           # 計算每一個 section * 比重後的分數
        score += df.iloc[i][section[j]] * weight[j]
    print(f'student: {df.iloc[i]["Student"]}, score: {score}')  # print 出該位學生的名字和分數


# Assignment 2
print('---------- Assignment 2 ----------')

def division(x, y):

    try:
        if type(y) != int:                              # TypeError 的情境是 y 不等於整數
            raise TypeError('y should be integer')      # 定義要顯示的文字
        else:
            print(x / y)                                # 無錯誤的情況時，做除法運算
    except ZeroDivisionError as e:
        print(f"{type(e).__name__}('y cannot be 0')")   # Throw ZeroDivisionError
    except TypeError as e:
        print(repr(e))                                  # Throw TypeError
    finally:
        print('---Finish---')                           # 無論結果為何最終顯示 "---Finish---"

division(100, 10)   # Should print 10.0 and "---Finish---"
division(100, 0)    # Should Throw ZeroDivisionError, print "y cannot be 0" and "---Finish---"
division(100, "a")  # Should Throw TypeError, print "y should be integer" and "---Finish---"
division(100, 0.5)  # Should Throw TypeError, print "y should be integer" and "---Finish---"


# Assignment 3
print('---------- Assignment 3 ----------')
def running_sum(nums):

    for i in range(1, len(nums)):   # 除了 index = 0 不變之外，其餘的值都需要重新計算
        nums[i] += nums[i - 1]      # 從 index = 1 開始，新的 list 中的值會變成 (前一個 index 新的值) + (自己原本的值)

    return nums                     # 全部的 index 都改寫完之後即可 return

print(running_sum([1, 2, 3, 4])) # Should be [1, 3, 6, 10] because [1, 1+2, 1+2+3, 1+2+3+4]
print(running_sum([1, 1, 1, 1, 1])) # Should be [1, 2, 3, 4, 5]
print(running_sum([3, 1, 2, 10, 1])) # Should be [3, 4, 6, 16, 17]