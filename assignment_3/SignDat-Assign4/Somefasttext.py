#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 10:48:16 2022

@author: dayman
"""

import fasttext as ft
import re
import fasttext
import numpy as np
import os

#data = np.load(os.getcwd() + 'news_data.npz')
#print("Training model")
model = fasttext.train_supervised(input="dat_data_new_labels_cleaned.txt", verbose=False)
#print("Testing model")
#model.test('dat_data_new_labels_cleaned.txt')

txt = open('dat_data_new_labels_cleaned.txt', 'r')
txt_arr = txt.read().split('\n')
#print(txt_arr[0:5])

tests = []
labels = []
for r, i in enumerate(txt_arr):
    try:
        to_append = i.split(' ', 1)
        
        #tests.append(i.split(' ', 1)[1])
        tests.append(to_append[1])
        labels.append(to_append[0])
    except:
        print(r)

print('Predicting')

print(labels[0:50])
su = 0
for i, test in enumerate(tests):
    predict_label = model.predict(test)[0][0]
    
    if predict_label == labels[i]:
        su += 1

print("Total accuracy was ", su/len(tests))

"""
text = 'He turned himself into a pickle! Funniest shit, ive ever seen!!!!'

def get_n_grams(text, n, lower=True, strip=True):
    Gets a specific n-gram for a given text string
    if lower:
        text = text.lower()
    if strip:
        text = re.sub('[^A-Za-z0-9 ]+', '', text) 

    text = text.split()
    n_grams = []
    
    for i, word in enumerate(text):
        if i+n > len(text):
            break
        n_grams.append(text[i: i+n])

    return n_grams


print(get_n_grams(text, 2, False))


def get_word_grams(word, n):
     the character wise n-grams for a single word
    word_grams = []

    # So really this is not something you should do for the actual model
    # String concatenation in python is O(N+M) complexity, which is blazingly slow
    # Probably nltk.ngrams function does it faster
    word = '<' + word + '>'

    for i, character in enumerate(word):
        if i+n > len(word):
            break

        word_grams.append(word[i:i+n])
    
    return word_grams


text = "He turned himself into a pickle... Funniest shit, ive ever seen!!!"

n_grams = get_n_grams(text, 3, lower=True, strip=True)
word_grams = [get_word_grams(words[0], 3) for words in n_grams]

print("N-grams here: \n ", n_grams)

print("Word-grams here: \n ", word_grams)
"""
