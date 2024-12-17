from peewee import *
from playhouse.migrate import SqliteMigrator, migrate

db = SqliteDatabase('hellsville.db')

class Person(Model):
    first_name = CharField()
    last_name = CharField()
    gender = CharField()
    age = IntegerField()
    occupation = CharField()
    alive = BooleanField(default=True)
    kill_count = IntegerField(default=0)
    sullied = BooleanField(default=False)

    class Meta:
        database = db

class TownStats(Model):
    stat = CharField()
    description = CharField()
    value = FloatField()

    class Meta:
        database = db

def migrate_changes():
    migrator = SqliteMigrator(db)
    with db.atomic():
        migrate(
            migrator.add_column('person', 'sullied', BooleanField(default=False)),
            migrator.add_column('person', 'kill_count', IntegerField(default=0))
        )

if __name__ == "__main__":
    db.connect()
    db.create_tables([Person])
    migrate_changes()