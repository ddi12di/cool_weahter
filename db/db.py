import os


from peewee import (
    AutoField,
    BooleanField,
    CharField,
    DateField,
    ForeignKeyField,
    IntegerField,
    Model,
    SqliteDatabase,
)

from dotenv import load_dotenv
DB_PATH = os.getenv('DB_PATH')
DATE_FORMAT = os.getenv('DATE_FORMAT')

# from config import DATE_FORMAT, DB_PATH

db = SqliteDatabase(DB_PATH)


class BaseModel(Model):
    class Meta:
        database = db


class Request(BaseModel):
    request_id = IntegerField(primary_key=True)
    date = CharField()
    time = CharField()
    username = CharField()
    firstname = CharField()
    city = CharField()
    temp = CharField()







def create_models():
    db.create_tables(BaseModel.__subclasses__())


