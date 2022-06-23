from flask import render_template, Blueprint, jsonify
from controller.response_msg import render_err_results, render_results
from controller.notion_integration import query_earnings
from sql import query_all, reset, clear, execute

index_page = Blueprint("index_page", __name__)

@index_page.route("/")
def index():

    # fetch database
    database = "data/jobs.db"
    reset(database)
    models = query_all(database)
    output = execute(
        "SELECT usd,usd_idr_rate,usd*usd_idr_rate,avail_date FROM earnings WHERE created_time=(select max(created_time) from earnings);",
        fetch=True,
        one=True
    )

    # define the context
    context = dict(
        models=models,
        formated_usd=f"${round(output[0]):,.2f}",
        formated_idr=f"Rp{round(output[2],2):,.2f}",
        usd_idr_rate=f"Rp{round(output[1],2):,.2f}",
        avail_date=output[3],
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

    # fetch earnings from notion
    results = query_earnings()
    context = dict(
        value_usd=f"${round(results['value_usd'],2):,.2f}",
        value_idr=f"Rp{round(results['value_idr'],2):,.2f}",
        usd_idr=f"Rp{round(results['usd_idr'],2):,.2f}",
        avail_date=results['avail_date']
    )

    # record the value into earnings local database
    cmd = f"INSERT INTO earnings VALUES(datetime('now'),{results['value_usd']},{results['usd_idr']},'{results['avail_date']}')"
    execute(cmd)

    return context

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