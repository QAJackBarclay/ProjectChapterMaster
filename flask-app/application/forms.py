from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError

class Legion_Name(FlaskForm):
    legion_name = StringField('What is the name of your chapter?', validators=[Length(min=1, max=40),DataRequired()])
    submit = SubmitField('Confirm.')