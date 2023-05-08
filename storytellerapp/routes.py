import os
import openai
# pip install mysql-connector-python and this should work
import mysql.connector
from storytellerapp import app
from flask import render_template, request, redirect, url_for, session
from .forms import SignUpForm, NewUserForm

# OpenAI API key currently stored as an environment variable
# i.e. on my local computer
openai.api_key = os.getenv("OPENAI_API_KEY")

# secret key for Flask 'session' - like cookies I think
# maybe secret key is for wtforms too?
app.secret_key = b'_5#y2L"Fkkk4Q8z\n\xec]/'

# Set up database connection
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="glendelvine3255",
  database="bedtimebard"
)

# Route for homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route for registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get form data
        username = request.form['username']
        password = request.form['password']

        # Create cursor
        cursor = db.cursor()

        # Insert user into database
        cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, password))
        db.commit()

        # Close cursor
        cursor.close()

        # Redirect to login page
        return redirect(url_for('login'))
    # If the request method is GET, render the registration form
    return render_template('register.html')

# Route to login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #Get form data
        username = request.form['username']
        password = request.form['password']

        # Create cursor
        cursor = db.cursor()
        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
        user = cursor.fetchone()
        cursor.close()

        if user:
            # User exists, set session variables
            session['loggedin'] = True
            session['id'] = user[0]
            session['username'] = user[1]

            # Redirect to home page
            return redirect(url_for('ai_story'))
        else:
            # User doesn't exist or password is incorrect, show error message
            error = 'Invalid credentials. Please try again.'
            return render_template('login.html', error=error)

    # GET request or invalid POST data, show login form
    return render_template('login.html')

# Route to generate story
@app.route("/ai_story", methods=["GET", "POST"])
def ai_story():
    if request.method == 'GET':
        return render_template("ai_story.html")
    elif request.method == 'POST':
        childname = request.form["childname"]
        monster = request.form["monster"]
        response = openai.Completion.create(
            model="text-davinci-003",
            # prompt=generate_prompt(childname, monster),
            prompt=f"You are an expert children's author who specialises in writing engaging stories. Please write a 400 word story. The story should be about a kid called {childname}, who travels to a magical land and battles {monster}.",
            temperature=0.8,
            max_tokens=4000,
            top_p=1.0,
            frequency_penalty=0.5,
            presence_penalty=0.0
        )
        return render_template("ai_story.html", result=response.choices[0].text)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.is_submitted():
        result = request.form
        return render_template('user.html', result=result)
    return render_template('signup.html', form=form)

@app.route('/register2', methods=['GET', 'POST'])
def register2():
    form = NewUserForm()
    if form.is_submitted():
        result = request.form
        return render_template('user.html', result=result)
    return render_template('register2.html', form=form)

@app.route('/bookshelf')
def bookshelf():
    return render_template('bookshelf.html')

# def generate_prompt(childname, monster):
#     return f"You are an expert children's author who specialises in writing engaging stories. Please write a 400 word story. The story should be about a kid called {childname}, who travels to a magical land and battles {monster}."
