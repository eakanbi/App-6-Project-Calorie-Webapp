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

@app.route('/calories', methods=['GET', 'POST'])
def calories():
    form = CaloriesForm()

    if request.method == 'POST':
        temperature = Temperature(country=form.country.data,
                                  city=form.city.data).get()
        
        calorie = Calorie(weight=form.weight.data,
                           height=form.height.data, 
                           age=form.age.data, 
                           temperature=temperature)                
        calories = calorie.calculate()
        
        
        
        return render_template('calories_form_page.html', title = 'Calories', 
                           caloriesform=form,
                            calories = calories,
                            result=True)
    return render_template('calories_form_page.html', title = 'Calories', 
                           caloriesform=form)




if __name__ == '__main__':
    app.run(debug=True)
