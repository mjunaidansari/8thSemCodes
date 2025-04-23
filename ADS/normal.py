#The weights of apples in a certain orchard follow a normal distribution with a mean of 150 grams and a standard deviation of 20 grams.
#a) What is the probability that a randomly selected apple weighs between 140 and 160 grams?
#b) What is the probability that a randomly selected apple weighs more than 170 grams?
#c) What is the probability that a randomly selected apple weighs less than 120 grams?

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
mean = 150
std_dev = 20
x = np.linspace(50, 250, 500)
y = norm.pdf(x, mean, std_dev)
plt.figure(figsize=(12, 6))
plt.plot(x, y, label='Normal Distribution (Mean=150, SD=20)')
plt.fill_between(x, 0, y, where=((x >= 140) & (x <= 160)), color='orange', alpha=0.5, label='Between 140 and 160 grams')
plt.fill_between(x, 0, y, where=(x > 160), color='green', alpha=0.5, label='More than 160 grams')
plt.fill_between(x, 0, y, where=(x < 120), color='red', alpha=0.5, label='Less than 120 grams')
plt.xlabel('Weight (grams)')
plt.ylabel('Probability Density')
plt.title('Normal Distribution of Apple Weights')
plt.legend()
plt.grid(True)
plt.show()
prob_between_140_160 = norm.cdf(160, mean, std_dev) - norm.cdf(140, mean, std_dev)
prob_more_than_170 = 1 - norm.cdf(170, mean, std_dev)
prob_less_than_120 = norm.cdf(120, mean, std_dev)
print(f"Probability of a randomly selected apple weighing between 140 and 160 grams: {prob_between_140_160:.4f}")
print(f"Probability of a randomly selected apple weighing more than 170 grams: {prob_more_than_170:.4f}")
print(f"Probability of a randomly selected apple weighing less than 120 grams: {prob_less_than_120:.4f}")
