from peewee import *

database_proxy = DatabaseProxy()


class Driver(Model):
    name = CharField()
    abbreviation = CharField()
    car = CharField()
    lap_time = CharField()

    class Meta:
        database = database_proxy

