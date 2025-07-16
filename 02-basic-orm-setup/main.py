from sqlalchemy import create_engine, MetaData,Table, Column, Integer, String, VARCHAR

engine = create_engine(r"sqlite:///orm.db")

# metadata will be passes in every table
meta = MetaData()

studends = Table(
    'students', meta,
    Column("id",Integer,primary_key=True),
    Column("name",VARCHAR(50),nullable=False),
    Column("major", VARCHAR(50))
)

# do all the action in database
meta.create_all(engine)