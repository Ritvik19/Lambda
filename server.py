from flask import Flask, render_template, url_for
import forms

app = Flask(__name__)
app.config['SECRET_KEY'] = '79e9d3b5d183b6e620e3776f77d95f4b'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/url', methods=['GET', 'POST'])
def url_clf():
    form = forms.URLForm()
    if form.url.data:
        print(form.url.data)
        return render_template('url.html', form=form, message=form.url.data)
    return render_template('url.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
