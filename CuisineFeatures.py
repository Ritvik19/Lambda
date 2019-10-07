import re

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
