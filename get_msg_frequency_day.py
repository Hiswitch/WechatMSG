import pandas as pd
import matplotlib.pyplot as plt

from help import *

# 1. 读取CSV文件并解析日期时间数据
df = pd.read_csv(data_path + 'clean_data.csv')

# 2. 将日期时间数据转换为Python的datetime对象
df['StrTime'] = pd.to_datetime(df['StrTime'])

# 3. 对日期时间数据进行分组，每30天为一组，并统计每组的数量
# 找到最早的日期
start_date = df['StrTime'].min()
# 计算每个日期距离最早日期的天数
df['DaysSinceStart'] = (df['StrTime'] - start_date).dt.days
# 根据每30天为一组进行分组
df['DateGroup'] = df['DaysSinceStart'] // 1
# 对新的时间段进行分组，并统计每组的数量
grouped = df.groupby('DateGroup').size().reset_index(name='Counts')

# 获取每组的第一个日期作为Y轴的刻度
yticks = [df[df['DateGroup'] == group]['StrTime'].iloc[0].strftime('%Y-%m-%d') for group in grouped['DateGroup']]

# 4. 绘制横向条形图
plt.figure(figsize=(10, 8))
bars = plt.barh(range(len(grouped)), [1] * len(grouped), color=plt.cm.Reds(grouped['Counts'] / max(grouped['Counts'])), height=0.5)

# 添加颜色标识和数量标签
cbar = plt.colorbar(plt.cm.ScalarMappable(cmap='Reds'))
cbar.set_label('Extent')

# 设置Y轴刻度，每隔三次显示一次yticks
plt.yticks(range(0, len(grouped), 15), [yticks[i] for i in range(0, len(yticks), 15)])

plt.ylabel('Date Group')
plt.title('Counts per 1 Days')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig(data_path + 'frequency_day.png')