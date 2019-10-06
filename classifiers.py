import pickle
import json, random
from nltk import ngrams

from URLfeatures import websiteInfo

# URL CLF

url_model1 = pickle.load(open('E:/Models/URL-Classfier/LR.pickle', 'rb'))
url_model2 = pickle.load(open('E:/Models/URL-Classfier/RFC.pickle', 'rb'))
url_model3 = pickle.load(open('E:/Models/URL-Classfier/SVC.pickle', 'rb'))

url_clf = lambda x, model: 'Malicious' if model.predict(websiteInfo(x).drop(['URL'], axis=1))[0] == 1 else 'Non Malicious'

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
    if text == '':
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
