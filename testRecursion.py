import random, timeit, sys

def getLine(syllablesRemaining, s):
	while syllablesRemaining > 0:
		toGet = random.randint(1,syllablesRemaining)
		syllablesRemaining -= toGet
		idx = random.randint(0,len(words[toGet])-1)
		s += words[toGet][idx]
	return s

def getLineRecursive(syllablesRemaining, s):
	#base case
	if syllablesRemaining == 0:
		return
	else:
		toGet = random.randint(1,syllablesRemaining)
		idx = random.randint(0,len(words[toGet])-1)
		s += words[toGet][idx]
		return getLineRecursive(syllablesRemaining - toGet, s)

fIn = open('HaikuSource.txt','r')
lineNum = 186524
words = [[],[],[],[],[],[],[]]
#Initalize arrays
while lineNum > 0:
	lineNum -= 1
	s = fIn.readline()
	s = s.replace('\n','')
	syllables = int(s[-1])
	s = s[:-1] #keep the space at the end
	if syllables < 8:
		words[syllables-1].append(s)

#Timer for iterative solution
iterative = timeit.Timer('getLine(syllables, s)', setup='syllables = 5; s = ""; from __main__ import getLine')#Yikes, semicolons!
#Timer for recursive solution
recursive = timeit.Timer('getLineRecursive(syllables, s)', setup='syllables = 5; s = ""; from __main__ import getLineRecursive')

#Default times to run is one million, that should suffice.
sys.stdout.write("Iterative: ")
print(iterative.timeit())
sys.stdout.write("Recursive: ")
print(recursive.timeit())
