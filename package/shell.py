import os


def init():
    os.system("pip install -r requirements.txt")


def test():
    os.system("flake8  --ignore E501")


def beautify():
    os.system("black ./package")
