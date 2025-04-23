import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis
tips = sns.load_dataset('tips')
data = tips['total_bill']
skewness = skew(data)
kurt = kurtosis(data)
plt.hist(data, bins=30, alpha=0.5, color='b', edgecolor='black')
plt.xlabel('Total Bill')
plt.ylabel('Frequency')
plt.title('Histogram of Total Bill')
plt.annotate(f'Skewness: {skewness:.2f}', xy=(0.05, 0.9), xycoords='axes fraction', fontsize=12)
plt.annotate(f'Kurtosis: {kurt:.2f}', xy=(0.05, 0.85), xycoords='axes fraction', fontsize=12)
plt.show()
print(f"Skewness: {skewness}")
print(f"Kurtosis: {kurt}")
