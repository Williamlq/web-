import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("environmental_data.csv", delimiter=',')
if data.shape[1]== 4:
    days = data[:,0]
    temps = data[:,1]

    plt.plot(days, temps, color='blue', marker='o')
    plt.title("Temperature Trend ver Days") # Chant title
    plt.xlabel("Day Number")
    plt.ylabel("Temperature (°c)")


    plt.grid(True,linestyle='--', color='gray')
    plt.show()