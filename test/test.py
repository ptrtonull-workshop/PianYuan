from pick import pick
import os

list = []

for i in os.listdir("./"):
    list.append(i)

title = "Please choose your favorite programming language (press SPACE to mark, ENTER to continue): "
options = list
options.append(">quit<")
selected = pick(options, title, multi_select=True, min_selection_count=1)
name = selected[0][0]
code = selected[0][1]
if code != len(list) - 1:
    shell = "python " + "./" + name
    os.system(shell)
else:
    quit()
