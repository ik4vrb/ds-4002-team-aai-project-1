#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 22:29:44 2023

@author: anacristinacordova
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


books = pd.read_csv("Top25_Books_Data.csv")
word_list = pd.read_csv("word_list.csv")
books.rename(columns={'response': 'hook'}, inplace=True)


mean_hook = books['num_words'].mean()
print(mean_hook)
    #Mean word count per hook of each book is 257.2


#Genre count of the books
gene_counts = books['Genre'].value_counts().reset_index()
gene_counts.columns = ['Genre', 'Book_Count']
print(gene_counts)

generes = sns.countplot(data=books, x='Genre')
generes.set(xlabel='Genre',
     ylabel='Number of Books',
     title='Genre of the Top 25 Books over 125 years')
plt.xticks(rotation=90)


#Average of Positive and Negative words per hook 
word_list['word'] = word_list['word'].str.lower()
books['hook'] = books['hook'].str.lower()
books['hook_cleaned'] = books['hook'].str.replace('[,.]', ' ', regex=True)

positive_words = word_list[word_list["category"]=="positive"]
pw = positive_words['word'].tolist()

negative_words = word_list[word_list["category"]=="negative"]
nw = negative_words['word'].tolist()

def count_words_in_text(text, word_list):
    words_in_text = text.split()
    word_count = sum(1 for word in words_in_text if word in word_list)
    return word_count

books['positive'] = books['hook_cleaned'].apply(lambda x: count_words_in_text(x, pw))
books['negative'] = books['hook_cleaned'].apply(lambda x: count_words_in_text(x, nw))

wcount = books[["story_name",'positive', "negative"]]
print(wcount)

