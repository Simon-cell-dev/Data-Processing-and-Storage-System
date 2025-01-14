# Data-Processing-and-Storage-System
This Python - based project integrates data from text/JSON files into a MySQL database(DBeaver24.3.2). Using custom classes (TextReader &amp; JsonFileReader) and pymysql, it creates the py_sql database and orders table, inserts data, and streamlines data management for analysis and decision - making.
You need to pay attention to the part of the code that I commented out.
main.py:
# cursor.execute("create database py_sql")  This code is to create a table called py_stql
# cursor.execute("create table orders(order_date date,order_id varchar(255),money int,province varchar(10))") This code is to create columns in the py_stql table
If the data you want to import is different from mine, you need to pay attention to every. py file for modification or contact me. (Because I am too lazy, I don't want to write a universal keyword code now.)
