# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import numpy as np
from tqdm import tqdm
import re

data = np.load('/media/dayman/Big Chongus/SignDat-Assign4/news_data.npz')
train_texts = data['train_texts']
test_texts = data['test_texts']
train_labels = data['train_labels']
test_labels = data['test_labels']
ag_news_labels = data['ag_news_label']





txt = ""
for i, (trains, tests) in tqdm(enumerate(zip(train_texts, train_labels))):
    trains = trains.lower()
    trains = re.sub('[^a-z0-9 ]+', '', trains)

    txt = txt + f'__label__{ag_news_labels[tests]} {trains}\n'

    
with open('/media/dayman/Big Chongus/SignDat-Assign4/dat_data_new_labels_cleaned.txt', 'w') as f:
    f.write(txt)
