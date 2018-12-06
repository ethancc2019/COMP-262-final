import random
import sys
import time
import math
import threading
# from sympy import *import numpy as np

ideal = "HHTHTHHHTHHHTHTH"
numOfFlips = 1000
totalFlips = 0 #keep track of the total number of flips
arrayOfProbability = []
arrayOfSequences = []  # sys.max size gives a capacity of 9223372036854775807 elements but we'll use 10,000 for testing
estimatedProbability = 0.0 # this variable will update
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
    for j in range(100000):
        flip = flip_n()
        arrayOfSequences.append(flip)


def look_and_count(start, finish):
    global ideal, flp, y, n, arrayOfSequences, numOfFlips
    counter = 0
    for i in range(start, finish):
        if arrayOfSequences[counter] == ideal:
            y += 1
        else:
            n += 1
        if i != 0 and i % numOfFlips == 0:
            probability = (float(y) / i)
            arrayOfProbability.append(probability)

        counter += 1




if __name__ == "__main__":
    now = time.time()
    lock = threading.Lock()
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

    #look_and_count(0, len(arrayOfSequences))
    t6 = threading.Thread(target=look_and_count, args=(0, len(arrayOfSequences))) # This thread sorts through the first half of our array
    print("Sorting through the array")
    t6.start()
    t6.join()




    then = time.time()

    print("Number of matches: " + str(y))
    print ("Number of non-matches: " + str(n))
    print ("Completed in: " + str(then - now))


