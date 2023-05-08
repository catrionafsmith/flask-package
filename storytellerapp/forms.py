from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

class SignUpForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Sign up')

class NewUserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    childname = StringField("Child's Name", validators=[DataRequired(), Length(max=50)])
    gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
                         validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    #need to edit these with the actual options :
    routine = SelectField('Bedtime Routine', choices=[('routine1', 'Routine 1'), ('routine2', 'Routine 2')],
                          validators=[DataRequired()])
    submit = SubmitField('Sign up')