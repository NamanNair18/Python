import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({'A': [1, 2, 3], 'B' : [4,5, 6] })
print (df)
df.plot(x='A', y='B', kind='line', marker= 'o', title='Basic Line Chart')
plt.xlabel('value of A')
plt.ylabel('value of B')
plt.show()
