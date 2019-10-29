from pick import pick
import os


# the file name is python soruce code ?
# name: a string like test.py
# return : true or false
def isPy(name):
    lens = len(name)
    code = name[lens - 3 :]
    if code == ".py":
        return True
    else:
        return False

# the path is a folder?
# path : target path like ./
# return : Ture or False
def isFolder(path):
    if os.path.isdir(path):
        return True
    elif os.path.isfile(path):
        return False

# find folder in path
# path : target path like ./
# return : a list like:
# ['.git', '.vscode', 'build', 'data', 'dist', 'pianyuan', 'pianyuan.egg-info', 'test', '__pycache__']
def find_folder(path):
    folder=[]
    all = os.listdir(path)
    for i in all:
        if isFolder(i) is True:
            folder.append(i)
    return folder


# find all python file name in a folder without folder
# # path : target path like ./
# return ['crawl.py', 'key.py', 'picks.py', 'spider.py', 'test.py', 'tinydb.py']
def find_py_in_last_folder(path):
    list_temp = []
    list = []

    for i in os.listdir(path):
        list_temp.append(i)

    for a in list_temp:
        if isPy(a):
            list.append(a)

    return list





# find all python file in path
# path : target path like ./
#return :
def find_py(path):
    all_menu=[]
    all_menus={}
    folder=find_folder(path)
    for i in folder:
        all_menu.append(i)
    if len(all_menu)!=0:
        for j in all_menu:
            all = os.listdir(path+j)
            for x in all:
                all_menus[j]=all
        return all_menus
    else:
        return find_py_in_last_folder(path)


# the folder have python file
def have_py_in(listname):
    for i in listname:
        if isPy(i):
            return True
    return False

# find all folder which has python file
def return_py_folder(path):
    folder=find_py(path)
    py_folder=[]
    for i in folder:
        if have_py_in(folder[i]) is True:
            py_folder.append(i)
    return py_folder



def menu(path):
    list_temp = []
    list = []

    for i in os.listdir(path):
        list_temp.append(i)

    for a in list_temp:
        if isPy(a):
            list.append(a)

    title = "Please choose a python file(press SPACE to mark, ENTER to continue): "
    options = list
    options.append(">quit<")
    selected = pick(options, title, multi_select=True, min_selection_count=1)
    name = selected[0][0]
    code = selected[0][1]
    if code != len(list) - 1:
        shell = "python " + path+"/" + name
        os.system(shell)
    else:
        quit()

