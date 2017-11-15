#!/usr/bin/env python3
########################################################
#
# Date: 19/10/2017
#
# Project: Euler question 2
#
########################################################

fibArray = []

def fibonnaci_below_4Mill():
    fibArraySum = 0
    fibArray.append(0)
    fibArray.append(1)

    while(int(fibArray[-2]) + int(fibArray[-1]) < 4000000):
        fibArray.append((fibArray[-2]+fibArray[-1]))

        if (fibArray[-1]) % 2 == 0 and int(fibArray[-1]) < 4000000:
            fibArraySum += int(fibArray[-1])
 
    print("Total sum of even fibonacci number below 4 Million is -> ", fibArraySum)

fibonnaci_below_4Mill()
