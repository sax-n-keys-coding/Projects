# Print the least positive integer that is 1) not present in the list 
#2) cannot be represented by summing up any elements in the list
#inputLst is not sorted

import time
import math
#Definitions:
#===========
#Progress icon
progressCharLst = ["\\","|", "/", "—"]
progressCharLstLen = len(progressCharLst)
#Efficiency: convert inputlst and list of all partial sums into two sets: inputSet and subSumsSet
print("Welcome!")
print("===")
print("Determine the integer that is ")
print("1) not present in the list!")
print("2) cannot be represented by summing up any elements in the list")
print("===")

#User Input
unParsedInput = input("Enter your list of integers, seperated by commas: ")
	
#String to list
filteredInput = unParsedInput.replace(" ", "").split(",")
inputLst = [int(x) for x in filteredInput]

lstToStr = ''.join(filteredInput)
print("Entered list, saved: " + str(filteredInput))
print()

#Sets:
inputSet = set()
for i in range(0, len(inputLst)):
	inputSet.add(inputLst[i])

subSumsSet = set()

#For speeding up loading animations 
permutationCoefficient = math.factorial(len(inputLst))


#Progress icon
globalProgressI = 0
def runProgressIcon(currentProgressI):
	if (currentProgressI < progressCharLstLen):
		print("Calculating" + "." * globalProgressI +  "  " + (" " * (4 - globalProgressI))
		 + progressCharLst[currentProgressI], end="\r")	
		currentProgressI += 1
		time.sleep(0.1 / permutationCoefficient)
	else:
		currentProgressI = 0
		print("Calculating" + "." * globalProgressI + "  " + (" " * (4 - globalProgressI))
		 + progressCharLst[currentProgressI], end="\r")	
		time.sleep(0.1 / permutationCoefficient)
	return currentProgressI



#Use/Not Use tree recursive idea (for permutations)
sum = 0
#recursive funct returns a number (sum of a permutation)
def findAllSubSums(lst, sum):
	if len(lst) == 0:
		subSumsSet.add(sum)
	else:
		global globalProgressI
		globalProgressI = runProgressIcon(globalProgressI)
		findAllSubSums(lst[1:], sum + lst[0]) 
		findAllSubSums(lst[1:], sum)


#Driver Code for SubSum tree
findAllSubSums(inputLst, 0)



leastPositiveInteger = 0
#finding least positive integer not in list and not in sub sums list
for i in range(0, 100000):
	globalProgressI = runProgressIcon(globalProgressI)
	if ((not (i in inputSet)) and (not (i in subSumsSet))):
		leastPositiveInteger = i
		break

print("                  ", end="\r")
print("Done!")
print("The least positive integer is: " + str(leastPositiveInteger))
