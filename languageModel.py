import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names
import pyaudio
import speech_recognition as spreg
from firebase import firebase
firebase = firebase.FirebaseApplication('https://parkpak-c41e3.firebaseio.com/')

def word_feats(words):
    return dict([(word, True) for word in words])


voc_p = ['great', 'fun', 'epic', 'good', 'happy', 'safe', 'normal','amazing' ]
voc_n = ['bad', 'terrible', 'help', 'danger', 'trouble']


ft_pos = [(word_feats(pos), 'pos') for pos in voc_p]
ft_ng = [(word_feats(neg), 'neg') for neg in voc_n]


tr_set = ft_ng + ft_pos

class_fy = NaiveBayesClassifier.train(tr_set)
# Predict
def predictNegPos(sentence):
    ng = 0
    ps = 0

    sentence = sentence.lower()
    words = sentence.split(' ')
    for word in words:
        classResult = class_fy.classify(word_feats(word))
        if classResult == 'neg':
            ng+=1
        if classResult == 'pos':
            ps+=1
    if ng > ps:
        result = firebase.put(
            '',
            '/microphone',
            {
                "distress": "distressed!"
            }
        )
        print(result)
    else:
        result = firebase.put(
            '',
            '/microphone',
            {
                "distress": "normal."
            }
        )
        print(result)
sample_rate = 48000
data_size = 2048

recog = spreg.Recognizer()
while 1:
    with spreg.Microphone(sample_rate = sample_rate, chunk_size = data_size) as source:
        recog.adjust_for_ambient_noise(source)
        print('Tell Something: ')
        speech = recog.listen(source)
    try:
        text = recog.recognize_google(speech)
        print('You have said: ' + text)
        predictNegPos(text)
    except spreg.UnknownValueError:
        print('Unable to recognize the audio')
    except spreg.RequestError as e:
        print("Request error from Google Speech Recognition service; {}".format(e))

