import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5,6,7,8,9,10]
y = [10, 20, 25, 30, 40.50,60,70,80,90,100]
plt.plot(x, y, marker='o')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot')
plt.grid(True)
plt.show()
