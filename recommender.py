import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


df = pd.read_csv('FinalKeywordsData.csv')

count_matrix = CountVectorizer().fit_transform(df['keywords'])
cosine_sim = cosine_similarity(count_matrix)


# Get symbol from index
def get_title_from_index(index):
  return df[df.index == index]["symbol"].values[0]

# Get index from symbol
def get_index_from_title(symbol):
  return df[df.symbol == symbol].index.values[0]

def get_similar(symbol):
    index = get_index_from_title(symbol)
    similar_stocks = list(enumerate(cosine_sim[index]))
    sortedstocks = sorted(similar_stocks, key=lambda x: x[1], reverse=True)

    dftest = pd.DataFrame()

    top5similar = []
    # Get top 5 similar stocks
    for i in range(1,6):
        index = sortedstocks[i][0]
        top5similar.append(get_title_from_index(index))

    return top5similar