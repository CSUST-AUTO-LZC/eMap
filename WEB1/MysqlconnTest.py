#!/user/python


import mysql.connector

config = {
    "user":"root",
    "password":"18390927803",
    "host":"localhost",
    "database":"test"
         }
#建立连接
cnx = mysql.connector.connect(**config)
cur = cnx.cursor(buffered=True)

#查找数据
sql_stmt = "SELECT name,pwd,sex,home,info,vip FROM user;"
cur.execute(sql_stmt)

#显示数据
for user_data in cur.fetchall():
    user_name = user_data[0]
    user_pwd = user_data[1]
    user_sex = user_data[2]
    user_home = user_data[3]
    user_info = user_data[4]
    user_vip = user_data[5]
    print("name: %s   password: %s  sex: %s %s %s %s " %(user_name,user_pwd,user_sex,user_home,user_info,user_vip))
    print('--'*25)

