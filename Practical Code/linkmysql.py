#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="192.168.1.107",    # your host, usually localhost
                     user="lizhe",         # your username
                     passwd="",  # your password
                     db="test")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM employee")

# print all the first cell of all the rows
for row in cur.fetchall():
    print str(row)

db.close()
