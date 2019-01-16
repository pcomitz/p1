# Notes 

1/6/2019 
Set up up git
1. Create empty repo on github
2. Clone : https://github.com/pcomitz/p1.git
3. Add files to repo
4. git add .
5. git commit -m "initial commit"
6. git push # need to add uname and pw
7. git status 

## Set up heroku

1. https://www.heroku.com
2. pcomitz@live.com
3. app is phcp1 
4. configure add ons 
5. view on https://www.adminer.org
6. Need to install heroku cli
7. do heroku login on cli
8. To connect to db
9. DATABASE_URL=$(heroku config:get DATABASE_URL -a your-app) your_process
    - my app is phcp1
    - heroku config:get DATABASE_URL -a phcp1
    - see https://devcenter.heroku.com/articles/connecting-to-heroku-postgres-databases-from-outside-of-heroku
    
10. Database Credentials 

Host
ec2-174-129-18-247.compute-1.amazonaws.com
Database
d740lk1tdq3uhl
User
tyivzozvjfptcx
Port
5432
Password
360dab57fd1a56af249e12d1d0bd82884585e75c8dc9b4c9ba679cffbffd942b

## Set up python 
1. path=%path%;G:\Python\Python37;
2. path=%path%;G:\Python\Python37\Scripts;
3. Now can run  
    - pip3 install -r requirements.txt
4. Can run flask with: <code>flask run</code> 


## Postgresql

Show all tables <br>
<code>
SELECT table_name FROM information_schema.tables WHERE table_schema='public'</code>

Show columns <br>
<code>
select * from information_schema.columns where table_schema = 'public'; </code>

Select<br>
`SELECT * FROM "books" LIMIT 50;`

<code>select * from users where users.uname = 'Jerry Garcia';</code>

<code>select * from users where users.uname = 'Jerry Garcia' and pw = 'darkstar';</code>

<code>select uname from users where uname = 'Jerry Garcia';</code>

Wildcards in postgresql<br>
`select * from books where author like '%James%'`

Delete <br>
https://www.w3schools.com/sql/sql_delete.asp <br>
`DELETE FROM Customers WHERE CustomerName='Alfreds Futterkiste';` <br>
`DELETE FROM users WHERE uname = 'PigPen'; `

## SQLAlchemy
https://docs.sqlalchemy.org/en/latest/core/tutorial.html

## Markdown 
https://docs.microsoft.com/en-us/contribute/how-to-write-use-markdown
https://code.visualstudio.com/Docs/languages/markdown

Visual Studio code toggle view 
ctrl + shift + V

*** Cheat Sheet ***  
https://blog.ghost.org/markdown/

## sqlalchemy
[Connections Tutorial] (https://docs.sqlalchemy.org/en/latest/core/connections.html)


### 1/13/2019

## 1/15/2019
added white space trim with s.strip()
Login notes
Case: 
- Valid username and password entered, Log user in
- ResultObject , rows == 0  
  1. No username entered, Login or register clicked
  2. Invalid username, Login clicked 
- Register selected , username exists
- Register selected, new username, proceed with registration 

