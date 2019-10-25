import argparse
from pianyuan.spider import *
from pianyuan.shell import *
from pianyuan.package import *


def main():
    start = 0
    end = 0
    host = ""
    usename = ""
    password = ""
    parser = argparse.ArgumentParser()
    parser.add_argument("-G", help="login in mysql and Crawl", type=str, nargs=5)
    parser.add_argument(
        "-g", help="login in mysql without password and Crawl", type=str, nargs=4)
    parser.add_argument("-S", help="Shell action", type=str, nargs=1)
    parser.add_argument("-P", help="package action", type=str, nargs=1)
    args = parser.parse_args()
    if args.G or args.g:
        if args.G:
            start = args.G[0]
            end = args.G[0]
            host = args.G[2]
            usename = args.G[3]
            password = args.G[4]
        elif args.g:
            start = args.g[0]
            end = args.g[0]
            host = args.g[2]
            usename = args.g[3]
        acc = mysql.modify(host, usename, password)
        db = mysql.create(acc)
        run(start, end, db)
    if args.S:
        if args.S[0] == "init":
            init()
        elif args.S[0] == "beautify":
            beautify()
        elif args.S[0] == "test":
            test()
        else:
            print("There is no action : " + args.S[0])
    if args.P:
        if args.P[0] == "package":
            package()
        elif args.P[0] == "upload":
            upload()
        elif args.P[0] == "update":
            update()
        else:
            print("There is no action : " + args.S[0])


if __name__ == "__main__":
    main()
