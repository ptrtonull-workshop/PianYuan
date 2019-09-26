import sys
from package import spider
from package import mysql
from package import shell


def main():
    Len = len(sys.argv)
    if sys.argv[1] == "-G":
        if Len < 6:
            print("too less value")
        elif Len == 6:
            acc = mysql.modify(sys.argv[4], sys.argv[5], "")
        else:
            acc = mysql.modify(sys.argv[4], sys.argv[5], sys.argv[6])
        db = mysql.create(acc)
        spider.run(sys.argv[2], sys.argv[3], db)
    elif sys.argv[1] == "-S":
        if Len < 3:
            print("too less value")
        elif sys.argv[2] == "init":
            shell.init()
        elif sys.argv[2] == "test":
            shell.test()
        elif sys.argv[2] == "beautify":
            shell.beautify()
        else:
            print("This is no function for -S")
    elif sys.argv[1] == "-M":
        if Len < 5:
            print("too less value")
        else:
            if sys.argv[2] == "number":
                if Len == 5:
                    acc = mysql.modify(sys.argv[3], sys.argv[4], "")
                else:
                    acc = mysql.modify(sys.argv[3], sys.argv[4], sys.argv[5])
            else:
                print("I can't understand you.")
        db = mysql.create(acc)
        mysql.number(db)
    else:
        print("I can't understand you.")


main()
