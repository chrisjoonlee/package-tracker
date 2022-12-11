from flask_wtf import FlaskForm
from wtforms import BooleanField, SelectField, StringField, SubmitField
from wtforms.validators import DataRequired

from map.map import map


class ShippingForm(FlaskForm):
    sender = StringField("Sender name", [DataRequired()])
    recipient = StringField("Recipient name", [DataRequired()])
    origin = SelectField("Origin", [DataRequired()], choices=map.keys())
    destination = SelectField(
        "Destination", [DataRequired()], choices=map.keys())
    express = BooleanField("Express shipping")
    submit = SubmitField("Submit")
    cancel = SubmitField("Cancel")
