from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FloatField
# from wtform.validators import DataRequired, Length, Email, EqualTo, ValidationError

class CaloriesForm(FlaskForm):
    weight = FloatField("Weight", default="70")
    height = FloatField("Height", default="175")
    age = FloatField("Age", default="32")
    country = StringField("Country", default="USA")
    city = StringField("City", default="San Francisco")
    button = SubmitField("Calculate")