#!/usr/bin/python

import random, sys

whichClass = sys.argv[2]
classFile = sys.argv[1]
names = []

classList = open(classFile, 'rU')
for line in classList:
    studentData = line.strip().split(',')
    if studentData[-1] == whichClass:
        names.append(studentData[:2])

random.shuffle(names)
group = 0
for (i, n) in enumerate(names):
    if i % 4 == 0:
        group += 1
	print "GROUP ", group
    print '\t', i+1, n[0], ',', n[1]

