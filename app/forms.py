# forms for adding, etc
from wtforms import StringField
from wtforms.fields.choices import SelectField
from flask_wtf import FlaskForm
from wtforms.fields.simple import URLField, SubmitField, TextAreaField, PasswordField, EmailField
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
    submit = SubmitField("Submit")

class Register(FlaskForm):
    first_name = StringField('First name', [InputRequired()])
    last_name = StringField('Last name', [InputRequired()])
    email = EmailField('Email', [InputRequired()])
    password = PasswordField('Password', [InputRequired()])
    submit = SubmitField("Submit")
    
class Login(FlaskForm):
    email = EmailField('Email', [InputRequired()])
    password = PasswordField('Password', [InputRequired()])
    submit = SubmitField("Submit")

class CommentForm(FlaskForm):
    comment_text = TextAreaField("Add your comment:", validators=[DataRequired()])
    submit = SubmitField("Add Comment")