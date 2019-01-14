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
    regFlag = False
    #
    # got here from index.html 
    # 1) Check for Login or Register
    # 2) if Register - set register flag
    # 3) get name and password
    # 4) if result is empty, return back to this this page
    #   - TODO how to display a message? 
    # 5) if result is not empty 
    # 6) check database for user 
    # 7) if user found check password 
    # 8) If OK, display logged in message go to book page 
    # 9) else, display error message return to this page 
    # 
      
    if request.form['btn'] == 'Login':
        print("Login button") 
    else:
        print("Register")
        regFlag = True
    
    # get data from form 
    form_name = request.form.get("uname")
    form_pw = request.form.get("password")
    
    # for debug
    print(f"name {form_name}")
    print(f"pw {form_pw}")
    
    # lookup in db
    statement = "select * from users where uname ='"+form_name+"'"
    # for debug
    print(f"statement: {statement}")
    result = db.execute(statement)
    rows = result.fetchall()
    print("len(rows) is:", len(rows))

    # was anything entered? 
    if len(rows) == 0 and not regFlag:
        print(f"result: {result}")
        print("result is empty")
        uname = "none"
        pw = "none"
        message = "Please enter a username and a password"
        return render_template("index.html", message = message)
    # parse result
    elif not regFlag:
        print(f"result: {result}")
        for row in rows:
            print("username:", row['uname'])
            uname = row['uname']
            pw = row['pw']
            id = row['id']
            print(f"uname: {uname}, password: {pw}, id:{id}") 
        # check for valid password
        if form_pw == pw:
            message = uname+" "+pw+" password matches"
        else: 
            message = "Password does not match"
            return render_template("index.html", message = message)
               
    if(regFlag):
       message =  register(form_name, form_pw)

    return message

@app.route("/register", methods=["POST"] )
def register(uname, pw):
    print("In register() method")
    #INSERT INTO users (uname, pw) VALUES ('Jerry Garcia', 'darkstar');
    statement = "INSERT INTO users(uname, pw) VALUES('"+uname+"','"+pw+"')"
    print(f"register statement is: {statement}")
    db.execute(statement)
    db.commit()
    print(f"added: {uname},{pw}")
    return f"<h1>Register , {uname}, {pw}</H1>"
