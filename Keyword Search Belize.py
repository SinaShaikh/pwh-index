""" 
Belize Keyword Search
Perry World House, Zeid Ra'ad Al Hussein
Sina Shaikh
"""

# Additional imports
from typing import List
import numpy as np
from openai import OpenAI
import pandas as pd
import ast

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
 
print("rocks :", lemmatizer.lemmatize("rocks"))
print("corpora :", lemmatizer.lemmatize("corpora"))


# Import master sheet with all recommendations
df = pd.read_csv(r"/Users/sinashaikh/Desktop/PWH/Master.csv")

# Read in Belize's letter
letter = open(r"/Users/sinashaikh/Desktop/PWH/Belize_Letter.txt",'r')
letter_content = letter.readlines()
letter_content = ''.join(letter_content)

# Clean the master doc
cleaned = []

for i in range(0,len(df)):
    cleaned_row = []
    temp = df.iloc[i][0].split('/')
    for j in range(0,len(temp)):
        token = temp[j]
        if '[or]' in token:
            token = token.split('[or]', 1)[0]
        cleaned_row.append(token)
    cleaned.append(cleaned_row)

# Find terms in master doc which apply
applicable = []

for i in range(0,len(cleaned)):
    marker = True
    for j in range(0,len(cleaned[i])):
        if cleaned[i][j] not in letter_content:
            marker = False
    if marker:
        applicable.append(cleaned[i])

print(applicable)


# Read in speech data
speeches = open(r"/Users/sinashaikh/Desktop/PWH/BelizeSpeeches.txt",'r')
speeches = speeches.readlines()
speeches = ''.join(speeches)


final =[]

for i in range(0,len(applicable)):
    marker = True
    for j in range(0,len(applicable[i])):
        if applicable[i][j] not in speeches:
            marker = False
    if marker:
        final.append(applicable[i])

print(final)
