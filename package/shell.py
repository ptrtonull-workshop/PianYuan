import os


def init():
    os.system("pip install -r requirements.txt")


def test():
    if os.system("flake8  --ignore E501") == 1:
        exit(1)


def beautify():
    os.system("black ./package")
