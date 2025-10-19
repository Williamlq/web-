import numpy as np

data = np.genfromtxt("environmental_data.csv",delimiter = ',')

if data.shape[1] == 4:
    temp_avg = round(np.mean(data[:,1]),2)
    humi_avg = round(np.mean(data[:, 2]), 2)
    pm25_avg = round(np.mean(data[:, 3]), 2)

    print(f"温度(°C) 平均值:{temp_avg}")
    print(f"湿度(%) 平均值:{humi_avg}")
    print(f"pm2.5浓度(μg/m²) 平均值:{pm25_avg}")
