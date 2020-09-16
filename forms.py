from flask_wtf import FlaskForm
from wtforms import StringField, TextField, BooleanField
from wtforms.validators import DataRequired, optional


class TodoForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    description = TextField('desctrition', validators=[DataRequired()])
    status = BooleanField('status', validators=[optional()])

    