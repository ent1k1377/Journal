import sqlalchemy as sqla
engine = sqla.create_engine('postgresql://postgres:root@localhost/test')
print(engine)
engine.connect()