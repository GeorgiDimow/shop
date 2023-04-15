from collections import deque

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey

engine = create_engine('mysql+mysqlconnector://root:Goshoprasetolosho123!@localhost/wood_shop_schema')

metadata_obj = MetaData()

clients = Table(
    "clients",
    metadata_obj,
    Column("client_id", Integer, primary_key=True),
    Column("first_name", String(45)),
    Column("last_name", String(45)),
)

orders = Table(
    "orders",
    metadata_obj,
    Column("order_id", Integer, primary_key=True),
    Column("client_id", Integer, ForeignKey("clients.client_id"), nullable=False),
    Column("item_id", Integer, ForeignKey("items.item_id"), nullable=False),
)

items = Table(
    "items",
    metadata_obj,
    Column("item_id", Integer, primary_key=True),
)


metadata_obj.create_all(engine)

metadata_obj.bind = engine

conn = engine.connect()

select_query = clients.select()

result_set = deque(conn.execute(select_query).fetchall())

conn.close()

