import os


def init():
    os.system("pip install -r requirements.txt")


def test():
    # if os.system("flake8  --ignore E501") == 1:
    if os.system("flake8  --ignore E501") != 0:
        exit("test error")


def beautify():
    os.system("black ./package")
