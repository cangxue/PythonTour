#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2017-12-20
@author: Palesnow

功能：mysql学习

网址：http://www.runoob.com/mysql/mysql-create-database.html

"""

########## prepare ##########

# install mysql-connector-python:
# pip3 install mysql-connector-python --allow-external mysql-connector-python

import mysql.connector

# 链接数据库
conn = mysql.connector.connect(user='root', password='root', database='ROOT1')
cursor = conn.cursor()

# 创建user表
cursor.execute('CREATE TABLE IF NOT EXISTS user (id VARCHAR(20) PRIMARY KEY, name VARCHAR(20))')

# 创建friend表
cursor.execute('CREATE TABLE IF NOT EXISTS friend (id VARCHAR(20) PRIMARY KEY, name VARCHAR(20), age VARCHAR(20))')

# 插入一行记录
# cursor.execute('insert into friend (id, name, age) values (%s, %s, %s)', ('4', 'xiaoma', 23))
# 提交事务:
# conn.commit()

# 更新数据
# cursor.execute('update friend set age="15" where id = %s', ('2',))
# 提交事务:
# conn.commit()  # 提交

# 删除数据
# cursor.execute('delete from user where name=%s', ('pig',))

# like查询:
cursor = conn.cursor()
cursor.execute('select id, name, age from user where name like %s or name=%s', ("%ig%", 'Bob',))
values = cursor.fetchall()
# print(values)

# union语句
cursor.execute('select id, name, age from user where name=%s UNION DISTINCT SELECT id, name, age FROM user where age=%s order by age', ('Bob', 17,))
values = cursor.fetchall()
# print(values)

# 运行查询:
cursor = conn.cursor()
cursor.execute('select id, name, age from user where age = %s and name=%s', (17, 'Bob',))
values = cursor.fetchall()
# print(values)

# 排序
cursor.execute('select * from user order by age desc, id desc ')
values = cursor.fetchall()
# print(values)

# GROUP BY 语句
# 按名字进行分组，并统计每个名字相同的个数
cursor.execute('select name, count(*) from user GROUP BY name')
values = cursor.fetchall()
# print(values)
# 按名字进行分组，并统计每个名字的总年龄数
# cursor.execute('select name, sum(age) as age_sum from user group by name with ROLLUP ')
# 使用 coalesce 来设置一个可以取代 NUll 的名称
cursor.execute('select coalesce(name, "总年龄数"), sum(age) as age_sum from user group by name with ROLLUP ')
values = cursor.fetchall()
# print(values)

# Mysql 连接的使用
# 使用 INNER JOIN
# cursor.execute('select b.id, b.name, a.age from user a inner join friend b on a.age = b.age')
# LEFT JOIN 会读取左边数据表的全部数据，即便右边表无对应数据
# cursor.execute('select b.id, b.name, a.age from user a left join friend b on a.age = b.age')
# # RIGHT JOIN 会读取右边数据表的全部数据，即便左边边表无对应数据
cursor.execute('select b.id, b.name, a.age from user a right join friend b on a.age = b.age')
values = cursor.fetchall()
# print(values)

# NULL 值处理
# cursor.execute('select * from user where name is null')
cursor.execute('select * from user where name is not null')
values = cursor.fetchall()
print(values)

# 正则表达式
cursor.execute('select name from user where name regexp "g{2,3}"')
values = cursor.fetchall()
print(values)

# 事务
# conn.commit()  # 提交
# conn.rollback()  # 回滚
# conn.autocommit = 0  # 禁止自动提交
# conn.autocommit = 1  # 开启自动提交

# ALTER命令
# cursor.execute('alter table friend add date_time DATE ')
# cursor.execute('alter table friend drop date_time')
# conn.commit()
# MODIFY 或 CHANGE 子句
# cursor.execute('alter table friend modify age CHAR(10) ')
# cursor.execute('alter table friend change age ages INT ')
# conn.commit()
# cursor.execute('alter table friend modify age not null default "25" ')
# 设置默认值
# cursor.execute('alter table friend alter age set default "25"')
# conn.commit()
# 修改表名
# cursor.execute('alter table friend rename to friends')

# MySQL 索引
# 创建索引
# cursor.execute('create index name_indexname on friend(name)')
# 修改表结构(添加索引)
# cursor.execute('alter table friend add index name_indexname(name)')
# conn.commit()
# 删除索引
# cursor.execute('drop index indexname on friend')
# conn.commit()
# 显示索引信息
# cursor.execute('show index from friend ')
# values = cursor.fetchall()
# print('显示索引信息：' % values)

# MySQL 临时表
# cursor.execute('create temporary table temp_friend (id VARCHAR )')

# MySQL 复制表
# 1、获取数据表的完整结构。
# cursor.execute('show create table friend')
# 2、修改SQL语句的数据表名，并执行SQL语句
# cursor.execute('create table clone_tbl (friend_id INT(11) PRIMARY KEY , friend_name VARCHAR(20) )')
# 3、拷贝数据表的数据
# cursor.execute('insert into clone_tbl (friend_id, friend_name) SELECT id, name FROM friend')


# 关闭Cursor和Connection:
cursor.close()
conn.close()