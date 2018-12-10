"""
# References / Resources

# Math is being cited from this website:
# http://math.ucr.edu/home/baez/games/games_9.html
# http://www.probabilityformula.org/empirical-probability-formula.html

# Intuition behind coin flipping
# https://math.stackexchange.com/questions/151262/looking-for-intuition-behind-coin-flipping-pattern-expectation
#
# Nice references for Pool and Process
# http://cslocumwx.github.io/blog/2015/02/23/python-multiprocessing/
# docs.python.org/dev/library/multiprocessing.html
# https://www.ellicium.com/python-multiprocessing-pool-process/
#
# Optimization
# https://stackoverflow.com/questions/5549190/is-shared-readonly-data-copied-to-different-processes-for-multiprocessing/5550156#5550156
# https://stackoverflow.com/questions/20914828/python-multiprocessing-pool-join-not-waiting-to-go-on
# https://stackoverflow.com/questions/13672429/python-multiprocessing-for-expensive-operation-with-2d-array
#
"""
"""
Name: Tai Alvitre, Ethan Collins
Class: COMP 262
Project: Final Project
"""

import random
import math
import multiprocessing as mp  # alias
import time

"""
 Our starting sequence to match:
 HHTHTHHHTHHHTHTH = 11 Heads, 5 Tails
"""
coinChoices = ("H", "T")  # choices
idealFlip = "HHTHTHHHTHHHTHTH"
flip = ""  # resets flip

data = []  # stores flips

quiT = 0  # testing
c_found = 0  # match finder oooooohhhh ;)
is_match = 0  # testing

num_matches = 0.0  # matched strings
probability = 0  # calc. probability
counter = 0  # global iterations
d_count = 1  # iterates coin flips
true_d_cnt = 0  # fixes count issue
flag = 1  # exit token

"""
# TESTING
def fill_er_up(get_in_there):
    get_in_there.append(["A"])
    get_in_there.append(["B"])
    get_in_there.append(random.choice(coinChoices))
"""

"""
 Flip coins initially
 2D array; (however many) X (16) flips
"""
def sys_coin_flip():
    global data, d_count, true_d_cnt
    chunk_c = 1
    del data[:]  # Clears our array holding our sequences

    # 0 mod (anything) = 0; +1 to d_count and chunk_c

    while d_count % 100001 != 0:  # number of iterations
        chunk = []
        while chunk_c % 17 != 0:  # number of coins
            chunk.append(random.choice(coinChoices))
            chunk_c += 1
        data.append(chunk)  # Adds our random coin flips to our data list

        d_count += 1
        chunk_c = 1

    true_d_cnt += 100000
    d_count += 1  # continue flipping in next iter

    # ex. [[HHTHTHHHTHHHTHTH], [THHHTHTHHHTHTHHH], [THTHHTHHTHHHHTHH], ...]


"""
    Multiple cores handle  or 2-D array data[[]];
    break into strings to compare
"""
def handler(a):
    global flip, counter, is_match

    """
    Append the 16 flips from our data and then compare them 
        
    """
    flip += (a[0] + a[1] + a[2] + a[3] + a[4] + a[5] + a[6] + a[7] +
             a[8] + a[9] + a[10] + a[11] + a[12] + a[13] + a[14] + a[15])

    counter += 1

    if flip == idealFlip:
        flip = ""
        return 1
    flip = ""  # Didn't find a match, rest the string


"""
Computing our initial probability of the sequence 
Probability of heads or tails on a fair coin is 1/2 

probability = (1/2)^lengthOfSequence
"""
def compute_probability():
    size = len(idealFlip)
    return math.pow(0.5, size)


"""
This function is called after we have gotten the number of matches after 1 iteration to show our updated probability 
after every iteration

empiricalProb = number of matches / number of flips
"""
def empirical_probability(count, num_flips):
    return count / num_flips


"""
    Main Driver
"""
if __name__ == "__main__":
    # print("# cores: %d" % mp.cpu_count())

    probability = compute_probability()
    print("\nInitial probability of landing on the sequence: " + str(probability) + "%\n")

    actualProb = 0
    empiricalProb = 0

    sys_coin_flip()  # Initial fill of our 2-D array of sequences

    while flag != 0:  # Every time we execute this while loop is a single iteration of 1.6 Million flips
        now = time.time()
        pool = mp.Pool(mp.cpu_count())

        """
        The data parameter is our 2-D array of sequences
        Result gets iterable list from handler that is a collection of 1s or 0s, depending if there was a match 
        If there was a match a 1 is returned, else a 0 is returned 
        """
        results = pool.map(handler, data)

        pool.close()  # Close the thread pool
        pool.join()  # This makes sure that every thread finishes it job before returning

        counter += true_d_cnt * 16  # 16 coins in sequence

        """
        After we have our collection of 1s and 0s all we really want is the number of matches(number of 1s in result)
        Filter basically strips any unwanted data from the list and here we are stripping all of the 0s
        """
        results = filter(lambda x: x == 1, results)

        for i in results:
            c_found += i

        num_matches += c_found

        print("MATCHES FOUND: " + str(c_found))
        print("TOTAL MATCHES FOUND: " + str(num_matches))
        print("ESTIMATED PROB: " + str(empirical_probability(num_matches, counter)) + "%")

        then = time.time()
        print("Time to compare 1.6M number of flips: " + str(then - now))
        print("TOTAL NUMBER OF FLIPS: " + str(counter) + "\n")

        c_found = 0  # Reset our counter for number of comparisons

        sys_coin_flip()  # At the end of this while loop we jump back into this function to flip another 1.6M coins and 100,000 comparisons.

# End of File
