import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from help import *

# 读取CSV文件
df = pd.read_csv(data_path + 'all_data.csv')

# 将StrTime列转换为datetime类型
df['StrTime'] = pd.to_datetime(df['StrTime'])

# 提取小时信息
df['Hour'] = df['StrTime'].dt.hour

# 分别统计IsSender为1和0的每个小时的数量
hourly_counts_IsSender_1 = df[df['IsSender'] == 1].groupby('Hour').size()
hourly_counts_IsSender_0 = df[df['IsSender'] == 0].groupby('Hour').size()

# 创建新的图形
plt.figure(figsize=(10, 6))

# 设置柱形的宽度
bar_width = 0.35

# 创建每个小时对应两个柱形的位置
x = np.arange(len(hourly_counts_IsSender_1))

# 绘制IsSender为1的柱形图
plt.bar(x - bar_width/2, hourly_counts_IsSender_1.values, bar_width, color='lightblue', label='HSW')

# 绘制IsSender为0的柱形图
plt.bar(x + bar_width/2, hourly_counts_IsSender_0.values, bar_width, color='lightpink', label='HJN')

# 设置图表标题和坐标轴标签
plt.title('Hourly Counts')
plt.xlabel('Hour of Day')
plt.ylabel('Count')

# 设置x轴刻度
plt.xticks(x, hourly_counts_IsSender_1.index)

# 添加图例
plt.legend()

# 显示图形
plt.tight_layout()
plt.savefig(data_path + 'frequency_hour.png')
