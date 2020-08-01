from flask import Flask, render_template
from flask import redirect, url_for, request

# from flask_sqlalchemy import SQLAlchemy

# from main_server import *

web_server = Flask(__name__)

# web_server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DataBase.sqlite3'
# web_server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# DataBase = SQLAlchemy(web_server)

smsg = ["Hello", "New Message", "This is a message"]

""" ROUTING """

@web_server.route("/")
@web_server.route("/home")
def index():
    # GetDatabaseData()
    return render_template("index.html", messages=smsg)

@web_server.route("/newUser", methods=["POST", "GET"])
def newUser():
    if request.method == "POST":
        usr = request.form["username"]
        pas = request.form["password"]

        # found_user = QueryDatabase("Username", usr)

        # if found_user == False:
        #     new = DataBase(usr, pas)
        #     db.session.add(new)
        #     db.session.commit()
        
        return render_template("index.html")
    else:
        return render_template("newUser.html")


""" ERROR HANDLING """

@web_server.errorhandler(404)
def error404(error):
    return render_template("error.html", EC="Error! Page Not Found!"), 404

if __name__ == "__main__":
    # DataBase.create_all()
    web_server.run(port="8080")