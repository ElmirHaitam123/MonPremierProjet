import math
import sys 

nbs1_1000 = []


def summ(number):
        for multiple in range(number):
            if (multiple % 3 == 0 or multiple % 5 == 0) :
                    nbs1_1000.append(multiple)
        return sum(nbs1_1000)
print(summ(1000))


