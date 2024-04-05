from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField,SearchField,SelectField,TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class SearchForm(FlaskForm):
    searched = StringField('Searched',
                        validators=[DataRequired()])

    
    submit = SubmitField('Submit')
class CreateForm(FlaskForm):
    FirstName = StringField('First Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    LastName = StringField('Last Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    JobTitle = StringField('Job Name',
                           validators=[DataRequired()])
    Overview = TextAreaField('Overview',
                           validators=[DataRequired()])
    Category = StringField('Category',
                           validators=[DataRequired()])
    Level = SelectField('Level', choices=["Beginner","Intermediate","Advanced"],
                           validators=[DataRequired()])
    NumberofHours=IntegerField('Number of Hours')
    MyStory = TextAreaField('My Story')
    Email = StringField('Email')
    LinkedIn= StringField('LinkedIn')

    submit = SubmitField('Submit')
    content=TextAreaField('Content')




# class LoginForm(FlaskForm):
#     email = StringField('Email',
#                         validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     remember = BooleanField('Remember Me')
#     submit = SubmitField('Login')