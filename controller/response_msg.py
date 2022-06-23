from flask import jsonify

def render_results(code=200,msg="success"):
    context = dict(code=code,msg=msg)
    return jsonify(context)

def render_err_results(code=-1,msg="system busy"):
    context = dict(code=code,msg=msg)
    return jsonify(context)