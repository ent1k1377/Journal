import sqlalchemy as sqla
engine = sqla.create_engine('postgresql://scott:tiger@localhost/mydatabase')
engine.connect()