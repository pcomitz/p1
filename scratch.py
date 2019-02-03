#
# 
# 1/19/2019
# for trying stuff out !!!
#
# LOOONG break - back on 2/3/19 
#

import os
from flask import Flask, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# create a Flask object 
app = Flask(__name__)

# for database connection
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


'''
check for null in name or password
Note - declaration required before use
no forward declaration in python
Return true if either username or password 
are null
Return false if either are null
'''
def checkForNull(form_name, form_pw):
    result = True
    print(f"form_name: {form_name} form_pw: {form_pw}")

    if(form_name): 
        print("form_name is true")
    
    if (form_pw):
        print("form_pw is true")   

    if form_name and form_pw: 
        print("both name and pw are true")
        result = False

    return result

def register(uname, pw):
    print("In register() method")
    # example INSERT
    #INSERT INTO users (uname, pw) VALUES ('Jerry Garcia', 'darkstar');
    statement = "INSERT INTO users(uname, pw) VALUES('"+uname+"','"+pw+"')"
    print(f"register statement is: {statement}")
    db.execute(statement)
    db.commit()
    print(f"added: {uname},{pw}")


@app.route("/")
def index():
    print("running scratch")
    return render_template("index.html")

@app.route("/authenticate", methods=["POST"])
def authenticate():
    # set to true when register button clicked
    regFlag = False
    login_result = False
    message = ""
    debug_message = ""
    # get data from form and strip any blanks 
    form_name = request.form.get("uname").strip()
    form_pw = request.form.get("password").strip()

    # check for null strings
    null_result = checkForNull(form_name, form_pw)
    if null_result:
        message = "Please enter a username and a password"

    if(not null_result): 
        # check for Login or Register button click
        if request.form['btn'] == 'Login':
            print("Login button clicked") 
        else:
            print("Register button clicked")
            regFlag = True
        # 
        # Need to check presence of name in db for either case
        # Login: Does password match? 
        # Register: Does name already exist
        #
        # lookup in db
        statement = "select * from users where uname ='"+form_name+"'"
        # for debug
        print(f"sql statement: {statement}")
        db_result = db.execute(statement)
        rows = db_result.fetchall()
        # retreve the Result
        # this loop does not execute of rows == 0
        for row in rows:
            #print("username retrieved from db:", row['uname'])
            uname = row['uname']
            pw = row['pw']
            id = row['id']
            print(f"from db: uname: {uname}, password: {pw}, id:{id}") 

        lenOfRows = len(rows)
        print(f"number of rows returned from db is: {lenOfRows}")

        # check login
        if(not regFlag):
            if lenOfRows == 0: 
                # login clicked for user that does not exist
                print(f"user {form_name} does not exist in db")
                message = form_name + " does not exist in db. Please click Register"\
                " to create an account"
            elif form_pw == pw: 
                    login_result = True
                    print(f"uname {uname} is logged in")
                    message = uname + " is logged in"
            else:
                login_result = False
                print(f"uname {uname} password does not match")
                message = uname + " password does not match"
        else:
            #Register
            if(lenOfRows == 0): 
                print("regFlag true")
                register(form_name, form_pw)
                message = form_name + " registered."
            else: 
                #register selected for an existing username
                print(uname + "aready exists in db")
                message = uname + " already exists in db"

        # to convert bool to string 
        # https://stackoverflow.com/questions/10509803/how-do-i-concatenate-a-boolean-to-a-string-in-python
        debug_message = message + " null result:"+str(null_result) \
                        +" login_result:"+str(login_result)
        print(f"debug_message:{debug_message}")

    return render_template("index.html", message = message)


# if not used as a module, run flask app
if __name__ == "__main__" :
    print("__name__  is :", __name__)
    app.run()   


