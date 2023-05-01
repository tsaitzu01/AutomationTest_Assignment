# Assignment 1
print('---------- Assignment 1 ----------')
import mysql.connector
from faker import Faker

fake = Faker()

cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='assignment',
                              auth_plugin='mysql_native_password')
cursor = cnx.cursor(buffered = True, dictionary = True)


user_email = fake.email()
user_password = fake.random_number(digits = 5)
data_user = (user_email, user_password)
add_user = ("INSERT INTO user "
            "(email, password) "
            "VALUES (%s, %s)")

select_id =  ("SELECT id FROM user "
              "WHERE email = '{}'".format(user_email))

new_password = fake.random_number(digits = 6)
update_password = ("UPDATE user SET password = '{}'"
                   "WHERE email = '{}';"
                   "SELECT * FROM user"
                   "WHERE email = '{}'".format(new_password, user_email, user_email))

delete_id = 2
delete_user = ("DELETE FROM user "
               "WHERE id = %s" % delete_id)

cursor.execute(add_user, data_user)             # Create data
cnx.commit()                                    # Make sure data is committed to the database

cursor.execute(select_id)                       # Select(Read) data

cursor.execute(update_password, multi = True)   # Update data
cnx.commit()

cursor.execute(delete_user)                     # Delete data
cnx.commit()

cursor.close()
cnx.close()


# Assignment 2
print('---------- Assignment 2 ----------')
cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='assignment',
                              auth_plugin='mysql_native_password')
cursor = cnx.cursor(buffered = True, dictionary = True)

list_chinese_score = ("SELECT score FROM StudentScore "
                      "WHERE course = '{}'".format("Chinese"))


list_english_score = ("SELECT score FROM StudentScore "
                      "WHERE course = 'English' "
                      "ORDER BY score DESC")

list_student_name = ("SELECT name FROM StudentScore ")

avg_chinese_score = ("SELECT AVG(score) FROM StudentScore "
                     "WHERE course = 'Chinese' ")

min_english_score = ("SELECT MIN(score) FROM StudentScore "
                     "WHERE course = 'English' ")

max_maths_score = ("SELECT MAX(score) FROM StudentScore "
                     "WHERE course = 'Maths' ")

number_of_english_score_higher_60 = ("SELECT COUNT(name) FROM StudentScore "
                                     "WHERE course = 'English'"
                                     "AND score >= 60")

list_score_of_boy_chou_student = ("SELECT * FROM StudentScore "
                                  "WHERE sex = '男' "
                                  "AND name LIKE '周%'")

cursor.execute(list_chinese_score)
cursor.execute(list_english_score)
cursor.execute(list_student_name)
cursor.execute(avg_chinese_score)
cursor.execute(min_english_score)
cursor.execute(max_maths_score)
cursor.execute(number_of_english_score_higher_60)
cursor.execute(list_score_of_boy_chou_student)


cursor.close()
cnx.close()


# Assignment 3
print('---------- Assignment 3 ----------')
cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='assignment',
                              auth_plugin='mysql_native_password')
cursor = cnx.cursor(buffered = True, dictionary = True)

join_tables = ("SELECT Customers.customer, SUM(Orders.amount) "
               "FROM Customers "
               "LEFT JOIN Orders "
               "ON Orders.customerID = Customers.customerID "
               "GROUP BY Customers.customer")

cursor.execute(join_tables)


results = cursor.fetchall()
for i in range(len(results)):
    print(f'{results[i]["customer"]}: ${results[i]["SUM(Orders.amount)"]}')

cursor.close()
cnx.close()


# Assignment 5
print('---------- Assignment 5 ----------')
def pagination(current_page, no_of_record):
    cnx = mysql.connector.connect(user='root', password='root',
                                  host='127.0.0.1',
                                  database='pagination',
                                  auth_plugin='mysql_native_password')
    cursor = cnx.cursor(buffered = True, dictionary = True)

    list_items_of_pagination = ("SELECT first_name, last_name FROM users "
                                "LIMIT %s, %s;" % ((current_page - 1) * no_of_record, no_of_record) )
    cursor.execute(list_items_of_pagination)


    results = cursor.fetchall()

    cursor.close()
    cnx.close() 

    if len(results) != 0 :
        return f'{results}\n'
    else:
        return '[], No records found'
    


print(pagination(1, 10))
# [{'first_name': 'Tyler', 'last_name': 'Spradley'}, 
# {'first_name': 'David', 'last_name': 'Desmarais'}, 
# {'first_name': 'Miles', 'last_name': 'Harlow'}, 
# {'first_name': 'Becca', 'last_name': 'Kingman'}, 
# {'first_name': 'Rotana', 'last_name': 'Greger'}, 
# {'first_name': 'Cinzia', 'last_name': 'Derige'}, 
# {'first_name': 'Karen', 'last_name': 'Boyce'}, 
# {'first_name': 'Don', 'last_name': 'Ringer'}, 
# {'first_name': 'Dane', 'last_name': 'Schuette'}, 
# {'first_name': 'Melessa', 'last_name': 'Steinhauer'}]

print(pagination(6, 9))
# Remain Five Record in the last page
# [{'first_name': 'Muhammed', 'last_name': 'Knotts'}, 
# {'first_name': 'Allyson', 'last_name': 'Kjelstad'}, 
# {'first_name': 'Tara', 'last_name': 'Wigmanich'}, 
# {'first_name': 'Patrick', 'last_name': 'Baillargeon'}, 
# {'first_name': 'Louise', 'last_name': 'Sublewski'}]

print(pagination(6, 10))
# [], No records found