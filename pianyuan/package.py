from pianyuan import *
import os

upload_path = "twine upload dist/pianyuan-" + version + ".tar.gz"
def package():
    os.system(r"python setup.py sdist")

def upload():
    package()
    os.system(upload_path)
