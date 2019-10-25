import MySQLdb

db = MySQLdb.connect{"localhost","root","root"}

cursor = db.cursor()

cursor.execute("create database if not exists douban;")
cursor.execute("use douban;")
cursor.execute("create table if not exists douban;")
