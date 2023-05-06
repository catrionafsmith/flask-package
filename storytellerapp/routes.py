from storytellerapp import app
from flask import render_template, request

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/basic_story', methods=['POST'])
def basic_story():
    childname = request.form['childname']
    return render_template('basic_story.html', childname=childname)

