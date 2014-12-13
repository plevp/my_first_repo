#!/usr/bin/python

import matplotlib.pyplot as plt

def main():
    x = [1,2,3,4]
    y = [20, 21, 20.5, 20.8]

    #error data
    y_error = [0.12, 0.13, 0.3, 0.1]

    #plot data
    plt.plot(x, y, linestyle="dashed", marker="o", color="green")

    #plot only errorbars
    plt.errorbar(x, y, yerr=y_error, linestyle="None", marker="None", color="green")

    #configure  X axes
    plt.xlim(0.5,4.5)
    plt.xticks([1,2,3,4])

    #configure  Y axes
    plt.ylim(19.8,21.2)
    plt.yticks([20, 21, 20.5, 20.8])

    #labels
    plt.xlabel("this is X")
    plt.ylabel("this is Y")

    #title
    plt.title("Simple plot")

    #show plot
    #plt.show()

if __name__ == "__main__":
    main()
    
