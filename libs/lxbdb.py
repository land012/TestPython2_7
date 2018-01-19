#! /usr/bin/env python
# -*- coding: utf8
import MySQLdb
import os
import sys

from email import Utils

host = "127.0.0.1"
user = "root"
password = "123456"

#数据库连接
def getConnection():
    return MySQLdb.connect(host=host, user=user, passwd=password, db="db1", charset="utf8", port=3306)
    

#数据库查询
def scale(conn, sql):
    print sql
    cursor = conn.cursor()
    cursor.execute(sql)
    table = cursor.fetchall()
    return table

def scalebyparam(conn, sql,T):
    print sql
    cursor = conn.cursor()
    cursor.execute(sql,T)
    table = cursor.fetchall()
    return table
