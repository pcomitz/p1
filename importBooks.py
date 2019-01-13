#
# import books
# 1/10/2019 
#

import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("books.csv")
    reader = csv.reader(f)
    #for isbn,title, author, year in reader:
    for i, t, a, y  in reader:
        db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
                    {"isbn": i, "title": t, "author": a, "year": y})
        print(f"Added book:  {i} , {t} , {a}, {y} ")
    db.commit()

if __name__ == "__main__":
    main()
