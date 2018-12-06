import random
import sys
import time
import math
import threading
# from sympy import *import numpy as np
import matplotlib.pyplot as plt

ideal = "HHTHTHHHTHTHTHHH"
numOfFlips = 1000
totalFlips = 0
arrayOfProbability = []
arrayOfSequences = [sys.maxsize]  # Let's see how this goes lol
estimatedProbability = 0.0
flp = ""
y = 0  # counter for number of matches
n = 0  # counter for number of non matches


def flip_sixteen():
    global flp
    for i in range(16):
        flp += random.choice("H" "T")


def flip_n():
    flp = ""
    for i in range(len(ideal)):
        flp += random.choice("H" "T")

    return flp


def compare_strings():
    global ideal
    global flp
    global y, n
    if ideal == flp:
        y += 1
        return
    else:
        n += 1
        return


def update_estimate():
    global arrayOfProbability, estimatedProbability, totalFlips
    theSum = 0
    for i in arrayOfProbability:
        theSum += i
    estimatedProbability = (theSum / totalFlips) * 1000


def flip_add():
    for j in range(1000):
        flip = flip_n()
        arrayOfSequences.append(flip)


if __name__ == "__main__":
    t1 = threading.Thread(target=flip_add())
    t2 = threading.Thread(target=flip_add())
    t3 = threading.Thread(target=flip_add())
    t4 = threading.Thread(target=flip_add())
    t5 = threading.Thread(target=flip_add())


    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    for j in arrayOfSequences:
        print(j)



    print(flp)
    print(y)
    print(n)
# if __name__ == "__main__":
#     t1 = threading.Thread(target=flip_sixteen())
#     t1.start()
#     for i in range(1000):
#        for j in range(numOfFlips):
#            flip_n()
#            compare_strings()
#            flp = ""
#
#        probability = (float(y) / numOfFlips) * 100
#        arrayOfProbability.append(probability)
#        totalFlips += 1000
#        update_estimate()
#        # Reset values
#        probability = 0
#        y = 0
#        n = 0
