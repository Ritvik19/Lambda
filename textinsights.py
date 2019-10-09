from TextFeatures import cleanText

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fuzzywuzzy import fuzz


def jaccard_sim(str1, str2):
    a = set(cleanText(str1, True, False, True, False).split())
    b = set(cleanText(str2, True, False, True, False).split())
    c = a & b
    d = a | b
    return float(len(c)) / (len(d))*100

def cosine_sim(str1, str2):
    str_ = [cleanText(str1, True, False, True, False), cleanText(str2, True, False, True, False)]
    vectorizer = CountVectorizer()
    vect_ = vectorizer.fit_transform(str_).toarray()
    return cosine_similarity([vect_[0]], [vect_[1]])[0][0]*100

def fuzz_ratio(str1, str2):
    return fuzz.ratio(cleanText(str1, True, False, True, False),
                      cleanText(str2, True, False, True, False))

def fuzz_partial_ratio(str1, str2):
    return fuzz.partial_ratio(cleanText(str1, True, False, True, False),
                              cleanText(str2, True, False, True, False))

def fuzz_token_sort_ratio(str1, str2):
    return fuzz.token_sort_ratio(cleanText(str1, True, False, True, False),
                              cleanText(str2, True, False, True, False))

def fuzz_token_set_ratio(str1, str2):
    return fuzz.token_sort_ratio(cleanText(str1, True, False, True, False),
                              cleanText(str2, True, False, True, False))
