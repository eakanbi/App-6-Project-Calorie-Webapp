from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
# from wtform.validators import DataRequired, Length, Email, EqualTo, ValidationError

class CaloriesForm(FlaskForm):
    weight = StringField("Weight", default="70")
    height = StringField("Height", default="175")
    age = StringField("Age", default="32")
    country = StringField("Country", default="USA")
    city = StringField("City", default="San Francisco")
    button = SubmitField("Calculate")