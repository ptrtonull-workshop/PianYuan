import os, sys


def get_version():
    v = ""
    flag = 0
    try:
        with open(os.getcwd() + "\\pianyuan\\__init__.py", "r") as f:
            tmp = f.read()
            for i in range(len(tmp)):
                if i >= 11 and i < len(tmp) - 2:
                    v = v + tmp[i]
    except:
        return
    return v


def package():
    print("start packaging =================================")
    os.system(r"python setup.py sdist")


def upload():
    upload_path = (
        "twine upload " + os.getcwd() + "\\dist\\pianyuan-" + get_version() + ".tar.gz"
    )
    package()
    print("start upload=====================================")
    os.system(upload_path)


def update():
    os.system(r"python -m pip install --upgrade pianyuan")
