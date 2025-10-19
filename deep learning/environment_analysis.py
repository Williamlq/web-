import numpy as np
import matplotlib.pyplot as plt

# 数据读取与格式校验
try:
    # 使用NumPy读取CSV文件
    data = np.genfromtxt('environmental_data.csv', delimiter=',', skip_header=1)

    # 检查数据格式是否正确（4列数据）
    if data.ndim != 2 or data.shape[1] != 4:
        print("数据格式错误！需包含4列数据")
    else:
        # 提取各列数据
        date_indices = data[:, 0]  # 日期编号
        temperatures = data[:, 1]  # 温度 (℃)
        humidity = data[:, 2]  # 湿度 (%)
        pm25 = data[:, 3]  # PM2.5 浓度 (μg/m³)

        # 基础统计计算
        temp_mean = np.mean(temperatures)
        humidity_mean = np.mean(humidity)
        pm25_mean = np.mean(pm25)

        print(f"平均温度 (℃): {temp_mean:.2f}")
        print(f"平均湿度 (%): {humidity_mean:.2f}")
        print(f"平均PM2.5浓度 (μg/m³): {pm25_mean:.2f}")

        # 温度可视化
        plt.figure(figsize=(10, 6))
        plt.plot(date_indices, temperatures, color='blue', marker='o', label='Temperature')
        plt.title('Temperature Trend Over Days')
        plt.xlabel('Day Number')
        plt.ylabel('Temperature (℃)')
        plt.grid(True, linestyle='--', color='gray')
        plt.legend()
        plt.savefig('temperature_trend.png')
        plt.show()


        # PM2.5健康等级可视化
        def get_levels(pm_values):
            levels = []
            colors = []
            for pm in pm_values:
                if pm <= 50:
                    levels.append('Good')
                    colors.append('green')
                elif pm <= 100:
                    levels.append('Moderate')
                    colors.append('orange')
                else:
                    levels.append('Unhealthy')
                    colors.append('red')
            return np.array(levels), np.array(colors)


        pm_levels, pm_colors = get_levels(pm25)

        plt.figure(figsize=(12, 8))
        # 绘制灰色折线表示趋势
        plt.plot(date_indices, pm25, color='gray', linestyle='--', label='PM2.5 Trend')
        # 用不同颜色圆点标记等级
        for level in ['Good', 'Moderate', 'Unhealthy']:
            mask = (pm_levels == level)
            color = 'green' if level == 'Good' else ('orange' if level == 'Moderate' else 'red')
            plt.scatter(date_indices[mask], pm25[mask], color=color, label=level)

        plt.title('PM2.5 Concentration and Health Levels Over Days')
        plt.xlabel('Day Number')
        plt.ylabel('PM2.5 Concentration (μg/m³)')
        plt.grid(True, linestyle='--', color='gray')
        plt.legend()
        plt.savefig('pm25_health_levels.png')
        plt.show()

except FileNotFoundError:
    print("读取文件出错：文件不存在")
except Exception as e:
    print(f"处理数据时出错：{e}")
