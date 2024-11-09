from text_classifier import TextClassifier

import pylab as plt
import numpy as np
import seaborn as snb
from tqdm import tqdm


# load data
news_data = np.load('./news_data.npz', allow_pickle=True)
train_texts = news_data['train_texts']
test_texts = news_data['test_texts']
train_labels = news_data['train_labels']
test_labels = news_data['test_labels']
ag_news_labels = news_data['ag_news_label']

print(ag_news_labels)

# prep and train model
embed_dim = 32
classifier = TextClassifier(train_texts, train_labels, embed_dim, num_epochs=5)

# evaluate accuracy on test set
acc = 0
for text, y_true in tqdm(zip(test_texts, test_labels)):
    output = classifier.predict(text)
    if output == y_true:
        acc += 1

print('Classification error on test set', acc / len(test_texts))

# Make predictions on own text
ex_text_str = "MEMPHIS, Tenn. – Four days ago, Jon Rahm was \
    enduring the season’s worst weather conditions on Sunday at The \
    Open on his way to a closing 75 at Royal Portrush, which \
    considering the wind and the rain was a respectable showing. \
    Thursday’s first round at the WGC-FedEx St. Jude Invitational \
    was another story. With temperatures in the mid-80s and hardly any \
    wind, the Spaniard was 13 strokes better in a flawless round. \
    Thanks to his best putting performance on the PGA Tour, Rahm \
    finished with an 8-under 62 for a three-stroke lead, which \
    was even more impressive considering he’d never played the \
    front nine at TPC Southwind."

class_label_idx = classifier.predict(ex_text_str.lower())

print("This is a %s news" % ag_news_labels[class_label_idx])


snb.set_style('darkgrid')
Xtest = []
ctest = []

for text, cls in zip(test_texts, test_labels):
    emb = classifier.get_text_embedding(text)
    Xtest.append(emb)
    ctest.append(cls)

Xtest = np.row_stack(Xtest)
ctest = np.stack(ctest)

from sklearn.decomposition import PCA

pca = PCA(n_components=4)
Ztest = pca.fit_transform(Xtest)

colors = 'rgbk'

plt.figure(figsize=(20, 6))
plt.subplot(1, 3, 1)
for i in range(4):
    plt.plot(Ztest[ctest == i, 0], Ztest[ctest == i, 1], '.', color=colors[i], label=ag_news_labels[i])
plt.legend()
plt.xlabel('PC1')
plt.ylabel('PC2')

plt.subplot(1, 3, 2)
for i in range(4):
    plt.plot(Ztest[ctest == i, 1], Ztest[ctest == i, 2], '.', color=colors[i], label=ag_news_labels[i])
plt.legend()
plt.xlabel('PC2')
plt.ylabel('PC3')

plt.subplot(1, 3, 3)
for i in range(4):
    plt.plot(Ztest[ctest == i, 2], Ztest[ctest == i, 3], '.', color=colors[i], label=ag_news_labels[i])
plt.legend()
plt.xlabel('PC3')
plt.ylabel('PC4')
plt.show()