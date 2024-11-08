""" 
Russia Webscraper and analysis
"""

from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
import re



df = pd.read_csv(r"/Users/sinashaikh/Desktop/PWH/Master.csv")

letter = open(r"/Users/sinashaikh/Desktop/PWH/Russia_Letter.txt",'r')
letter_content = letter.readlines()

letter_content = ''.join(letter_content)

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

applicable = []


for i in range(0,len(cleaned)):
    marker = True
    for j in range(0,len(cleaned[i])):
        if cleaned[i][j] not in letter_content:
            marker = False
    if marker:
        applicable.append(cleaned[i])


print(applicable)

print(len(applicable))

speeches = open(r"/Users/sinashaikh/Desktop/PWH/RussiaSpeeches.txt",'r')
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








