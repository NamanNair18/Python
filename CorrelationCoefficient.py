import numpy as np

x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]
correlation_matrix = np.corrcoef(x, y)
correlation = correlation_matrix[0, 1]
print("Correlation Coefficient:- ", correlation)