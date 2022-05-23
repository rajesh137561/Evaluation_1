# -*- coding: utf-8 -*-
"""
Created on Sun May 22 20:29:43 2022

@author: Rajesh
"""

import pandas as pd

df = pd.read_csv("C:/Users/HP/Desktop/review_data.csv")

df.head()

cols = ['star', 'app_id','reviewDate']
df.drop(cols, axis=1, inplace=True)
df.head()


import language_tool_python
tool = language_tool_python.LanguageTool('en-US')

for i in df.index:
    text = df['text'][i]
    matches = tool.check(text)
    count = len(matches)
    if count == 0:
        print(text," -- No mistakes")
    else:
        print(text," -- Mistakes found, ",count," mistakes")

tool.close()
