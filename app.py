from flask import Flask, request, render_template, session

from flask_debugtoolbar import DebugToolbarExtension
from stories import story, story_options

app = Flask(__name__)

app.config["SECRET_KEY"] = "whatever"
debug = DebugToolbarExtension(app)


@app.route("/")
def home_page():
    """Shows home page"""
    stories = story_options.keys()
    return render_template("home.html", stories=stories)


@app.route("/form")
def form_page():
    """Shows home page"""
    session["choice"] = request.args["stories"]
    story_choice = story_options[session["choice"]]
    return render_template("form.html", prompts=story_choice.prompts)


@app.route("/story")
def story_page():
    """Shows home page"""
    answers = request.args
    choice = session["choice"]
    story_choice = story_options[choice]
    return render_template(
        "story.html", my_story=story_choice.generate(answers), title=choice
    )
