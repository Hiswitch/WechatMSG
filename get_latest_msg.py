import pandas as pd
from help import *

split_hour = 4

def compare_time(time0, time1):
    if time0.hour < split_hour and time1.hour >= split_hour:
        return 0
    elif time0.hour >= split_hour and time1.hour < split_hour:
        return 1
    else:
        # 分别比较时、分、秒
        if time0.hour > time1.hour:
            return 0
        elif time0.hour < time1.hour:
            return 1
        else:
            if time0.minute > time1.minute:
                return 0
            elif time0.minute < time1.minute:
                return 1
            else:
                if time0.second >= time1.second:
                    return 0
                elif time0.second < time1.second:
                    return 1
    

# 读取CSV文件
df = pd.read_csv(data_path + "clean_data.csv")

# 将StrTime列手动解析为datetime类型
df['StrTime'] = pd.to_datetime(df['StrTime'])

# 提取时间部分
df['Time'] = df['StrTime'].dt.time

times = df['Time'].to_list()
latest_time = times[0]
for i in range(len(times)):
    if compare_time(latest_time, times[i]):
        latest_time = times[i]

# 找到时间部分最晚的行数据
latest_row = df[df['Time'] == latest_time].iloc[0]

print("时间部分最晚的一行数据为：")
print(latest_row)
