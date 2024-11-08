""" 
Belize Word Embeddings using OpenAI
Perry World House, Zeid Ra'ad Al Hussein
Sina Shaikh
"""

# Additional imports
from typing import List
import numpy as np
from openai import OpenAI
import pandas as pd
import ast

client = OpenAI(api_key = "")

applicable = [['National ', 'into ', ' international human rights standards', ' torture'], ['Ensuring ', 'freedom ', 'expression'], ['Ensuring ', ' freedom ', 'assembly'], ['Ensuring ', ' freedom ', 'press'], ['Decriminalization ', 'defamation']]

df = pd.read_csv(r"/Users/sinashaikh/Desktop/PWH/Belize Embeddings.csv")

df['embedding'] = df['embedding'].apply(ast.literal_eval)

# Define relevant functions (no longer defined in newest version)
def get_embedding(text, model="text-embedding-ada-002"):
    text = text.replace("\n", " ")
    return client.embeddings.create(input = [text], model=model).data[0].embedding

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def search_reviews(df, product_description, n=3, pprint=True):
    product_embedding = get_embedding(
        product_description,
        model="text-embedding-ada-002"
    )
    df["similarity"] = df.embedding.apply(lambda x: cosine_similarity(x, product_embedding))

    results = (
        df.sort_values("similarity", ascending=False).speech
        .head(n)
    )
    if pprint:
        for r in results:
            print(r)
            print()
    return results

# Calculate similarity with a given phrase, printing the top n most simmilar lines
results = search_reviews(df, "Strengthening the national human rights framework  with principles relating to the status of national institutions for the protection of human rights", n=10)

"""
for i in range(len(applicable)):
    applicable[i] = ''.join(applicable[i])
    print(search_reviews(df, applicable[i], n=10))
"""