import sqlalchemy as sqla

engine = sqla.create_engine('postgresql://postgres:root@localhost/postgres')
print(engine)
conn = engine.connect()


def execute_into(text):
    conn.execute(text)


def execute_sel(text):
    sql = conn.execute(text)
    return sql.fetchall()

