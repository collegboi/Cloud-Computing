#!/usr/bin/python

value1 = 3
value2 = 5
counter = 0
allValues = []
newValue = 0

while newValue < 1000:
	counter = counter + 1
	newValue = value1 * counter
	allValues.append(newValue)
	if counter / 3 == 0:
		newValue = value2 * counter
		allValues.append(newValue)

print (allValues)
print ("Sum of all Values is:", newValue)


