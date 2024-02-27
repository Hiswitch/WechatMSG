import pandas as pd
from help import *

# 读取CSV文件
df = pd.read_csv(data_path + 'all_data.csv')

# 获取文本数据列
text_column = "StrContent"  # 请根据实际情况替换列名

# 删除空字符串
df = df[df[text_column].notna()]  # 删除包含NaN的行
df = df[df[text_column] != '']  # 删除空字符串

# 筛选掉包含<msg>的行
df = df[~df['StrContent'].str.contains('msg')]

# 保存结果为新的CSV文件
df.to_csv(data_path + 'clean_data.csv', index=False)
