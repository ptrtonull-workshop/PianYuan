import json


def apart(srting, char):
    tmp = ""
    a = []
    for i in srting:
        if i == char:
            a.append(tmp)
            tmp = ""
        else:
            tmp += i
    return a


# find a value according to a path
# path: './test/a'
# dic:  test={
#       "test":{
#           "a":"b",
#           "c":"x"
#       }
#   }
# or file path like "../test.json"
# return: b
def path_to_dic(path, dic):
    exm = ""
    if type(dic) == type(exm):
        dic = json_file(dic)
    path += "/"
    path = path.replace("./", "")
    a = apart(path, "/")
    lens = len(a)
    value = dic
    for j in a:
        value = value[j]
    return value


test = {"test": {"app": {"a": "b"}}}


def json_file(path):
    f = open(path, "r")
    data = f.read()
    json_string = json.loads(data)
    f.close()
    return json_string


print(path_to_dic("./test/app/a", test))
