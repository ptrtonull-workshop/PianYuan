from pianyuan import *
import os, sys


upload_path = "twine upload " + os.getcwd() + "\\dist\\pianyuan-" + version + ".tar.gz"


def package():
    print("start packaging =================================")
    os.system(r"python setup.py sdist")


def upload():
    package()
    print("start upload=====================================")
    os.system(upload_path)


def update():
    os.system(r"python -m pip install --upgrade pianyuan")
