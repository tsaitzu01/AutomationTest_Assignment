import mysql.connector
import pprint

cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='exercise',
                              auth_plugin='mysql_native_password')
cursor = cnx.cursor(buffered = True, dictionary = True)

# 新增 3 筆商店資料
shop_id = [1, 2, 3]
shop_name = ["Apple Store", "Banana Shop", "Candy Crash"]
shop_address = ["嘉義縣民雄鄉光明一街14號", "屏東縣內埔鄉展興路21號", "臺中市后里區舊社路4號"]
add_shop = ("INSERT INTO Shop "
            "(ShopId, Name, Address) "
            "VALUES (%s, %s, %s)")
# 新增 3 筆客戶資料
customer_id = [1, 2, 3]
customer_name = ["Amber", "Bob", "Chris"]
customer_address = ["南投縣南投市光明二路27號", "嘉義市西區福義街10號", "臺東縣大武鄉政通五街31號"]
customer_age = ["19", "20", "44"]
customer_sex = ["Female", "Male", "Male"]
add_customer = ("INSERT INTO Customer "
                "(CustomerId, Name, Address, Age, Sex) "
                "VALUES (%s, %s, %s, %s, %s)")
# 每位客戶都在各商店新增一筆訂單
amount = [200, 300, 400, 222, 111, 333, 234, 456, 789]
order_date = ["2023-01-01", "2023-02-01", "2023-03-01", 
              "2023-03-03", "2023-05-05", "2023-08-08", 
              "2023-01-02", "2023-04-05", "2023-07-08"]
add_order = ("INSERT INTO `Order` "
             "(CustomerId, ShopId, amount, order_date) "
             "VALUES (%s, %s, %s, %s)")

for i in range(len(shop_id)):
    data_shop = (shop_id[i], shop_name[i], shop_address[i])
    cursor.execute(add_shop, data_shop)
    cnx.commit()

for i in range(len(customer_id)):
    data_customer = (customer_id[i], customer_name[i], customer_address[i], customer_age[i], customer_sex[i])
    cursor.execute(add_customer, data_customer)
    cnx.commit()

for i in range(len(amount)):
    if int(i / 3) == 0:
        data_order = (customer_id[0], shop_id[i % 3], amount[i], order_date[i])
    elif int(i / 3) == 1: 
        data_order = (customer_id[1], shop_id[i % 3], amount[i], order_date[i])
    else:
        data_order = (customer_id[2], shop_id[i % 3], amount[i], order_date[i])
    cursor.execute(add_order, data_order)
    cnx.commit()
# 取得客戶的所有訂單資訊
def select_orders():
    select_orders = ("""
                    SELECT Customer.CustomerId, Customer.Name, Customer.Address, Shop.Name as Shop, `Order`.amount, `Order`.order_date
                    FROM `Order` 
                    INNER JOIN Customer ON `Order`.CustomerId = Customer.CustomerId 
                    INNER JOIN Shop ON `Order`.ShopId = Shop.ShopId""")
    cursor.execute(select_orders) 
    return cursor.fetchall()

pprint.pprint(select_orders(), sort_dicts = False)

cursor.close()
cnx.close()