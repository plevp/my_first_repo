import matplotlib.pyplot as plt


#define some data
x = [1,2,3,4]
y = [20, 21, 20.5, 20.8]

#plot data
# plt.plot(x, y)
plt.plot(x, y, linestyle="dashed", marker="*", color="green")

plt.xlim(0.5, 4.5)
plt.xticks([1,2,3,4])

plt.ylim(19.9, 21.2)
plt.yticks([20,21,20.5,20.8])
plt.xlabel("This is X")
plt.ylabel("This is Y")

plt.title("Simple plot")


#show plot
plt.show()

