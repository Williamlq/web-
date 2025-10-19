import numpy as np

try:
    data = np.genfromtxt("environmental_data.csv", delimiter=',')
    if data.shape[1] == 4:
        print("数据读取成功!共",data.shape[0],"行 4列")
    else:
        print("数据格式错误!需含4列(日期、温度、湿度、PM2.5)")
except FileNotFoundError:
    print("文件读取出错:文件‘environment_data.csv'不存在")