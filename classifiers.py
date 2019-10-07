import pickle
import json, random
import numpy as np
import pandas as pd
from nltk import ngrams
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from URLFeatures import websiteInfo
from CuisineFeatures import clean_ingredients

# URL CLF
DIR_URL = 'E:/Models/URL-Classfier'

url_model1 = pickle.load(open(f'{DIR_URL}/LR.pickle', 'rb'))
url_model2 = pickle.load(open(f'{DIR_URL}/RFC.pickle', 'rb'))
url_model3 = pickle.load(open(f'{DIR_URL}/SVC.pickle', 'rb'))

url_clf = lambda x, model: 'Malicious' if model.predict(websiteInfo(x).drop(['URL'], axis=1))[0] == 1 else 'Non Malicious'

# CUISINE
DIR_CSN = 'E:/Models/Cuisine-Classifier'
csn_model = pickle.load(open(f'{DIR_CSN}/CuisineClassfier.pkl', 'rb'))
ingredients_list = pickle.load(open(f'{DIR_CSN}/Ingredients.pkl', 'rb'))

def csn_clf(query):
    query = clean_ingredients(query)
    feature = np.zeros((1 ,len(ingredients_list)))
    for ing in query:
        try:
            feature[0][ingredients_list.index(ing)] = 1
        except ValueError as e:
            pass
    return csn_model.predict(feature)[0]

# SENTIMENT

def senti_clf(sentence):
    sia_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sia_obj.polarity_scores(sentence)
    if sentiment_dict['compound'] >= 0.05 :
        return 'Positive'
    elif sentiment_dict['compound'] <= - 0.05 :
        return 'Negetive'
    else :
        return 'Neutral'

# INSPYROBOT

DIR_INS = 'E:/Models/Inspyrobot-Probabilistic-v4'
n = 4
q = lambda x : list(ngrams(x.lower().split(), n, pad_left=True, pad_right=False,  left_pad_symbol=''))[-1]
with open(f'{DIR_INS}/model.json', 'r') as f:
    data = json.load(f)
    dic = json.loads(data)
    k = dic.keys()
    v = dic.values()
    k1 = [eval(i) for i in k]
    ins_model =  dict(zip(*[k1,v]))

with open(f'{DIR_INS}/vocab.json', 'r') as f:
    vocab = json.loads(json.load(f))

def inspyrobot(text=''):
    if text == '' or q(text) not in ins_model.keys:
        text = str(random.choice(vocab))
    sentence_finished = False
    while not sentence_finished:
        r = random.random()
        accumulator = .0
        if ins_model[q(text)].keys() is None or (len(ins_model[q(text)].keys()) == 1 and list(ins_model[q(text)].keys())[0] == ''):
            break
        for word in ins_model[q(text)].keys():
            accumulator = ins_model[q(text)][word]
            if word != 'endquote' and accumulator >= r:
                text += ' '+word
                break
            if word == 'endquote':
                sentence_finished = True
    return (' '.join([t for t in text.split() if t]))

inspyre = lambda: {'message': inspyrobot()}
