import random

def getLine(syllablesRemaining):
	s = ""
	while syllablesRemaining > 0:
		toGet = random.randint(1,syllablesRemaining)
		syllablesRemaining -= toGet
		idx = random.randint(0,len(words[toGet])-1)
		s += words[toGet][idx]
	return s

fIn = open('HaikuSource.txt','r')
lineNum = 187175
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

#first line
print(getLine(5))
print(getLine(7))
print(getLine(5))
