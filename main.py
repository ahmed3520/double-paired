file1 = open('sq.txt', 'r')
Lines = file1.readlines()
d = {}
path = []
count = 0
# Strips the newline character
L = ""
start = 4
stop = 6

for line in Lines:
    Line = line[0: start:] + line[stop + 1::]
    d[(Line[0:len(Line) - 6], Line[4:len(Line) - 2])] = (Line[1:len(Line) - 5], Line[5:len(Line) - 1])
print("D", d)


def check_start_point(key_check):
    status = False
    for key in d:
        if d[key] == key_check:
            status = True
    return status


def check_modulus():
    for key_in in d:
        if len(path) % 2 == 0:
            last_index = len(path) - 1
            check_path(path[last_index])


def check_path(value):
    for key_index in d:
        print(value, "key index :-", key_index)
        if value == key_index:
            print("kkkk")
            path.append(key_index)
            path.append(d[key_index])

for key in d:
    print(key, ":", d[key])
    print(path)
    if not check_start_point(key):
        path.append(key)
        path.append(d[key])
        print(path)
        check_modulus()
        path = list(dict.fromkeys(path))
        print(path)
        break

