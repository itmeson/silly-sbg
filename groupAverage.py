import sys

try:
    fNAME = sys.argv[1]
    fFILE = open(fNAME, 'rU')
except:
    print "averageGroup scores for input into Ulearn\n\n"
    print "Usage:   python groupAverage.py filename"
    sys.exit()

for line in fFILE:
    data = line.strip().split(',')
    scores = data[9:]
    scoreLIST = []
    for s in scores:
        scoreLIST.append(float(s.split(":")[1]))
    print data[1], data[2], "\t", sum(scoreLIST)*5/4/len(scoreLIST)

