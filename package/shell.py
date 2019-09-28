import os


def init():
    os.system("pip install -r requirements.txt")


def test():
    return os.system("flake8  --ignore E501")


def beautify():
    print(os.system("black ./package"))
