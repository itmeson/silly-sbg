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

def inputStandards():
    input = raw_input('List of standards to assess for all')
    standards = input.split(',')
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

def enterAttendance():
    #1. Get attendance book
    #2. Get desired date and column
    #3. Get student yes/no
    #4. repeat 3.
    #5. Write attendance book


import sys

# read in the names
namesF = sys.argv[1]
namesFile = open(namesF, 'rU')
names = namesFile.readlines()
names = [n.strip() for n in names]
completer = MyCompleter(names)
readline.set_completer(completer.complete)
readline.parse_and_bind('tab: complete')

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

