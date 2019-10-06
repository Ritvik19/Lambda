from flask import Flask, render_template, url_for
import json
import forms, classifiers

app = Flask(__name__)
app.config['SECRET_KEY'] = '79e9d3b5d183b6e620e3776f77d95f4b'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/url', methods=['GET', 'POST'])
def url_clf():
    form = forms.URLForm()
    if form.url.data:
        message=[
            classifiers.url_clf(form.url.data, classifiers.url_model1),
            classifiers.url_clf(form.url.data, classifiers.url_model2),
            classifiers.url_clf(form.url.data, classifiers.url_model3),
        ]
        return render_template('url.html', form=form, message=enumerate(message))
    return render_template('url.html', form=form)

@app.route('/inspyre')
def inspyre():
    message = classifiers.inspyre()
    return json.dumps(message)

if __name__ == '__main__':
    app.run(debug=True)
