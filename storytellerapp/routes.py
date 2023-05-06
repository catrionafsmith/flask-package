import os
import openai
from storytellerapp import app
from flask import render_template, request, redirect, url_for

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/basic_story', methods=['POST'])
# def basic_story():
#     childname = request.form['childname']
#     return render_template('basic_story.html', childname=childname)

@app.route("/ai_story", methods=["POST"])
def ai_story():
    
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

# def generate_prompt(childname, monster):
#     return f"You are an expert children's author who specialises in writing engaging stories. Please write a 400 word story. The story should be about a kid called {childname}, who travels to a magical land and battles {monster}."
