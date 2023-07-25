# plot_trajectory.py

import csv
import numpy as np
import matplotlib.pyplot as plt


def main():
    ns = []
    cm = []
    # Create a Python dictionary from the JSON file
    with open("Session 16 - Scientific Computing/ray.csv", newline="") as file:
        reader = list(csv.reader(file))

        for row in reader[1:]:
            ns.append(float(row[0]))
            cm.append(float(row[1]))

    plt.scatter(ns, cm)

    a, b = np.polyfit(ns, cm, 1)

    print("the velocity is: " + str(a) + " cm/ns")

    # using the slope formula:
    # a = rise / run = (x - cm[-1]) / (0 - 174300)
    x = (-174300 * a + cm[-1]) / 100000
    print("the original height in the stratosphere is: " + str(x) + " km")

    plt.plot(ns, [(a * i + b) for i in ns], "r",label = "line of best fit")

    plt.legend(loc="upper right")

    plt.title("trajectory of secondary particle")
    plt.xlabel("time (in ns)")
    plt.ylabel("distance (in cm)")

    plt.show()

if __name__ == "__main__":
    main()