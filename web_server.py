from flask import Flask, render_template
from flask import redirect, url_for

web_server = Flask(__name__)

""" ROUTING """

@web_server.route("/")
@web_server.route("/home")
def index():
    return render_template("index.html")

""" ERROR HANDLING """

@web_server.errorhandler(404)
def error404(error):
    return render_template("error.html", EC="Error! Page Not Found!"), 404

if __name__ == "__main__":
    web_server.run(port="3000")