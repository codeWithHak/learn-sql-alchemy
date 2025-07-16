from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

# db connection
engine = create_engine("sqlite:///alchemy.db", echo=True)

connection = engine.connect()

# We cannot execute simple text querries likt this, we need to import text function
# connection.execute("CREATE TABLE IF NOT EXISTS ")

# execute a create command
connection.execute(text("CREATE TABLE IF NOT EXISTS students(name varchar(30), age integer)"))



# working with Session 
from sqlalchemy.orm import Session

session = Session(engine)

# EXECUTING INSERT COMMAND
session.execute(text("INSERT INTO  students(name, age) VALUES('Khizar', 22)"))

# presist changes in db
session.commit()


