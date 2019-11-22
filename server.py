from flask import Flask, render_template, url_for, request
import json
import forms, classifiers, textinsights

app = Flask(__name__)
app.config['SECRET_KEY'] = '79e9d3b5d183b6e620e3776f77d95f4b'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/url', methods=['GET', 'POST'])
def url_clf():
    form = forms.URLForm()
    if request.method == 'POST':
        message = [
            classifiers.url_clf(form.url.data, classifiers.url_model1),
            classifiers.url_clf(form.url.data, classifiers.url_model2),
            classifiers.url_clf(form.url.data, classifiers.url_model3),
        ]
        return render_template('url.html', form=form, message=enumerate(message))
    return render_template('url.html', form=form)

@app.route('/inspyrobot', methods=['GET', 'POST'])
def inspyrobot():
    form = forms.INSForm()
    if request.method == 'POST':
        message = classifiers.inspyrobot(form.keyword.data.strip())
        return render_template('inspyrobot.html', form=form, message=message)
    return render_template('inspyrobot.html', form=form)

@app.route('/inspyre', methods=['GET', 'POST'])
@app.route('/inspyre/', methods=['GET', 'POST'])
def inspyre():
    keyword = request.args.get('q')
    print(keyword)
    if keyword is not None:
        message = classifiers.inspyre(keyword)
    else:
        message = classifiers.inspyre('')
    return json.dumps(message)

@app.route('/cuisine',methods=['GET', 'POST'])
def cuisine():
    form = forms.CuisineForm()
    if request.method == 'POST':
        message = classifiers.csn_clf(form.ingredients.data)
        return render_template('cuisine.html', form=form, message=message)
    return render_template('cuisine.html', form=form)

@app.route('/sentiment',methods=['GET', 'POST'])
def sentiment():
    form = forms.SentimentForm()
    if request.method == 'POST':
        message = classifiers.senti_clf(form.sentence.data)
        return render_template('sentiment.html', form=form, message=message)
    return render_template('sentiment.html', form=form)

@app.route('/spam',methods=['GET', 'POST'])
def spam():
    form = forms.SpamForm()
    if request.method == 'POST':
        message = classifiers.spam_clf(form.sentence.data)
        return render_template('spam.html', form=form, message=message)
    return render_template('spam.html', form=form)

@app.route('/similarity',methods=['GET', 'POST'])
def similarity():
    form = forms.SimilarityForm()
    if request.method == 'POST':
        message = [
            ('Jaccard Similarity', textinsights.jaccard_sim(form.sentence1.data, form.sentence2.data)),
            ('Cosine Similarity', textinsights.cosine_sim(form.sentence1.data, form.sentence2.data)),
            ('Fuzz Ratio', textinsights.fuzz_ratio(form.sentence1.data, form.sentence2.data)),
            ('Partial Ratio', textinsights.fuzz_partial_ratio(form.sentence1.data, form.sentence2.data)),
            ('Token Sort Ratio', textinsights.fuzz_token_sort_ratio(form.sentence1.data, form.sentence2.data)),
            ('Token Set Ratio', textinsights.fuzz_token_set_ratio(form.sentence1.data, form.sentence2.data)),
        ]
        return render_template('similarity.html', form=form, message=message)
    return render_template('similarity.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
