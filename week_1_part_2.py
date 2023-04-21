# Assignment 1
print('---------- Assignment 1 ----------')

class Student():

    def __init__(self, student_name, mark1, mark2, mark3):
        self.student_name = student_name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
        self.total_marks = 0                                        # total marks 初始值為 0

    def calculate_total(self):
        self.total_marks = self.mark1 + self.mark2 + self.mark3     # 計算 total marks
        print(self.total_marks)                                     # 因為需要印出結果，所以用 print 把 total_marks 印出來
    
    def display_student_details(self):                  
        print(self.student_name + ':', end = ' ')                   # 先印出 student name，再透過 calculate_total fuc 印出 total_marks 
        self.calculate_total()
    
student_a = Student('Mary', 50, 60, 70)
student_a.calculate_total() # should print 180
student_a.display_student_details() # should print "Mary: 180"


# Assignment 2
print('---------- Assignment 2 ----------')

class Animal():                         # Parent Class

    def __init__(self):
        self.sound = None               # contains an attribute

    def get_type(self):
        print('I am animal.')

    def get_sound(self):                # overridden method
        print('Hello World')

class Dog(Animal):                      # Sub class

    def get_sound(self):                # overridng method
        print('Woof! Woof!')

    def catch_cat(self):
        print('I caught a cat.')

class Cat(Animal):                      # Sub class

    def get_sound(self):                # overridng method
        print('Meow! Meow!')
 
    def catch_mouse(self):
        print('I caught a mouse.')

dog = Dog()
dog.get_type()  # Print "I am animal"
dog.get_sound() # Print "Woof! Woof!"
dog.catch_cat() # Print "I caught a cat."

cat = Cat()
cat.get_type()  # Print "I am animal" 
cat.get_sound() # Print "Meow! Meow!"
cat.catch_mouse() # Print "I caught a mouse."

animal = Animal()
animal.get_sound() # Print "Hello World"


# Assignment 3
print('---------- Assignment 3 ----------')

class Course():

    def __init__(self, title, instructor, price, lectures):
        self.title = title
        self.instructor = instructor
        self.price = price
        self.lectures = lectures
        self.users = []
        self.ratings = 0
        self.avg_rating = 0
        
    def new_user_enrolled(self, user):
        self.users.append(user)

    def received_a_rating(self, rating):
        self.ratings += rating
    
    def show_details(self):
        if len(self.users) != 0:
            self.avg_rating = self.ratings / len(self.users)

        print(f'Course Title : {self.title}\n'
              f'Instructor : {self.instructor}\n'
              f'Price : ${self.price}\n'
              f'Number of Lectures: {self.lectures}\n'
              f'Users: {self.users}\n'
              f'Average rating : {self.avg_rating}')
        
class VideoCourse(Course):

    def __init__(self, title, instructor, price, lectures, length_video):
        super().__init__(title, instructor, price, lectures)                   # 透過 super() 執行父類別的方法，init 交集的變數
        self.length_video = length_video                                       # 初始化 VideoCourse 的變數

    def show_details(self):
        super().show_details()                                                 # 執行父類別的 show_details() 
        print(f'Video Length: {self.length_video} mins\n')                     # 補上 Video length 的資訊

class PdfCourse(Course):

    def __init__(self, title, instructor, price, lectures, page):
        super().__init__(title, instructor, price, lectures)                    # 透過 super() 執行父類別的方法，init 交集的變數
        self.page = page                                                        # 初始化 PdfCourse 的變數 

    def show_details(self):
        super().show_details()                                                 # 執行父類別的 show_details() 
        print(f'Pages: {self.page}')                                           # 補上 Page 的資訊

vc = VideoCourse('Learn C++', 'Miss A', 5000, 30, 1000)
vc.new_user_enrolled('Student A')
vc.new_user_enrolled('Student B')
vc.new_user_enrolled('Student C')
vc.received_a_rating(3)
vc.received_a_rating(5)
vc.received_a_rating(4)
vc.show_details()

pc = PdfCourse('Learn Java', 'Mr B', 8000, 35, 100)
pc.new_user_enrolled('Student X')
pc.new_user_enrolled('Student Y')
pc.new_user_enrolled('Student Z')
pc.received_a_rating(5)
pc.received_a_rating(4)
pc.received_a_rating(4.5)
pc.show_details()


# Assignment 4
print('---------- Assignment 4 ----------')
def find_sum_of_factorials(number): 

    if number == 0:                         # 0! = 1
        return 1
    
    sum = 0
    factorial = 1                          # 因為 0! = 1, 所以初始值為 1

    for i in range(1, number + 1):         # 計算範圍從 1 到 number
        factorial *= i                     # 1! = 1 * 1 = 1, 2! = 1! * 2, 3! = 2! * 3... => rule is i! = (i - 1)! * i
        sum += factorial                   # 累加 1! 到 n! 的值
    return sum
    
print(find_sum_of_factorials(3))  # = 1! + 2! + 3!, =  1 + 1 x 2 + 1 x 2 x 3,  should print 9
print(find_sum_of_factorials(1))  # should print 1
print(find_sum_of_factorials(5))  # should print 153