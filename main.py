file1 = open('sq.txt', 'r')
firstLine = file1.readline()
file_test = open('ReadPairsOutput.txt', 'r')
file_test_check = file_test.readline()
Lines = file1.readlines()


def findSum(str1):
    temp = "0"

    Sum = 0

    for ch in str1:

        if (ch.isdigit()):
            temp += ch

        else:

            Sum += int(temp)

            temp = "0"

    return Sum + int(temp)


kAndD = 0
kAndD += findSum(firstLine)
d = {}
path = []
count = 0
prefix_count = 0

L = ""
start = 30
stop = 100
prefixString = ""
suffexString = ""

for line in Lines:
    Line = line[:30] + line[30 + 1:]
    # print("LINE=>", len(Line))
    print(line)
    print(Line[31: len(Line) - 1])
    d[(Line[0:len(Line) - 32], Line[30:len(Line) - 2])] = (Line[1:len(Line) - 31], Line[31:len(Line) - 1])
    # print(d)


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
        if value == key_index:
            path.append(key_index)
            path.append(d[key_index])


def get_prefix(pathLen, key_p, counter):
    prefix = ""

    if counter == pathLen - 1:
        prefix += key_p
    else:
        prefix += key_p[0]
    counter += 1
    return prefix


def get_suffex(pathLen, second_val, counter):
    suffex = ""

    if counter == pathLen - 1:
        suffex += second_val
    else:
        suffex += second_val[0]
    counter += 1
    return suffex


for key in d:
    if not check_start_point(key):
        path.append(key)
        path.append(d[key])
        check_modulus()
        path = list(dict.fromkeys(path))
        count = 0
        for key_p, c in path:
            prefixString += get_prefix(len(path), key_p, count)
            suffexString += get_suffex(len(path), c, count)
            count += 1
        break
sim = ""


def get_KD(sim):
    sim += prefixString
    sim += suffexString[-kAndD:]
    # print()
    #new_counter = 0
    #for i in reversed(suffexString):
        #if new_counter < kAndD:
            #sim += i
            #new_counter += 1
    print("sooo=>", sim)


get_KD(sim)
