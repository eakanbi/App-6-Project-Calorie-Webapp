from flask import Flask, render_template, request, redirect
from calorie import Calorie
from temperature import Temperature
from forms import CaloriesForm


app = Flask(__name__)
app.secret_key = b'B\xdak\x81\x1dmS\xa8I\xb6'

@app.route('/index')
@app.route('/')

def index():
    return render_template('index.html')

@app.route('/calories')
def calories():
    form = CaloriesForm()
    return render_template('calories_form_page.html', title = 'Calories', 
                           caloriesform=form)




if __name__ == '__main__':
    app.run(debug=True)
