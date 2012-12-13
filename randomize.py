#!/usr/bin/python

import random, sys


classPATH = sys.argv[1]
whichClass = sys.argv[2]
names = []

classList = open(classPATH + 'names.csv', 'rU')
for line in classList:
    studentData = line.strip().split(',')
    if studentData[-1] == whichClass:
        names.append(studentData[1:3])

random.shuffle(names)
group = 0
for (i, n) in enumerate(names):
    if i % 4 == 0:
        group += 1
	print "GROUP ", group
    print '\t', i+1, n[0], ',', n[1]

