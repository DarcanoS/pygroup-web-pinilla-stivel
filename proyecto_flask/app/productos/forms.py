from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired


class CreateCategoryForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    
class Create_Stock_Form(FlaskForm):
    product_id = IntegerField('product_id', validators=[DataRequired()])
    quantity = IntegerField('quantity', validators=[DataRequired()])