# forms for adding, etc
from wtforms import StringField
from wtforms.fields.choices import SelectField
from flask_wtf import FlaskForm
from wtforms.fields.simple import URLField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, DataRequired


class Add(FlaskForm):
    name = StringField('Cafe name', [InputRequired()])
    location_url = URLField('Google maps url', [InputRequired()])
    bg_url = URLField('Background image photo url', [InputRequired()])
    cafe_url = URLField('Cafe website url', [InputRequired()])
    cafe = SelectField('Taste of cafe', choices=["🚫", "☕", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"], validators=[DataRequired()], default="☕")
    wifi = SelectField('Strength of wifi', choices=["🚫", "🛜", "🛜🛜", "🛜🛜🛜", "🛜🛜🛜🛜", "🛜🛜🛜🛜🛜"], validators=[DataRequired()], default="🛜")
    sockets = SelectField('Availability of power sockets', choices=["🚫", "⚡", "⚡⚡", "⚡⚡⚡", "⚡⚡⚡⚡", "⚡⚡⚡⚡⚡"], validators=[DataRequired()], default="⚡")
    describe = TextAreaField('Short cafe description', [InputRequired()])
    submit = SubmitField("Enter data")