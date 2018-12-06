import random
import sys
import time
import math
import threading
# from sympy import *import numpy as np
import matplotlib.pyplot as plt

ideal = "HHTHT"
numOfFlips = 1000
totalFlips = 0
arrayOfProbability = []
arrayOfSequences = [
    10000]  # sys.max size gives a capacity of 9223372036854775807 elements but we'll use 10,000 for testing
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


def look_and_count(start, finish):
    global ideal, flp, y, n, arrayOfSequences
    for i in range(start, round(finish)):
        if arrayOfSequences[i] == ideal:
            y += 1
        else:
            n += 1


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

    # look_and_count(1, len(arrayOfSequences)/2)
    #TODO: here
    t6 = threading.Thread(target=look_and_count, args=(1, len(arrayOfSequences) - 1))
    print("Sorting through the first half of the array")
    t6.start()
    t6.join(10)
    pos = len(arrayOfSequences) / 2
    t7 = threading.Thread(target=look_and_count, args=(pos + 1, len(arrayOfSequences) - 1))
    print("Sorting through the second half of the array")
    t7.start()
    t7.join()

    # t6.join()
    # print(flp)
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
