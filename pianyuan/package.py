from pianyuan import *
import os

upload_path = "twine upload dist/pianyuan-" + version + ".tar.gz"
def package():
    print("start packaging =================================")
    os.system(r"python setup.py sdist")
    print("start installing ================================")
    os.system(r"python setup.py install")

def upload():
    package()
    print("start upload=====================================")
    os.system(upload_path)
