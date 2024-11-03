from text_classifier import TextClassifier

import pylab as plt
import numpy as np
import seaborn as snb
from tqdm import tqdm


# load data
spam_data = np.load('./spam_data.npz', allow_pickle=True)
train_texts = spam_data['train_texts']
test_texts = spam_data['test_texts']

train_labels = spam_data['train_labels']
test_labels = spam_data['test_labels']
spamlabels = spam_data['labels']

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


ex_text_str = "you can get all this stuff for free."
print(60*'-')
print('Text: %s' % ex_text_str)
print(60*'-')

class_label_idx = classifier.predict(ex_text_str.lower())
probs = classifier.predict(ex_text_str.lower(), return_prob=True)

print("This is a %s" % spamlabels[class_label_idx])

print('\nProbabilities')
for label, prob in zip(spamlabels, probs.T):
    print('\t%-15s%3.2f' % (label, prob))
print('')



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
for i in range(2):
    plt.plot(Ztest[ctest == i, 0], Ztest[ctest == i, 1], '.', color=colors[i], label=spamlabels[i])
plt.legend()
plt.xlabel('PC1')
plt.ylabel('PC2')

plt.subplot(1, 3, 2)
for i in range(2):
    plt.plot(Ztest[ctest == i, 1], Ztest[ctest == i, 2], '.', color=colors[i], label=spamlabels[i])
plt.legend()
plt.xlabel('PC2')
plt.ylabel('PC3')

plt.subplot(1, 3, 3)
for i in range(2):
    plt.plot(Ztest[ctest == i, 2], Ztest[ctest == i, 3], '.', color=colors[i], label=spamlabels[i])
plt.legend()
plt.xlabel('PC3')
plt.ylabel('PC4')
plt.show()