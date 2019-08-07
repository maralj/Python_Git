myList = [7, 1, 2, 3]	

def stackAdd(myList, add):

	newList = []
	n = 1
	for i in myList:
	 	newList.append(myList[-n])
	 	n = n + 1
	newList.append(add)
	print(newList)
	return newList


stackAdd(myList, 5)

newList = stackAdd(myList, 5)


def stackPop(newList):
	for i in newList:
		newList = newList[:-1]
		print(newList)
	return 


stackPop(newList)