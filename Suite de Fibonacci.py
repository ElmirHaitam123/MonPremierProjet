import math
import sys

def calculSuiteFibo(max):

    F1, F2 = 1, 2
    suite_fib = 0
    while F2 <= max:
        if F2 % 2 == 0:
            suite_fib += F2
        
        F1, F2 = F2, F1 + F2
    return suite_fib
print(calculSuiteFibo(35))