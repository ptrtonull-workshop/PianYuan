import os


def init():
    os.system("pip3 install -r requirements.txt")


def test():
    if os.system("flake8  --ignore E501 F403 F405 F401") != 0:
        exit("test error")


def beautify():
    os.system("black ./")
    os.system("black ./pianyuan")
