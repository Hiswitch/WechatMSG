import pandas as pd
import jieba
from collections import Counter
from help import *

# 读入CSV文件，设置 "StrContent" 列的数据类型为字符串
file_path = data_path + "is_sender_1.csv"  # 请替换为实际的CSV文件路径
df = pd.read_csv(file_path, dtype={'StrContent': str})

# 获取文本数据列
text_column = "StrContent"  # 请根据实际情况替换列名

# 删除空字符串
df = df[df[text_column].notna()]  # 删除包含NaN的行
df = df[df[text_column] != '']  # 删除空字符串

# 合并文本数据
all_text = ' '.join(df[text_column])

# 使用jieba分词
seg_list = jieba.cut(all_text, cut_all=False)

# 从停用词文件中读取停用词列表
stop_words_file = data_path + "stopwords.txt"  # 请替换为实际的停用词文件路径
with open(stop_words_file, 'r', encoding='utf-8') as stop_words_file:
    stop_words = [line.strip() for line in stop_words_file]

# 过滤停用词和空格字符
filtered_words = [word for word in seg_list if word not in stop_words and word.strip()]

# 统计词频
word_count = Counter(filtered_words)

# 获取前十个词频最高的词语
top_10_words = word_count.most_common(10)

# 打印结果
for word, count in top_10_words:
    print(f"{word}: {count}")