import pickle

from URLfeatures import websiteInfo

url_model1 = pickle.load(open('E:/Models/URL-Classfier/LR.pickle', 'rb'))
url_model2 = pickle.load(open('E:/Models/URL-Classfier/RFC.pickle', 'rb'))
url_model3 = pickle.load(open('E:/Models/URL-Classfier/SVC.pickle', 'rb'))

url_clf = lambda x, model: 'Malicious' if model.predict(websiteInfo(x).drop(['URL'], axis=1))[0] == 1 else 'Non Malicious'
