from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError

class User_Name(FlaskForm):
    user_name = StringField('What is your Battle Brother name?', validators=[Length(min=2, max=40),DataRequired()])
    submit = SubmitField('Confirm.')

class BasicForm(FlaskForm):
    update_name = StringField("Try another name?: ", validators=[DataRequired()])
    favourite_1 = SelectField("Pick an allegiance: ", choices = ['Loyalist', 'Heretic'])
    submit = SubmitField ('Send to the Warp')