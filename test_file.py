import random
import math
import threading

# from sympy import *import numpy as np

ideal = "HHTHTHHHTHHHTHTH"
numOfFlips = 1000
totalFlips = 0  # keep track of the total number of flips
arrayOfProbability = []
arrayOfSequences = []  # sys.max size gives a capacity of 9223372036854775807 elements but we'll use 10,000 for testing
estimatedProbability = 0.0  # this variable will update

flp = ""
check = math.ceil(pow(2, len(ideal)) / 2)  # used for printing prob
num_matches = 0.0  # matched strings
flag = 1
y = 0
n = 0

def flip_sixteen():
    global flp
    for i in range(16):
        flp += random.choice("H" "T")


def flip_n():
    flp = ""
    for i in range(len(ideal)):
        flp += random.choice("H" "T")

    return flp


def empirical_probability(count, num_flips):
    return count / num_flips


def compute_probability():
    size = len(ideal)
    return math.pow(0.5, size)


def flip_add():
    for j in range(1000):
        flip = flip_n()
        arrayOfSequences.append(flip)

def flip():
    global flp
    for i in range(8):
        flp += random.choice("H" "T")
    #return flp


def look_and_count(start, finish):
    global ideal, flp, y, n, arrayOfSequences, numOfFlips
    counterI = 0
    for i in range(round(start), round(finish)):
        if arrayOfSequences[counterI] == ideal:
            y += 1
        else:
            n += 1

        counterI += 1


def populate():
    arrayOfSequences.clear()  # Clear the list
    t1 = threading.Thread(target=flip_add())
    t2 = threading.Thread(target=flip_add())
    t3 = threading.Thread(target=flip_add())
    t4 = threading.Thread(target=flip_add())
    t1.start()
    t1.join()
    t2.start()
    t2.join()
    t3.start()
    t3.join()
    t4.start()
    t4.join()



def thread_compare():
    t5 = threading.Thread(target=look_and_count(0, len(arrayOfSequences) / 2))
    t6 = threading.Thread(target=look_and_count(len(arrayOfSequences) / 2, len(arrayOfSequences)))
    t5.start()
    t5.join()
    t6.start()
    t6.join()


if __name__ == "__main__":


    probability = compute_probability()  # Getting initial probability of the sequence
    print("\nInitial probability of landing on the sequence: " + str(probability) + "\n")

    actualProb = 0
    empiricalProb = 0
    counter = 0
    while y == 0:
        populate()
        thread_compare()

    while flag != 0:
        populate()
        thread_compare()

        if counter != 0:
            empiricalProb = empirical_probability(y, counter)
            print("ESTIMATED PROBABILITY: " + str(empiricalProb))


        counter += 1
        # if counter % check is 0:

        flp = ""
        #print("Still running...")


