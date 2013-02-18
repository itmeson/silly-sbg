import sys

path = sys.argv[1]
days = float(sys.argv[2])
addIN = int(sys.argv[3])

attFILE = open(path, 'rU')

for (i, line) in enumerate(attFILE):
    if i == 0:
        continue
    info = line.strip().split(',')
    name = info[1:3]
    att = info[7:27]
    tot = 0
    for d in att:
        if d == '1':
            tot += 1
    print (tot+addIN)/days, '\t', name[0], name[1] 
