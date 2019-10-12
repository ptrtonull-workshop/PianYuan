import os


def init():
    os.system("pip install -r requirements.txt")


def test():
    if os.system("flake8  --ignore E501 F403 F405 F401") != 0:
        exit("test error")


def beautify():
    os.system("black ./pianyuan")
