reads=['GACC','GCGC','TACC','GGCT','GCTT','TTAC']
#reads = ['GAGG', 'GGGG', 'GGGA', 'CAGG', 'AGGG', 'GGAG']

file1 = open('sq.txt', 'r')
Lines = file1.readlines()
d={}
count = 0
# Strips the newline character
L=""
start = 4
stop = 6

for line in Lines:
   Line = line[0: start:] + line[stop + 1::]
   d[(Line[0:len(Line)-6] , Line[4:len(Line)-2])]=(Line[1:len(Line)-5],Line[5:len(Line)-1])
print("D", d)
def check_function(key_check):
    status = False
    for key in d:
        if d[key] == key_check:
            status = True
        print("lol:-",d[key], " status ", status, "key check", key_check)
    return  status
for key in d:
        print(key,":", d[key])
        print(check_function(key))