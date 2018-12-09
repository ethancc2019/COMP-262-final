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
import numpy as np

# import Cython as Cy

# from multiprocessing.dummy import Pool as ThreadPool

# initial sequence:
# HHTHTHHHTHHHTHTH

coinChoices = ("H", "T")        # choices
idealFlip = "HHTHTHHHTHHHTHTH"    # string to match
flip = ""                         # resets flip

# data = np.empty((10000, 16), dtype=object)      # empty numpy array
data = []
# chunk = []

"""
# TESTING
work1 = ([0], [1], [2])
work2 = (["A"], ["B"], ["C"], ["B"], ["C"], ["B"], ["C"], ["B"], ["C"], ["B"], ["C"])
work3 = []
work4 = (["A", 0], ["B", 1], ["C", 2])
"""

# margin_error = 0.1  # accuracy *NOT USED*
num_matches = 0.0   # matched strings
probability = 0     # calc. probability
counter = 0         # global iterations
d_count = 1         # iterates coin flips
# h_count = 0         # used in handler()
flag = 1            # exit token

# check = math.ceil(pow(2, len(idealFlip))/2)  # used for printing prob *NOT USED*
check = 10

# pool = ThreadPool(4)


"""
# TESTING
def fill_er_up(get_in_there):
    get_in_there.append(["A"])
    get_in_there.append(["B"])
    get_in_there.append(random.choice(coinChoices))
"""

"""
# flips a coin  *NOT USED*
def flip_coin(coins):
    return str(random.choice(coins))


# for use w/ below
def helper_func(p):
    return lambda args: p(*args)


# requests (num) tasks to be completed *NOT USED*
def flip_coin_num(processes=helper_func(lambda p1,p2,p3,p4:(p1,p2,p3,p4))):
    return str(random.choice(coinChoices))
"""


# Flip coins initially
# 2D array; (however many) X (16) flips
def sys_coin_flip():
    global data, d_count
    chunk_c = 1

    while d_count % 100001 != 0:
        chunk = []
        while chunk_c % 17 != 0:
            chunk.append(random.choice(coinChoices))
            chunk_c += 1
            # print("C_c: " + str(chunk_c))
        data.append(chunk)
        # data.append(random.choice(coinChoices))
        # del chunk[:]
        d_count += 1
        chunk_c = 1
    # print("DONE FLIPPING")


"""
# 1Dim. list
def sys_coin_flip():
    global data, d_count

    while d_count % 100 != 0:
        data.append(random.choice(coinChoices))
        d_count += 1

    print(*data, sep=" ")

# def data_wrapper(args):
#    handler(*args)
"""


def handler(a):
    global flip, num_matches, counter

    # cell = args[h_count]
    # cell.append(args[h_count])

    # for i in cell:
    #    flip += cell[i]
    # flip += "".join(cell)

    # print("%s%s" % (a[0], a[1]))

    counter += 1

    flip += (a[0] + a[1] + a[2] + a[3] + a[4] + a[5] + a[6] + a[7] +
             a[8] + a[9] + a[10] + a[11] + a[12] + a[13] + a[14] + a[15])

    # print(flip)

    if flip == idealFlip:
        num_matches += 1

    print("COUNTER: " + str(counter) + "  NUM MATCHES: " + str(num_matches))

    # print("%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s" % (a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9], a[10], a[11], a[12], a[13], a[14], a[15]))
    # print("%s %s %s %s" % (args[4], args[5], args[6], args[7]))

    # h_count += 1
    # print(flip + "\n")
    flip = ""


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
    # tasks = range(len(idealFlip))
    # print(*data, sep=" ")

    sys_coin_flip()

    # print(*data, sep=" ")

    # fill_er_up(work3)

    while flag != 0:
        # with mp.Pool(processes=4) as pool:
        #    temp = pool.map(flip_coin_num, tasks)
        #    add other processes?
        # handles close / join itself

        pool = mp.Pool(1)  # mp.cpu_count()
        temp = pool.map(handler, data)

        pool.close()
        pool.join()

        # flip += "".join(temp)
        # print(temp)
        # print(flip)

        if counter != 0:
            empiricalProb = empirical_probability(num_matches, counter)
        # if flip == idealFlip:
        #    num_matches += 1

        # counter += 1
        # flip = ""

        # if counter % check is 0:
        print("PROBABILITY: " + str(empiricalProb))
        break
        sys_coin_flip()
