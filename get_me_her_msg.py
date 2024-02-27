import pandas as pd
from help import *



# 读取CSV文件
df = pd.read_csv(data_path + 'clean_data.csv')

# 提取IsSender为1时的StrContent
is_sender_1 = df[df['IsSender'] == 1][['StrContent']]

# 提取IsSender为0时的StrContent
is_sender_0 = df[df['IsSender'] == 0][['StrContent']]

# 保存结果为新的CSV文件
is_sender_1.to_csv(data_path + 'is_sender_1.csv', index=False)
is_sender_0.to_csv(data_path + 'is_sender_0.csv', index=False)
