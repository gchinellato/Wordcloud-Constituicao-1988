import numpy as np
import pandas as pd

with open('stopwords-pt-br-full.txt', 'r', encoding='utf-8') as fo:
    lines = fo.readlines()
	
df = pd.DataFrame(lines)
df = df.replace('\n','', regex=True)
df = df.replace('^\s|\s$','', regex=True)
df.drop_duplicates(keep='first', inplace=True)
df.to_excel('stopwords.xlsx')
