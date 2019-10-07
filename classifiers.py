import pickle
import json, random, re
import numpy as np
import pandas as pd
from nltk import ngrams

from URLfeatures import websiteInfo

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

def delete_brand_(ingredient):
    ingredient = re.sub("country crock|i can't believe it's not butter!|bertolli|oreo|hellmann's", '', ingredient)
    ingredient = re.sub("red gold|hidden valley|original ranch|frank's|redhot|lipton", '', ingredient)
    ingredient = re.sub("recipe secrets|eggland's best|hidden valley|best foods|knorr|land o lakes", '', ingredient)
    ingredient = re.sub("sargento|johnsonville|breyers|diamond crystal|taco bell|bacardi", '', ingredient)
    ingredient = re.sub("mccormick|crystal farms|yoplait|mazola|new york style panetini", '', ingredient)
    ingredient = re.sub("ragu|soy vay|tabasco|truvía|crescent recipe creations|spice islands", '', ingredient)
    ingredient = re.sub("wish-bone|honeysuckle white|pasta sides|fiesta sides", '', ingredient)
    ingredient = re.sub("veri veri teriyaki|artisan blends|home originals|greek yogurt|original ranch", '', ingredient)
    ingredient = re.sub("jonshonville", '', ingredient)
    ingredient = re.sub("old el paso|pillsbury|progresso|betty crocker|green giant|hellmanns|hellmannâ€", '', ingredient)
    ingredient = re.sub("oscar mayer deli fresh smoked|half & half", '', ingredient)
    return ingredient

def delete_state_(ingredient):
    ingredient = re.sub('frozen|chopped|ground|fresh|powdered', '', ingredient)
    ingredient = re.sub('sharp|crushed|grilled|roasted|sliced', '', ingredient)
    ingredient = re.sub('cooked|shredded|cracked|minced|finely', '', ingredient)
    return ingredient

def delete_comma_(ingredient):
    ingredient = ingredient.split(',')
    ingredient = ingredient[0]
    return ingredient

def original_(ingredient):
    ingredient = re.sub('[0-9]', '', ingredient)
    ingredient = ingredient.replace("oz.", '')
    ingredient = re.sub('[&%()®™/]', '', ingredient)
    ingredient = re.sub('[-.]', '', ingredient)
    return ingredient

def clean_ingredients(X):
    cleaned = []
    rmC = u'®™,.;![]\'’"-_@#$%&`/'
    for x in X:
        x_ = x.lower()
        for rm in rmC:
            x_ = x_.replace(rm, ' ')
        x_ = delete_brand_(x_)
        x_ = delete_state_(x_)
        x_ = delete_comma_(x_)
        x_ = original_(x_)
        x_ = re.sub('less\s\w*\s', ' ', x_)
        x_ = re.sub('\(.*\)', ' ', x_)
        x_ = re.sub('[^A-Za-z ]', ' ', x_)
        x_ = re.sub('\s+', ' ', x_)
        x_ = x_.strip()
        x_ = ' '.join(_ for _ in x_.split() if len(_) > 2)
        if len(x_) > 2:
            cleaned.append(x_)
    return cleaned

def csn_clf(query):
    query = clean_ingredients(query)
    feature = np.zeros((1 ,len(ingredients_list)))
    for ing in query:
        try:
            feature[0][ingredients_list.index(ing)] = 1
        except ValueError as e:
            pass
    return csn_model.predict(feature)[0]

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
