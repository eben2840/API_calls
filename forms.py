from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, IntegerField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError, Regexp,Length


class Rooms(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    phonenumber =  StringField('phonenumber', validators=[DataRequired()])
    course =  StringField('course', validators=[DataRequired()])
    level =  StringField('course', validators=[DataRequired()])
    singlebooking =  StringField('course', validators=[DataRequired()])
    numberofbooking =  StringField('course', validators=[DataRequired()])
    date =  StringField('course', validators=[DataRequired()])
    room =  StringField('course', validators=[DataRequired()])
    bed =  StringField('course', validators=[DataRequired()])
    submit = SubmitField('submit')  
 