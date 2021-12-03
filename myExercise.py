import sys

f = open(sys.argv[1], 'r')
names = sys.argv[2]
names = names.split(',')

commands = f.readlines()
commands2 = []
for c in commands:
    com = c.strip()
    commands2.append(c.split(':'))

stu = dict()
for i in range(len(commands2)):
    stu[commands2[i][0]] = commands2[i][1]

for n in names:
    try:
        print('Name: ' + n + ', University: ' + stu[n].strip(), end=' ')
    except KeyError:
        print('No record of ’' + n + '’ was found!',end=' ')
