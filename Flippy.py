# Ethan Collins
# Tai Alvitre
# 12/3/18
#
# Finish implementing multiprocessing in python.  Optimize code.
#

# References / Resources
#
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
# Nice references for Pool and Process
# http://cslocumwx.github.io/blog/2015/02/23/python-multiprocessing/
# docs.python.org/dev/library/multiprocessing.html
# https://www.ellicium.com/python-multiprocessing-pool-process/
#

import random
import time
import math
import multiprocessing as mp  # alias

# from multiprocessing.dummy import Pool as ThreadPool

# initial sequence:
# HHTHTHHHTHHHTHTH

coinChoices = ["H", "T"]  # choices
idealFlip = "HHT"    # string to match
flip = ""                 # resets flip

margin_error = 0.1  # accuracy
num_matches = 0.0   # matched strings
probability = 0     # calc. probability
counter = 0         # iterations
flag = 1            # exit token

check = math.ceil(pow(2, len(idealFlip))/2)  # used for printing prob

# pool = ThreadPool(4)


# flips a coin  *NOT USED*
def flip_coin(coins):
    return str(random.choice(coins))


# requests (num) tasks to be completed
def flip_coin_num(num):
    return str(random.choice(coinChoices))


# theoretical probability
def compute_probability():
    size = len(idealFlip)
    return math.pow(0.5, size)


# actual probability
def empirical_probability(count, num_flips):
    return count / num_flips


# TODO: implement multiprocessing
if __name__ == "__main__":
    # print("# cores: %d" % mp.cpu_count())

    probability = compute_probability()
    print("\nInitial probability of landing on the sequence: " + str(probability) + "\n")

    actualProb = 0
    empiricalProb = 0

    tasks = range(len(idealFlip))

    while flag != 0:
        with mp.Pool(processes=4) as pool:
            temp = pool.map(flip_coin_num, tasks)
            # add other processes?
        # handles close / join

        flip = "".join(temp)
        # print(temp)
        # print(flip)

        if counter != 0:
            empiricalProb = empirical_probability(num_matches, counter)
        if flip == idealFlip:
            num_matches += 1

        counter += 1
        flip = ""

        if counter % check is 0:
            print("PROBABILITY: " + str(empiricalProb))
