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


class User(BaseModel):
    user_id = IntegerField(primary_key=True)
    username = CharField()
    first_name = CharField()
    last_name = CharField(null=True)





def create_models():
    db.create_tables(BaseModel.__subclasses__())


