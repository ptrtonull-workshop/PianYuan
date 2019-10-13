import sys, os, json


def getVersion():
    NowPath = os.getcwd()
    with open(NowPath + "\\" + "\\pianyuan\\__init__.py", "r") as f:
        tmp = f.read()
        tmp = json.loads(tmp)
        tmp = tmp["inf"][0]["version"]
    return tmp
