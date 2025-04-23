# Question: A soft drink company claims that the mean sugar content in its soda bottles is 40 grams. 
# To test this claim, a random sample of 25 bottles is selected, and the sugar content is measured.
# The sample mean is found to be 38 grams with a standard deviation of 4 grams. 
# Conduct a Z-test at a significance level of 0.05 to determine if there is enough evidence to reject the company's claim.

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
sample_mean = 38
pop_mean = 40
sample_std = 4
sample_size = 25
alpha = 0.05
z_statistic = (sample_mean - pop_mean) / (sample_std / np.sqrt(sample_size))
p_value = 2 * (1 - stats.norm.cdf(np.abs(z_statistic)))
x = np.linspace(-4, 4, 1000)
y = stats.norm.pdf(x, 0, 1)
plt.plot(x, y, 'b-', linewidth=2)
shade = np.linspace(abs(z_statistic), 4, 300)
plt.fill_between(shade, stats.norm.pdf(shade, 0, 1), color='red', alpha=0.5)
plt.title('Z-test for Mean Sugar Content')
plt.xlabel('Z')
plt.ylabel('Density')
plt.annotate('Critical Region\n(p < {:.3f})'.format(alpha), xy=(2, 0.1), xytext=(2.5, 0.2),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.axvline(x=abs(z_statistic), color='black', linestyle='--', label='Z statistic')
plt.legend()
plt.show()
if p_value < alpha:
    print("Reject the null hypothesis: There is enough evidence to conclude that the mean sugar content is not 40 grams.")
else:
    print("Fail to reject the null hypothesis: There is not enough evidence to conclude that the mean sugar content is not 40 grams.")
