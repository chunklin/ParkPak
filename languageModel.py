import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names


def word_feats(words):
    return dict([(word, True) for word in words])


voc_p = ['great', 'fun', 'epic', 'good', ':)']
voc_n = ['bad', 'terrible', 'help', 'danger', ':(']


ft_pos = [(word_feats(pos), 'pos') for pos in voc_p]
ft_ng = [(word_feats(neg), 'neg') for neg in voc_n]


train_set = ft_ng + ft_pos

classifier = NaiveBayesClassifier.train(train_set)

# Predict
ng = 0
ps = 0
sentence = "Awesome movie, I liked it"
sentence = sentence.lower()
words = sentence.split(' ')
for word in words:
    classResult = classifier.classify(word_feats(word))
    if classResult == 'neg':
        ng = ng + 1
    if classResult == 'pos':
        ps = ps + 1
if ps < ng :
    print('distress')

