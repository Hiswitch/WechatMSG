import pandas as pd
import jieba
from wordcloud import WordCloud
from help import *

# 读取CSV文件
df = pd.read_csv(data_path + 'is_sender_1.csv')

# 合并所有的StrContent为一个文本字符串
text = ' '.join(df['StrContent'].astype(str))

# 使用jieba进行分词
words = ' '.join(jieba.cut(text))

# 导入中文停用词库
stopwords_path = data_path + 'stopwords.txt'  # 替换为你的中文停用词库文件路径
stopwords = set([line.strip() for line in open(stopwords_path, 'r', encoding='utf-8')])

# 设置中文字体路径
font_path = data_path + 'STSONG.TTF'  # 替换为你的中文字体文件路径

# 生成词云
wordcloud = WordCloud(width=800, height=400, background_color='white', font_path=font_path, stopwords=stopwords).generate(words)

# 可视化词云
output_path = data_path + 'wordcloud_me.png'  # 替换为你想保存的文件路径
wordcloud.to_file(output_path)