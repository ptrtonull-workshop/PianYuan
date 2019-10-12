from pianyuan import *
import os

upload = "twine upload dist/pianyuan-" + version + ".tar.gz"
os.system(r"python setup.py sdist")
os.system(upload)
