#
# Paul Comitz 
# Project 1
# January 8 2019
# app.py - this is the flask controller
#

import os

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/authenticate", methods=["POST"])
def authenticate():
    form_name = request.form.get("uname")
    form_pw = request.form.get("password")
    print(f"name {form_name} ")
    print(f"pw {form_pw} ")
    statement = "select * from users where uname ='"+form_name+"'" 
    print(f"statement: {statement}")
    result = db.execute(statement)
    rows = result.fetchall()
    print("len(rows) is:", len(rows))

    if len(rows) == 0:
        print(f"result: {result}")
        print("result is empty")
        uname = "none"
        pw = "none"
    else:    
        print(f"result: {result}")
        for row in rows:
            print("username:", row['uname'])
            uname = row['uname']
            pw = row['pw']
            print(f"uname: {uname}")    

    return uname+" "+pw

