import sys

path = sys.argv[1]

attFile = open(path+"attendance.csv", 'rU')

for line in attFile:
    data = line.strip().split(',')
    if data[7] != '1' and data[8] != '1':
        print line

