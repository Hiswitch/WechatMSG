import pandas as pd
from help import *
# 读取CSV文件

# 提取IsSender为1时的StrContent
me = pd.read_csv(data_path + 'is_sender_1.csv')['StrContent']

# 提取IsSender为0时的StrContent
her = pd.read_csv(data_path + 'is_sender_0.csv')['StrContent']

# 计算包含“爱”字的数量
count_1 = me.str.count('爱你').sum() + me.str.count("喜欢你").sum()
count_0 = her.str.count('爱你').sum() + her.str.count("喜欢你").sum()

# 打印结果
print("me: ", count_1)
print("her: ", count_0)

# 比较数量并输出结果
if count_1 > count_0:
    print("I love her more.")
elif count_1 < count_0:
    print("She loves me more.")
else:
    print("We love each other very much.")
