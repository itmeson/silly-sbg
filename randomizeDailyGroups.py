import sys, random

try:
    classPATH = sys.argv[1]
    day = int(sys.argv[3]) + 5
    whichCLASS = sys.argv[2]
except:
    print "USAGE:\n\nrandomizeDailyGroups.py class section day\n\n"
    sys.exit()


classFILE = open(classPATH + 'attendance.csv', 'rU')

studentsPRESENT = []
for (i, line) in enumerate(classFILE):
    if i == 0:
        continue
    data = line.strip().split(',')
    if data[6] == whichCLASS:
        if data[day] == '1':
            studentsPRESENT.append(data[1:3])

random.shuffle(studentsPRESENT)
group = 0
for (i,n) in enumerate(studentsPRESENT):
    if i%4 == 0:
        group += 1
	print "GROUP ", group
    print '\t', i+1, n[0], ',', n[1]

