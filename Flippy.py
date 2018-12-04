# coding=utf-8
# Math is being cited from this website:
# http://math.ucr.edu/home/baez/games/games_9.html
#
# and
# http://www.probabilityformula.org/empirical-probability-formula.html
#
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
#
# researching openmp in python
# https://software.intel.com/en-us/forums/intel-many-integrated-core/topic/413789
#
# cython for multiprocessing (openmp)
# http://technicaldiscovery.blogspot.com/2011/06/speeding-up-python-numpy-cython-and.html
#
# or openmpi ?
# https://ipython.org/ipython-doc/3/parallel/parallel_mpi.html
#

import random
import time
import math
from multiprocessing.dummy import Pool as ThreadPool

# initial sequence:
# HHTHTHHHTHHHTHTH

coinChoices = ["H", "T"]  # choices
idealFlip = "HHTHTHHH"    # string to match
flip = ""                 # resets flip

margin_error = 0.1  # accuracy
num_matches = 0.0   # matched strings
probability = 0     # calc. probability
counter = 0         # iterations
flag = 1            # exit token

# pool = ThreadPool(4)

# flips a coin
def flip_coin(coins):
    return str(random.choice(coins))


# theoretical probability
def compute_probability():
    size = len(idealFlip)
    return math.pow(0.5, size)


# actual probability
def empirical_probability(count, num_flips):
    return count / num_flips


# make number of threads based on the length of the ideal flip
def make_threads():
    pool = ThreadPool(len(idealFlip))


if __name__ == "__main__":

    probability = compute_probability()
    print("\nInitial probability of landing on the sequence: " + str(probability) + "\n")

    actualProb = 0
    empiricalProb = 0

    while flag != 0:
        # then = time.clock()
        for i in range(len(idealFlip)):
            # Each iteration represents a independent flip of the coin
            flip += flip_coin(coinChoices)

        # TESTING
        # print("Actual flip = " + flip + " Ideal flip = " + idealFlip)

        # prevent division by zero
        if counter != 0:
            # actualProb = (counter / len(idealFlip))
            empiricalProb = empirical_probability(num_matches, counter)

        # found a match
        if flip == idealFlip:
            # now = time.time()
            num_matches += 1
            print("FOUND ON ITERATION: " + str(counter))
            actualProb = 0  # reset after found

        # TESTING
        # actualProb += probability
        # print("iteration number: " + str(counter))  # + " Probability: " + str(actualProb))
        # print("calculated probability: " + str(probability))
        # print("cumulative probability: " + str(actualProb))
        print("empirical probability:  " + str(empiricalProb))

        counter += 1
        flip = ""

        # percent error used for accurate prob. estimate
        if abs(compute_probability()-empirical_probability(num_matches, counter))/compute_probability() <= margin_error:
            flag = 0
            # now = time.clock()

    # results
    print("\nDONE ON ITERATION:     " + str(counter))
    print("EMPIRICAL PROBABILITY: " + str(empirical_probability(num_matches, counter)))
    print("EXPECTED PROBABILITY:  " + str(compute_probability()))

    # diff = now - then
    # print(str(diff % 60))
    # print("FOUND ON ITERATION: " + str(counter))
