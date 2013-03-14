import readline

class MyCompleter(object):  # Custom completer
    """"Borrowed from http://stackoverflow.com/questions/7821661/how-to-code-autocompletion-in-python
    This class provides BASH style tab completion (1 tab gives match if there's a unique, 2 gives list of possible)
    """
    
    def __init__(self, options):
        self.options = sorted(options)

    def complete(self, text, state):
        if state == 0:  # on first trigger, build possible matches
            if text:  # cache matches (entries that start with entered text)
		self.matches = [s for s in self.options 
                   if text in s]

                #self.matches = [s for s in self.options 
                #                    if s and s.startswith(text)]
            else:  # no text entered, all matches possible
                self.matches = self.options[:]

        # return match indexed by state
        try: 
            return self.matches[state]
        except IndexError:
            return None

def inputNames(standards=False, AllScoreData = {}):
    while True:
        results = {}
        name = raw_input("Name: ")
        print "You entered", name
        if name == "xx":
	    break
        elif standards:
	    scores = raw_input(str(standards) + ' :').split(",")
	    for i in range(len(standards)):
		results[standards[i]] = scores[i]
	    if len(scores) > len(standards):
		results = standardScorePairs(scores[len(standards):], results)
        else:
            scores = raw_input('st:sc, ').split(",")
	    results = standardScorePairs(scores, results)
	saveScores(name, results, AllScoreData)

def standardScorePairs(scores, results):
    for s in scores:
	pair = s.split(":")
	results[pair[0]]=pair[1]
    return results

def inputStandards(defaultStandards = ["AC.1"]):
    input = raw_input('List of standards to assess for all')
    if input:
    	standards = input.split(',')
    else:
	standards = defaultStandards
    return standards

def saveScores(name, results, AllScoreData):
    if name in AllScoreData:
        AllScoreData[name].update(results)
    else:
	AllScoreData[name] = results

def writeGradebook(fname, AllScoreData):
    import pickle
    fData = open(fname, 'w')
    pickle.dump(AllScoreData, fData)
    fData.close()
    
def readGradebook(fname):
    import pickle
    fData = open(fname, 'rU')
    return pickle.load(fData)

def enterAttendance(path):
    print path + 'hah'
    #1. Get attendance book
    book = open(path + 'attendance.csv', 'rU')
    attendanceData = {}
    for (i,line) in enumerate(book):
	if i == 0:
	    firstLINE = line
	    continue
        data = line.strip().split(',')
	attendanceData[i] = data
    book.close()

    #2. Get desired date and column
    date = int(raw_input('Which class day do you want?'))
    dateCol = date + 5   #attendance data starts in column 7

    #3. Get student yes/no
    #4. repeat 3.
    while True:
        name = raw_input('Name:?')
	print "You entered: ", name
        if name == "xx":
	    break  
        try:
	    studentID = int(name.split(',')[0])
 	    attendanceData[studentID][dateCol] = 1
	except:
	    print "something was wrong with that name -- try again", sys.exc_info()
    #5. Write attendance book
    IDs = attendanceData.keys()
    IDs.sort()
    book = open(path + 'attendance.csv', 'w')
    book.write(firstLINE)
    for ID in IDs:
        book.write(",".join(map(str, attendanceData[ID])))
	book.write('\n')
    book.close()

def enterHW(path):
    #1. Get list of assignments
    hwLISTfile = open(path+'grade_header', 'rU')
    hwLIST = hwLISTfile.readline().strip().split(',')
    hwLISTfile.close()
    hwCOLUMNS = hwLIST[9:29]   #9 and 29 are hard-coded. TODO: generalize
    #2 Ask which one to enter
    while True:    
        whichHW = hwCOLUMNS[int(raw_input('Which HW? '+str(hwCOLUMNS)))]
        print '\n\n'
        check = raw_input(whichHW + '? 1 if correct, 0 if not')
        if check == '1':
            print '\n\n'
            break
    #3. Enter names and scores
    homeworkFILE = open(path + 'homework.csv', 'a')
    while True:
        name = raw_input("Name: ")
        print "You entered", name
        if name == "xx":
            break
        score = raw_input("Score? Default is 5")
        if score:
            score = int(score)
        else:
            score = 5
        output = name + ',' + whichHW + ',' + str(score) + '\n'
        homeworkFILE.write(output)
        #4. Write to the ulearn file

    #n. Close the homework file
    homeworkFILE.close()



def exportToUlearn(path):
    pass

def exportToActiveGrade(path):
    pass

def enterIndividual(path):
    pass

def enterGroup(path):
    import time
    standards = inputStandards()
    standardsFILE = open(path + 'standards.csv', 'a')
    QuizID = raw_input('Enter string identifer for Quiz (Q1,Q2, etc.)')
    scores = ["4" for x in standards]
    while True:
        results = {}
        name = raw_input("Name: ")
        print "You entered", name
        if name == "xx":
	    break
        elif standards:
	    scoreINPUT = raw_input(str(standards) + " :(" + str(scores) + ")")
	    if scoreINPUT:
                scores = scoreINPUT.split(",")
	    for i in range(len(standards)):
		results[standards[i]] = scores[i]
	    if len(scores) > len(standards):
		results = standardScorePairs(scores[len(standards):], results)
        else:
            scores = raw_input('st:sc, ').split(",")
	    results = standardScorePairs(scores, results)
        resultsOUTPUT = []
	resKEYS = results.keys()
	resKEYS.sort()
        for key in resKEYS:
            resultsOUTPUT.append(key + ':' + results[key])
	timeOUT = time.strftime('%X %x')
        standardsFILE.write(name + ',' + timeOUT + ',' + QuizID + ',' + ','.join(resultsOUTPUT) + '\n')


def enterFinal(path):
    import time
    standards = inputStandards()
    testFORM = raw_input('Test ID?')
    finalFILE = open(path + 'final.csv', 'a')
    scores = ["4" for x in standards]
    while True:
	name = raw_input("Name: ")
	print "You entered", name
	if name == "xx":
	    break
        else:
	    scoreINPUT = raw_input("scores: ")
	    if scoreINPUT == "xx":
		break
	    elif scoreINPUT:
		scores = scoreINPUT.split()
            	

        if len(scores) != len(standards):
	    print "Score error with: ", name, "\n", len(scores), scores
	    print "Enter the name and scores again"
	    continue
        s = sum([int(d) for d in scores])/67.0
	print s
	finalFILE.write(testFORM + ',' + name + ',' + ','.join(scores) + '\n')



def quit(path):
    print "Thanks for playing!"
    sys.exit()

def chooseAction(path):
    ActionDict = {'H':enterHW, 'A':enterAttendance, 'I': enterIndividual, 'G': enterGroup, 'F':enterFinal, 'Q':quit}
    while True:
        action = raw_input('(H)omework, (A)ttendance, (I)ndividual Standards, (G)roup standards, (F)inal, (Q)uit')
	ActionDict[action](path)


import sys

#1. Go to the class directory, and get the list of names:
path = sys.argv[1]

# read in the names
namesF = path + "names.csv"#sys.argv[1]
namesFile = open(namesF, 'rU')
names = namesFile.readlines()
names = [n.strip() for n in names]
completer = MyCompleter(names)
readline.set_completer(completer.complete)
readline.parse_and_bind('tab: complete')
readline.parse_and_bind('set editing-mode vi')

#2. Choose mode:
chooseAction(path)

 #a. attendance
enterAttendance(path)
sys.exit()   #stop after entering attendance.  more later.

AllScoreData = {}

#decide what to do:
while True:
    action = raw_input("What do you want? ((i)ndividual, (g)roup, (q)uit)")
    if action == "i":
	AllScoreData = inputNames(AllScoreData)
        writeGradebook("data1.txt", AllScoreData)
    elif action == "g":
	standards = inputStandards(AllScoreData)
	AllScoreData = inputNames(standards, AllScoreData)
        writeGradebook("data1.txt", AllScoreData)
    elif action == "q":
	sys.exit()

