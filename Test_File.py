import random
import time
import math
import threading
#from sympy import *import numpy as np
import matplotlib.pyplot as plt



ideal = "HHTHTHHH"
numOfFlips = 1000
totalFlips = 0
arrayOfProbability = []
estimatedProbability = 0.0
flp = ""
y = 0
n = 0


def flip_sixteen():
   global flp
   for i in range(16):
       flp += random.choice("H" "T")

def flip_n():
    global flp
    for i in range(len(ideal)):
        flp += random.choice("H" "T")

def compare_strings():
   global ideal
   global flp
   global y,n
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
   print ("Estimated probability = " + str(estimatedProbability * 100))

if __name__ == "__main__":

   for i in range(1000):
       for j in range(numOfFlips):
           flip_n()
           compare_strings()
           flp = ""

       probability = (float(y) / numOfFlips) * 100
       arrayOfProbability.append(probability)
       totalFlips += 1000
       update_estimate()
       # Reset values
       probability = 0
       y = 0
       n = 0




