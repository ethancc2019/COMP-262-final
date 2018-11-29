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

import random
import time
import math
from multiprocessing.dummy import Pool as ThreadPool

coinChoices = ["H", "T"]
# number of flips
idealFlip = "HHTHTTHT"
counter = 0
flag = 1
probability = 0
flip = ""


# pool = ThreadPool(4)

def flip_coin(coins):
    return str(random.choice(coins))


def compute_probability():
    size = len(idealFlip)
    return math.pow(0.5, size)


# make number of threads based on the length of the ideal flip
def make_threads():
    pool = ThreadPool(len(idealFlip))


if __name__ == "__main__":

    probability = compute_probability()
    print("Initial probability of landing on the sequence: " + str(probability))
    actualProb = 0
    while flag != 0:
        # then = time.time()
        for i in range(len(idealFlip)):
            # Each iteration represents a independent flip of the coin
            flip += flip_coin(coinChoices)

        print("Actual flip = " + flip + " Ideal flip = " + idealFlip)
        if counter != 0:
            actualProb = (probability / counter)
        if flip == idealFlip:
            # now = time.time()
            flag = 0

        print("iteration number: " + str(counter) + " Probability: " + str(actualProb))

        counter += 1
        flip = ""

    # diff = now - then
    # print(str(diff % 60))
    print("FOUND ON ITERATION: " + str(counter))
