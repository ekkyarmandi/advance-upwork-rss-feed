from flask import render_template, Blueprint
from sql import query_all

index_page = Blueprint("index_page", __name__)

@index_page.route("/")
def index():
    
    # run the upwork rss feed parser in seperate terminal

    # fetch database every 1 minutes and update the templates
    models = query_all("data/jobs.db")

    # define the context
    context = dict(models=models)
    return render_template("index.html",**context)