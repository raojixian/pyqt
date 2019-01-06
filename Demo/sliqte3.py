# coding:utf-8
import sqlite3

conn = sqlite3.connect('database/user.db')
c = conn.cursor()

sql = '''INSERT INTO user VALUES('raojixian','raojixian')'''

c.execute(sql)

sql_name_password = "SELECT name,password FROM user"
for i in c.execute(sql_name_password):
    print(i)
