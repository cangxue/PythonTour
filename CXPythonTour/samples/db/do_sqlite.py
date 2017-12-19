#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 导入SQLite驱动:
import sqlite3

# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:

# conn = sqlite3.connect('test.db')
#
# # 创建一个Cursor
# cursor = conn.cursor()

# # 执行一条SQL语句，创建user表：
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

#
# # 继续执行一条SQL语句，插入一条数据:
# cursor.execute('insert into user (id, name) values (\'2\', \'Michael\')')
#
# # 通过rowcount获得插入的行数:
# print('rowcount=', cursor.rowcount)
#
# # 关闭Cursor
# cursor.close()
#
# # 提交事务：
# conn.commit()
#
# # 关闭Connection:
# conn.close()


# 查询记录：
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# 插入数据
cursor.execute('INSERT INTO user (id, name) VALUES (\'3\', \'Bob\')')
cursor.execute('INSERT INTO user (id, name) VALUES (\'4\', \'Dog\')')

# 删除数据
cursor.execute('DELETE FROM user WHERE id=?', '1')

# 执行查询语句:
cursor.execute('select * from user where id=?', '3')
values = cursor.fetchone()
print(values)

cursor.execute('SELECT * FROM user')
#获得查询结果:
values = cursor.fetchall()
print(values)

cursor.execute('SELECT * FROM user WHERE id=?', '2')
values = cursor.fetchone()
print(values)




cursor.close()
conn.close()