from flask import render_template, Blueprint, jsonify
from controller.response_msg import render_err_results, render_results
from controller.notion_integration import query_earnings
from sql import query_all, reset, clear

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
        formated_usd="$0",
        formated_idr="Rp0",
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

@index_page.get("/get-earnings")
def get_earnings():
    results = query_earnings()
    results['value_usd']=f"${results['value_usd']}"
    results['value_idr']=f"Rp{round(results['value_idr'],2):,.2f}"
    results['usd_idr']=f"Rp{round(results['usd_idr'],2):,.2f}"
    return results

@index_page.get("/clear-database")
def clear_database():

    try:
        # clear database
        clear("data/jobs.db")

        # return success message
        return render_results(msg="Database Cleared!")

    except:
        # return error message
        return render_err_results(msg="System Error")