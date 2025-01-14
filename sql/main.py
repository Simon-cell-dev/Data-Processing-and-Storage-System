from pymysql import Connection
from file_defince import *
from data_defince import *

tr = TextReader("D:/销售1月.txt")
jr = JsonFileReader("D:/销售二月JSON.txt")

list1:list[Record] = tr.read_data()
list2:list[Record] = jr.read_data()

# 将两个list合并为一个list
all_data:list[Record] = list1 + list2
# 获取到MySql数据库的链接对象
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='', # 密码
    autocommit=True # 设置自动提交
)
# 数据读取
cursor = conn.cursor()
# cursor.execute("create database py_sql")
conn.select_db('py_sql') # 先选择数据库
# cursor.execute("create table orders(order_date date,order_id varchar(255),money int,province varchar(10))")
for record in all_data:
    sql = "insert into orders values (%s, %s, %s, %s)"
    cursor.execute(sql, (record.date, record.order_id, record.money, record.province))
# 关闭到服务器链接
conn.close()