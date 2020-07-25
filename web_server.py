from flask import Flask, render_template
from flask import redirect, url_for, request

from flask_sqlalchemy import SQLAlchemy

web_server = Flask(__name__)

web_server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Messages.sqlite3'
web_server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(web_server)

""" DATABASE """

class Messages(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column("username", db.String(100), nullable=False)
    msg = db.Column("msg", db.String(100), nullable=False)

    def __init__(self, username, msg):
        self.username = username
        self.msg = msg

""" ROUTING """

@web_server.route("/", methods=["POST", "GET"])
@web_server.route("/home", methods=["POST", "GET"])
def index():

    for m in Messages.query.all():
        m_user = m.username
        m_msg = m.msg
        print(f"USERNAME: {m_user} | MESSAGE: {m_msg}")

    if request.method == "POST":
        usr = request.form["username"]
        message = request.form["message-to-send"]

        found_user = Messages.query.filter_by(username=usr).first()
        
        if found_user:
            msg = Messages(found_user, message)
            db.session.add(msg)
            db.session.commit()
        else:
            msg = Messages(usr, message)
            db.session.add(msg)
            db.session.commit()

        return render_template("index.html", user=usr, msg=message)
    else:
        return render_template("index.html")

""" ERROR HANDLING """

@web_server.errorhandler(404)
def error404(error):
    return render_template("error.html", EC="Error! Page Not Found!"), 404

if __name__ == "__main__":
    db.create_all()
    web_server.run(port="8080")