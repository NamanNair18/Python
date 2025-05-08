import numpy as np
import matplotlib.pyplot as plt

data= np.random.normal(loc=50, scale=10, size=1000)
plt.hist(data, bins=30, density=True, alpha=0.6, color='skyblue')
plt.title("Histogram")
plt.xlabel("value")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()