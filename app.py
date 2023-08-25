from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from calorie import Calorie
from temperature import Temperature


app = Flask(__name__)

@app.route('/index')
@app.route('/')

def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
