from scipy.stats import poisson
import numpy as np
import matplotlib.pyplot as plt
n = 1000
prob = 0.3
x = np.arange(0, n, 0.5)
plt.plot(x, poisson.pmf(x, 600))

plt.show()
# Probability mass function --> https://en.wikipedia.org/wiki/Binomial_distribution The probability of getting
# exactly k successes(in our case just one) in n trials is given by the probability mass function:
