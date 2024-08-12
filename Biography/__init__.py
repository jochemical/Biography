# Here we define our flask app

from flask import Flask, render_template, abort

# Create app
app = Flask(__name__)

# Projects
projects = [
    {
        "name": "Discussion forum",
        "thumb": "img/Discussion_forum.png",
        "hero": "img/Discussion_forum.png",
        "categories": ["Flask", "MongoDB"],
        "slug": "discussion_forum",
    },
    {
        "name": "Daily tasks",
        "thumb": "img/daily_tasks_overview.png",
        "hero": "img/daily_tasks.png",
        "categories": ["Flask", "MongoDB"],
        "slug": "daily-tasks",
    },
    {
        "name": "My Cinema",
        "thumb": "img/my_cinema_register.png",
        "hero": "img/my_cinema_detailpage.png",
        "categories": ["Flask", "MongoDB"],
        "slug": "my_cinema",
    },
    {
        "name": "Warehouse REST API",
        "thumb": "img/warehouse.png",
        "hero": "img/warehouse.png",
        "categories": ["REST API","SQL & Docker"],
        "slug": "warehouse",
    },
]

# change the list to a dictionary of dictionaries:
slug_to_project = { project["slug"]: project for project in projects }



# homepage
@app.route("/")
def home():
    return render_template("home.html", projects=projects)

# about page
@app.route("/about")
def about():
    return render_template("about.html")

# contact page
@app.route("/contact")
def contact():
    return render_template("contact.html")

# route for the invidual project pages
@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(
        f"project_{slug}.html",
        project=slug_to_project[slug]
    )

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404
