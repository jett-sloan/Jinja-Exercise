from flask import Flask, render_template, request
from stories import story



""""
shows the html using @route
"""
app = Flask(__name__, template_folder='../templates')


@app.route('/')
def get_form():
    words = story.words
    return render_template("form.html", words=words)



@app.route('/story')
def get_story():
    text = story.generate(request.args)
    return render_template("story.html", text=text)


