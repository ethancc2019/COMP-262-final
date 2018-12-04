# coding=utf-8
# Math is being cited from this website:
# http://math.ucr.edu/home/baez/games/games_9.html

# and
# http://www.probabilityformula.org/empirical-probability-formula.html

# Could check out this also
# 3. If you repeat the experiment of flipping a coin ten times 10,000 times, (so 100,000 flips
# in all), about how many times do you expect to get the sequence HTHHTTHHHT?
# Answer: Since probability represents “long-range frequency”, we expect this particular
# sequence to occur about once for every 1000 repeats of the experiment of flipping a
# coin 10 times. So if we repeat the experiment 10,000 times, then we expect to get this
# particular sequence about 10 times.
#
# intuition behind coin flipping
# https://math.stackexchange.com/questions/151262/looking-for-intuition-behind-coin-flipping-pattern-expectation


# https://en.wikipedia.org/wiki/Binomial_distribution OMG WE NEED TO USE PROBABILITY MASS FUNCTION WHATTTT
# Probability mass function --> https://en.wikipedia.org/wiki/Binomial_distribution
# The probability of getting exactly k successes(in our case just one) in n trials is given by the probability mass function:

import random
import time
import math
import threading
from scipy.stats import poisson
import numpy as np
import matplotlib.pyplot as plt

# ***Global Variables***
coinChoices = ["H", "T"]
idealFlip = "HHTHTHHHTHHHTHTH"
numOfFlips = 20  # We can change this easily depending on how many flips our experiment needs
flip = ""

counter = 0  # keep track of the iterations to divide by
flag = 1  # flag to break the while loop
probability = 0

numOfHeads = 0
numOfTails = 0


# pool = ThreadPool(4)

def flip_coin(coins):
    return str(random.choice(coins))


def compute_probability():  # This function assumes that the probability of H or T is 1/2
    global idealFlip
    size = len(idealFlip)
    return math.pow(0.5, size)


def count_occurrence():  # Counts the number of H and T in the sequence
    global numOfHeads
    global numOfTails
    for i in idealFlip:
        if i == "H":
            numOfHeads += 1
        else:
            numOfTails += 1

def binomial_dist():
    global numOfFlips
    p = 0.5

    s = np.random.binomial(numOfFlips,0.166)
    print s


# make number of threads based on the length of the ideal flip


if __name__ == "__main__":
    binomial_dist()

    print("Initial probability of landing on the sequence: " + str(probability))
    actualProb = 0
    probability = compute_probability()
    while flag != 0:
        for i in range(len(idealFlip)):
            # Each iteration represents a independent flip of the coin
            flip += flip_coin(coinChoices)

        print("Actual flip = " + flip + " Ideal flip = " + idealFlip)
        if counter != 0:
            actualProb = (probability / numOfFlips - 1)
        if flip == idealFlip:
            flag = 0

        print("Iteration number: " + str(counter) + " Probability on this iteration: " + str(actualProb))

        counter += 1
        # reset this string
        flip = ""

    # diff = now - then
    # print(str(diff % 60))
    print("FOUND ON ITERATION: " + str(counter))
