import MySQLdb

account = {"host": "localhost", "username": "root", "password": "root"}


def modify(host_t, username_t, password_t):
    global account
    account["host"] = host_t
    account["username"] = username_t
    account["password"] = password_t
    return account


def create(account):
    db = MySQLdb.connect(
        account["host"], account["username"], account["password"], "sys", charset="utf8"
    )
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE if Not Exists pianyuan;")
    cursor.execute("USE pianyuan;")
    cursor.execute(
        "create table if Not Exists film(quality char(50),moive_name mediumblob, url mediumblob,size char(50),flash_time char(50))ENGINE=MyISAM DEFAULT CHARSET=utf8;"
    )
    db.commit()
    return db


def close(db):
    db.close()


def delect(db, table):
    cursor = db.cursor()
    cursor.execute("USE pianyuan;")
    if table == "film":
        cursor.execute("truncate table film;")
    db.commit()


def add(info, db):
    cursor = db.cursor()
    sql = "insert into (quality,moive_name,url,size,flash_time) values(%s,%s,%s,%s,%s)"
    cursor.execute(
        sql,
        (
            str(info["quality"]),
            str(info["movie_name"]),
            str(info["url"]),
            str(info["size"]),
            str(info["flash_time"]),
        ),
    )
    db.commit()


def add_douban(info, db):
    cursor = db.cursor()
    sql = "insert into douban()"


def number(db):
    cur = db.cursor()
    print("共有%d条记录" % cur.execute("SELECT * FROM pianyuan.film;"))


def clean(db):
    cur = db.cursor()
    sql = "use pianyuan;truncate table film;"
    cur.execute(sql)
    db.commit()
    db.close()
