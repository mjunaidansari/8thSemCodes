#The annual number of industrial accidents occurring in a particular manufacturing plant is known to
# follow Poisson distribution with mean 12.
#a)What is the probability of observing exactly 5 accidents at this plant during the coming year?
#b)What is the probability of observing not more than 12 accidents at this plant the coming year?
#c)What is the probability of observing at least 15 accidents at this plant during the coming year?
#d)What is the probability of observing between 10 and 15 accidents (inclusive) at this plant during the coming year?

from scipy.stats import poisson
import matplotlib.pyplot as plt
import numpy as np
mean = 12
x = np.arange(0, 30)
poisson_dist = poisson.pmf(x, mean)
plt.figure(figsize=(12, 6))
plt.bar(x, poisson_dist, label='Poisson Distribution (Mean=12)', alpha=0.5)
plt.fill_between(x, 0, poisson_dist, where=(x == 5), color='red', alpha=0.5, label='Exactly 5 accidents')
plt.fill_between(x, 0, poisson_dist, where=(x <= 12), color='green', alpha=0.5, label='Not more than 12 accidents')
plt.fill_between(x, 0, poisson_dist, where=(x >= 15), color='blue', alpha=0.5, label='At least 15 accidents')
plt.fill_between(x, 0, poisson_dist, where=((x >= 10) & (x <= 15)), color='orange', alpha=0.5, label='Between 10 and 15 accidents')
plt.xlabel('Number of Accidents')
plt.ylabel('Probability')
plt.title('Poisson Distribution of Accidents in a Manufacturing Plant')
plt.legend()
plt.grid(True)
plt.show()
prob_5_accidents = poisson.pmf(5, mean)
print(f"Probability of observing exactly 5 accidents: {prob_5_accidents}")
prob_not_more_than_12 = poisson.cdf(12, mean)
print(f"Probability of observing not more than 12 accidents: {prob_not_more_than_12}")
prob_at_least_15 = 1 - poisson.cdf(14, mean)
print(f"Probability of observing at least 15 accidents: {prob_at_least_15}")
prob_between_10_and_15 = poisson.cdf(15, mean) - poisson.cdf(9, mean)
print(f"Probability of observing between 10 and 15 accidents: {prob_between_10_and_15}")
