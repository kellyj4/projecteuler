#!/usr/bin/env python3
########################################################
#
# Author: James Kelly
#
# Date: 19/10/2017
#
# Project: Euler question 1
#
########################################################

numberValue = int(input("Please input in an integer between 1 and a 1000 -> "))

count = 1
arrayValue = []
totalValue = 0

while (count < numberValue):
    if count % 3 == 0 or count % 5 == 0:
        arrayValue.append(count)
        totalValue += count
    else:
        print("Current loop number is -> ", count)

    count += 1

print("This is now complete and all the values are -> ", arrayValue)
print("The sum of these values is -> ", totalValue)
