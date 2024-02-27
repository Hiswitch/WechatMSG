import pandas as pd
import matplotlib.pyplot as plt
from help import *

# 读取CSV文件
df = pd.read_csv(data_path + 'all_data.csv') 
df_copy = df.copy()
# 将StrTime列转换为datetime类型
df_copy['StrTime'] = pd.to_datetime(df_copy['StrTime'])

# 获取星期几并统计数量
weekday_counts = df_copy['StrTime'].dt.day_name().value_counts()

# 打印结果
print(weekday_counts)

# 将结果排序，以确保按照星期顺序绘制
weekday_counts = weekday_counts.reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

# 绘制分布图
plt.figure(figsize=(10, 6))
bars = weekday_counts.plot(kind='bar', color='skyblue')
plt.title('Distribution of Messages by Weekday')
plt.xlabel('Weekday')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 在每个柱子上添加数量标签
for bar in bars.patches:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(int(bar.get_height())), ha='center', va='bottom')

plt.tight_layout()
plt.savefig(data_path + 'msg_ratio_mon2sun.png')