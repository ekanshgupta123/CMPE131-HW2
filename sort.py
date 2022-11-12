def sort_dictionary(input): 
	returnList = []
	keyList = list(input.keys())
	valList = list(input.values())
	inputValues = list(input.values())
	for i in range (0, len(inputValues)):
		for j in range(0, len(inputValues)-i-1):
			if (inputValues[j][-1] > inputValues[j+1][-1]):
				temp = inputValues[j]
				inputValues[j] = inputValues[j+1]
				inputValues[j+1] = temp
	for i in inputValues:
		returnList.append(tuple([keyList[valList.index(i)], i[0]]))
	return returnList
