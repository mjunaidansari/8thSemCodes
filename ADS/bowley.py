import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
tips = sns.load_dataset('tips')
data = tips['total_bill']
Q1 = np.percentile(data, 25)
Q2 = np.percentile(data, 50)
Q3 = np.percentile(data, 75)
print(f"Q1: {Q1}, Q2: {Q2}, Q3: {Q3}")
B = (Q1 + Q3 - 2*Q2) / (Q3 - Q1)
sns.boxplot(x=data)
plt.annotate(f'Bowley Skewness: {B:.2f}', xy=(0.05, 0.9), xycoords='axes fraction', fontsize=12)
plt.show()
