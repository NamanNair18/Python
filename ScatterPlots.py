import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

plt.scatter(x,y, color='red')
plt.title("Scatter PLot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.grid(True)
plt.show()