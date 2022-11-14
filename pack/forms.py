from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired


class ProductForm(FlaskForm):
    item_name=StringField("product name",validators=[DataRequired()])
    item_price=StringField("product price",validators=[DataRequired()])
    submit=SubmitField("add product",validators=[DataRequired()])
