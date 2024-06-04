from datetime import datetime, timezone

from databases import Database
import sqlalchemy
from sqlalchemy import ForeignKey, DateTime

from sem6_hw.dbs.settings import settings

DATABASE_URL = settings.DATABASE_URL



database = Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table("users",
                         metadata,
                         sqlalchemy.Column("user_id", sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column("first_name", sqlalchemy.String(20)),
                         sqlalchemy.Column("last_name", sqlalchemy.String(20)),
                         sqlalchemy.Column("email", sqlalchemy.String(50)),
                         sqlalchemy.Column("password", sqlalchemy.String),
                         )

goods = sqlalchemy.Table("goods",
                         metadata,
                         sqlalchemy.Column("good_id", sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column("name", sqlalchemy.String(25)),
                         sqlalchemy.Column("description", sqlalchemy.String(100)),
                         sqlalchemy.Column("price", sqlalchemy.Float),
                         )

orders = sqlalchemy.Table("orders",
                         metadata,
                         sqlalchemy.Column("order_id", sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column("user_id", sqlalchemy.Integer, ForeignKey("users.user_id")),
                         sqlalchemy.Column("good_id", sqlalchemy.Integer, ForeignKey("goods.good_id")),
                         sqlalchemy.Column("quantity", sqlalchemy.Integer),
                         sqlalchemy.Column("status", sqlalchemy.Boolean),
                         sqlalchemy.Column("date", sqlalchemy.DateTime, default=datetime.now()),
                         )

engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={'check_same_thread': False})
metadata.create_all(engine)
