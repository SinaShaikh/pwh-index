""" 
Belize Webscraper
Perry World House, Zeid Ra'ad Al Hussein
Sina Shaikh
"""

from bs4 import BeautifulSoup
import pandas as pd
 
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


""" 
Using modified code from https://cookbook.openai.com/examples/get_embeddings_from_dataset
"""

# Additional imports
from typing import List
import numpy as np
from openai import OpenAI

# Set API key and datafile path
client = OpenAI(api_key = "")
datafile_path = r"/Users/sinashaikh/Desktop/PWH/Belize Speeches.csv"
embedding_model = "text-embedding-ada-002"

# store data in df
df = pd.read_csv(datafile_path)
df.columns = ['speech']

# add embeddings
def get_embedding(text, model="text-embedding-ada-002"):
   text = text.replace("\n", " ")
   return client.embeddings.create(input = [text], model=model).data[0].embedding

df["embedding"] = df.iloc[:, 0].apply(lambda x: get_embedding(x, model=embedding_model))

# export df with csv's
df.to_csv('Belize Embeddings.csv', index=False)
