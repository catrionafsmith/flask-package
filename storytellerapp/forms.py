from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, IntegerField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

class SignUpForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Sign up')

class NewUserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    childname = StringField("Child's Name", validators=[DataRequired(), Length(max=50)])
    #need to edit these with the actual options :
    gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
                         validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    
    # think this needs to be a different type of input
    routine = SelectMultipleField('Bedtime Routine', choices=[('routine1', 'Brush teeth'), ('routine2', 'Bedtime snack/drink'), ('routine3', 'Pyjamas on'), ('routine2', 'Get into bed')],
                          validators=[DataRequired()])
    submit = SubmitField('Sign up')