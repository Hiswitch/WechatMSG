import pandas as pd
import matplotlib.pyplot as plt
from help import *

df = pd.read_csv(data_path + 'clean_data.csv') 
counts = df['Type'].value_counts()

print(counts)