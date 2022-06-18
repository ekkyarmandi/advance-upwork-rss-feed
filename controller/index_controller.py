from flask import render_template, Blueprint, jsonify
from sql import query_all, reset

index_page = Blueprint("index_page", __name__)

@index_page.route("/")
def index():

    # fetch database
    database = "data/jobs.db"
    reset(database)
    models = query_all(database)

    # define the context
    context = dict(
        models=models,
        results=len(models)
    )
    return render_template("index.html",**context)

@index_page.route("/query")
def query():
    
    # query new job post
    entries = []
    database = "data/jobs.db"
    models = query_all(database)
    for model in models:
        entry = dict(
            title=model.title,
            description=model.description,
            timestamp=model.timestamp,
            category=model.category,
            country=model.country,
            budget=model.budget,
            link=model.link,
            tags=model.tags,
            timestr=model.timestr
        )
        entries.append(entry)

    # turn the data into json dictionary
    return jsonify(entries)