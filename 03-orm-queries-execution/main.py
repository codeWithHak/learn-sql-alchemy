from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer

engine = create_engine("sqlite:///university.db")

meta = MetaData()

# create a table
students = Table(
    'students',meta,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("major", String),
)

# metadata will convert your python code into sql commands
meta.create_all(engine)

# connect the db
connection = engine.connect()


# querries
insert_query = students.insert().values(id=3, name="Farrukh",major="BBA")

delete_query = students.delete().where(students.c.id == 3)

# slects all the tables if no where clause given you van give a where clause like given in delte_qquery
select_query = students.select()

update_query = students.update().where(students.c.id == 1).values(name="Khizar bakhtiyar")


# execute query
result = connection.execute(select_query)

# save data in db
connection.commit()

# fetch all tables that are selected
for column in result.fetchall():
    
    print(f"\nID: {column[0]}")
    print(f"Name: {column[1]}")
    print(f"Major: {column[2]}")