from flask import Flask
from controller.index_controller import index_page

app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = "TheSecretKey"

app.register_blueprint(index_page, url_prefix="/")

if __name__ == "__main__":
    app.run(debug=True)