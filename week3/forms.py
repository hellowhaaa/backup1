from flask_wtf import FlaskForm
from wtforms import IntegerField,SubmitField,StringField
from wtforms.validators import DataRequired

class SumUpForm(FlaskForm):
    number = StringField('Number', validators=[DataRequired()])
    
    # pass the string that dirctly from the label
    # 這些 attrbute 可以send back to html
