import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("environmental_data.csv", delimiter=',')
if data.shape[1]== 4:
    days = data[:,0]
    pm25 = data[:,3]
    for numd in days:
        for pm25_val in pm25:
            num = float(pm25_val)
            if 0<=num<=50:
                lebel = "良好"
                plt.plot(numd, num, color='green', marker='o')
            elif 50<num<=100:
                lebel = "中等"
                plt.plot(numd, num, color='orange', marker='o')
            elif num>100:
                lebel = "不佳"
                plt.plot(numd, num, color='red', marker='o')


plt.xlabel("Day Number")
plt.ylabel("pm2.5 (μg/m³)")
plt.grid(True,linestyle='--', color='gray')
plt.show()
