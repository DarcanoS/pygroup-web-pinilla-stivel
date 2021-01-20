from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import DataRequired


class CreateCategoryForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    
class Create_Product_Form(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    image = StringField('image')
    price = IntegerField('price', validators=[DataRequired()])
    weight = StringField('weight')
    description = StringField('description')
    refundable = BooleanField('refundable')
    category_id = IntegerField('category_id', validators=[DataRequired()])
    