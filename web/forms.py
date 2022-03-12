from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired

class GetUserDay(FlaskForm):
    name = StringField(validators=[DataRequired()])
    bday = DateField(validators=[DataRequired()])
    submit = SubmitField(validators=[DataRequired()])
