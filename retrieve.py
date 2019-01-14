#
# retrieve.py
# practice retreiving data from db
#

import os, sys

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

def main():
    # get connection to db
    engine = create_engine(os.getenv("DATABASE_URL"))
    db = scoped_session(sessionmaker(bind=engine))
    print("python version is :", sys.version)

    # get the data 
    books = db.execute("SELECT isbn, title, author from books limit 20")
    for book in books:
        print(f"isbn: {book.isbn}, title:{book.title}, author: {book.author}")

if __name__ == "__main__":
    main()