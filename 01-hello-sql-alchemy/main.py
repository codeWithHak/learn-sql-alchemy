from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

# db connection
engine = create_engine("sqlite:///alchemy.db", echo=True)

connection = engine.connect()

# We cannot execute simple text querries likt this, we need to import text function
# connection.execute("CREATE TABLE IF NOT EXISTS ")

# execute a create command
# connection.execute(text("CREATE TABLE IF NOT EXISTS employees(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, position TEXT NOT NULL, salary INTEGER NOT NULL)"))
# connection.execute(text("CREATE TABLE IF NOT EXISTS students(name varchar(30), age integer)"))


# presist changes in db

# working with Session 
from sqlalchemy.orm import Session

session = Session(engine)
session.execute(text("INSERT INTO  students(name, age) VALUES('Khizar', 22)"))
session.commit()


