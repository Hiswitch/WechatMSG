import matplotlib.pyplot as plt
import pandas as pd
from help import *

# 数据
labels = ['HSW', 'HJN']
sizes = []

# 读取CSV文件
df = pd.read_csv(data_path + 'all_data.csv')

# 计算IsSender为1和0的数目
is_sender_counts = df['IsSender'].value_counts()

# 打印结果
print("IsSender为1的数目:", is_sender_counts[1])
print("IsSender为0的数目:", is_sender_counts[0])

sizes.append(is_sender_counts[1])
sizes.append(is_sender_counts[0])

# 颜色
colors = ['#ff9999','#66b3ff']

# 绘图
plt.figure(figsize=(6,6))
plt.pie(sizes, labels=labels, colors=colors, autopct=lambda p: '{:.0f} ({:.1f}%)'.format(p * sum(sizes) / 100, p), startangle=140)
plt.axis('equal')  # 使饼图比例相等
plt.title('Proportion of messages on both sides')
plt.savefig(data_path + 'msg_raito_two.png')
