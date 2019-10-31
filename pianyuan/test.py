def open_data(num):
    f = open("../data/" + str(num) + ".json", "r")
    data = f.read()
    return data
